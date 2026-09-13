---
title: "OUYANG THERMAL Engineering Resources"
description: "Thermal interface material engineering tools, qualification checklists and original diagrams for selection, validation and supplier discussions."
permalink: /engineering-resources/
alternate_zh: /zh/engineering-resources/
commercial_contact: true
---

[中文工程资源 / Chinese Version]({{ '/zh/engineering-resources/' | relative_url }})

<div class="quick"><strong>Answer first</strong><p>These original OUYANG THERMAL resources turn common TIM decisions into practical checklists, workflows and engineering diagrams. Use them to define requirements and plan validation—not as substitutes for application testing or supplier qualification.</p></div>

## Thermal interface material engineering tools, checklists and diagrams

Each asset identifies its underlying technical page and assumptions. **Free to reference for technical and educational use with attribution to OUYANG THERMAL and a link to this original resource.** Author and technical contact: **Owen Ouyang (Ouyang Xiaohui / 欧阳小辉)**.

### 1. Thermal Pad Supplier Qualification — 12-Gate Checklist {#thermal-pad-12-gate-checklist}

**Answer first:** A pad is ready for supplier qualification only when material, converted-part, reliability, multi-lot and pilot-build evidence all close—not when one sample or conductivity value looks acceptable.

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/thermal-pad-supplier-qualification-12-gate-checklist.webp' | relative_url }}" width="1439" height="810" loading="lazy" decoding="async" alt="Twelve-gate thermal pad supplier qualification checklist covering requirements, dimensions, compression, testing, multiple lots, pilot build and change control"><figcaption><strong>Engineering Diagram.</strong> Source: OUYANG THERMAL · Owen Ouyang. Acceptance criteria remain application-specific.</figcaption></figure>

[Read the complete thermal-pad supplier qualification guide]({{ '/thermal-pad-supplier-china/' | relative_url }}).

### 2. TIM Second-Source Qualification Workflow {#tim-second-source-workflow}

**Answer first:** Freeze the requirement and incumbent benchmark before sampling; progress through comparable testing, reliability, multiple lots and pilot build before RFQ approval.

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/tim-second-source-supplier-qualification-flow.webp' | relative_url }}" width="1440" height="540" loading="lazy" decoding="async" alt="Thermal interface material second-source workflow from requirement definition and benchmark through sample, reliability, pilot build, qualification and RFQ"><figcaption><strong>Engineering Diagram.</strong> Source: OUYANG THERMAL · Owen Ouyang. The workflow does not claim completed customer qualification.</figcaption></figure>

[Read the China TIM supplier and second-source evaluation framework]({{ '/china-thermal-interface-material-supplier/' | relative_url }}).

### 3. Thermal Pad Compression, BLT and Contact Resistance Decision Guide {#thermal-pad-compression-blt-guide}

**Answer first:** Choose nominal thickness from the tolerance stack, then verify compressed bond-line thickness, contact at maximum gap and force at minimum gap. More compression may reduce contact resistance while increasing mechanical stress.

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/800g-1-6t-optical-module-thermal-pad-compression.webp' | relative_url }}" width="1439" height="810" loading="lazy" decoding="async" alt="Under-compressed, controlled and over-compressed thermal pad states showing contact resistance and mechanical stress tradeoffs"><figcaption><strong>Representative Engineering Diagram.</strong> Source: OUYANG THERMAL · Owen Ouyang. No universal compression percentage is implied.</figcaption></figure>

Use the decision sequence: `gap tolerance → selected thickness → compressed BLT → pressure/contact → thermal result → post-aging recovery`. [Read the detailed compression guide]({{ '/optical-module/thermal-pad-compression-for-800g-1-6t-modules/' | relative_url }}) or use the [bulk thermal-resistance calculator]({{ '/engineering-resources/thermal-resistance-calculator/' | relative_url }}) for a first-order layer calculation.

### 4. Thermal Gel Failure Diagnosis {#thermal-gel-failure-diagnosis}

**Answer first:** Diagnose void, slump, pump-out, squeeze-out and cure problems by separating incoming-material condition, dispensing, assembly geometry and reliability exposure; do not assign every defect to viscosity alone.

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/thermal-gel-supplier-dispensing-qualification-flow.webp' | relative_url }}" width="1439" height="810" loading="lazy" decoding="async" alt="Thermal gel failure diagnosis and supplier qualification flow covering storage, mixing, cure, dispensing, void, slump, pump-out, multiple lots and pilot build"><figcaption><strong>Engineering Diagram.</strong> Source: OUYANG THERMAL · Owen Ouyang. Equipment and acceptance limits are application-specific.</figcaption></figure>

| Observation | First checks |
| --- | --- |
| Void | Conditioning, mixing, interruption, bead path and assembly sequence |
| Slump | Temperature, wait time, bead geometry and vertical orientation |
| Pump-out | Gap, pressure, cycling amplitude, adhesion and surface condition |
| Squeeze-out | Shot mass, assembly stop, closing speed and keep-out areas |
| Cure problem | Ratio, mixing, time, temperature and material compatibility |

[Read the China thermal-gel supplier and dispensing qualification guide]({{ '/thermal-gel-supplier-china/' | relative_url }}).

### 5. IGBT / SiC Thermal Insulator Selection Matrix {#igbt-sic-insulator-matrix}

**Answer first:** Select the insulation architecture before selecting the TIM. Compare thermal resistance at installed thickness, electrical safety, conformity, mounting pressure, rework and assembly-level aging.

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/igbt-sic-thermal-insulator-selection-matrix.webp' | relative_url }}" width="1672" height="941" loading="lazy" decoding="async" alt="IGBT and SiC thermal insulator selection matrix comparing thin coated, ceramic-based and conformable insulating interfaces"><figcaption><strong>Engineering Diagram.</strong> Source: OUYANG THERMAL · Owen Ouyang. Selection depends on the complete insulation system and application validation.</figcaption></figure>

[Read the IGBT thermal-insulator supplier qualification guide]({{ '/thermal-insulator/thermal-insulator-supplier-for-igbt-modules/' | relative_url }}) and [SiC power-module TIM selection guide]({{ '/power-electronics/thermal-interface-material-for-sic-power-modules/' | relative_url }}).

## Use an asset in a controlled evaluation

Start with the relevant diagram, then [benchmark the current TIM]({{ '/benchmark-your-current-tim/' | relative_url }}), [request a sample evaluation]({{ '/request-sample/' | relative_url }}) or [ask Owen a private engineering question]({{ '/discuss-your-application/' | relative_url }}).
