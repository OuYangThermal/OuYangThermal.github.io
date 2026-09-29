# Experiment Log

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
