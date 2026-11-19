---
title: "Thermal Interface Materials Video: AI Servers, Energy Storage and EVs"
description: "Watch a 60-second overview of thermal gap pads, thermal gap fillers and thermally conductive potting compounds for AI servers, energy storage PCS and EV power electronics — plus five 10-second explainers on compression, pad thickness, second-source benchmarking, PCS module gaps and optical-module TIM checks."
permalink: /thermal-interface-materials-video/
author: Ouyang Xiaohui
updated: 2026-11-19
commercial_contact: true
contact_message: "Hi Ouyang, I watched the thermal interface materials video. Could you help me evaluate a material for my application? Source: Thermal Interface Materials Video"
email_subject: "Thermal Material Inquiry – Video"
---

## Answer first

This 60-second video shows where thermal interface materials work: [thermal gap pads]({{ '/thermal-pad/' | relative_url }}), [thermal gap fillers]({{ '/thermal-gel/' | relative_url }}) and [thermally conductive potting compounds]({{ '/potting-compound/' | relative_url }}) in AI servers, energy storage PCS and EV power electronics. The narration is in English with bilingual English/Chinese subtitles. The video states no material performance data; material selection should be based on the applicable technical data sheet and application testing.

<video controls preload="metadata" poster="{{ '/assets/videos/thermal-interface-materials-video-cover.jpg' | relative_url }}" width="1280" height="720" style="width:100%;height:auto;">
  <source src="{{ '/assets/videos/thermal-interface-materials-video-60s.mp4' | relative_url }}" type="video/mp4">
  Your browser cannot play this video inline. <a href="{{ '/assets/videos/thermal-interface-materials-video-60s.mp4' | relative_url }}">Download the 60-second video (MP4, 60 s)</a>.
</video>

<script type="application/ld+json">{"@context":"https://schema.org","@type":"VideoObject","name":"Thermal Interface Materials for AI Servers, Energy Storage & EVs | HONGJING","description":"A 60-second overview of thermal gap pads, thermal gap fillers and thermally conductive potting compounds for AI servers, energy storage PCS and EV power electronics.","thumbnailUrl":"https://ouyangthermal.github.io/assets/videos/thermal-interface-materials-video-cover.jpg","uploadDate":"2026-10-28","duration":"PT60S","contentUrl":"https://ouyangthermal.github.io/assets/videos/thermal-interface-materials-video-60s.mp4","embedUrl":"https://ouyangthermal.github.io/thermal-interface-materials-video/","inLanguage":"en"}</script>

## Engineering Shorts — 10-second explainers

Five 10-second clips, each answering one engineering question with a visual. Subtitles are in English. The footage is AI-generated concept illustration, like the 60-second video above: no clip shows a measured result or a product performance claim. Numbers shown come from the linked tool or guide, and the worked examples are labelled as examples.

### 1. How compression changes thermal resistance

<video controls preload="metadata" poster="{{ '/assets/videos/engineering-short-compression-thermal-resistance.jpg' | relative_url }}" width="1280" height="720" style="width:100%;height:auto;">
  <source src="{{ '/assets/videos/engineering-short-compression-thermal-resistance.mp4' | relative_url }}" type="video/mp4">
  Your browser cannot play this video inline. <a href="{{ '/assets/videos/engineering-short-compression-thermal-resistance.mp4' | relative_url }}">Download the 10-second video (MP4, 10 s)</a>.
</video>

A 2.0 mm pad installed in a 1.6 mm gap is compressed 0.4 mm (20%). The clip shows the theoretical bulk resistance for that installed state; the installed interface measures higher once contact resistance is included, so model your own gap with the [Thermal Pad Compression Calculator]({{ '/engineering-resources/thermal-pad-compression-calculator/' | relative_url }}).

### 2. Pick a pad thicker than the gap

<video controls preload="metadata" poster="{{ '/assets/videos/engineering-short-pad-thicker-than-gap.jpg' | relative_url }}" width="1280" height="720" style="width:100%;height:auto;">
  <source src="{{ '/assets/videos/engineering-short-pad-thicker-than-gap.mp4' | relative_url }}" type="video/mp4">
  Your browser cannot play this video inline. <a href="{{ '/assets/videos/engineering-short-pad-thicker-than-gap.mp4' | relative_url }}">Download the 10-second video (MP4, 10 s)</a>.
</video>

An engineering-forum question asked how to move heat from a PCB across a ~6 mm gap to an aluminum enclosure. The rule is simple — the pad must be thicker than the gap it fills — illustrated with the worked example of a 2.0 mm pad in a 1.6 mm gap. See [How to Select a Thermal Pad]({{ '/thermal-pad/how-to-select-a-thermal-pad/' | relative_url }}) for the selection steps.

### 3. Same W/m·K, different installed resistance

<video controls preload="metadata" poster="{{ '/assets/videos/engineering-short-same-wmk-different-resistance.jpg' | relative_url }}" width="1280" height="720" style="width:100%;height:auto;">
  <source src="{{ '/assets/videos/engineering-short-same-wmk-different-resistance.mp4' | relative_url }}" type="video/mp4">
  Your browser cannot play this video inline. <a href="{{ '/assets/videos/engineering-short-same-wmk-different-resistance.mp4' | relative_url }}">Download the 10-second video (MP4, 10 s)</a>.
