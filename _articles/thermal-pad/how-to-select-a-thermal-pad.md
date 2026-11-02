---
title: "How to Select a Thermal Pad"
description: "Select by required gap, tolerance, allowable compression force, thermal impedance, electrical needs, temperature, and reliability."
category: "Thermal Pad"
category_slug: "thermal-pad"
category_url: "/thermal-pad/"
author: "Ouyang Xiaohui"
date: 2026-09-10
updated: 2026-11-02
---

<div class="quick"><strong>Quick answer</strong><p>Use the thinnest practical pad that covers the worst-case gap without overload.</p></div>

## Key takeaways

<div class="takeaways">

- Define the installed geometry, heat path, and acceptance limit before selecting a material.
- Compare values only when test methods and conditions are aligned.
- Validate thermal, mechanical, electrical, process, and lifetime behavior in representative hardware.

</div>

## Selection steps

Select in this order — geometry first, headline conductivity last:

1. **Measure the installed gap.** Record the nominal gap and the worst-case gap from the tolerance stack, plus flatness of both mating surfaces.
2. **Set the thermal budget.** Define the allowed temperature rise (ΔT) or thermal resistance (Rth) for the interface at the actual heat load, not from a datasheet headline.
3. **Screen by thickness and compression.** Choose the thinnest practical pad whose compression window covers the worst-case gap without overloading components. See the [thickness selection guide]({{ '/thermal-pad/thermal-pad-thickness-selection-guide/' | relative_url }}) and [compression ratio explained]({{ '/thermal-pad/thermal-pad-compression-ratio-explained/' | relative_url }}).
4. **Check conductivity against the budget, not alone.** Use R = t/(k·A) for bulk resistance only, then confirm with measured impedance at the installed thickness and pressure. A higher-W/m·K pad at a larger thickness can have higher bulk resistance than a lower-W/m·K pad installed thinner.
5. **Confirm hardness and electrical needs.** Hardness sets conformability under the available clamping force; electrical insulation, if required, must be verified at the installed thickness.
6. **Validate in representative hardware.** Thermal, mechanical, electrical, process, and aging behavior must be checked in the actual assembly before approval. A supplier typical value is not a design limit.

The [TIM Selection Tool]({{ '/engineering-resources/tim-selection-tool/' | relative_url }}) applies the same screening order interactively: application, gap range, insulation need, rework need, and tolerance sensitivity narrow the TIM category before any product is considered.

## Worked example (illustrative calculation)

This example shows the arithmetic only. It is not a product recommendation and not measured data for any material.

- A pad with conductivity k = 6 W/m·K, installed thickness t = 1.0 mm, contact area A = 40 × 40 mm² (0.0016 m²).
- Bulk thermal resistance R = t/(k·A) = 0.001 / (6 × 0.0016) ≈ **0.104 K/W**.
- The same pad installed at 1.6 mm (a 2.0 mm pad compressed 0.4 mm, a 20% compression ratio) gives R = 0.0016 / (6 × 0.0016) ≈ **0.167 K/W** — thickness alone raises bulk resistance by about 60% in this calculation.
- For comparison, an 8 W/m·K pad at 1.5 mm over the same area gives R = 0.0015 / (8 × 0.0016) ≈ **0.117 K/W** — higher conductivity, yet higher bulk resistance than the 6 W/m·K pad at 1.0 mm. This is why conductivity values must never be compared without thickness.

Check any candidate with the [Thermal Resistance Calculator]({{ '/engineering-resources/thermal-resistance-calculator/' | relative_url }}) and the [Thermal Pad Compression Calculator]({{ '/engineering-resources/thermal-pad-compression-calculator/' | relative_url }}).

## Model assumptions and limits

The worked example uses a steady-state, one-dimensional bulk-resistance model: uniform thickness, uniform conductivity, full contact over the stated area. It excludes contact resistance, spreading resistance, voids, and aging — all of which raise installed resistance in real assemblies. Datasheet conductivity values are comparable only when the test method, specimen, thickness, pressure, and temperature match; otherwise use controlled side-by-side testing under matched conditions, as in the [TIM TDS Comparison Tool]({{ '/engineering-resources/tim-tds-comparison-tool/' | relative_url }}).

*Methodology maintained by Ouyang Xiaohui (Owen Ouyang), Ouyang Thermal. Last reviewed 2026-11-02.*

## Get help selecting a pad

If the gap range, thermal budget, and electrical requirement are known, a same-condition comparison can be structured against the material currently in use — [Benchmark Your Current TIM]({{ '/benchmark-your-current-tim/' | relative_url }}) — or a candidate can be requested once target conductivity, thickness, hardness, and size are defined: [Request a Sample]({{ '/request-sample/' | relative_url }}).

## Technical explanation

Too thin loses contact; too thick or hard can bow boards. Higher conductivity does not automatically compensate for thickness.

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

Measure the assembled gap distribution, calculate both tolerance corners, and test temperature plus board strain.

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

