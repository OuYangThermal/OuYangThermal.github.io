# OUYANG THERMAL GEO Discovery Baseline Audit

**Audit date:** 2026-09-15 (Asia/Shanghai)

**Scope:** Production site and current `main` source snapshot; read-only external checks; no production change or Search Console access.
**Commercial objective:** Engineering discovery → direct contact → benchmark → sample → validation → second-source qualification → RFQ.

## Executive baseline

The site has moved beyond a launch-stage brochure. It is an **early discovery / evidence-building site** with 89 public sitemap URLs, 39 technical articles, application and supplier-evaluation hubs, direct-contact routes, structured article metadata, and two genuine benchmark-evidence pages.

The public technical baseline is healthy: the 2026-09-15 live audit reached all 89 sitemap URLs with HTTP 200, found no critical or high-priority canonical, schema or broken-link problem, and measured a 664 ms average response time. `robots.txt` allows Googlebot, Bingbot, OAI-SearchBot, GPTBot and other named crawlers. `sitemap.xml` and `llms.txt` are public. This is **crawl readiness**, not proof of index coverage or ranking.

### External data boundary

- **Google Indexing / impressions / clicks / CTR / average position:** `NOT VERIFIED — GSC DATA UNAVAILABLE`.
- **Bing Webmaster indexed-page data:** `NOT VERIFIED — BING WEBMASTER DATA UNAVAILABLE`.
- **Exact Google and Bing rankings:** `NOT VERIFIED — no reproducible, locale-controlled SERP dataset was retained.`
- The Google verification file is deliberately a minimal verification artifact. Its missing title/H1/canonical warnings are expected and must not be “fixed” or removed.

## Production technical audit

| Area | Finding | Status | Action |
|---|---|---:|---|
| Homepage | Public, one clear H1, contact card, phone/email and commercial paths above the fold. | Good | Keep direct-contact prominence. |
| Product/application hubs | Thermal pad, gel, insulation, OBC, PCS, server and optical clusters exist. | Good | Strengthen evidence links within money-page clusters. |
| Engineering resources | Four core calculators/selectors plus qualification generator are public and linked. | Good | Simplify only the TDS comparison first screen; do not rebuild tools now. |
| Articles | 39 technical articles; article layout exposes author, published/updated dates, TechArticle and breadcrumb schema. | Good | Standardize visible “Related Guides” headings where the audit parser flags variants. |
| Case / benchmark evidence | Two benchmark-evidence pages exist; Case 001 states methods, conditions, limits and disclosures. | Strong differentiator | Add more evidence only after provenance and review gates. |
| Robots / sitemap / llms | HTTP 200; crawler access allowed; 89 URLs on sitemap. | Good | Preserve exact implementation. |
| Canonical / schema | Unified self-canonical template; TechArticle and BreadcrumbList on article pages. | Good | Add FAQPage only when FAQ content is materially maintained and eligible. |
| Internal links | No high-priority broken internal links in live audit. | Good | Add reciprocal money-page ↔ evidence links before adding content. |
| CTA / contact | WhatsApp, email, call and private-question routes are available on commercial pages. | Good | Give each money page one primary “Benchmark” or “Sample” CTA, while retaining direct options. |
| Orphan risk | Sitemap pages are reachable; no formal orphan finding in the live audit. | Monitor | Recheck after each new page or cluster edit. |

### Why the 45 live-audit warnings are not all content defects

Thirty-nine warnings come from a deliberately narrow parser that expects exact labels such as `Related Guides`, `Direct Answer`, and `Technical Explanation`. Many pages use equivalent labels such as “Related OBC and gel guides,” “What engineers should compare,” or “Answer first.” Treat this as a **consistency opportunity**, not a reason to mechanically rewrite published engineering content. Six warnings are correctly attributable to the required Google verification file and should be ignored.

## Discovery matrix

**Reading rule:** “Current competitor” and “competitor URL” must not be guessed. The matrix records `NOT VERIFIED` where a reproducible, locale-controlled result was not retained. “Competitor type” describes the result family to beat, not a claimed current ranking.

