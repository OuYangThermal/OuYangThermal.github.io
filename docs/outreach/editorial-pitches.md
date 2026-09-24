# Editorial Pitches — Round 1

> A-level media: pitch the TOPIC first, never the full manuscript. One outlet per topic (Electronic Design and Power Electronics News require exclusivity).

---

## 1. Electronics Cooling — pitch

- Outlet: Electronics Cooling (electronics-cooling.com)
- Guidelines: https://www.electronics-cooling.com/editorial-contributions/
- Process: manuscript via on-page form; no named editor published on the guideline page. Fallback contact from the site's own call-for-authors: editor@electronicscooling.com (not a published editorial contact — use only if the form gives no route).
- Requirements observed: unbiased, non-commercial technical content; product promotion will be rejected. No fee published. No geographic restriction found.
- Proposed topic (preferred): **"Why Thermal Conductivity Alone Cannot Qualify a Thermal Interface Material"**
- Recommended landing page: https://ouyangthermal.github.io/benchmark-your-current-tim/ (verified HTTP 200)

### Abstract (150–200 words)

Engineers often screen thermal interface materials by a single datasheet number — thermal conductivity in W/m·K — and assume a higher value means better installed performance. This article explains why that assumption fails in practice and what to compare instead.

Thermal conductivity is measured under specific laboratory conditions: defined thickness, pressure, temperature, and surface finish. In a real assembly, heat crosses not a material but an interface — and the installed thermal resistance depends on contact resistance, compressed thickness or bond-line thickness, mounting pressure, surface condition, and the gap tolerance stack of the assembly. A 6 W/m·K pad installed at the wrong compression can underperform a 3 W/m·K pad installed correctly.

The article walks through a practical comparison workflow: defining the real heat path, normalizing test conditions between incumbent and candidate materials, holding thickness, pressure, surfaces, and temperature constant, and validating finished die-cut parts rather than sheet data alone. It closes with multi-lot consistency, aging exposure, and pilot-build checks that turn a laboratory comparison into a qualification decision — so engineering and procurement freeze requirements on evidence, not on a single number.

### Detailed outline

1. **Introduction: the datasheet trap** — why W/m·K dominates screening and why it misleads.
2. **What W/m·K actually measures** — test-method dependence, thickness/pressure/temperature dependence, reported vs. installed values.
3. **The installed interface** — series resistance model: bulk resistance plus two contact resistances; surfaces, wetting, conformity.
4. **Compressed thickness and bond-line thickness** — why the installed dimension, not the free-state thickness, sets performance.
5. **Pressure and tolerance stack** — compression-deflection behavior, gap min/nom/max, force limits on components and solder joints.
6. **Why coupon results do not prove installed performance** — fixture vs. assembly, edge effects, real surfaces.
7. **A practical incumbent-vs-candidate comparison** — matched-condition test matrix: thickness, pressure, surfaces, temperature, method, acceptance criteria.
8. **Beyond the bench** — finished-part validation, multi-lot consistency, aging and reliability exposure, pilot build.
9. **From data to decision** — what engineering and procurement should freeze before RFQ; requalification and change-control triggers.
10. **Conclusion.**

### Planned original figures

1. Heat-path diagram: heat source → TIM → spreader/heatsink, with bulk and contact resistances labeled. (Engineering diagram.)
2. Representative curve: thermal resistance vs. compressed thickness for a gap-pad family. (Illustrative — labeled representative, not measured data.)
3. Tolerance-stack illustration: assembly gap min/nom/max mapped against pad thickness options and compression window. (Engineering diagram.)
4. Matched-condition benchmark matrix: table of conditions held constant between incumbent and candidate. (Table/figure.)
5. Qualification-gate flowchart: requirement → TDS screen → bench comparison → application validation → reliability/multi-lot → pilot build → RFQ. (Engineering diagram.)

> Per repository policy, all figures are labeled as engineering/representative diagrams. No measured performance data, customer cases, or certification claims are included.

---

## 2. Electronic Design — pitch (to be finalized)

- Outlet: Electronic Design (electronicdesign.com)
- Guidelines: https://www.electronicdesign.com/contribute
- Process: one-paragraph abstract or outline FIRST to EDContributedArticles@endeavorb2b.com (published mailbox; no editor name). Full manuscript only after acceptance. Exclusivity required — this topic must not be offered elsewhere.
- Requirements observed: technically oriented, what/how/why (not a product pitch); products only as illustrative examples; contributed-article template with image specs; explicitly free ("There is no charge for having an article posted").
- Proposed topic: **"What Engineers Should Compare Before Approving a Second-Source Thermal Pad"**
- Recommended landing page: https://ouyangthermal.github.io/thermal-pad-supplier-china/ (verified HTTP 200)

## 3. Power Electronics News — pitch (to be finalized)

- Outlet: Power Electronics News (powerelectronicsnews.com)
- Guidelines: https://www.powerelectronicsnews.com/editorial-contributions-guide/
- Process: pitch OR manuscript to Aalyia Shaukat <aalyia.shaukat@aspencore.com> (named, published). Editor-in-chief: Maurizio Di Paolo Emilio.
- Requirements observed: technical articles ~1500–2000 words; guest blogs ~800–1200 words; vendor lane explicitly open; must not have been published elsewhere; 1–2+ figures as separate PNG/JPG with captions and source; author bio + headshot required.
- Proposed topic: **"A Qualification Workflow for Thermal Interface Materials in IGBT and SiC Power Modules"**
- Recommended landing page: https://ouyangthermal.github.io/optical-transceiver-tim-supplier/ — NO; power-module topic pairs better with a power-electronics page. Options: https://ouyangthermal.github.io/thermal-pad-supplier-china/ (covers IGBT/SiC modules, HTTP 200). Final choice: thermal-pad-supplier-china.

