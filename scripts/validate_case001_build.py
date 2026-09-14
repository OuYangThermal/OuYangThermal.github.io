#!/usr/bin/env python3
"""Validate the rendered Case 001 page without deploying it."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET


SITE_ORIGIN = "https://ouyangthermal.github.io"
CASE_PATH = "/benchmark-evidence/ft-bn035-vs-sp2000-reference-sample/"
CRITICAL_PATHS = {
    "/benchmark-evidence/",
    "/sp2000-alternative-evaluation/",
    "/comparison/sp2000-thermal-pad-alternative-what-parameters-should-engineers-compare/",
    "/comparison/thermal-conductivity-vs-thermal-resistance/",
    "/engineering-resources/thermal-pad-compression-calculator/",
    "/engineering-resources/tim-tds-comparison-tool/",
    "/engineering-resources/second-source-qualification-generator/",
    "/testing/why-can-the-same-thermal-material-produce-different-test-results/",
    "/benchmark-your-current-tim/",
    "/request-sample/",
    "/discuss-your-application/",
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.canonicals: list[str] = []
        self.links: set[str] = set()
        self.images: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "link" and values.get("rel") == "canonical":
            self.canonicals.append(values.get("href", ""))
        elif tag == "a" and values.get("href"):
            self.links.add(values["href"])
        elif tag == "img":
            self.images.append(values)


def rendered_path(site: Path, path: str) -> Path:
    parsed = urlparse(path)
    clean = parsed.path.lstrip("/")
    if not clean:
        return site / "index.html"
    candidate = site / clean
    if parsed.path.endswith("/"):
        return candidate / "index.html"
    if candidate.suffix:
        return candidate
    return candidate / "index.html"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    page_file = rendered_path(site, CASE_PATH)
    if not page_file.is_file():
        fail(f"Case 001 rendered page missing: {page_file}")

    html = page_file.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(html)

    expected_canonical = SITE_ORIGIN + CASE_PATH
    if parser.canonicals != [expected_canonical]:
        fail(f"canonical mismatch: {parser.canonicals!r}; expected {expected_canonical}")
    print("PASS: rendered canonical")

    required_phrases = (
        "Internal comparative testing under the stated conditions",
        "Not an independent third-party certification",
        "approximately 21% lower",
        "What this benchmark does not prove",
        "SP2000 is referenced solely for comparative identification",
    )
    missing_phrases = [phrase for phrase in required_phrases if phrase not in html]
    if missing_phrases:
        fail(f"rendered Case 001 content missing: {missing_phrases}")

    case_images = [img for img in parser.images if "/benchmark-evidence/case-001/" in img.get("src", "")]
    if len(case_images) != 5:
        fail(f"expected 5 Case 001 images, found {len(case_images)}")
    for image in case_images:
        missing = [key for key in ("src", "alt", "width", "height") if not image.get(key)]
        if missing:
            fail(f"Case image missing attributes {missing}: {image.get('src')}")
        image_file = rendered_path(site, image["src"])
        if not image_file.is_file():
            fail(f"rendered image missing: {image['src']}")
    print("PASS: Case 001 rendered page and five images")

    missing_links = []
    broken_targets = []
    for path in sorted(CRITICAL_PATHS):
        if path not in parser.links:
            missing_links.append(path)
        if not rendered_path(site, path).is_file():
            broken_targets.append(path)
    if missing_links:
        fail(f"critical links absent from Case 001: {missing_links}")
    if broken_targets:
        fail(f"critical link targets missing from build: {broken_targets}")
    print("PASS: critical links")

    sitemap_file = site / "sitemap.xml"
    if not sitemap_file.is_file():
        fail("rendered sitemap.xml missing")
    root = ET.parse(sitemap_file).getroot()
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    if root.tag != namespace + "urlset":
        fail(f"unexpected sitemap root: {root.tag}")
    locations = [node.text or "" for node in root.findall(f"{namespace}url/{namespace}loc")]
    if expected_canonical not in locations:
        fail("Case 001 canonical URL missing from sitemap")
    if len(locations) != len(set(locations)):
        fail("duplicate URLs found in sitemap")
    invalid = [url for url in locations if not url.startswith(SITE_ORIGIN + "/")]
    if invalid:
        fail(f"non-canonical sitemap origins found: {invalid[:5]}")
    print(f"PASS: sitemap ({len(locations)} URLs)")


if __name__ == "__main__":
    main()
