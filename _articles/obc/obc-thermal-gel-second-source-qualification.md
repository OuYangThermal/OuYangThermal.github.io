---
title: "OBC Thermal Gel Second-Source Qualification: A Practical Test-Gate Plan"
description: "A buyer and engineering workflow for benchmarking and qualifying an alternative thermal gel in an OBC assembly without relying on datasheet matching alone."
category: "OBC"
category_slug: "obc"
category_url: "/obc/"
author: "Ouyang Xiaohui"
date: 2026-09-11
updated: 2026-09-11
contact_message: "Hi Ouyang, I found your OBC thermal gel second-source qualification guide. We are evaluating an alternative gel and would like to discuss benchmark testing or a controlled sample."
email_subject: "OBC Thermal Gel Second-Source Qualification"
commercial_url: "/obc-thermal-material-supplier/"
commercial_label: "OBC Thermal Material Supplier Evaluation"
cta_title: "Preparing an OBC thermal gel second-source evaluation?"
cta_text: "Share the incumbent reference, gap range, dispense format and first validation gate for a controlled sample discussion."
cta_label: "Request a Sample for Evaluation"
cta_url: "/request-sample/"
cta_type: "sample"
cta_application: "obc-thermal-gel"
---

> Search demand remains Unknown. This is a high-commercial-value Tier B precision topic and is not represented as a high-volume query.

## Answer first

Qualifying an OBC thermal gel second source requires proving that the candidate can perform the same **installed function** across thermal, mechanical, electrical, dispensing and reliability conditions. Matching thermal conductivity on two datasheets is not sufficient.

Use staged test gates: freeze the incumbent and interface requirements, normalize supplier data, verify dispensing and bond-line behavior, run controlled thermal and reliability comparisons, confirm production controls, then approve through the responsible quality process. If a gate fails, retain the evidence and correct the test plan rather than lowering the acceptance criterion after seeing the result.

## Why OBC gel equivalence is difficult

An OBC can contain power semiconductors, magnetics, capacitors, control electronics, shields and a liquid-cooled or air-cooled housing. A dispensed gel may bridge different gaps across those zones. The material is part of both the heat path and the manufacturing process.

Two gels with the same stated W/m·K may differ in rheology, bond-line thickness, contact, dispense pressure, slump, mixing behavior, cure, rework, density and aging. A second source must therefore be compared at the assembly conditions that matter, not at a marketing label.

## Gate 0 — Freeze the requirement

Before requesting samples, document:

| Input | Unit or evidence | Decision it supports |
| --- | --- | --- |
| Gap range by zone | mm, minimum/nominal/maximum | Dispense volume and contact coverage |
| Contact area | mm² | Thermal path and material volume |
| Thermal target | Component temperature, heat-flow condition or K/W | Pass/fail definition |
| Mechanical limit | N, kPa, warpage or component constraint | Housing and PCB protection |
| Electrical requirement | Dielectric method, voltage and thickness if applicable | Isolation decision |
| Process | Equipment, cartridge, mixer, needle/nozzle, speed | Production compatibility |
| Environment | °C, cycles, vibration, humidity and dwell | Reliability test envelope |
| Incumbent baseline | Grade, lot, TDS, process and measured results | Controlled comparison |

The application owner must define acceptance limits. Do not invent universal limits for OBC thermal gel.

## Gate 1 — Normalize the evidence

Create a side-by-side matrix for the incumbent and candidate. Record the method and conditions behind thermal conductivity and impedance, not only the values. Include viscosity or rheology, density, working time, cure schedule for two-part products, hardness after cure where relevant, dielectric data, temperature range, shelf life, storage and change-control documentation.

Mark data as “not comparable” when methods differ. A blank cell is more useful than false equivalence.

## Gate 2 — Verify dispensing

Use the intended production equipment or a controlled equivalent. For two-part gel, record mix ratio, cartridge condition, mixer type, purge method and evidence that the two components are mixing consistently. For all dispensable gels, record nozzle or needle, pressure, flow rate or shot time, bead geometry, pause behavior and material temperature.

Inspect:

- Shot-to-shot mass or volume variation.
- Bead position, height and spreading after closure.
- Voids, air entrapment and incomplete wetting.
- Stringing, dripping, slump or separation.
- Equipment pressure and cycle time.
- Cleanup, rework and inspection practicality.

The candidate should not pass Gate 2 merely because one hand-dispensed sample looks acceptable.

## Gate 3 — Confirm installed thermal and mechanical behavior

Build representative joints at minimum, nominal and maximum gap. Keep surfaces, torque or closure method, fixture, sensors and conditioning consistent. Compare the incumbent and candidate under the same heat load and cooling boundary.