| Keyword | Intent | Google indexed? / ranking | Bing indexed? | Existing Ouyang page | Competitor / URL | Competitor type | Gap and recommended action | Commercial value | AI citation potential | Priority |
|---|---|---|---|---|---|---|---|---:|---:|---|
| thermal pad supplier China | Supplier evaluation | NOT VERIFIED — GSC DATA UNAVAILABLE / NOT VERIFIED | NOT VERIFIED | `/thermal-pad-supplier-china/` | NOT VERIFIED | Supplier, distributor, directory | UPDATE: add evidence-index table and benchmark CTA; do not claim manufacturer status. | Very high | 78 | P1 |
| thermal interface material supplier China | Supplier / second source | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/china-thermal-interface-material-supplier/` | NOT VERIFIED | Supplier evaluation / directory | UPDATE: this is the canonical general second-source page; lead with the gated qualification table. | Very high | 92 | P0 |
| thermal gel supplier China | Supplier / process validation | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/thermal-gel-supplier-china/` | NOT VERIFIED | Supplier / product page | UPDATE: surface dispensing, void and multi-lot evidence links above the fold. | Very high | 84 | P1 |
| thermal pad manufacturer China | Supplier discovery | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/thermal-pad-supplier-china/` | NOT VERIFIED | Manufacturer claims / directories | UPDATE: answer sourcing intent without asserting ownership; distinguish supplier route from manufacturing proof. | Very high | 76 | P1 |
| thermal gap filler supplier China | Supplier / category selection | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/thermal-gel-supplier-china/` and `/thermal-pad-supplier-china/` | NOT VERIFIED | Product supplier pages | UPDATE: add a short pad-vs-gel decision bridge; preserve distinct URLs. | High | 75 | P2 |
| SP2000 alternative | Alternative / benchmark | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/sp2000-alternative-evaluation/` | NOT VERIFIED | Brand alternative pages | UPDATE: promote Case 001 method/condition table and a controlled-benchmark CTA. | Very high | 93 | P0 |
| Bergquist SP2000 alternative China | Alternative / sourcing | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/sp2000-alternative-evaluation/` | NOT VERIFIED | Brand / distributor pages | UPDATE: retain comparative-identification disclosure; do not create a second overlapping page. | Very high | 91 | P0 |
| Laird thermal pad alternative | Alternative / qualification | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/china-thermal-interface-material-supplier/` | NOT VERIFIED | Brand alternative pages | UPDATE existing general second-source hub with a brand-neutral “incumbent reference” module; no brand-targeted clone. | Very high | 86 | P1 |
| Henkel thermal pad alternative | Alternative / qualification | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/china-thermal-interface-material-supplier/` | NOT VERIFIED | Brand alternative pages | UPDATE existing general second-source hub; use “benchmark candidate” language. | Very high | 86 | P1 |
| thermal interface material second source China | Second-source qualification | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/china-thermal-interface-material-supplier/` | NOT VERIFIED | Supplier qualification / engineering guidance | UPDATE: make this the page’s explicit secondary target and link its qualification generator. | Very high | 95 | P0 |
| thermal pad for OBC | Application selection | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/obc/thermal-pad-vs-thermal-gel-for-obc/` | NOT VERIFIED | Supplier / application articles | UPDATE: add interface map and pad-specific evidence cross-links on existing OBC cluster. | High | 82 | P1 |
| thermal gel for OBC | Application / dispensing | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/obc/obc-thermal-gel-second-source-qualification/` | NOT VERIFIED | Supplier / application articles | UPDATE: state gap, process and validation questions before material direction. | Very high | 94 | P0 |
| thermal pad for optical transceiver | Application selection | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/optical-module/thermal-pad-selection-for-optical-modules/` | NOT VERIFIED | Optical component supplier / technical guide | UPDATE: add a single decision table for gap, force, contamination and rework. | High | 87 | P1 |
| thermal interface material for optical module | Application overview | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/optical-module/thermal-interface-materials-for-optical-transceivers/` | NOT VERIFIED | Component supplier / technical guide | UPDATE: use this as cluster hub; add links to 800G and 1.6T evidence constraints. | High | 86 | P1 |
| thermal pad for AI server | Application selection | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/server/thermal-pad-vs-thermal-gel-for-ai-servers/` | NOT VERIFIED | Data-center supplier / technical guide | UPDATE: add a rack/serviceability/pressure decision block. | High | 84 | P1 |
| thermal interface material for AI server | Application overview | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/server/thermal-management-materials-for-ai-servers/` | NOT VERIFIED | Data-center supplier / technical guide | UPDATE: replace generic architecture emphasis with interface-by-interface evidence roadmap. | High | 85 | P1 |
| thermal gel for battery pack | Application / liquid cooling | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/battery-pack/thermal-gel-for-battery-pack-liquid-cooling-plates/` | NOT VERIFIED | Battery supplier / technical guide | UPDATE: add installation geometry, compression/coverage and aging evidence requests. | High | 82 | P2 |
| thermal interface material for PCS | Application / power electronics | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/pcs/tim-selection-for-pcs/` | NOT VERIFIED | Power-electronics supplier / technical guide | UPDATE: connect PCS page to insulation and installed-resistance evidence. | High | 79 | P2 |
| how to select thermal pad thickness | Engineering selection | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/thermal-pad/thermal-pad-thickness-selection-guide/` | NOT VERIFIED | Engineering guide / calculator | UPDATE: link calculator result → validation checklist → direct contact. | High | 88 | P1 |
| how to qualify second source thermal interface material | Qualification workflow | NOT VERIFIED / NOT VERIFIED | NOT VERIFIED | `/china-thermal-interface-material-supplier/` | NOT VERIFIED | Supplier qualification / technical guide | UPDATE: retain as primary workflow and use the existing generator as supporting, not primary, conversion. | Very high | 96 | P0 |

