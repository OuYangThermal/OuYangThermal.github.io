# OUYANG THERMAL Indexing Checklist

Actions below require access to third-party webmaster accounts or domain verification. They are deliberately not represented as completed.

## Google Search Console — MANUAL ACTION REQUIRED

- [ ] Add or select the property for `https://ouyangthermal.github.io/`.
- [ ] Complete the verification method requested by Google.
- [ ] Submit `https://ouyangthermal.github.io/sitemap.xml`.
- [ ] Use URL Inspection on the homepage and six commercial-intent pages.
- [ ] Request indexing only where Google reports a page is not indexed and no technical exclusion applies.
- [ ] Review Page indexing, HTTPS, Core Web Vitals, and manual-action reports.
- [ ] Run `site:ouyangthermal.github.io` and branded queries; record observations in `GEO-VALIDATION.md`.

## Bing Webmaster Tools — MANUAL ACTION REQUIRED

- [ ] Add or import the site property.
- [ ] Complete ownership verification.
- [ ] Submit `https://ouyangthermal.github.io/sitemap.xml`.
- [ ] Inspect the homepage and six commercial-intent URLs.
- [ ] Use Bing URL Submission only for important changed URLs and within platform rules.
- [ ] Review crawl information, indexing coverage, and blocked-resource reports.
- [ ] Run `site:ouyangthermal.github.io` and branded queries; record real observations only.

## Repeatable technical checks

- [ ] Confirm `/robots.txt` returns HTTP 200 and declares the canonical sitemap.
- [ ] Confirm `/sitemap.xml` is valid XML, contains only canonical production URLs, and contains no 404s.
- [ ] Confirm `/llms.txt` returns HTTP 200 and lists only real resources and contacts.
- [ ] Confirm each core page has one title, one H1, one canonical, and valid JSON-LD.
- [ ] Confirm mobile viewport and direct WhatsApp, email, and telephone links.
- [ ] Confirm no page is unintentionally `noindex`; `/404.html` and internal benchmark pages are intentionally excluded.

## Status vocabulary

- **MANUAL ACTION REQUIRED** — an authenticated owner action is needed.
- **NOT TESTED** — no reliable test has been performed.
- **PASS / FAIL** — use only after a reproducible check.
