# AI Visibility Log

Test how AI search systems answer TIM buying questions. Goal: become a citable
engineering source — never attempt to deceive AI systems.

## Test questions

1. What is thermal interface material?
2. How to select thermal pad?
3. China thermal interface material suppliers
4. SP2000 alternatives
5. Thermal pad for OBC
6. TIM for SiC module
7. TIM for IGBT
8. Thermal interface material for AI server

## Results

| Date | Platform | Question | Ouyang Thermal cited? | Competitors cited | Sources cited | Notes |
|---|---|---|---|---|---|---|
| 2026-09-27 | Google AI Overviews (Perplexity public quota exhausted, login required) | What is thermal interface material? | No | Laird, Parker Chomerics, Voltera, DigiKey | Voltera blog TIM Selection Guide, Laird TIM product page, ScienceDirect | Answer leans on supplier content hubs |
| 2026-09-27 | Google AI Overviews | How to select thermal pad? | No | Fujipoly (sidebar only) | ALLPCB guides (8-step selection process) | How-to guides win this query |
| 2026-09-27 | Google AI Overviews | China thermal interface material suppliers | No | Aochuan (Shenzhen), SinoGuide, Sheen, Naikos, Nuomi Glue | Made-in-China.com, sg-thermal.com, sheenmaterials.com | Domestic competitors cited via own sites + directories |
| 2026-09-27 | Google AI Overviews | SP2000 alternatives (thermal) | No | Bergquist (Sil-Pad 2000/A2000), Laird Tpcm, Krayden, MG Chemicals | New England Die Cutting, Krayden | Our /sp2000-alternative-evaluation/ not cited |
| 2026-09-27 | Google AI Overviews | Thermal pad for OBC (EV) | No | Jiuju, Sheen, MacDermid Alpha, Aochuan | jiujutech.com, sheenmaterials.com, MacDermid Alpha | Our OBC pages not cited |
| 2026-09-27 | Google AI Overviews | TIM for SiC power module | No | HALA, Semikron Danfoss, Infineon | IDTechEx, Infineon Developer Community, IEEE Xplore | Standards/community sources dominate |
| 2026-09-27 | Google AI Overviews | TIM for IGBT module | No | 3M, Bergquist, Panasonic, Shin-Etsu, Wakefield, Infineon, Fuji Electric | IEEE Xplore, Infineon Developer Community, Fuji app notes | Global brands dominate product queries |
| 2026-09-27 | Google AI Overviews | Thermal interface material for AI server | No | Honeywell PTM7950, Indium, Sheen, Krayden | ACS Material, Krayden blog, Indium Corp, NEDC | Our AI server page not cited |

## Rules

- Record what is observed; one AI answer is not a ranking.
- Note WHY competitors get cited (data tables? clear definitions? tools?) and close that gap with real content.

## Retest cadence
- Monthly, or after a major content/authority push. One AI answer is not a ranking — track trends, not snapshots.

## Key pattern (2026-09-27)

- Ouyang Thermal: **zero mentions** across all 8 queries — answers and cited sources.
- What gets cited: supplier-owned how-to guides and content hubs (Voltera blog, ALLPCB, Krayden blog, New England Die Cutting, Sheen sites) + standards/communities (IEEE Xplore, Infineon Developer Community).
- Implication: AI citation is winnable without outspending Henkel/Laird — citable how-to methodology content (selection guides, test conditions, comparison frameworks) is the format AI prefers. Our engineering tools and Gate 0-6 qualification content are the right asset class; they need more authority signals and clearer citation packaging (methodology, test conditions, last-updated, author).
- "China TIM suppliers" answers cite domestic competitors via their own sites + Made-in-China/Alibaba — a supplier-listing presence gap to close with real profiles only.

## Retest cadence

- Monthly, or after a major content/authority push. One AI answer is not a ranking — track trends, not snapshots.

## Retest 2026-10-08 — Perplexity BLOCKED (login wall, no data)

Two live-browser attempts, both failed with zero data gathered:
- Attempt 1: browser agent reported failure after 22 steps on the "How to select thermal pad?" search page; no per-query table produced.
- Attempt 2 (narrowed brief, 2 queries): Perplexity now shows a **non-dismissible** full-page sign-in wall ("登录以继续使用 Perplexity" — Log in to continue using Perplexity) after the brief "researching" state. No close button; Escape does not dismiss it. Per the no-bypass rule the task stopped; query 2 ("Dow 5121C alternative") never attempted.

**Change vs 2026-09-29:** the wall was dismissible then (modal appeared twice, both dismissible); it is now a hard block on public search. Standing baseline remains the 2026-09-29 result (Ouyang Thermal: zero mentions across 3 questions).

