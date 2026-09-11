# OUYANG THERMAL PROJECT HANDOFF

If you are a new Codex/AI agent taking over this repository,
READ THIS FILE FIRST.

## Project purpose

OUYANG THERMAL is an engineering knowledge and commercial lead-generation website for global B2B thermal-management customers. It is not a community, public comment system, generic factory brochure, or unverified customer-case catalogue.

Core materials: Thermal Pad, Thermal Gel, Thermal Grease, Thermal Potting Compound, Thermal Insulator, Thermal Structural Adhesive, and Thermal Interface Materials.

Core applications: OBC, DC/DC, PDU, IGBT, PCS, ESS, Battery Pack, BMS, Liquid Cooling, AI Server, Optical Module, Industrial Power, and Automotive Electronics.

Commercial path:

```text
Google / AI Search
→ Engineering Content
→ Technical Trust
→ WhatsApp / Email / Call
→ Technical Discussion
→ Benchmark
→ Sample
→ Qualification
→ RFQ
→ Order
```

## Repository and deployment

| Item | Current value |
| --- | --- |
| Repository | `OuYangThermal/OuYangThermal.github.io` |
| Repository URL | `https://github.com/OuYangThermal/OuYangThermal.github.io` |
| Git transport | HTTPS |
| Remote | `origin` → `https://github.com/OuYangThermal/OuYangThermal.github.io.git` |
| Default branch | `main` |
| Current branch at handoff | `main`, tracking `origin/main` |
| Production URL | `https://ouyangthermal.github.io/` |
| Deployment method | GitHub Pages, deploy from branch |
| Pages source | `main`, `/(root)` according to repository deployment documentation |
| Build method | GitHub Pages Jekyll build; no custom deploy workflow is present |
| Dependencies | `Gemfile` uses the `github-pages` gem group; no `Gemfile.lock`, so an exact local Jekyll version is not pinned |
| Site plugins | `jekyll-feed`, `jekyll-sitemap`, `jekyll-seo-tag` |

The only repository workflow currently present is `.github/workflows/daily-geo-audit.yml`. It audits the live site and updates a monitoring issue; it does not deploy the website. Verify Settings → Pages after authenticating a new account because the Pages API was not available in the handoff environment.

## Current factual state

Snapshot date: 2026-09-11 (Asia/Shanghai).

- Latest committed and deployed `main`: `e38ec72` — `Fix thermal pad hub front matter`; the preceding Day 1 content commit is `b643931`.
- Published technical article source count: 32 under `_articles/`.
- Live sitemap verification after Day 1 deployment: 66 formal URLs, including the two new Day 1 article URLs; XML parsing passed.
- Remaining local controlled-pilot material: the Day 1 brief and the Article A review copy under `drafts/controlled-pilot/day-1/`. Article B and C moved into the published collection.
- Keyword map: 70 rows in `data/keyword-map.csv` (currently untracked local work at handoff).
- Image manifest: 25 registered assets; last local audit found zero duplicate binary groups and two intentionally unused source/intake assets.
- Homepage: `/`.
- Private inquiry page: `/discuss-your-application/`.
- Success page: `/inquiry-received/`; it is `noindex, nofollow` and excluded from sitemap.
- Inquiry delivery: Formspree endpoint configured in `_config.yml`; submission is private and not rendered as public content.
- Direct contact paths: WhatsApp/phone `+86 133 6790 9790`; email `5672306@gmail.com`.
- Main product hubs include `/thermal-pad/`, `/thermal-gel/`, `/thermal-grease/`, `/potting-compound/`, `/thermal-insulator/`, and `/structural-adhesive/`.
- Main application hubs include `/applications/`, `/obc/`, `/battery-pack/`, `/energy-storage/`, `/pcs/`, `/power-electronics/`, `/server/`, and `/optical-module/`.
- Canonical URLs are emitted by `_includes/head.html` using `page.url | absolute_url`.
- Homepage and About/Contact structured data are also defined in `_includes/head.html`.

## Google Search Console and crawl status

