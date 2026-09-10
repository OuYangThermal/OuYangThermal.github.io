#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const root = path.resolve(__dirname, '..');
const manifestPath = path.join(root, 'data', 'image-library.json');
const imageExtensions = new Set(['.webp', '.png', '.jpg', '.jpeg', '.svg']);
const textExtensions = new Set(['.html', '.md', '.css', '.js', '.yml', '.yaml', '.xml', '.txt']);
const ignoredDirectories = new Set(['.git', '_site', 'node_modules', 'vendor']);
const controlledContentTypes = new Set(['real-photo', 'real-photo-composite', 'engineering-diagram', 'application-diagram', 'portrait', 'product-sample', 'production-reference']);
const controlledAuthenticity = new Set(['real-user-supplied-photo', 'real-production-reference', 'generated-engineering-diagram', 'edited-user-supplied-portrait', 'source-uncertain-do-not-claim']);

function walk(directory) {
  const results = [];
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (entry.isDirectory() && ignoredDirectories.has(entry.name)) continue;
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) results.push(...walk(absolute));
    else results.push(absolute);
  }
  return results;
}

function slash(value) { return value.split(path.sep).join('/'); }
function relative(absolute) { return slash(path.relative(root, absolute)); }
function sha256(buffer) { return crypto.createHash('sha256').update(buffer).digest('hex'); }

