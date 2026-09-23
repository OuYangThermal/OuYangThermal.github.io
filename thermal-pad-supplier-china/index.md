---
title: Thermal Pad Supplier Evaluation in China
description: Engineering criteria for evaluating thermal pad candidates and supply coordination in China.
permalink: /thermal-pad-supplier-china/
alternate_zh: /zh/thermal-pad/
commercial_contact: true
contact_message: "Hi Ouyang, I'm evaluating a thermal pad for my application. Could you help me select the right material? Source: Thermal Pad Supplier China"
email_subject: "Thermal Pad Inquiry – China Supplier"
---

## Direct answer

[中文：导热垫片送样测试与量产验证]({{ '/zh/thermal-pad/' | relative_url }})

**OUYANG THERMAL supplies thermal pads (gap pads) for power-electronics and high-reliability assemblies** — BMS, PCS, OBC, DC/DC, IGBT and SiC power modules, AI servers, and optical modules. What an engineer or buyer gets here:

- **Thermal grade matched to the application** — the conductivity grade is selected from the ΔT budget and interface requirement, not from a headline W/m·K number. Published thermal-resistance evidence: [Case 001]({{ '/benchmark-evidence/ft-bn035-vs-sp2000-reference-sample/' | relative_url }}) and [Case 002]({{ '/benchmark-evidence/ft-bn050-thermal-resistance-vs-thickness/' | relative_url }}).
- **Thickness, hardness, and compression defined from the real gap** — nominal and worst-case gap, flatness, pressure distribution, and compression limits drive the choice; see [How to Select a Thermal Pad]({{ '/thermal-pad/how-to-select-a-thermal-pad/' | relative_url }}).
- **Electrical insulation where the design needs it** — dielectric strength and breakdown voltage verified at the installed thickness, not quoted from a different specimen.
- **Current-TIM benchmark** — send the incumbent material and TDS; we structure a same-condition comparison instead of declaring a replacement from datasheets ([Benchmark Your Current TIM]({{ '/benchmark-your-current-tim/' | relative_url }})).
- **Samples** — requestable once the target conductivity, thickness, hardness, and size are known ([Request a Sample]({{ '/request-sample/' | relative_url }})).
- **Second-source qualification** — a gated path from requirement mapping to pilot build, with "potential alternative subject to validation" as the only status until evidence is complete.

OUYANG THERMAL supports engineering evaluation, while Hongjing New Materials Technology (Shenzhen) Co., Ltd. coordinates commercial and supply-chain inquiries.

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/thermal-pad-supplier-qualification-12-gate-checklist.webp' | relative_url }}" width="1439" height="810" loading="lazy" decoding="async" alt="Twelve-gate thermal pad supplier qualification checklist from requirement definition through pilot build and change control"><figcaption><strong>Engineering Diagram.</strong> Twelve evidence gates for thermal-pad supplier qualification. The application owner defines acceptance criteria; this is not a certification claim.</figcaption></figure>

## Why 6 W/m·K ≠ 6 W/m·K

A datasheet thermal-conductivity value alone does not predict how a pad performs in an assembly. Installed performance is **thermal resistance across a real interface**, and two pads rated 6 W/m·K can behave very differently once installed. The actual result also depends on:

- **Thickness (BLT)** — a thicker bond line adds bulk resistance. [Case 002]({{ '/benchmark-evidence/ft-bn050-thermal-resistance-vs-thickness/' | relative_url }}) shows measured resistance rising across a thickness series of the same material.
- **Compression** — too little leaves air gaps; too much risks component damage. Force–deflection must be mapped across the minimum/maximum gap ([compression calculator]({{ '/engineering-resources/thermal-pad-compression-calculator/' | relative_url }}), [compression ratio explained]({{ '/thermal-pad/thermal-pad-compression-ratio-explained/' | relative_url }})).
- **Hardness** — sets how the pad conforms to surfaces under a given pressure.
- **Contact resistance** — surface flatness, finish, and wetting on both sides of the interface.
- **Pressure** — clamping-force distribution across the contact area, not a single nominal value.
- **Surface condition** — oxidation, coatings, contamination, and heatsink finish.
- **Test method** — ASTM D5470 results are only comparable when pressure, temperature, and specimen conditions match.

**When qualifying an alternative, compare thermal resistance / interface performance under matched conditions — not W/m·K numbers taken from different datasheets.** Useful references: [Thermal Conductivity vs Thermal Resistance]({{ '/comparison/thermal-conductivity-vs-thermal-resistance/' | relative_url }}), [3 vs 6 vs 8 W/mK Pads]({{ '/comparison/3w-vs-6w-vs-8w-thermal-pad/' | relative_url }}), [Thermal Resistance Calculator]({{ '/engineering-resources/thermal-resistance-calculator/' | relative_url }}).

