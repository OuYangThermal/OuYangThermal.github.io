# Experiment Log

## 2026-10-08 — Weekly growth loop: Dow page discoverability + compression calculator upgrade

- **Money page pick:** `/dow-5121c-alternative-evaluation/` (opportunity score 19/25: commercial intent 4 / engineering relevance 4 / authority gain 3 / AI citation potential 4 / ease 4). The 2026-10-02 money page had only 1 inbound internal link (from SP2000 page) → discoverability was the binding constraint. Change: (a) pillar `/china-thermal-interface-material-supplier/` now links to the Dow page twice — inline in the second-source paragraph and in Related engineering guides; (b) Dow page "What engineers should compare" links "compression response" contextually to the compression calculator. No URL/title change (rank-protection rule); no invented incumbent data; SP2000 cross-link kept brand-neutral per that page's own disclaimer (an initial "Bergquist Sil-Pad 2000" wording was caught and corrected before push).
- **Engineering resource pick:** `/engineering-resources/thermal-pad-compression-calculator/` (score 20/25: intent 2 / relevance 5 / authority 4 / AI citation 4 / ease 5). Replicated the proven 2026-09-29 resistance-calculator packaging: "Model assumptions" paragraph; verifiable worked example (2.0 mm → 1.6 mm gap = 0.4 mm compression, 20% ratio; k = 6 W/m·K, 40×40 mm² → R ≈ 0.167 K/W — arithmetic checked); visible provenance "maintained by Ouyang Xiaohui (Owen Ouyang), Ouyang Thermal. Last reviewed 2026-10-08"; JSON-LD dateModified 2026-09-14 → 2026-10-08.
- **Hypothesis:** internal-link strengthening helps Google discover and crawl the Dow page; citable methodology packaging moves the compression calculator toward the format AI systems cite for how-to queries.
- **URLs:** https://ouyangthermal.github.io/dow-5121c-alternative-evaluation/ · https://ouyangthermal.github.io/engineering-resources/thermal-pad-compression-calculator/ · https://ouyangthermal.github.io/china-thermal-interface-material-supplier/
- **Commits:** 14ea1b7 (EMPTY — see incident) → recovery 582c344 (2 files, 12 insertions, 4 deletions; verified non-empty via git diff --stat before reporting).
- **Incident 2026-10-08 (shared-clone collision; cf. 2026-09-30 lesson):** this run's site edits sat uncommitted during the Gmail outreach work; the concurrent daily-GEO run pushed 936af2b ("Add Dow TC-3120 official citation", 2026-10-07 work) and its post-push `git reset --hard` wiped this run's uncommitted pillar/calculator edits — and swept this run's Dow-page edit into 936af2b (my exact wording visible in its diff). This run's push_website.py then pushed identical-to-base content → empty commit 14ea1b7. Detected via production check (Dow page live with the link, pillar/calculator stale) + `git diff 936af2b 14ea1b7 --stat` empty. Recovery: re-applied the two lost edits, rebuilt, re-validated, pushed 582c344 (verified non-empty), re-synced. Dow page needed no re-push (already live via 936af2b). Second self-inflicted wipe: the growth-log edits made after the first push were lost by this run's own post-recovery `reset --hard`; re-applied and pushed together this time.
- **Build:** Jekyll build PASS (LC_ALL=C.UTF-8 LANG=C.UTF-8); front matter YAML valid; canonicals correct; sitemap includes Dow page; growth/ exclusion intact; new links present in built HTML.
- **Production verified 2026-10-08:** homepage, Dow page, pillar, compression calculator, sitemap.xml, robots.txt, googlebd2df6f2d347ec36.html, request-sample — all HTTP 200; live-content re-verified after recovery push.
- **Result:** pending — check GSC in 2–4 weeks for Dow-page impressions once Google access is restored; AI retest next cycle for the calculator.

## 2026-09-27 — Pillar upgrade: /china-thermal-interface-material-supplier/

- **Hypothesis:** "thermal interface material" (seed keyword, GSC pos 1.5 on homepage) has supplier-intent variants with commercial value; a dedicated pillar capturing supplier/manufacturer/second-source intent will earn impressions Google currently gives the homepage.
- **Change:** Title → "China Thermal Interface Material Supplier | Ouyang Thermal"; description covers supplier/manufacturer/pad/gel/grease/benchmark/sample/second source; answer-first entity block; "What is a thermal interface material?" quotable short answer + FAQ JSON-LD; backlink from /sp2000-alternative-evaluation/.
- **URL:** https://ouyangthermal.github.io/china-thermal-interface-material-supplier/
- **Commit:** 64302961c08348d54fbb8aeb86618bc9dab3467c
- **Result:** pending — check GSC in 2–4 weeks for impressions on supplier-intent queries.
- **Risk note:** meta description says "TIM manufacturer" — identity claim to re-verify against company framework before further iteration.

## 2026-09-27 — Growth memory infrastructure

- **Change:** created `/growth/` (8 files + README), excluded from Jekyll build, seeded with first real GSC read.
- **Commit:** _pending push_

## 2026-09-27 — OBC second-source page (earlier)

- **URL:** https://ouyangthermal.github.io/obc/obc-thermal-gel-second-source-qualification/
- **Commit:** a41148d467fe2bace25f6bf793d1bad9d61b3414
- **Result:** production HTTP 200; GSC impressions pending.

## 2026-09-27 — AI server page (daily cron)

- **URL:** https://ouyangthermal.github.io/server/thermal-management-materials-for-ai-servers/
- **Commit:** 6836258
- **Result:** production HTTP 200; GSC impressions pending.

## 2026-09-29 — Weekly growth loop: pillar + calculator upgrade

- **Money page pick:** `/china-thermal-interface-material-supplier/` (opportunity score 18/25). Change: inline-linked Thermal Resistance Calculator in the R = t/(kA) section + added calculator to Related engineering guides. No URL/title change (rank-protection rule).
- **Engineering resource pick:** `/engineering-resources/thermal-resistance-calculator/` (score 19/25). Change: citable methodology packaging — model assumptions (steady-state 1-D), worked example (6 W/m·K, 1.0 mm, 40×40 mm² → ≈0.104 K/W), visible provenance "maintained by Ouyang Xiaohui (Owen Ouyang), last reviewed 2026-09-28"; JSON-LD dateModified → 2026-09-28.
- **Commit:** e501e3a (shipped via concurrent daily-GEO run; working tree was clean — no duplicate commit).
- **Production verified 2026-09-29:** calculator + pillar + homepage + sitemap.xml + robots.txt + googlebd2df6f2d347ec36.html + request-sample all HTTP 200; "Worked example" live on calculator page; pillar→calculator link live.
- **Build:** Jekyll build PASS (bundle install required first); canonical/sitemap/robots/growth-exclusion validated.
- **Risk note:** ~~meta description says "TIM manufacturer" — identity claim to re-verify against company framework before further iteration.~~ RESOLVED 2026-09-29: removed by `c40161e`; current meta reads "China thermal interface material supplier evaluation…". Verified live.
