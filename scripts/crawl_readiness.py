#!/usr/bin/env python3
"""Check production sitemap URLs, canonical counts, and internal discoverability."""

import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from html import unescape

BASE = "https://ouyangthermal.github.io/"


def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": "OUYANG-Technical-QA/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.status, response.geturl(), response.read().decode("utf-8", "replace")


_, _, sitemap = get(urllib.parse.urljoin(BASE, "sitemap.xml"))
root = ET.fromstring(sitemap)
urls = [node.text for node in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
known = {url.rstrip("/") for url in urls}
inbound = {url: 0 for url in known}
errors = []
bad_canonicals = []

def inspect(url):
    try:
        status, final_url, html = get(url)
        result_errors = []
        if status != 200 or final_url.rstrip("/") != url.rstrip("/"):
            result_errors.append((url, status, final_url))
        canonical_bad = len(re.findall(r'<link[^>]+rel=["\']canonical["\']', html, re.I)) != 1
        links = []
        for href in re.findall(r'href=["\']([^"\']+)', html, re.I):
            linked = urllib.parse.urljoin(url, unescape(href)).split("#")[0].split("?")[0].rstrip("/")
            if linked in inbound and linked != url.rstrip("/"):
                links.append(linked)
        return result_errors, canonical_bad, links
    except Exception as error:
        return [(url, "ERROR", str(error))], False, []


with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(inspect, url): url for url in urls}
    for future in as_completed(futures):
        url = futures[future]
        result_errors, canonical_bad, links = future.result()
        errors.extend(result_errors)
        if canonical_bad:
            bad_canonicals.append(url)
        for linked in links:
            inbound[linked] += 1

orphans = [url for url, count in inbound.items() if count == 0 and url != BASE.rstrip("/")]
print(f"sitemap_urls={len(urls)}")
print(f"http_or_redirect_errors={len(errors)}")
print(f"non_single_canonical={len(bad_canonicals)}")
print(f"orphan_pages={len(orphans)}")
if errors:
    print("errors:", errors)
if bad_canonicals:
    print("bad_canonicals:", bad_canonicals)
if orphans:
    print("orphans:", orphans)
