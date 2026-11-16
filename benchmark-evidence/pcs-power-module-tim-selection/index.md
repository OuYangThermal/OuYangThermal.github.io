---
layout: article
title: "Case 003 — PCS Power Module TIM Selection (Engineering Analysis)"
description: "Engineering analysis for thermal interface selection in PCS power modules: worked bulk-resistance calculation examples for IGBT baseplates and magnetics gaps, with stated assumptions and limits. No measured test data in this case."
permalink: /benchmark-evidence/pcs-power-module-tim-selection/
category: Benchmark Evidence
category_url: /benchmark-evidence/
date: 2026-11-16
updated: 2026-11-16
author: Owen Ouyang
contact_message: "Hi Owen, I reviewed Case 003 and would like to benchmark my current TIM for a PCS power module under controlled application conditions."
email_subject: "TIM Benchmark Evidence Case 003 — PCS Power Module"
commercial_url: /china-thermal-interface-material-supplier/
commercial_label: "China TIM supplier evaluation"
cta_title: "Need to benchmark your current TIM?"
cta_text: "Send the current TDS, target thickness, pressure or assembly gap, electrical requirement and application conditions for a controlled comparison plan."
cta_label: "Benchmark Your Current TIM"
cta_url: /benchmark-your-current-tim/
cta_type: benchmark
cta_application: pcs-power-module-tim-selection
---

<aside class="notice"><strong>Engineering analysis — no measured data in this case.</strong><p>This case contains no measured test results. All numbers below are worked calculation examples using the steady-state one-dimensional bulk-resistance model R = t/(k·A), with illustrative inputs stated next to each result. They show how geometry and conductivity interact; they are not product data, not a material recommendation, and not a substitute for application testing.</p></aside>

## Answer first

A PCS power module usually needs more than one thermal interface material family: a thin, clamped interface under IGBT modules, a compliant gap filler for magnetics with large tolerances, and a controlled interface for capacitors and control boards. The worked examples below show the governing effect — a 3.0 mm gap at 3 W/m·K carries roughly thirteen times the bulk resistance of a 1.0 mm interface at 6 W/m·K on a comparable area — so thickness and installed geometry dominate the selection, not the conductivity headline alone.

## Case scope

| Scope item | Recorded context |
|---|---|
| Application | PCS / inverter power module (IGBT modules, magnetics, capacitors, controls) |
| Method | Steady-state one-dimensional bulk resistance, R = t/(k·A) |
| Measured data | None in this case — worked calculation examples only |
| Inputs | Illustrative conductivity, thickness and area values stated per example |
| Electrical context | Insulation requirements are listed as a selection parameter; no breakdown-voltage data is presented in this case |
| Source article | [TIM Selection for PCS]({{ '/pcs/tim-selection-for-pcs/' | relative_url }}) |

## Worked example A — IGBT module baseplate interface

A clamped module baseplate with a thin interface: conductivity 6 W/m·K, installed thickness 1.0 mm, contact area 60 × 60 mm².

- Bulk resistance: R = t/(k·A) = 0.001 / (6 × 0.0036) ≈ **0.046 K/W**.
- At 20% compression the same pad installs at 0.8 mm: R = 0.0008 / (6 × 0.0036) ≈ **0.037 K/W**.

The arithmetic is verifiable: a thinner installed bond line lowers the bulk contribution proportionally. In a real assembly, contact resistance, surface flatness and pressure distribution add terms this model excludes — see the assumptions below.

## Worked example B — magnetics gap filler

A transformer or inductor with a large tolerance gap: conductivity 3 W/m·K, installed thickness 3.0 mm, contact area 40 × 40 mm².

- Bulk resistance: R = t/(k·A) = 0.003 / (3 × 0.0016) ≈ **0.625 K/W**.
- At 20% compression the filler installs at 2.4 mm: R = 0.0024 / (3 × 0.0016) ≈ **0.500 K/W**.

Compare with Example A: the magnetics interface carries roughly 13 times the bulk resistance (0.625 vs 0.046 K/W) despite using a material only one step lower in conductivity — because the heat path is three times thicker on a smaller area. This is why ranking PCS materials by W/m·K alone misleads: the thick-gap interface dominates the thermal budget and must be evaluated at its installed thickness, not at the datasheet's headline conductivity.

## Model assumptions and limits

- Steady-state, one-dimensional bulk conduction only; contact resistance, spreading resistance, interface voids and aging are excluded.
- Inputs are illustrative, not measured material data and not a product recommendation.
- Results apply only to the stated geometry; changing area, thickness or pressure changes the result.
- Electrical insulation, compression force, vibration, temperature cycling and process repeatability still require application-level validation with the candidate's verified TDS.
- Verify any supplier value against the original TDS and its stated method before using it in a design decision.

## Selection parameters

| Parameter | Engineering question | Evidence to request |
|---|---|---|
| Conductivity | Which method, direction, and temperature? | Standard and specimen conditions |
| Thermal impedance | At what BLT and pressure? | Data at application conditions |
| Thickness / gap | What is the tolerance range? | Installed measurement |
| Mechanical response | What load reaches the hardware? | Compression-deflection or modulus data |
| Electrical behavior | Is isolation required? | Method, thickness, and aging context |
| Process | How is placement or dispensing controlled? | Work instruction and acceptance criteria |

