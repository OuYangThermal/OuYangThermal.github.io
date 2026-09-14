#!/usr/bin/env python3
"""Validate the rendered Case 002 page and its publication boundaries."""

from __future__ import annotations

import sys
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

SITE_ORIGIN = "https://ouyangthermal.github.io"
CASE_PATH = "/benchmark-evidence/ft-bn050-thermal-resistance-vs-thickness/"
CRITICAL_PATHS = {
    "/benchmark-evidence/",
    "/thermal-pad/",
    "/engineering-resources/tim-selection-tool/",
    "/engineering-resources/thermal-pad-compression-calculator/",
    "/engineering-resources/tim-tds-comparison-tool/",
    "/comparison/thermal-conductivity-vs-thermal-resistance/",
    "/testing/why-can-the-same-thermal-material-produce-different-test-results/",
    "/benchmark-your-current-tim/",
    "/request-sample/",
    "/discuss-your-application/",
}


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []
        self.links = set()
        self.images = []

    def handle_starttag(self, tag, attrs):
        values = {key: value or "" for key, value in attrs}
        if tag == "link" and values.get("rel") == "canonical":
            self.canonicals.append(values.get("href", ""))
        elif tag == "a" and values.get("href"):
            self.links.add(values["href"])
        elif tag == "img":
            self.images.append(values)


def rendered_path(site, path):
    parsed = urlparse(path)
    candidate = site / parsed.path.lstrip("/")
    if parsed.path.endswith("/"):
        return candidate / "index.html"
    return candidate if candidate.suffix else candidate / "index.html"


def fail(message):
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    page_file = rendered_path(site, CASE_PATH)
    if not page_file.is_file():
        fail(f"Case 002 rendered page missing: {page_file}")
    html = page_file.read_text(encoding="utf-8")
    parser = Parser()
    parser.feed(html)

    expected = SITE_ORIGIN + CASE_PATH
    if parser.canonicals != [expected]:
        fail(f"canonical mismatch: {parser.canonicals!r}")
    print("PASS: canonical")

    required = (
        "0.179 °C·in²/W",
        "0.292 °C·in²/W",
        "Internal ASTM D5470 testing at 50 psi",
        "This is not a third-party certification report or product guarantee",
        "No customer endorsement is implied",
        "does not establish thermal conductivity",
    )
    missing = [phrase for phrase in required if phrase not in html]
    if missing:
        fail(f"required Case 002 content missing: {missing}")
    if re.search(r"[\u4e00-\u9fff]", html):
        fail("source-language text appears in the public Case 002 page")

    images = [img for img in parser.images if "/benchmark-evidence/case-002/" in img.get("src", "")]
    if len(images) != 3:
        fail(f"expected 3 Case 002 images, found {len(images)}")
    for image in images:
        if any(not image.get(key) for key in ("src", "alt", "width", "height")):
            fail(f"image attributes incomplete: {image}")
        if not rendered_path(site, image["src"]).is_file():
            fail(f"rendered image missing: {image['src']}")
    print("PASS: rendered page, privacy boundaries and images")

    missing_links = [path for path in sorted(CRITICAL_PATHS) if path not in parser.links]
    broken = [path for path in sorted(CRITICAL_PATHS) if not rendered_path(site, path).is_file()]
    if missing_links or broken:
        fail(f"critical links missing={missing_links}, broken={broken}")
    print("PASS: critical links")

    root = ET.parse(site / "sitemap.xml").getroot()
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    locations = [node.text or "" for node in root.findall(f"{ns}url/{ns}loc")]
    if expected not in locations or len(locations) != len(set(locations)):
        fail("sitemap missing Case 002 or contains duplicates")
    print(f"PASS: sitemap ({len(locations)} URLs)")


if __name__ == "__main__":
    main()