---

## Email drafts (DRAFT — not sent)

### Draft 1 — Electronics Cooling

- **To:** editor@electronicscooling.com *(fallback from the site's call-for-authors; the guideline page itself routes submissions through an on-page form with no named editor — pitch via email first per Round 1 instruction, then use the form if asked)*
- **Subject:** Article Proposal: Why Thermal Conductivity Alone Cannot Qualify a Thermal Interface Material

Hello Electronics Cooling Editorial Team,

I read your "Top 20 Considerations For Selecting Thermal Interface Materials" with interest — it gives engineers a broad map of material families and selection factors. I would like to propose a complementary technical article that goes deep on one specific failure mode in that selection process: "Why Thermal Conductivity Alone Cannot Qualify a Thermal Interface Material."

The article would explain why thermal conductivity alone is insufficient for qualification and show engineers how to compare an incumbent and candidate material under controlled conditions, including matched compressed thickness, pressure, surface condition, temperature and aging exposure.

The proposed article would cover:

- defining the real heat path and tolerance stack;
- comparing thermal resistance under stated test conditions;
- checking compression, contact pressure and bond-line thickness;
- evaluating finished die-cut parts instead of sheet data alone;
- conducting multi-lot, reliability and pilot-build validation;
- defining requalification and supplier change-control triggers.

The article would be educational and non-promotional. We can provide original diagrams, comparison tables and a qualification-flow illustration. It has not been submitted or published elsewhere.

OUYANG THERMAL works with engineering teams evaluating thermal pads, gels and related interface materials for electronics applications. A short engineering-resource reference can be supplied for the author biography if permitted by your editorial policy. One relevant resource is our practical TIM benchmark guide: https://ouyangthermal.github.io/benchmark-your-current-tim/

Would this topic be suitable for Electronics Cooling? I would be glad to send a detailed outline before preparing the manuscript.

Best regards,

Owen
OUYANG THERMAL
Technical Contact
5672306@gmail.com
https://ouyangthermal.github.io/

### Draft 2 — Electronic Design

- **To:** EDContributedArticles@endeavorb2b.com *(published mailbox on the contribute page; no editor name published)*
- **Subject:** Contributed Article Proposal: What Engineers Should Compare Before Approving a Second-Source Thermal Pad

Hello Electronic Design Editorial Team,

Your recent "Thermal-Management Design Banks On Advanced Materials/Adhesives" coverage shows your readers are actively working through TIM selection for demanding applications. I am proposing an original contributed article that complements that materials survey with a practical engineering workflow: "What Engineers Should Compare Before Approving a Second-Source Thermal Pad."

The article is intended for design and reliability engineers rather than as a product promotion. It would examine the difference between datasheet screening and installed interface performance.

The proposed outline includes:

1. Why W/m·K does not determine system performance by itself.
2. The effect of compressed thickness and contact resistance.
3. How gap tolerance and pressure limits affect material selection.
4. How to structure an incumbent-versus-candidate benchmark.
5. Why finished-part, multi-lot and aging validation matter.
6. What engineering and procurement should freeze before RFQ approval.

We can provide original diagrams and a concise comparison table. The manuscript would be exclusive and prepared according to your contributor guidelines.

A relevant engineering resource from our side: https://ouyangthermal.github.io/thermal-pad-supplier-china/

Please let me know whether the topic fits your current editorial needs. I can first send a one-paragraph abstract and detailed outline.

Best regards,

Owen
OUYANG THERMAL
Technical Contact
5672306@gmail.com
https://ouyangthermal.github.io/

### Draft 3 — Power Electronics News

- **To:** Aalyia Shaukat <aalyia.shaukat@aspencore.com> *(named contact published on the editorial-contributions guide)*
- **Subject:** Article Proposal: TIM Qualification for IGBT and SiC Power Modules

Hello Aalyia,

Your recent coverage of "Silicone TIMs in IGBT-7 Power Modules" and "Advanced thermal management and packaging techniques for SiC" shows your readers are making TIM decisions in power modules right now. I would like to propose a technical article that extends that coverage from material options to a decision workflow: "A Qualification Workflow for Thermal Interface Materials in IGBT and SiC Power Modules."

The article would focus on a common power-electronics design problem: materials that appear similar on datasheets can behave differently after installation because of thickness, pressure, surface condition, contact resistance and reliability exposure.

The article would present a practical workflow covering:

- heat-path and interface definition;
- electrical-insulation and mechanical constraints;
- matched-condition thermal-resistance comparison;
- compression and assembly-force limits;
- temperature cycling and application-relevant aging;
- finished-part and multi-lot validation;
- pilot-build and supplier change-control requirements.

The content would be vendor-neutral, technically focused and unpublished. Original diagrams and test-plan tables can be supplied.

A relevant resource from our side: https://ouyangthermal.github.io/thermal-pad-supplier-china/

Would this topic be relevant to your readers? I would be happy to provide an abstract and outline for review.

Best regards,

Owen
OUYANG THERMAL
Technical Contact
5672306@gmail.com
https://ouyangthermal.github.io/