Also record temperature range, surface finish, vibration or power cycling, material compatibility, inspection, rework, storage, lot control, and any applicable regulatory requirement. A supplier typical value is not a universal guarantee.

## What this case does not prove

- It does not report any measured test result.
- It does not prove one material is better than another.
- It does not establish a guaranteed or drop-in replacement.
- It does not replace customer qualification or application-specific testing.
- It does not predict actual device temperature by itself.
- It does not establish independent, official or third-party certification.
- It does not establish production approval, customer use or supplier authorization.

## Frequently asked questions

### Did Case 003 measure anything?

No. Case 003 is an engineering analysis built from worked calculation examples. No specimens were tested and no measured thermal resistance, conductivity or electrical values are reported. Measured-data cases in this library are Case 001 and Case 002.

### Why does the magnetics gap dominate the thermal budget?

Because bulk resistance scales with thickness divided by area. Example B (3.0 mm, 40 × 40 mm², 3 W/m·K) gives ≈ 0.625 K/W, roughly thirteen times Example A (1.0 mm, 60 × 60 mm², 6 W/m·K) at ≈ 0.046 K/W. Thickness and area matter as much as conductivity.

### Can this analysis select a material for my PCS?

No — it can only frame the comparison. Selection requires the candidate's verified TDS at the application's thickness, pressure and temperature, plus validation in representative hardware. Use the [Second Source Qualification Generator]({{ '/engineering-resources/second-source-qualification-generator/' | relative_url }}) to turn the requirements into a project checklist.

### Can my current TIM be benchmarked the same way Case 001 was?

Yes. Send the current material and TDS, target thickness, pressure or assembly gap, electrical requirement and application conditions, and a controlled same-condition comparison can be structured: [Benchmark Your Current TIM]({{ '/benchmark-your-current-tim/' | relative_url }}).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://ouyangthermal.github.io/benchmark-evidence/pcs-power-module-tim-selection/#faq",
  "mainEntity": [
    {"@type":"Question","name":"Did Case 003 measure anything?","acceptedAnswer":{"@type":"Answer","text":"No. Case 003 is an engineering analysis built from worked calculation examples. No specimens were tested and no measured thermal resistance, conductivity or electrical values are reported. Measured-data cases in this library are Case 001 and Case 002."}},
    {"@type":"Question","name":"Why does the magnetics gap dominate the thermal budget?","acceptedAnswer":{"@type":"Answer","text":"Because bulk resistance scales with thickness divided by area. Example B (3.0 mm, 40 x 40 mm2, 3 W/m-K) gives approximately 0.625 K/W, roughly thirteen times Example A (1.0 mm, 60 x 60 mm2, 6 W/m-K) at approximately 0.046 K/W. Thickness and area matter as much as conductivity."}},
    {"@type":"Question","name":"Can this analysis select a material for my PCS?","acceptedAnswer":{"@type":"Answer","text":"No, it can only frame the comparison. Selection requires the candidate's verified TDS at the application's thickness, pressure and temperature, plus validation in representative hardware."}},
    {"@type":"Question","name":"Can my current TIM be benchmarked the same way Case 001 was?","acceptedAnswer":{"@type":"Answer","text":"Yes. Provide the current material and TDS, target thickness, pressure or assembly gap, electrical requirement and application conditions, and a controlled same-condition comparison can be structured."}}
  ]
}
</script>

## Second-source qualification

Use this case as a framing input within a gated process. Freeze the incumbent reference and requirements; align thickness, pressure, substrates and methods; test multiple specimens and lots; confirm compression, electrical insulation and reliability; and complete a representative pilot build before RFQ approval.

Continue with the [TIM Selection for PCS]({{ '/pcs/tim-selection-for-pcs/' | relative_url }}), [China TIM Supplier Evaluation]({{ '/china-thermal-interface-material-supplier/' | relative_url }}) and [Second Source Qualification Generator]({{ '/engineering-resources/second-source-qualification-generator/' | relative_url }}).

## Related engineering tools

- [Thermal Pad Compression Calculator]({{ '/engineering-resources/thermal-pad-compression-calculator/' | relative_url }})
- [TIM TDS Comparison and Second-Source Check]({{ '/engineering-resources/tim-tds-comparison-tool/' | relative_url }})
- [Thermal Resistance Calculator]({{ '/engineering-resources/thermal-resistance-calculator/' | relative_url }})
- [Thermal Conductivity vs Thermal Resistance]({{ '/comparison/thermal-conductivity-vs-thermal-resistance/' | relative_url }})

## Next step

[Discuss Your Application]({{ '/discuss-your-application/' | relative_url }}), [Benchmark Your Current TIM]({{ '/benchmark-your-current-tim/' | relative_url }}) or [Request a Sample]({{ '/request-sample/' | relative_url }}). Send the current material, target thickness, gap or pressure, electrical requirement and validation conditions.

<p>Maintained by Ouyang Xiaohui (Owen Ouyang), Ouyang Thermal. Last reviewed 2026-11-16.</p>

## Disclosure

Engineering analysis with worked calculation examples only. No measured test data in this case. Not an independent third-party certification.