## Thermal pad selection and qualification map

Scan by application, then validate by measurement. These are typical engineering considerations, not product specifications — limits must be defined by the responsible engineering team and verified in the actual assembly.

| Application | Target conductivity | Thickness | Hardness / compression | Electrical insulation | Thermal resistance concern | Recommended validation |
| --- | --- | --- | --- | --- | --- | --- |
| BMS / battery pack | Set from cell-to-coolant ΔT budget | Match measured gap plus tolerance stack | Soft; low clamping force | Usually required (pack voltage) | Large area with low pressure — contact resistance dominates | Force–deflection curve plus Rth at min/max gap; aging under vibration |
| PCS / energy storage | Set from device loss and heatsink budget | Match gap; watch tall-component tolerance | Medium; even pressure distribution | Required for high-voltage sections | Power cycling can cause settling or pump-out | Thermal cycling with Rth measured before and after |
| OBC (on-board charger) | Per power-device interface | Tight gaps; die-cut registration matters | Medium-soft; protect solder joints | Required (400/800 V architectures) | Mixed gaps across one assembly | Map each interface separately — see [OBC guide]({{ '/obc-thermal-material-supplier/' | relative_url }}) |
| DC/DC converter | Per hotspot ΔT | Small gaps; flatness critical | Medium | Required where primary/secondary bridge | Small area — alignment and BLT control dominate | Rth at defined pressure plus dielectric at installed thickness |
| IGBT module | Follows the module maker's Rth target | Match substrate flatness | Medium; avoid substrate bow | Required (isolation to heatsink) | Flatness and torque sequence | Rth plus dielectric per module spec — see [IGBT guide]({{ '/thermal-insulator/thermal-insulator-supplier-for-igbt-modules/' | relative_url }}) |
| SiC power module | Higher heat flux needs a lower Rth budget | Thin BLT preferred; flatness critical | Medium; controlled compression | Required; higher dV/dt stress | Interface voids hurt more at high heat flux | Rth at target pressure plus insulation validation in the assembly |
| AI server | Per component (GPU, VRM, memory) | Mixed gaps; needs compressibility range | Soft to medium; protect BGA packages | Sometimes (keep-out zones) | Large boards with warpage | Gap survey plus Rth at min/max compression |
| Optical module (800G / 1.6T) | Low power but tight ΔT | Thin; tight tolerance | Soft; low force on DSP/ASIC | Usually not the driver | Small area with low pressure | Rth at low pressure; liner and handling for small die-cuts |

## Benchmark Your Current Thermal Pad

Do not replace from a datasheet. Compare under the same conditions.

Send the following and we will structure a controlled benchmark plan — not a drop-in declaration:

- Current supplier and material (for example Bergquist, Laird, Henkel/Loctite, or another incumbent)
- TDS of the current pad
- Installed thickness and hardness
- Application and heat source
- Operating temperature range
- Compression / clamping condition
- Thermal target (ΔT or thermal resistance)

**Commercial path:** Current TIM → Benchmark → Sample → Validation → Second Source Qualification → Production.

<aside class="cta contextual-cta"><strong>Benchmark Your Current Thermal Pad</strong><p>Send the existing pad model or TDS, the gap range, and the first result to verify. Owen can help structure a same-condition benchmark — not declare a drop-in replacement from datasheet values.</p><p><a data-conversion="pad_benchmark_click" data-source="Thermal Pad Supplier China" data-cta-type="tim_benchmark" href="{{ '/benchmark-your-current-tim/' | relative_url }}">Benchmark Your Current Pad →</a></p><p><a data-conversion="sample_request_click" data-source="Thermal Pad Supplier China" href="{{ '/request-sample/' | relative_url }}">Request a Sample</a> · <a data-conversion="whatsapp_click" data-source="Thermal Pad Supplier China" href="https://wa.me/8613367909790">WhatsApp Owen</a> · <a data-conversion="email_click" data-source="Thermal Pad Supplier China" href="mailto:5672306@gmail.com">Email Owen</a></p></aside>

## Measured evidence: Case 001

One published internal benchmark shows how a matched-condition comparison is presented:

- **0.25 mm FT-BN035 measured 0.211 °C·in²/W** versus **0.267 °C·in²/W for the tested SP2000 reference sample** — approximately 21% lower **in this specific comparison**.
- Method: ASTM D5470 at approximately 50 psi; same nominal thickness for both samples.
- Full traceability (thickness series, electrical data, raw evidence, and limits) is on the case page: [Case 001: FT-BN035 vs SP2000 reference sample]({{ '/benchmark-evidence/ft-bn035-vs-sp2000-reference-sample/' | relative_url }}).

This is internal comparative testing under the stated conditions — not a third-party certification, not universal superiority, and not a drop-in replacement claim. Your material must still be benchmarked under your conditions.