**Implication:** Perplexity public search is no longer a usable AI-visibility test route without login. Next retest options: (a) Google AI Overviews (worked 2026-09-27), (b) another AI answer engine with public access, (c) skip AI retest until after a major content/authority push. Do NOT attempt to bypass the login wall.

## Retest 2026-09-29 — Perplexity (3 questions)

Retest executed on perplexity.ai (no login): all three answers fully generated, no blocking login wall/quota/CAPTCHA (a "sign in to continue" modal appeared twice but was dismissible).

**Result: Ouyang Thermal — zero mentions across all 3 questions**, answers and source lists alike. Unchanged from the 2026-09-27 baseline (the 2026-09-29 calculator methodology upgrade had not yet had time to matter for indexing/citation).

| Date | Engine | Question | Ouyang cited? | Brands mentioned/cited | Sources cited |
|---|---|---|---|---|---|
| 2026-09-29 | Perplexity | What is thermal interface material? | No | Laird, Indium, Boyd, Ohmite (via sources, not in answer body) | en.wikipedia.org, laird.com (×3), indium.com, boydcorp.com, ohmite.com, onlinelibrary.wiley.com, electronics-cooling.com, forum.digikey.com |
| 2026-09-29 | Perplexity | How to select thermal pad? | No | Sheen Thermal, T-Global, AiVon, Power CTC, NFION Thermal, ALLPCB (via sources) | allpcb.com ("How to Choose Thermal Pads for PCB Applications"), sheenthermal.com, tglobaltechnology.com, nfionthermal.com, powerctc.com, aivon.co.kr |
| 2026-09-29 | Perplexity | Thermal interface material for AI server | No | Ziitek (cited inline in answer body), Laird, Intel, Google, Tesla, IBM, Arctic, Krayden, Sheen, NovoLINC/MaxLINC | eps.ieee.org, krayden.com, ziitek.com (×2), patsnap.com, sheenthermal.com, sheenmaterials.com, igorslab.de, finance.yahoo.com (ResearchAndMarkets) |

### Reads (hypotheses, not facts)

1. **Q2 ("How to select thermal pad?") is the most winnable format**: all 6 cited sources are how-to content sites, no dominant brand owns the answer. Our calculator + selection tool are exactly this asset class.
2. **ALLPCB validation signal**: Perplexity already cites ALLPCB's thermal-pad guide — our Batch 1 outreach target. A calculator link from that article would put us directly in the citation path. Follow-up #1 (2026-10-02 – 2026-10-04) matters more now.
3. **Q3 cites R = t/(k·A) explicitly** in selection criteria — our calculator page covers exactly this formula; needs indexation + a citing page.
4. **Q1 is brand/Wikipedia territory** (Laird ×3, Wikipedia) — not worth chasing head-on; win via Q2/Q3-style methodology content instead.

## Retest 2026-10-12 — Google AI Overviews: findings not retrievable

- Live-browser task ran the 3 test questions on google.com ("What is thermal interface material?", "How to select thermal pad?", "Thermal interface material for AI server") and reported completion via handoff, but its final report was NOT delivered to this run — per-question results cannot be verified or quoted.
- Recorded honestly: no AI-visibility data obtained this week. Do NOT report "Ouyang Thermal still not cited" or any per-question result as a finding.
- Standing baseline remains the 2026-09-29 Perplexity retest (Ouyang Thermal: zero mentions across 3 questions) and the 2026-10-08 Perplexity login-wall note (public search no longer usable without login). Next retest after a major content/authority push, or when a reliable public route is confirmed.

## Retest 2026-10-12 — CORRECTION: browser findings delivered (Google AI Overviews, 3 questions)

- The 2026-10-12 browser task's structured report arrived after the earlier log entry was pushed. Real findings (plain google.com searches, English UI, ~15:00 CST; AI Overview appeared for all 3 questions):
- **Ouyang Thermal: NOT mentioned or cited in any of the 3 answers or their source lists.** Unchanged from the 2026-09-29 baseline.
- The earlier 2026-10-12 entry ("findings not retrievable") is superseded by this correction.

