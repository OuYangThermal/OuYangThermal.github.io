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

## 2026-10-08 — Weekly growth loop

**Money page pick:** `/dow-5121c-alternative-evaluation/` (opportunity score 19/25). The new page had only 1 inbound internal link → discoverability was the binding constraint. Pillar page now links to it (inline in the second-source paragraph + Related engineering guides); Dow page "What engineers should compare" links "compression response" to the compression calculator (this edit landed via the concurrent daily run's 936af2b, verified live). No URL/title change; no invented incumbent data; SP2000 cross-link kept brand-neutral.

**Engineering resource pick:** `/engineering-resources/thermal-pad-compression-calculator/` (score 20/25). Replicated the 2026-09-29 resistance-calculator packaging: model assumptions, verifiable worked example (2.0 mm → 1.6 mm = 20% compression; 6 W/m·K, 40×40 mm² → R ≈ 0.167 K/W), visible author/date provenance, JSON-LD dateModified → 2026-10-08.

**Validation:** Jekyll build PASS; front matter/canonical/sitemap/robots/growth-exclusion verified in built output. Recovery push `582c344` verified non-empty (first push `14ea1b7` was empty — shared-clone collision, see EXPERIMENT_LOG); local clone re-synced to origin/main. Production: 8 URLs HTTP 200 (homepage, Dow page, pillar, compression calculator, sitemap.xml, robots.txt, googlebd2df6f2d347ec36.html, request-sample); live-content verified on all changed pages after recovery push.

**Outreach (5672306@gmail.com):** reply/bounce pre-check clean (no replies/bounces from voltera.io or allpcb.com). Voltera + ALLPCB follow-up #1 SENT 2026-10-08 as replies in original threads; follow-up #2 window 2026-10-09 – 2026-10-18 (final). PCBWay first pitch send BLOCKED by Gmail tool instability (3 failed attempts, 0 sends confirmed); prepared text saved as Gmail draft for one-click manual send. Mailer-daemon scan: FII hard bounce (known) + editor@electronicscooling.com bounce (2026-09-26) — both dead addresses, never retry; unrelated to this week's outreach.

**GSC:** still blocked (session expired since 2026-09-29; verified via live browser, no login attempted). Standing baseline: 5 clicks / 24 impressions. OWNER ACTION: user re-signs in to Google in the managed browser.

**Unverified:** Dow-page impressions/clicks (no GSC access); Perplexity AI retest results (browser task in flight at time of push — logged separately on arrival).

## 2026-10-07 — Dow TC-3120 reference citation on 5121C alternative page

**Action:** Added a "What Dow publicly offers today" section to `/dow-5121c-alternative-evaluation/` citing Dow's May 28, 2026 DOWSIL™ TC-3120 Thermal Gel launch (~12 W/m·K silicone gel, 800G/1.6T optical modules, 200 µm min bondline, −45 to 150 °C, reworkable, minimal oil bleed/outgassing). Facts verified against the official Dow press release (corporate.dow.com) and Dow product page before push. Explicit non-equivalence disclaimer included; no incumbent test data invented.

- Staged from earlier GEO run; facts verified 2026-10-07. Push deferred: research-stage network policy blocks GitHub API writes, so build → push → production 200 verification is queued for the delivery agent. Local clone files (page + this log) are ready to push as-is.