function dimensions(buffer, extension) {
  if (extension === '.png') {
    if (buffer.toString('ascii', 1, 4) !== 'PNG') throw new Error('Invalid PNG signature');
    return { width: buffer.readUInt32BE(16), height: buffer.readUInt32BE(20) };
  }
  if (extension === '.jpg' || extension === '.jpeg') {
    let offset = 2;
    while (offset + 9 < buffer.length) {
      if (buffer[offset] !== 0xff) { offset += 1; continue; }
      const marker = buffer[offset + 1];
      if ([0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf].includes(marker)) {
        return { height: buffer.readUInt16BE(offset + 5), width: buffer.readUInt16BE(offset + 7) };
      }
      if (marker === 0xd8 || marker === 0xd9) { offset += 2; continue; }
      const length = buffer.readUInt16BE(offset + 2);
      if (length < 2) break;
      offset += 2 + length;
    }
    throw new Error('JPEG dimensions not found');
  }
  if (extension === '.webp') {
    if (buffer.toString('ascii', 0, 4) !== 'RIFF' || buffer.toString('ascii', 8, 12) !== 'WEBP') throw new Error('Invalid WebP signature');
    const chunk = buffer.toString('ascii', 12, 16);
    if (chunk === 'VP8X') return { width: 1 + buffer.readUIntLE(24, 3), height: 1 + buffer.readUIntLE(27, 3) };
    if (chunk === 'VP8 ') return { width: buffer.readUInt16LE(26) & 0x3fff, height: buffer.readUInt16LE(28) & 0x3fff };
    if (chunk === 'VP8L') {
      const bits = buffer.readUInt32LE(21);
      return { width: (bits & 0x3fff) + 1, height: ((bits >> 14) & 0x3fff) + 1 };
    }
    throw new Error(`Unsupported WebP chunk ${chunk}`);
  }
  if (extension === '.svg') {
    const text = buffer.toString('utf8');
    const viewBox = text.match(/viewBox\s*=\s*["']\s*[-\d.]+\s+[-\d.]+\s+([\d.]+)\s+([\d.]+)\s*["']/i);
    const width = text.match(/<svg[^>]*\bwidth\s*=\s*["']([\d.]+)/i);
    const height = text.match(/<svg[^>]*\bheight\s*=\s*["']([\d.]+)/i);
    if (width && height) return { width: Number(width[1]), height: Number(height[1]) };
    if (viewBox) return { width: Number(viewBox[1]), height: Number(viewBox[2]) };
    throw new Error('SVG width/height or viewBox not found');
  }
  throw new Error(`Unsupported format ${extension}`);
}

function routeForSource(source) {
  if (source.startsWith('_includes/')) return '*';
  if (source === 'index.html' || source === 'index.md') return '/';
  if (source.startsWith('_articles/')) return `/${source.slice('_articles/'.length).replace(/\.(md|html)$/, '')}/`;
  if (/\/index\.(md|html)$/.test(source)) return `/${source.replace(/\/index\.(md|html)$/, '')}/`;
  return `/${source.replace(/\.(md|html)$/, '')}/`;
}

const allFiles = walk(root);
const images = allFiles.filter(file => imageExtensions.has(path.extname(file).toLowerCase()));
const texts = allFiles.filter(file => textExtensions.has(path.extname(file).toLowerCase()))
  .filter(file => {
    const rel = relative(file);
    return rel !== 'data/image-library.json' && rel !== 'docs/IMAGE_LIBRARY.md' && rel !== 'AGENTS.md' && rel !== 'scripts/audit-image-library.js';
  });
const textSources = texts.map(file => ({ path: relative(file), content: fs.readFileSync(file, 'utf8') }));

const errors = [];
const warnings = [];
if (!fs.existsSync(manifestPath)) {
  console.error('ERROR: data/image-library.json does not exist.');
  process.exit(1);
}
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
const records = Array.isArray(manifest.images) ? manifest.images : [];
const recordsByPath = new Map(records.map(record => [String(record.path || '').replace(/^\//, ''), record]));
const recordIds = new Set();
const recordPaths = new Set();
for (const record of records) {
  const rel = String(record.path || '').replace(/^\//, '');
  if (!record.id || recordIds.has(record.id)) errors.push(`Missing or duplicate manifest id: ${record.id || '(empty)'}`);
  if (!rel || recordPaths.has(rel)) errors.push(`Missing or duplicate manifest path: ${rel || '(empty)'}`);
  if (!record.alt || !record.caption || !record.reuse_policy) errors.push(`${record.id || rel}: alt, caption and reuse_policy are required`);
  recordIds.add(record.id);
  recordPaths.add(rel);
}
const physicalByPath = new Map();
const hashGroups = new Map();

for (const file of images) {
  const rel = relative(file);
  const buffer = fs.readFileSync(file);
  let size;
  try { size = dimensions(buffer, path.extname(file).toLowerCase()); }
  catch (error) { errors.push(`${rel}: ${error.message}`); continue; }
  const info = { path: rel, fileSize: buffer.length, sha256: sha256(buffer), ...size };
  physicalByPath.set(rel, info);
  if (!hashGroups.has(info.sha256)) hashGroups.set(info.sha256, []);
  hashGroups.get(info.sha256).push(rel);
}

for (const [hash, paths] of hashGroups) if (paths.length > 1) errors.push(`Duplicate SHA-256 ${hash}: ${paths.join(', ')}`);
for (const rel of physicalByPath.keys()) if (!recordsByPath.has(rel)) errors.push(`Image is not registered: ${rel}`);
for (const [rel, record] of recordsByPath) {
  const info = physicalByPath.get(rel);
  if (!info) { errors.push(`Registered image does not exist: ${rel}`); continue; }
  if (!controlledContentTypes.has(record.content_type)) errors.push(`${record.id}: invalid content_type ${record.content_type}`);
  if (!controlledAuthenticity.has(record.authenticity)) errors.push(`${record.id}: invalid authenticity ${record.authenticity}`);
  if (record.width !== info.width || record.height !== info.height) errors.push(`${record.id}: dimensions ${record.width}x${record.height} do not match ${info.width}x${info.height}`);
  if (record.file_size_bytes !== info.fileSize) errors.push(`${record.id}: file size does not match`);
  if (record.sha256 !== info.sha256) errors.push(`${record.id}: SHA-256 does not match`);
  if (record.format !== path.extname(rel).slice(1).toLowerCase()) errors.push(`${record.id}: format does not match extension`);

  const needle = `/${rel}`;
  const usedSources = textSources.filter(source => source.content.includes(needle));
  const actualUsedOn = [...new Set(usedSources.map(source => routeForSource(source.path)))].sort();
  const declaredUsedOn = [...(record.used_on || [])].sort();
  if (JSON.stringify(actualUsedOn) !== JSON.stringify(declaredUsedOn)) errors.push(`${record.id}: used_on ${JSON.stringify(declaredUsedOn)} does not match actual ${JSON.stringify(actualUsedOn)}`);
  if (actualUsedOn.length === 0) warnings.push(`${record.id}: registered but not used on a rendered page`);
}

const knownPaths = new Set(physicalByPath.keys());
for (const source of textSources) {
  const matches = source.content.matchAll(/["'(]\/((?:assets|visual-inbox)\/[^"')\s]+\.(?:webp|png|jpe?g|svg))/gi);
  for (const match of matches) if (!knownPaths.has(match[1])) errors.push(`${source.path}: referenced image is missing or unregistered: ${match[1]}`);
  if (!['.html', '.md'].includes(path.extname(source.path).toLowerCase())) continue;
  for (const match of source.content.matchAll(/<img\b[^>]*>/gi)) {
    const tag = match[0];
    const src = (tag.match(/\bsrc\s*=\s*["']([^"']+)/i) || [])[1] || '(unknown src)';
    for (const attribute of ['alt', 'width', 'height']) if (!new RegExp(`\\b${attribute}\\s*=`, 'i').test(tag)) errors.push(`${source.path}: img ${src} missing ${attribute}`);
    if (!/\bdecoding\s*=\s*["']async["']/i.test(tag)) errors.push(`${source.path}: img ${src} missing decoding=async`);
    const isHero = /\bfetchpriority\s*=\s*["']high["']/i.test(tag);
    if (!isHero && !/\bloading\s*=\s*["']lazy["']/i.test(tag)) errors.push(`${source.path}: img ${src} missing loading=lazy`);
  }
}

console.log(`Image files: ${images.length}`);
console.log(`Manifest records: ${records.length}`);
console.log(`Duplicate binary groups: ${[...hashGroups.values()].filter(group => group.length > 1).length}`);
console.log(`Unused registered images: ${warnings.length}`);
for (const warning of warnings) console.log(`WARN: ${warning}`);
for (const error of errors) console.error(`ERROR: ${error}`);
if (errors.length) {
  console.error(`FAIL: ${errors.length} serious image-library issue(s).`);
  process.exit(1);
}
console.log('PASS: image library paths, metadata, hashes, references and page image attributes are consistent.');