Record installed bond-line thickness, contact coverage and component or housing temperatures. Where a thermal-resistance measurement is used, report geometry and uncertainty. ASTM D5470 can support material comparison under controlled steady-state conditions, but its idealized heat flow does not directly reproduce an OBC assembly.

Also inspect the mechanical outcome. The gel must fill the interface without creating unacceptable force, PCB deflection, housing distortion or component movement.

## Gate 4 — Run relevant reliability stress

Select stresses from the OBC design requirements and known risks. They may include thermal cycling, power cycling, high-temperature storage, vibration, humidity or combined environments. Define specimen count, dwell, measurement intervals and failure criteria before testing.

After stress, inspect for void growth, separation, cracking after cure where applicable, leakage, migration, contact loss and surface change. Repeat the agreed thermal measurement. Do not use the phrase “no pump-out” unless the test duration, motion, temperature and inspection method support that conclusion.

## Gate 5 — Confirm supplier and production controls

Engineering performance is necessary but not sufficient for a second source. Review:

- Product and lot identification.
- Certificate-of-analysis content and limits.
- Incoming-inspection methods.
- Shelf life, storage and transport controls.
- Process and formulation change notification.
- Nonconformity and corrective-action process.
- Capacity, lead time and continuity evidence.
- Packaging compatibility with the dispense equipment.

Keep claims precise. A company can coordinate supply without being the material manufacturer or an authorized distributor.

## Gate 6 — Pilot build and release

Run a controlled pilot using production-intent material, equipment and work instructions. Record yield, dispense stability, inspection findings, cycle time, rework and final performance. Close deviations through the responsible engineering and quality functions.

Approval should state the exact material, revision, supplier route, manufacturing site where relevant, process settings and validated application. It should not silently approve every thickness, formulation or OBC platform.

## Common qualification mistakes

- Treating equal conductivity values as product equivalence.
- Changing the gel and dispense settings simultaneously without a controlled baseline.
- Testing only nominal gap.
- Ignoring two-part mix quality, purge and working time.
- Using a coupon test as the only assembly evidence.
- Running reliability first and defining acceptance after results arrive.
- Omitting lot traceability or change-notification requirements.
- Calling a sample a qualified replacement before pilot production.
- Describing an engineering example as a customer case.

## FAQ

### Must the second source use the same thermal conductivity?

Not necessarily. The required outcome is application performance within the defined mechanical, electrical, process and reliability limits. Conductivity is only one input.

### Should the incumbent and candidate use the same dispense parameters?

Begin with a controlled comparison, but do not assume one parameter set is optimal for both rheologies. Document any tuning and confirm that the final process remains manufacturable.

### How many samples are required?

There is no universal count. Choose enough specimens to evaluate the expected variation and the risk of the decision. The responsible quality plan should define the count and acceptance logic.

### Can supplier laboratory data replace OBC testing?

No. It can support screening and method alignment. The application owner must validate representative hardware and production conditions.

## Related OBC and gel guides

- [OBC Thermal Material Supplier Evaluation]({{ '/obc-thermal-material-supplier/' | relative_url }})
- [Thermal Interface Materials for OBC: Complete Selection Guide]({{ '/obc/thermal-interface-materials-for-obc-complete-selection-guide/' | relative_url }})
- [Why Do OBC Modules Use Two-Part Thermal Gel?]({{ '/obc/why-do-obc-modules-use-two-part-thermal-gel/' | relative_url }})
- [5 W/m·K Thermal Gel for OBC: When Is It Necessary?]({{ '/obc/5w-mk-thermal-gel-for-obc-when-is-it-necessary/' | relative_url }})
- [Common Thermal Gel Dispensing Problems]({{ '/thermal-gel/common-thermal-gel-dispensing-problems/' | relative_url }})
- [Why Does Thermal Gel Pump Out?]({{ '/thermal-gel/why-does-thermal-gel-pump-out/' | relative_url }})
- [Benchmark Your Current TIM]({{ '/benchmark-your-current-tim/' | relative_url }})

## Next step

For an OBC second-source review, send the incumbent reference, gap range, dispense format, application temperatures and the first validation gate. [Request a Sample]({{ '/request-sample/' | relative_url }}) for controlled evaluation, or [Discuss Your Application]({{ '/discuss-your-application/' | relative_url }}). Existing WhatsApp, email and phone options remain available.

## Technical reference

- [ASTM D5470-17(2024)](https://store.astm.org/standards/d5470), Standard Test Method for Thermal Transmission Properties of Thermally Conductive Electrical Insulation Materials.
