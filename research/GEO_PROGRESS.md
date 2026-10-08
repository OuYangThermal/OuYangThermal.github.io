# GEO Progress — OUYANG THERMAL (Phase II: Authority → Discovery → Inquiry)

Standing baseline and change log. KPIs here are discovery and commercial inquiry, not page count.

## Baseline — 2026-10-02 (Phase II kickoff)

| Metric | Value | Source / note |
|---|---|---|
| Sitemap URLs (formal) | 82 | project-state.json (pre-new-page) |
| GSC clicks / impressions | 5 / 24 | 2026-09-09 → 2026-09-25, filter-free read |
| Avg CTR / position | 20.8% / 8.8 | same read |
| Receiving pages | homepage only | all other pages 0 impressions |
| Queries | "thermal interface material" 2 impr, pos 1.5, 0 clicks; 5 clicks anonymized per-query by Google | do not claim brand/seed-keyword traffic |
| Geography | 100% United States | same read |
| GSC access | **BLOCKED since 2026-09-30** (Google session expired) | OWNER ACTION: user re-signs in to Google in the managed browser |
| Benchmark cases | 2 (Case 001 FT-BN035, Case 002 FT-BN050) | /benchmark-evidence/ |
| Engineering tools | 5 (selection, resistance calc, compression calc, TDS comparison, second-source generator) | /engineering-resources/ |
| Commercial/money pages | 5 (sp2000-alternative-evaluation, thermal-pad-supplier-china, thermal-gel-supplier-china, obc-thermal-material-supplier, china-thermal-interface-material-supplier) | + 1 added today (see below) |
| External mentions / new backlinks | none verified | no GSC data available; do not claim |
| Verified inquiries | none reported to date | no fabricated leads |

## 2026-10-02 — Phase II audit + first actions

**Audit finding:** Benchmark Library (Case 001/002), CTA infrastructure (quick-contact, sticky-contact, WhatsApp/Email), FAQPage schema, llms.txt all in place. Highest-value gap: zero coverage of cluster A keyword "Dow 5121C alternative / replacement" (no page, no keyword-map entry, only incidental mentions). Everything except the homepage is invisible in GSC — new money pages need internal links to be discoverable.

**Action 1:** Created `/dow-5121c-alternative-evaluation/` money page. Mirrors the SP2000 evaluation pattern (qualification framework, benchmark workflow, FAQ + FAQPage JSON-LD, simple Email/WhatsApp CTA). **No invented incumbent data** — page states explicitly that no Dow 5121C test data is published and evaluation starts from the reader's own TDS. Brand disclaimer included. Benchmark method diagram NOT reused (image-library reuse_policy = primary-page-only for that SVG).

**Action 2:** Internal-link / index sync: added Dow page link to SP2000 page "Related engineering guides"; added page to llms.txt; added Tier B entries to `growth/KEYWORD_MAP.md` and `data/keyword-map.csv`.

**Validation:** Jekyll build PASS; production HTTP 200 on new URL; sitemap regenerated automatically (jekyll-sitemap).

- URLs: https://ouyangthermal.github.io/dow-5121c-alternative-evaluation/
- Commit: e9ea342 ("GEO Phase II: add Dow 5121C alternative evaluation page + keyword map sync") — pushed 2026-10-02, local clone re-synced to origin/main
- Production: new URL returns HTTP 200; SP2000 page (internal-link edit) returns 200
- Unverified: GSC impressions/clicks for the new page (no access until owner re-signs in); actual search demand for "Dow 5121C alternative" (no autocomplete evidence — hypothesis, monitor).

**Next:** Watch for new page entering coverage once GSC access returns; consider indexing request for the new URL; continue Phase II with OBC/ESS/SiC cluster work per priority order.

## 2026-10-07 — Dow TC-3120 reference citation on 5121C alternative page

**Action:** Added a "What Dow publicly offers today" section to `/dow-5121c-alternative-evaluation/` citing Dow's May 28, 2026 DOWSIL™ TC-3120 Thermal Gel launch (~12 W/m·K silicone gel, 800G/1.6T optical modules, 200 µm min bondline, −45 to 150 °C, reworkable, minimal oil bleed/outgassing). Facts verified against the official Dow press release (corporate.dow.com) and Dow product page before push. Explicit non-equivalence disclaimer included; no incumbent test data invented.

- Staged from earlier GEO run; facts verified 2026-10-07. Push deferred: research-stage network policy blocks GitHub API writes, so build → push → production 200 verification is queued for the delivery agent. Local clone files (page + this log) are ready to push as-is.
