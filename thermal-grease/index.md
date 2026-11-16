---
title: Thermal Grease
description: "Thermal grease for thin, clamped, controlled bond lines in IGBT and power modules: how to compare bond-line thickness, thermal impedance, pump-out and silicone-free options before sampling."
permalink: /thermal-grease/
author: Ouyang Xiaohui
updated: 2026-11-16
commercial_contact: true
contact_message: "Hi Ouyang, I'm evaluating thermal grease for a power module interface. Could you help me compare bond-line thickness, thermal impedance and silicone-free options? Source: Thermal Grease"
email_subject: "Thermal Grease Evaluation — IGBT / Power Module"
---

<div class="quick"><strong>Answer first</strong><p>Thermal grease fits thin, clamped, flat interfaces — typically IGBT and power-module baseplates — where a controlled bond line under 25–50 µm keeps thermal impedance low. It is the wrong choice for large or uneven gaps: use a thermal pad or gap filler there. Compare grease by thermal impedance at a stated bond-line thickness and pressure, not by conductivity alone.</p></div>

Thin bond-line compounds for controlled, clamped interfaces.

<p><a href="{{ '/video-guide/thermal-management-materials-video-guide/' | relative_url }}">See thermal interface materials in real applications</a> — a video guide showing where thermal pads, gels and other TIMs are actually used inside electronic products.</p>

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/thermal-grease-thin-bond-line-interface.webp' | relative_url }}" width="1200" height="800" loading="lazy" decoding="async" alt="Thin thermal grease bond line between a power device and heat sink"><figcaption><strong>Engineering Diagram.</strong> Engineering comparison of a controlled grease bond line, excess material and an unsuitable large gap.</figcaption></figure>

## How to compare thermal grease

| Parameter | Engineering question | Evidence to request |
|---|---|---|
| Thermal impedance | At what bond-line thickness and pressure? | Impedance at application BLT and pressure, not a single headline value |
| Thermal conductivity | Measured how, and after what conditioning? | Method, specimen conditions, and whether the value is before or after solvent evaporation |
| Bond-line thickness | How thin can it be held under clamp load? | BLT vs pressure data for the actual surfaces |
| Pump-out and dry-out | Does impedance drift under thermal cycling? | Impedance after cycling and long-term aging, not only fresh values |
| Electrical isolation | Is the grease isolating or conductive? | Method, thickness, and voltage context — grease alone is not an insulation rating |
| Silicone migration | Does silicone outgassing or bleed matter here? | Silicone-free formulation or outgassing data where optics or sensitive contacts are nearby |
| Rework and cleaning | Can the interface be reworked without residue? | Cleaning procedure and re-application guidance |

A supplier typical value is not a guaranteed design limit. Record the test method, bond-line thickness, pressure, surfaces and temperature before treating two values as comparable.

## Silicone-free grease: what to compare

Silicone-free grease matters where silicone outgassing or migration is a contamination risk — for example near optical components or sensitive contacts. On 2026-11-09 Henkel announced Loctite Bergquist TGR 5000SF, a silicone-free thermal grease for high-power components ([Henkel press release, 2026-11-09](https://www.henkel.com/press-and-media/press-releases-and-kits/2026-11-09-high-performance-thermal-grease-from-henkel-delivers-for-high-power-applications-2273388)). Henkel's stated values for the product are: bond line under 25 µm at 40 psi, thermal conductivity 5.3 W/m·K after solvent evaporation, and thermal impedance 5.6 mm²·K/W. Henkel also states less than 15% thermal degradation after 1,000 hours at various temperatures and no performance loss during thermal cycling from −40 °C to 125 °C. These are the manufacturer's stated values, not our test results.

Read the impedance, not just the conductivity. For a 25 µm bond line at 5.3 W/m·K, the bulk contribution alone is t/k = 25 × 10⁻⁶ / 5.3 ≈ 4.72 mm²·K/W. The stated total impedance of 5.6 mm²·K/W is higher because it also includes contact resistance (about 0.88 mm²·K/W by subtraction). Two greases with the same conductivity can therefore show different installed impedance — always compare impedance at the same bond-line thickness and pressure, and request the verified TDS and aging data before treating any candidate as equivalent.

Ouyang Thermal does not claim an equivalent product. A second-source evaluation starts from the incumbent's verified TDS and the application's bond line, pressure, temperature and contamination requirements — see the [second-source qualification framework]({{ '/dow-5121c-alternative-evaluation/' | relative_url }}) and the [Second Source Qualification Generator]({{ '/engineering-resources/second-source-qualification-generator/' | relative_url }}).

## Grease vs pad vs gel

- **Grease:** thin, clamped, flat interfaces; lowest bond line; needs controlled dispensing and rework planning.
- **Thermal pad:** uneven gaps and tolerance stack-up; dry, reworkable, electrically insulating options available.
- **Thermal gel:** large or complex gaps, automated dispensing, and interfaces that need a cured compliant filler.

Compare the three families side by side in [Thermal Pad vs Thermal Grease vs Thermal Gel]({{ '/comparison/thermal-pad-vs-thermal-grease-vs-thermal-gel/' | relative_url }}). For IGBT and MOSFET interfaces, see [How to Select TIM for IGBT and MOSFET]({{ '/power-electronics/how-to-select-tim-for-igbt-and-mosfet/' | relative_url }}).

## Related engineering tools

- [Thermal Resistance Calculator]({{ '/engineering-resources/thermal-resistance-calculator/' | relative_url }}) — estimate bulk resistance R = t/(k·A) for a candidate bond line.
- [TIM TDS Comparison and Second-Source Check]({{ '/engineering-resources/tim-tds-comparison-tool/' | relative_url }}) — compare two TDS values at aligned conditions before sampling.
- [TIM Selection Tool]({{ '/engineering-resources/tim-selection-tool/' | relative_url }}) — narrow the TIM family from gap, insulation, rework and tolerance inputs.

<p>Maintained by Ouyang Xiaohui (Owen Ouyang), Ouyang Thermal. Last reviewed 2026-11-16.</p>

{% include visual-cta.html visual_id="V05" %}

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "thermal-grease" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
