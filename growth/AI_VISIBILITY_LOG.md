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
