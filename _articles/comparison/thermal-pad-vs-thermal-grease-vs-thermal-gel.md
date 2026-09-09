---
title: "Thermal Pad vs Thermal Grease vs Thermal Gel"
description: "Use grease for thin controlled interfaces, pads for defined gaps and clean placement, and gel for variable gaps with low assembly stress."
category: "Comparison Hub"
category_slug: "comparison"
category_url: "/comparison/"
author: "Ouyang Xiaohui"
date: 2026-09-10
updated: 2026-09-10
---

<div class="quick"><strong>Quick answer</strong><p>Geometry and manufacturing determine the appropriate TIM family.</p></div>

## Key takeaways

<div class="takeaways">

- Define the installed geometry, heat path, and acceptance limit before selecting a material.
- Compare values only when test methods and conditions are aligned.
- Validate thermal, mechanical, electrical, process, and lifetime behavior in representative hardware.

</div>

## Technical explanation

Grease remains flowable; pads are preformed solids; gels are dispensable and may cure after mixing.

Thermal conductivity describes heat transport through material. The installed interface also includes geometry and contact resistance. For a simplified uniform layer, bulk resistance follows R = t/(kA), where t is thickness, k conductivity, and A area. Real assemblies require additional terms and measured validation.

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

## Application example

Use grease under a flat clamped module, a pad across a known gap, and gel over uneven magnetics, subject to validation.

This is an engineering illustration, not a claimed customer case. Final limits depend on the design, material formulation, and stated test conditions.

## Common mistakes

Ranking only by W/m·K; mixing data from different methods; ignoring tolerance and pressure; treating a typical value as a guaranteed design limit; skipping application-level aging.

## FAQ

<details><summary>Is conductivity enough for selection?</summary><p>No. Installed thickness, contact, pressure, geometry, electrical needs, processing, and aging must be evaluated.</p></details>
<details><summary>Can two datasheets be compared directly?</summary><p>Only when methods, units, specimen conditions, and definitions align. Otherwise use controlled side-by-side testing.</p></details>
<details><summary>What belongs in final validation?</summary><p>Verify temperature, installed geometry, mechanical load, electrical requirements, process repeatability, and relevant environmental aging.</p></details>


## References and standards

- [ASTM D5470-17(2024)](https://store.astm.org/standards/d5470), Standard Test Method for Thermal Transmission Properties of Thermally Conductive Electrical Insulation Materials. ASTM states that its idealized heat flow does not directly reproduce most applications.
- [ISO 22007-2:2022](https://www.iso.org/standard/81836.html), Plastics — Determination of thermal conductivity and thermal diffusivity — Part 2: Transient plane heat source method.

Confirm the current revision, scope, specimen suitability, and licensing with the issuing organization. Verify supplier values against the original TDS and its stated method.

