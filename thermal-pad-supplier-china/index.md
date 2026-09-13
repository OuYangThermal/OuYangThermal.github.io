---
title: Thermal Pad Supplier Evaluation in China
description: Engineering criteria for evaluating thermal pad candidates and supply coordination in China.
permalink: /thermal-pad-supplier-china/
commercial_contact: true
contact_message: "Hi Ouyang, I'm evaluating a thermal pad for my application. Could you help me select the right material? Source: Thermal Pad Supplier China"
email_subject: "Thermal Pad Inquiry – China Supplier"
---

## Direct answer

A thermal pad candidate should be selected from the actual gap, pressure, thermal resistance, electrical, reliability, and assembly requirements—not conductivity alone. OUYANG THERMAL supports engineering evaluation, while Hongjing New Materials Technology (Shenzhen) Co., Ltd. coordinates commercial and supply-chain inquiries.

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/thermal-pad-supplier-qualification-12-gate-checklist.webp' | relative_url }}" width="1439" height="810" loading="lazy" decoding="async" alt="Twelve-gate thermal pad supplier qualification checklist from requirement definition through pilot build and change control"><figcaption><strong>Engineering Diagram.</strong> Twelve evidence gates for thermal-pad supplier qualification. The application owner defines acceptance criteria; this is not a certification claim.</figcaption></figure>

## Applications and materials

Evaluation can cover pads for OBC, PCS, ESS, BMS, IGBT and MOSFET interfaces, optical modules, and server hardware. Relevant constructions may include electrically insulating gap pads and other compliant sheet interfaces, subject to supplier documentation and application validation.

## Selection and testing

Specify nominal and worst-case gap, flatness, pressure distribution, compression limits, hardness scale, thickness tolerance, thermal resistance method, dielectric strength, breakdown voltage, operating temperature, flame or regulatory needs, and aging conditions. Verify handling, die-cut geometry, liner design, placement, rework, and storage.

{% include quick-contact.html %}

## Second-source process

Build a controlled comparison matrix. Select a benchmark candidate, measure thickness and mechanical response, then test thermal performance and electrical isolation using consistent methods. Reliability and production trials should precede qualification. “Potential alternative subject to validation” is the correct status until evidence is complete.

## Twelve tests and gates before mass production

| Gate | Evidence to review | Why it matters |
| --- | --- | --- |
| 1. Requirement | Gap range, area, force, temperature and insulation role | Prevents selection from a product name alone |
| 2. TDS and method | Original method, units, specimen and conditions | Makes supplier data comparable |
| 3. Dimensions | Finished outline, holes, notches and registration | Confirms fit in the real assembly |
| 4. Thickness | Nominal and tolerance across multiple locations | Controls compression and bulk resistance |
| 5. Compression | Force-deflection across minimum/maximum gap | Protects components while maintaining contact |
| 6. Thermal test | Impedance at stated thickness, pressure and temperature | Tests installed behavior, not only W/m·K |
| 7. Electrical test | Method, thickness, electrode and aging condition | Supports the defined insulation function |
| 8. Reliability | Relevant cycling, humidity, vibration and recovery | Checks retained contact and properties |
| 9. Die cut and liner | Edge debris, orientation, release and placement | Verifies manufacturability |
| 10. Multi-lot | Raw sheet and finished-part variation from several lots | Separates a good sample from a stable source |
| 11. Pilot build | Operators, fixtures, rework and inspection | Validates production integration |
| 12. Change control / RFQ | Approved revision, sites, notification and commercial scope | Prevents an RFQ from silently changing the requirement |

These are qualification gates, not twelve universal laboratory standards. The responsible engineering organization must choose methods and limits for its product.

## Multi-lot and finished-part validation

Do not qualify only one hand-selected sheet. Link each die-cut lot to its raw-material lot and converting process. Compare thickness distribution, dimensions, appearance, compression response and relevant thermal/electrical evidence across multiple delivered lots. Review packaging and storage after transport, not only parts collected at the converter.

For die cuts, freeze drawing revision, cutting orientation, critical feature tolerances, liner construction and cleanliness criteria. A stable sheet can still produce unstable assemblies if the converted part shifts, tears, retains debris or is difficult to release.

## Reliability, change notification and RFQ readiness

Reliability testing should reproduce relevant mechanical load and interface geometry before and after exposure. Record compression set, displacement, cracking, contamination, electrical evidence and thermal response as applicable. Do not claim lifetime from a generic material aging result.

Supplier approval should define which changes require notification: formulation, filler, carrier, liner, raw-material source, converting tool, process, site and test method. A sample can enter pilot build only after engineering screening passes. RFQ readiness begins when the approved part revision, quality evidence, packaging, quantity and commercial scope are frozen.

```text
Sample → Same-condition benchmark → Reliability → Multi-lot review
→ Pilot build → Supplier qualification → RFQ readiness
```

## Related engineering guides

- [How to Select a Thermal Pad]({{ '/thermal-pad/how-to-select-a-thermal-pad/' | relative_url }})
- [Thickness Selection Guide]({{ '/thermal-pad/thermal-pad-thickness-selection-guide/' | relative_url }})
- [Compression Ratio Explained]({{ '/thermal-pad/thermal-pad-compression-ratio-explained/' | relative_url }})
- [3 vs 6 vs 8 W/mK Pads]({{ '/comparison/3w-vs-6w-vs-8w-thermal-pad/' | relative_url }})
- [Thermal Pad Compression Set]({{ '/thermal-pad/thermal-pad-compression-set-explained/' | relative_url }})
- [IGBT Thermal Insulator Supplier Qualification]({{ '/thermal-insulator/thermal-insulator-supplier-for-igbt-modules/' | relative_url }})
- [China TIM Supplier Evaluation]({{ '/china-thermal-interface-material-supplier/' | relative_url }})
- [Benchmark Your Current TIM]({{ '/benchmark-your-current-tim/' | relative_url }})
- [Request a Sample]({{ '/request-sample/' | relative_url }})

{% include contact-card.html subject="Thermal Pad Supplier Evaluation" %}