## Request a Thermal Pad Sample

If the target conductivity, thickness, hardness, and outline size are already known, a sample can be requested directly: [Request a Thermal Pad Sample]({{ '/request-sample/' | relative_url }}).

Include where possible: application, gap range, operating temperature, compression condition, electrical requirement, and annual volume estimate. The more complete the inputs, the fewer sample iterations.

## Second-source qualification

If the assembly currently uses Bergquist, Laird, Henkel/Loctite, or another incumbent TIM, the engineering path is:

**Current material → Requirement mapping → Candidate selection → Sample → Thermal/mechanical validation → Qualification → Second source**

No "equivalent" or "drop-in replacement" status is claimed before validation evidence exists. "Potential alternative subject to validation" is the correct status until the gates below are complete. The [Second Source Qualification Generator]({{ '/engineering-resources/second-source-qualification-generator/' | relative_url }}) structures the requirement map, and the [TIM TDS Comparison Tool]({{ '/engineering-resources/tim-tds-comparison-tool/' | relative_url }}) keeps incumbent-versus-candidate data comparable.

## Applications and materials

Evaluation can cover pads for OBC, PCS, ESS, BMS, IGBT and MOSFET interfaces, optical modules, and server hardware. Relevant constructions may include electrically insulating gap pads and other compliant sheet interfaces, subject to supplier documentation and application validation. For gel-type gap fillers, see [Thermal Gel]({{ '/thermal-gel-supplier-china/' | relative_url }}).

## Selection and testing

Specify nominal and worst-case gap, flatness, pressure distribution, compression limits, hardness scale, thickness tolerance, thermal resistance method, dielectric strength, breakdown voltage, operating temperature, flame or regulatory needs, and aging conditions. Verify handling, die-cut geometry, liner design, placement, rework, and storage. Start with the [thickness selection guide]({{ '/thermal-pad/thermal-pad-thickness-selection-guide/' | relative_url }}) and [compression set explained]({{ '/thermal-pad/thermal-pad-compression-set-explained/' | relative_url }}).

{% include quick-contact.html %}

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

## What measured evidence should a supplier provide?

A useful qualification packet must connect each result to a named sample or lot, measured thickness, test method, pressure, temperature and conditioning history. Ask for the original units and specimen details—not only a rounded value copied into a sales table. For multi-lot validation, keep the same fixture and reporting format so that material variation is not confused with method variation.

Two published evidence examples show how this traceability can be presented:

- [Case 001: same-thickness FT-BN035 and SP2000 reference comparison]({{ '/benchmark-evidence/ft-bn035-vs-sp2000-reference-sample/' | relative_url }}) records measured thickness, ASTM D5470 thermal resistance and electrical evidence under the stated internal test conditions.
- [Case 002: FT-BN050 thermal resistance versus thickness]({{ '/benchmark-evidence/ft-bn050-thermal-resistance-vs-thickness/' | relative_url }}) shows why qualification should examine a thickness series rather than treating one conductivity value as installed performance.

These are internal comparative-test examples, not customer cases, independent certifications or universal product specifications. A buyer should define its own limits, repeat critical measurements across representative lots and confirm performance in the actual assembly before supplier approval.

## Frequently asked questions

### How do I compare two thermal pads with the same W/m·K?

Compare thermal resistance measured under matched conditions: same nominal thickness, same pressure, same temperature, same method (for example ASTM D5470). Then check hardness, compression behavior, tolerance, and electrical data at the installed thickness. The [TIM TDS Comparison Tool]({{ '/engineering-resources/tim-tds-comparison-tool/' | relative_url }}) keeps the two datasets side by side.

### What thickness thermal pad should I use?

Start from the measured gap — nominal and worst case — plus flatness and tolerance stack, then choose a thickness whose compression window covers that range without over-compressing. See the [thickness selection guide]({{ '/thermal-pad/thermal-pad-thickness-selection-guide/' | relative_url }}) and verify with the [compression calculator]({{ '/engineering-resources/thermal-pad-compression-calculator/' | relative_url }}).

### How does compression affect thermal resistance?

Moderate compression reduces contact resistance by closing air gaps; excessive compression risks component damage and diminishing returns. Map force–deflection across the real gap range and measure Rth at the minimum and maximum compression the assembly will see ([compression ratio explained]({{ '/thermal-pad/thermal-pad-compression-ratio-explained/' | relative_url }})).

### Can you benchmark our current thermal pad?

Yes. Send the current supplier and material, TDS, installed thickness and hardness, application, operating temperature, compression condition, and thermal target. We structure a same-condition benchmark plan: [Benchmark Your Current TIM]({{ '/benchmark-your-current-tim/' | relative_url }}).

### Can you provide a second-source thermal pad?