| Date | Engine | Question | Ouyang cited? | Brands mentioned/cited | Sources cited |
|---|---|---|---|---|---|
| 2026-10-12 | Google AI Overviews | What is thermal interface material? | No | Laird, Voltera, Parker Chomerics, Indium, Boyd, Honeywell, DigiKey, Prostech, RS Components, Wikipedia | Laird TIM page, Indium TIM page, Wikipedia, Parker Chomerics TIM page, Boyd TIM page, Voltera "Thermal Interface Material (TIM): Selection Guide", Honeywell TIM role article, Prostech TIM/YouTube, DigiKey editorial, RS Components guide, Parker Chomerics theory/YouTube |
| 2026-10-12 | Google AI Overviews | How to select thermal pad? | No | Arctic, Gelid, Fujipoly, ALLPCB, T-Global, CTC POWER, Sheen, FIBERSTAMP, New England Die Cutting, SerpentX Tech, Tech YES City, Springgrasstech | ALLPCB "Beginner's Guide to Thermal Pads", T-Global guide, CTC POWER guide, Sheen 2026 guide, FIBERSTAMP selection guide, NEDC GPU/CPU thermal pad guides, SerpentX Tech/Tech YES City YouTube tutorials, Springgrasstech, one 2026-05 selection article (domain not visible) |
| 2026-10-12 | Google AI Overviews | Thermal interface material for AI server | No | Indium, Krayden, New England Die Cutting, Laird, Sheen, Honeywell (PTM7950/PTM7900), DuPont (TGel 600), NVIDIA (H100/H200/B200 as examples) | Krayden blog (AI server TIM, Nov 2025), Indium metal TIMs for AI GPU (Dec 2025), Laird TGel 600 (Apr 2025), NEDC engineer's guide (Aug 2025), Sheen AI server pages (Jul/Sep 2026), one Sep 2026 best-practices article (domain not visible) |

### Reads (hypotheses, not facts)

1. **Q2 is the most winnable format, confirmed again**: every cited source is a how-to guide built around conductivity/thickness data tables (ALLPCB, T-Global, CTC POWER, Sheen, NEDC, FIBERSTAMP). Our three methodology-packaged tools are exactly this asset class. Notably, **ALLPCB's "Beginner's Guide to Thermal Pads" is in the citation path** — our Batch 1 outreach target — which raises the value of that relationship (and its prepared-but-unsent follow-up).
2. **Q1 cites Voltera's TIM Selection Guide with a product-selection table** — our other Batch 1 target. Both outreach targets sit directly in the AI citation path; the TIM Selection Tool upgrade (this week) is the right asset to keep pitching them.
3. **Q3 is won by application-specific data/specs blogs** (Indium metal TIMs, Laird TGel 600, Krayden distributor blog, Sheen AI-server pages). Our AI server page is not cited — a data/spec-anchored AI-server piece (real specs, no invented data) remains the gap; requires the user's real product data before it can be built honestly.
4. Domestic competitors (Sheen) appear in Q2/Q3 via their own sites — the "China supplier presence" gap persists; not closable with content alone.
5. AI Overview content is dynamic/personalized — this is a 2026-10-12 ~15:00 CST snapshot, not a ranking. Retest monthly or after a major push.

## Retest 2026-10-19 — Google AI Overviews (2 questions, no login)

- Live-browser run 15:10–15:20 CST, plain google.com English queries. AI Overview rendered for both.
- **Ouyang Thermal: NOT mentioned or cited in either answer or their cited sources.** Unchanged from the 2026-10-12 baseline. One AI answer is not a ranking — this is a snapshot.

| Date | Engine | Question | Ouyang cited? | Brands mentioned/cited | Sources cited |
|---|---|---|---|---|---|
| 2026-10-19 | Google AI Overviews | How to select thermal pad? | No | None in answer body (only component types: GPU, CPU, MOSFET, VRAM, SSD) | tglobaltechnology.com (T-Global how-to/selection guide), powerctc.com (CTC Power guide), allpcb.com (PCB vendor guide with size table), Sheen Technology (conductivity & hardness guide), FIBERSTAMP (selection guide), Shenzhen AOCHUAN Technology (selection guide), Tech YES City YouTube video (thermal pad comparison) |
| 2026-10-19 | Google AI Overviews | Thermal interface material for AI server | No | Honeywell (PTM7900/7950/6000), Indium Corporation, Boston Materials (LMZ) | blog.krayden.com (Krayden AI-server TIM guide), indium.com (metal TIMs for AI GPU), eps.ieee.org (IEEE Electronics Packaging Society TIM strategy whitepaper), exponentialindustry.com, OCP YouTube (2026-10-15), Semiconductor Digest, nedc.com (NEDC engineer's guide), sheenthermal.com, sheenmaterials.com |

### Reads (hypotheses, not facts)

1. **Q1 is still won by manufacturer how-to/selection guides and data tables** (gap measurement, W/mK ranges, hardness tables) — ALLPCB remains in the citation path (Batch 1 outreach target; follow-up closed per user decision 2026-10-09). A re-run of the same question cited a different set (ziitek.com.vn, haktak.com, TermoPasty, thermalconductivematerials.com) — citation sets vary by exact phrasing; one snapshot is not a ranking.
2. **Q2 is won by recent (2025–2026) topical application guides + one engineering whitepaper** (IEEE EPS). No Chinese manufacturer brands appear anywhere. Our AI-server page is not cited — still a data/spec-anchored content gap; requires the user's real product data before it can be built honestly.
3. This week's TDS Comparison Tool packaging (assumptions + worked example + provenance) is the right asset class for Q1-style citations; it needs indexation + an external citing page to enter the path.