## Five money pages

| Priority | Existing coverage | Recommended action | Main conversion |
|---|---|---|---|
| P0 | SP2000 Alternative Evaluation + Case 001 | Strengthen existing URL; no new alternative page. | Benchmark request |
| P0 | China TIM Supplier Evaluation / generic second-source framework | Strengthen existing URL; make it the canonical qualification hub. | Benchmark → sample → RFQ |
| P0 | OBC thermal gel second-source qualification | Strengthen existing article and OBC hub link architecture. | Controlled sample discussion |
| P1 | Optical Transceiver TIM Supplier Evaluation | Strengthen existing URL and optical cluster; no new URL. | Optical module evaluation |
| P1 | AI Server thermal management cluster | Strengthen existing hub and power-supply article; no new generic duplicate. | Application discussion / benchmark |

Detailed briefs and the scoring rubric are in [MONEY_PAGE_PRIORITY.md](../docs/MONEY_PAGE_PRIORITY.md).

## AI citation readiness

The site already has important citation foundations: answer-first blocks, author identity, dates, canonical tags, TechArticle schema, controlled language, direct source/standard references and a published internal benchmark case with conditions. The limiting factor is not the absence of more articles; it is the sparse distribution of **reproducible evidence blocks** across application and supplier pages.

| Page / cluster | AI citation readiness | Commercial intent | Engineering trust | Conversion readiness | Primary improvement |
|---|---:|---:|---:|---:|---|
| SP2000 Alternative Evaluation + Case 001 | 88 | 96 | 91 | 91 | Put test condition, scope and non-equivalence limit into one reusable evidence table. |
| China TIM Supplier Evaluation | 90 | 97 | 88 | 93 | Elevate the gated qualification table; link to evidence only where provenance supports it. |
| OBC thermal-gel second source | 91 | 96 | 89 | 92 | Add a compact “evidence required at each gate” table and one named, cited method section. |
| Optical Transceiver TIM Supplier Evaluation | 75 | 89 | 76 | 90 | Add application-specific force, contamination, BLT and post-aging evidence requirements. |
| AI-server TIM cluster | 74 | 90 | 77 | 86 | Add explicit interface map and power-module / serviceability limits, then cite sources. |

Scores are an internal content-structure assessment, not an AI-platform rank or citation prediction.

## Conversion and tool audit

Direct WhatsApp, email, call and private-question paths are consistently available on commercial pages. This is a strength: an engineer with an active project can contact Owen without a long form.

The compression calculator has 2 required plus 2 optional values; the selector and qualification generator each have 5 required inputs. These meet the intended lightweight pattern. The TDS comparison tool exposes a full two-column technical worksheet (12 fields per material), which is valuable later in a benchmark but too dense as a first interaction. **Do not rebuild it in this phase.** When approved, introduce a 3-input “compare only what matters first” entry path that reveals the full matrix only after a result.

## GSC DATA PENDING

Before treating any page as indexed or prioritizing by impressions, export or read the following for the last 28 and 90 days: queries, pages, countries, devices, impressions, clicks, CTR and average position. Map each observed query to the existing canonical URL before adding or changing content. This is a measurement task, not a reason to alter sitemap, canonical or robots implementation.

## Next best action

**Strengthen `/china-thermal-interface-material-supplier/` as the canonical TIM second-source qualification hub, starting with a sourced, reusable “evidence by gate” table and a single primary Benchmark CTA.**

It has the highest combined commercial intent, broadest internal-link leverage, strongest fit with existing qualification tools and least cannibalization risk. It can improve the full path from discovery to benchmark/sample/RFQ without publishing a new URL or making unverified supplier claims.