</video>

Two materials can share the same datasheet conductivity and still behave differently once installed — thickness, compression, contact resistance, hardness and surface condition all contribute. Compare thermal resistance under matched conditions instead. The method is on the [Dow 5121C Alternative Evaluation]({{ '/dow-5121c-alternative-evaluation/' | relative_url }}) page.

### 4. PCS module: two gaps, one thermal budget

<video controls preload="metadata" poster="{{ '/assets/videos/engineering-short-pcs-two-gaps.jpg' | relative_url }}" width="1280" height="720" style="width:100%;height:auto;">
  <source src="{{ '/assets/videos/engineering-short-pcs-two-gaps.mp4' | relative_url }}" type="video/mp4">
  Your browser cannot play this video inline. <a href="{{ '/assets/videos/engineering-short-pcs-two-gaps.mp4' | relative_url }}">Download the 10-second video (MP4, 10 s)</a>.
</video>

A PCS power module usually needs more than one thermal interface: a thin, clamped interface under the IGBT module and a compliant gap filler for magnetics with large tolerances. The worked examples from [Case 003 — PCS Power Module TIM Selection]({{ '/benchmark-evidence/pcs-power-module-tim-selection/' | relative_url }}) show the thick magnetics gap carrying roughly thirteen times the bulk resistance of the thin IGBT interface — 0.625 K/W against 0.046 K/W — so thickness and installed geometry dominate the selection, not the conductivity headline alone. These are worked calculation examples, not measured data.

### 5. Optical modules: 12 W/m·K is not enough

<video controls preload="metadata" poster="{{ '/assets/videos/engineering-short-optical-12w-not-enough.jpg' | relative_url }}" width="1280" height="720" style="width:100%;height:auto;">
  <source src="{{ '/assets/videos/engineering-short-optical-12w-not-enough.mp4' | relative_url }}" type="video/mp4">
  Your browser cannot play this video inline. <a href="{{ '/assets/videos/engineering-short-optical-12w-not-enough.mp4' | relative_url }}">Download the 10-second video (MP4, 10 s)</a>.
</video>

In 800G/1.6T optical modules, a 12 W/m·K gel such as Dow's DOWSIL TC-3120 is only the start: oil bleed can contaminate lenses and fibers, and a gel that slumps in a vertically mounted transceiver leaves a voided interface. Dow reports no cracking or slumping for TC-3120 after 1,000-hour vertical aging at 150 °C — ask for that test, not just the conductivity headline. See [Thermal Interface Materials for Optical Transceivers]({{ '/optical-module/thermal-interface-materials-for-optical-transceivers/' | relative_url }}) for the selection criteria.

<script type="application/ld+json">[{"@context":"https://schema.org","@type":"VideoObject","name":"How compression changes thermal resistance","description":"A 2.0 mm thermal gap pad installed in a 1.6 mm gap is compressed 0.4 mm (20%); the clip shows the theoretical bulk resistance for that installed state.","thumbnailUrl":"https://ouyangthermal.github.io/assets/videos/engineering-short-compression-thermal-resistance.jpg","uploadDate":"2026-11-10","duration":"PT10S","contentUrl":"https://ouyangthermal.github.io/assets/videos/engineering-short-compression-thermal-resistance.mp4","embedUrl":"https://ouyangthermal.github.io/thermal-interface-materials-video/","inLanguage":"en"},{"@context":"https://schema.org","@type":"VideoObject","name":"Pick a pad thicker than the gap","description":"A 10-second explainer: the pad must be thicker than the gap it fills, illustrated with a 2.0 mm pad in a 1.6 mm gap.","thumbnailUrl":"https://ouyangthermal.github.io/assets/videos/engineering-short-pad-thicker-than-gap.jpg","uploadDate":"2026-11-12","duration":"PT10S","contentUrl":"https://ouyangthermal.github.io/assets/videos/engineering-short-pad-thicker-than-gap.mp4","embedUrl":"https://ouyangthermal.github.io/thermal-interface-materials-video/","inLanguage":"en"},{"@context":"https://schema.org","@type":"VideoObject","name":"Same W/m·K, different installed resistance","description":"Two materials can share the same datasheet conductivity and still behave differently once installed; compare thermal resistance under matched conditions.","thumbnailUrl":"https://ouyangthermal.github.io/assets/videos/engineering-short-same-wmk-different-resistance.jpg","uploadDate":"2026-11-14","duration":"PT10S","contentUrl":"https://ouyangthermal.github.io/assets/videos/engineering-short-same-wmk-different-resistance.mp4","embedUrl":"https://ouyangthermal.github.io/thermal-interface-materials-video/","inLanguage":"en"},{"@context":"https://schema.org","@type":"VideoObject","name":"PCS module: two gaps, one thermal budget","description":"Worked calculation examples from Case 003: a thin IGBT interface at 1 mm gives about 0.046 K/W while a thick magnetics gap at 3 mm gives about 0.625 K/W — roughly thirteen times more.","thumbnailUrl":"https://ouyangthermal.github.io/assets/videos/engineering-short-pcs-two-gaps.jpg","uploadDate":"2026-11-17","duration":"PT10S","contentUrl":"https://ouyangthermal.github.io/assets/videos/engineering-short-pcs-two-gaps.mp4","embedUrl":"https://ouyangthermal.github.io/thermal-interface-materials-video/","inLanguage":"en"},{"@context":"https://schema.org","@type":"VideoObject","name":"Optical modules: 12 W/m·K is not enough","description":"In 800G/1.6T optical modules, conductivity alone is not enough: oil bleed can contaminate optics, and Dow reports no cracking or slumping for DOWSIL TC-3120 after 1,000-hour vertical aging at 150 °C.","thumbnailUrl":"https://ouyangthermal.github.io/assets/videos/engineering-short-optical-12w-not-enough.jpg","uploadDate":"2026-11-19","duration":"PT10S","contentUrl":"https://ouyangthermal.github.io/assets/videos/engineering-short-optical-12w-not-enough.mp4","embedUrl":"https://ouyangthermal.github.io/thermal-interface-materials-video/","inLanguage":"en"}]</script>