The user confirmed Google Search Console ownership verification for `OuYangThermal.github.io` and submitted `https://ouyangthermal.github.io/sitemap.xml`. The verification file `googlebd2df6f2d347ec36.html` must remain at the repository root and must remain publicly available at:

`https://ouyangthermal.github.io/googlebd2df6f2d347ec36.html`

Recorded sitemap diagnosis:

- HTTP 200.
- `Content-Type: application/xml`.
- XML parser passed.
- Google Sitemap Protocol structure passed.
- `robots.txt` permits Googlebot and references the sitemap.
- Canonical checks passed.
- No sitemap `noindex` error, 404 URL, duplicate URL, localhost URL, preview URL, or malformed date was found.

Search Console initially displayed “Couldn't Fetch” shortly after verification/submission. No technical sitemap defect was found; the working assessment is Google-side first-fetch or processing delay. The homepage has had Request Indexing initiated. Do not redesign the sitemap merely to react to this transient status. Check Search Console again and use its current report as the authority.

## Directory map

- `_articles/` — 30 published technical articles, grouped by topic/application.
- `_layouts/`, `_includes/` — shared rendering, SEO, schema, navigation and conversion components.
- Product/application directories — formal landing and hub pages.
- `assets/` — CSS, JavaScript and published images.
- `data/` — image manifest, keyword map, opportunity queues and machine-readable project inputs.
- `docs/` — durable human instructions and audits; excluded from Jekyll output.
- `reports/` — keyword research and evidence outputs; local untracked work at this snapshot.
- `drafts/` — unpublished controlled-pilot work.
- `scripts/` — source, image, content and live-site audit utilities.
- `visual-inbox/` — temporary image intake only, never the canonical published asset directory.
- `.github/workflows/` — monitoring automation.

## Current GEO/SEO phase

The strategy is “Keyword Research First, Content Second.” Search-demand validation is complete. The current work phase is a **7-Day Controlled Pilot**, not unrestricted daily publishing.

Day 1 was approved, built, deployed and verified on 2026-09-11:

- Keyword brief: `drafts/controlled-pilot/day-1/keyword-brief.md`.
- Article A updated the existing China TIM supplier evaluation URL; no competing URL was created.
- Article B published at `/thermal-pad/thermal-pad-compression-set-explained/`.
- Article C published at `/obc/obc-thermal-gel-second-source-qualification/` and explicitly states that Search Demand is `Unknown`.

GitHub Pages deployment run `34550651609` completed successfully. The three target pages returned HTTP 200 with one H1, self-referential canonical and working contact paths. The live sitemap returned HTTP 200 with `Content-Type: application/xml` and included all three target URLs.

## Automation status

`Ouyang Thermal Daily GEO Content` is **PAUSED**. Do not resume it automatically. The current pilot requires:

```text
Keyword Brief → 3 Topics → Drafts → Internal Link Plan → Human Review
```

Commit, push and deploy are prohibited by default during the pilot unless the user explicitly approves them. The separate repository workflow named **OUYANG THERMAL Daily GEO Audit** is a monitoring workflow scheduled by GitHub Actions; do not confuse it with the paused content-production automation.

## Non-negotiable protections

- Preserve all published URLs, canonical behavior, sitemap and robots directives.
- Preserve the Google verification HTML file permanently.
- Preserve the private inquiry system and direct contact details unless explicitly instructed otherwise.
- Never create comments, public user submissions or indexed inquiry URLs.
- Never fabricate customer cases, supplier/manufacturer claims, authorization, search volume, test results, material specifications or certifications.
- Search for an existing mapped URL before creating content. Prefer updating a suitable page to creating a near-duplicate.
- Read `data/image-library.json` before assigning an image and obey its authenticity and reuse fields.
- Never put a secret in Git, documentation, Actions logs or public output.
- Preserve all uncommitted files when taking over.

## First actions for a new agent

Perform the read-only audit in `NEW_CODEX_START_PROMPT.md`. Compare the live repository and Search Console status with this snapshot. Then review `NEXT_ACTIONS.md`; do not make changes until the user chooses the next task.
