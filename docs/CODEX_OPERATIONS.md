# Codex Operations Manual

Use this manual together with `AGENTS.md` and `PROJECT_HANDOFF.md`. Commands assume the repository root and PowerShell-compatible quoting where necessary.

## READ — inspect before acting

```bash
git status --short --branch
git remote -v
git branch -vv
git log -5 --oneline --decorate
rg --files _articles
rg -n "^(title|description|permalink|published):" _articles .
rg -n "target phrase" _articles *.md *.html
```

Search keywords in `data/keyword-map.csv`. Search images in `data/image-library.json`, then read `docs/IMAGE_LIBRARY.md`. Inspect actual references with `rg -n "filename.webp" .`.

## CREATE — add an article safely

1. Search existing pages and the keyword map. Record why the intent is distinct.
2. During review, keep the file in `drafts/` with `published: false`.
3. After approval, place it under the appropriate `_articles/<category>/` folder with a lowercase, hyphenated English filename.
4. Follow existing article Front Matter. Required operational fields are:

```yaml
---
title: "Unique visible title"
description: "Accurate, unique search description"
category: "Thermal Pad"
category_slug: "thermal-pad"
category_url: "/thermal-pad/"
author: "Ouyang Xiaohui"
date: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Commercial articles may also use the existing `contact_message`, email subject and contextual CTA fields. Do not add an H1 inside article Markdown because `_layouts/article.html` renders the H1 from `title`.

5. Use a direct answer, engineering explanation, parameters and units, application selection logic, mistakes, validation method, FAQ, related guides and restrained CTA.
6. Use Liquid-aware internal links, for example `[Guide]({{ '/thermal-pad/' | relative_url }})`.
7. To add an image, first read the image manifest, obey `reuse_policy`, supply accurate width, height, alt, loading and decoding attributes, then update both image-library files.
8. Published `_articles` are output through the configured collection and normally enter the generated sitemap. Confirm the built sitemap rather than assuming.

## UPDATE — retain URL equity

- Edit the existing source file mapped to the current public URL.
- Do not rename the file, category folder or explicit `permalink` unless a migration is approved.
- Preserve the original intent; update `updated` when the content materially changes.
- Keep title/description unique and canonical self-referential.
- Add evidence and useful sections without erasing valid content or unrelated user edits.
- When the same primary keyword maps to an existing URL, enhance that URL instead of publishing a competitor.

## DELETE — exceptional operation

Delete only after explicit user approval and a documented reason. Before deletion:

```bash
rg -n "exact-public-slug|source-filename" .
```

Check navigation, hubs, articles, sitemap, feed, image manifest, structured data and external importance. Prefer updating stale content. If the URL has backlinks, traffic or an equivalent destination, create and verify a permanent redirect using a project-compatible method before removal. GitHub Pages/Jekyll does not provide server configuration, so never promise a redirect until the implementation is proven. After deletion, rebuild and confirm no internal 404.

## SEARCH — prevent cannibalization

```bash
rg -ni "primary keyword|close synonym" _articles . --glob "*.md" --glob "*.html"
rg -n "Existing URL" data/keyword-map.csv
```

Compare search intent, not just exact words. Two pages conflict when they answer substantially the same user need for the same audience. Choose `UPDATE` if an existing page can satisfy it; `CREATE` only when the audience, application or decision task is genuinely distinct; otherwise `SKIP`.

## BUILD

Do not casually upgrade dependencies. This repository uses `gem "github-pages"` and has no lockfile.

```bash
bundle install
bundle exec jekyll build
bundle exec jekyll serve
```

Use a Ruby/Bundler environment compatible with current GitHub Pages. If the local machine lacks Ruby, use the established isolated validation branch/worktree or a temporary non-publishing GitHub Actions build. Never merge or deploy merely to test. A successful command is necessary but not sufficient: inspect `_site` and run the tests below.

## TEST

Current lightweight checks:

```bash
node scripts/audit-image-library.js
python scripts/check_site.py
git diff --check
```

After a Jekyll build, verify:

- Every changed HTML page has one intended H1, title and meta description.
- Every internal link resolves in `_site`.
- `sitemap.xml` parses as XML and contains canonical published URLs only.
- `robots.txt` allows formal content and names the production sitemap.
- Each published page has exactly one self-referential canonical.
- No published URL returns or builds as 404.
- `/discuss-your-application/` submits only to the configured private endpoint.
- `/inquiry-received/` remains noindex and outside sitemap.
- WhatsApp, email and telephone CTAs retain their intended values.
- Mobile layout and images do not overflow or cause avoidable layout shift.

For a production read-only audit, `scripts/geo_audit.py` accepts a base URL and output directory. Do not run submission helpers unless explicitly authorized.

## GIT — review before recording

```bash
git status --short --branch
git diff
git diff --check
git add <explicit-file-list>
git diff --cached
git commit -m "Concise description"
git push origin main
```

Never use broad staging without reviewing untracked files. The final push command requires explicit user authorization unless the current request already instructs deployment. Do not force push.

## DEPLOY

Current repository documentation configures GitHub Pages to deploy `main` from `/(root)`. A push to `main` triggers GitHub Pages' Jekyll build. `.github/workflows/daily-geo-audit.yml` is monitoring only and is not the deploy workflow.

After pushing, open the repository Actions/Deployments/Pages view and wait for the specific commit to complete. Record the commit SHA and deployment URL. If Settings → Pages differs from this document, stop and update the handoff with verified reality before changing anything.

## VERIFY — production acceptance

Check HTTP status and rendered content for:

- `https://ouyangthermal.github.io/`
- Every changed or new URL.
- `https://ouyangthermal.github.io/sitemap.xml`
- `https://ouyangthermal.github.io/robots.txt`
- `https://ouyangthermal.github.io/discuss-your-application/`
- `https://ouyangthermal.github.io/googlebd2df6f2d347ec36.html`

Parse the sitemap with an XML parser, verify canonical tags in final HTML, test internal links, confirm no public inquiry data appears, and inspect desktop/mobile layouts. Do not rely only on a browser visually opening a page.

## ROLLBACK — recover without destroying work

For a deployed bad commit, inspect history and create a new inverse commit:

```bash
git status --short --branch
git log -5 --oneline --decorate
git revert <bad-commit-sha>
git diff --cached
git push origin main
```

Use `git revert` because it preserves history. Before reverting, protect or commit unrelated local changes and understand whether later commits depend on the target. Never use `git reset --hard`, `git clean`, destructive checkout, history rewriting or force push unless the user explicitly authorizes the exact operation and its consequences.