## What the video shows

- **0:00–0:10 — The thermal challenge.** Inside an AI data center, GPUs and power electronics run hot; the contact interface between a heat-generating device and its cooling structure decides how well heat leaves the device.
- **0:10–0:20 — Thermal gap filler.** A dispensed gap filler conforms to uneven surfaces and fills the microscopic air gaps at the contact interface, giving heat a path into the heat sink.
- **0:20–0:30 — Thermal gap pad.** A compliant gap pad is placed at the power-stage interface inside an energy storage PCS and compressed under assembly, improving contact and heat transfer.
- **0:30–0:40 — Thermally conductive potting.** A two-part potting compound fills an EV power electronics module around coils, PCBs and components, supporting protection and heat transfer.
- **0:40–0:50 — Three applications.** AI infrastructure, energy storage stations and electric mobility — the same interface problem at different scales.
- **0:50–1:00 — Materials and contact.** Gap pads, gap fillers and potting compounds from HONGJING New Materials, with sample, technical evaluation and RFQ routes via Ouyang Thermal.

## Transcript

> As computing power rises, thermal challenges become more demanding.
>
> Thermal gap fillers conform to uneven surfaces, helping transfer heat.
>
> Thermal gap pads provide compliant interfaces for power electronics.
>
> Thermally conductive potting compounds support protection and heat transfer.
>
> From AI infrastructure to energy storage and electric mobility.
>
> HONGJING New Materials. Your partner for thermal interface solutions.

## Start from the application

| Need | Start here |
| --- | --- |
| Compressible sheet gap filler | [China thermal pad supplier evaluation]({{ '/thermal-pad-supplier-china/' | relative_url }}) |
| Dispensed gap filler | [China thermal gel supplier evaluation]({{ '/thermal-gel-supplier-china/' | relative_url }}) |
| AI-server power conversion | [AI server and 800V DC TIM map]({{ '/server/thermal-interface-materials-for-ai-server-power-supplies-and-800v-dc/' | relative_url }}) |
| PCS and energy storage | [PCS TIM selection]({{ '/pcs/tim-selection-for-pcs/' | relative_url }}) |
| OBC and EV power electronics | [OBC complete selection guide]({{ '/obc/thermal-interface-materials-for-obc-complete-selection-guide/' | relative_url }}) |
| Second-source qualification | [Second Source Qualification Generator]({{ '/engineering-resources/second-source-qualification-generator/' | relative_url }}) |

<aside class="cta contextual-cta"><strong>Benchmark Your Current TIM</strong><p>Send the existing material model or TDS, the application and the first result to verify — thermal, compression, dispensing or reliability. Owen can help structure a same-condition benchmark on representative hardware.</p><p><a data-conversion="tim_benchmark_click" data-source="Thermal Interface Materials Video" data-cta-type="tim_benchmark" href="{{ '/benchmark-your-current-tim/' | relative_url }}">Benchmark Your Current TIM →</a></p><p><a data-conversion="sample_request_click" data-source="Thermal Interface Materials Video" href="{{ '/request-sample/' | relative_url }}">Request a Sample</a> · <a data-conversion="whatsapp_click" data-source="Thermal Interface Materials Video" href="https://wa.me/8613367909790">WhatsApp Owen</a> · <a data-conversion="email_click" data-source="Thermal Interface Materials Video" href="mailto:5672306@gmail.com">Email Owen</a></p></aside>

## About the footage

The footage is AI-generated concept illustration. It does not depict HONGJING production facilities, production lines or any customer's hardware, and no frame should be read as a customer case, a tested result or a performance claim. OUYANG THERMAL provides engineering knowledge, application analysis, TIM selection and benchmark guidance. Hongjing New Materials Technology (Shenzhen) Co., Ltd. handles commercial inquiries, sample coordination, RFQs and supply-chain coordination.