As a qualified second source through a gated process — requirement mapping, candidate selection, sample, thermal/mechanical validation, qualification — not as an unvalidated "equivalent." See [Second-source qualification](#second-source-qualification) and the [qualification generator]({{ '/engineering-resources/second-source-qualification-generator/' | relative_url }}).

### What information is needed to request a sample?

Target conductivity or thermal target, thickness, hardness, outline size, application, gap range, operating temperature, compression condition, electrical requirement, and estimated annual volume: [Request a Thermal Pad Sample]({{ '/request-sample/' | relative_url }}).

### How should thermal pads for IGBT/SiC modules be qualified?

Against the module maker's thermal and isolation requirements: Rth at the defined pressure and BLT, dielectric strength at installed thickness, flatness and torque-sequence control, plus thermal cycling relevant to the mission profile. See the [IGBT module guide]({{ '/thermal-insulator/thermal-insulator-supplier-for-igbt-modules/' | relative_url }}).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": {{ page.url | append: '#faq' | absolute_url | jsonify }},
  "mainEntity": [
    {"@type":"Question","name":"How do I compare two thermal pads with the same W/m·K?","acceptedAnswer":{"@type":"Answer","text":"Compare thermal resistance measured under matched conditions: same nominal thickness, same pressure, same temperature, and same method such as ASTM D5470. Then check hardness, compression behavior, tolerance, and electrical data at the installed thickness."}},
    {"@type":"Question","name":"What thickness thermal pad should I use?","acceptedAnswer":{"@type":"Answer","text":"Start from the measured gap, nominal and worst case, plus flatness and tolerance stack, then choose a thickness whose compression window covers that range without over-compressing. Verify with a compression calculator."}},
    {"@type":"Question","name":"How does compression affect thermal resistance?","acceptedAnswer":{"@type":"Answer","text":"Moderate compression reduces contact resistance by closing air gaps; excessive compression risks component damage with diminishing returns. Map force-deflection across the real gap range and measure thermal resistance at the minimum and maximum compression the assembly will see."}},
    {"@type":"Question","name":"Can you benchmark our current thermal pad?","acceptedAnswer":{"@type":"Answer","text":"Yes. Provide the current supplier and material, TDS, installed thickness and hardness, application, operating temperature, compression condition, and thermal target, and a same-condition benchmark plan can be structured."}},
    {"@type":"Question","name":"Can you provide a second-source thermal pad?","acceptedAnswer":{"@type":"Answer","text":"As a qualified second source through a gated process — requirement mapping, candidate selection, sample, thermal and mechanical validation, then qualification — not as an unvalidated equivalent."}},
    {"@type":"Question","name":"What information is needed to request a sample?","acceptedAnswer":{"@type":"Answer","text":"Target conductivity or thermal target, thickness, hardness, outline size, application, gap range, operating temperature, compression condition, electrical requirement, and estimated annual volume."}},
    {"@type":"Question","name":"How should thermal pads for IGBT/SiC modules be qualified?","acceptedAnswer":{"@type":"Answer","text":"Against the module maker's thermal and isolation requirements: thermal resistance at the defined pressure and bond-line thickness, dielectric strength at installed thickness, flatness and torque-sequence control, plus thermal cycling relevant to the mission profile."}}
  ]
}
</script>

## Related engineering guides

- [How to Select a Thermal Pad]({{ '/thermal-pad/how-to-select-a-thermal-pad/' | relative_url }})
- [Thickness Selection Guide]({{ '/thermal-pad/thermal-pad-thickness-selection-guide/' | relative_url }})
- [Compression Ratio Explained]({{ '/thermal-pad/thermal-pad-compression-ratio-explained/' | relative_url }})
- [3 vs 6 vs 8 W/mK Pads]({{ '/comparison/3w-vs-6w-vs-8w-thermal-pad/' | relative_url }})
- [Thermal Pad Compression Set]({{ '/thermal-pad/thermal-pad-compression-set-explained/' | relative_url }})
- [IGBT Thermal Insulator Supplier Qualification]({{ '/thermal-insulator/thermal-insulator-supplier-for-igbt-modules/' | relative_url }})
- [China TIM Supplier Evaluation]({{ '/china-thermal-interface-material-supplier/' | relative_url }})
- [Benchmark Your Current TIM]({{ '/benchmark-your-current-tim/' | relative_url }})
- [Thermal Pad Compression Calculator]({{ '/engineering-resources/thermal-pad-compression-calculator/' | relative_url }})
- [TIM TDS Comparison & Benchmark Tool]({{ '/engineering-resources/tim-tds-comparison-tool/' | relative_url }})
- [Request a Sample]({{ '/request-sample/' | relative_url }})

{% include contact-card.html subject="Thermal Pad Supplier Evaluation" %}
{% include commercial-authority-path.html %}
