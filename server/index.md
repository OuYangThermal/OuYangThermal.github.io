---
title: "AI Server TIM Selection and Second-Source Evaluation"
description: "Plan AI server TIM benchmarks and samples by interface, installed thickness, force, electrical requirements and pilot-build acceptance criteria."
permalink: /server/
commercial_contact: true
updated: 2026-09-24
contact_message: "Hi Owen, we are evaluating an AI server TIM or second source. We can share the current TDS, interface location and gap range."
email_subject: "AI Server TIM Benchmark and Sample Discussion"
---

<div class="quick"><strong>Answer first</strong><p>Start an AI server TIM sourcing project with one defined interface: the heat source, mating surface, installed gap and permitted load. Compare the current material and candidate under agreed thermal, mechanical and electrical conditions, then check assembly repeatability and reliability before approving a second source. A matching conductivity value alone does not establish replacement suitability.</p></div>

OUYANG THERMAL provides engineering selection guidance and benchmark planning. Discuss your interface with **Owen Ouyang** to define the evidence needed for sample evaluation; final material approval belongs to the application owner.

## Choose the interface before choosing the material

The heat path is component or package → TIM → heat sink or cold plate → cooling system. Confirm which part of that path your proposed replacement actually changes.

| Interface to review | First decision | Evidence needed before sampling |
| --- | --- | --- |
| Processor or accelerator to cold plate | Confirm the package-approved TIM class and load limits; a gap pad is not automatically suitable for a thin processor interface | Package guidance, surface geometry, installed BLT and clamping limits |
| Memory, VRM or other supporting components to spreader | Compare pad placement with gel dispensing for the actual height variation | Minimum/maximum gap, total assembly force, coverage and rework needs |
| Power module or DC-DC stage to heat sink | Determine whether electrical isolation is supplied by the construction or required from the TIM | Working insulation requirements, thickness, pressure and relevant electrical test conditions |

HBM locations and cooling constructions vary by package. Do not assume exposed, individually padded memory. Likewise, an 800V DC system description does not specify the voltage across a particular TIM or establish its required dielectric rating.

Use the [pad-versus-gel application guide]({{ '/server/thermal-pad-vs-thermal-gel-for-ai-servers/' | relative_url }}) for material-family decisions and the [power-supply and 800V DC interface guide]({{ '/server/thermal-interface-materials-for-ai-server-power-supplies-and-800v-dc/' | relative_url }}) for power-conversion boundaries.

## A practical incumbent-versus-candidate benchmark

**Recommended test plan, not a reported server test result.** Agree acceptance criteria with thermal, mechanical, process and quality owners before testing.

1. **Freeze the reference.** Record the incumbent TDS revision, interface dimensions, gap tolerance, surfaces, cooling boundary and failure being investigated. Use sanitized information for the initial discussion.
2. **Compare installed performance.** Record heat load in W, temperature measurement locations, installed BLT in mm, contact area and force or pressure. Separate material conductivity in W/m·K from measured interface resistance in K/W; retain area-normalized units when that is what the report provides.
3. **Check contact and assembly.** For pads, evaluate compression and total force, placement and liner removal. For gels, evaluate deposited quantity, coverage, voids, squeeze-out and cure where applicable. Hardness readings require the same scale and method and cannot replace force measurements.
4. **Validate the service conditions.** Define temperature exposure, cycling and service/rework sequences from the application requirements. Check thermal drift, mechanical damage and electrical isolation where required after exposure. Select multiple production lots and sample counts through the agreed qualification plan.
5. **Run a pilot build.** Confirm inspection criteria, lot traceability, packaging/storage controls and supplier change notification. Advance to RFQ with the finished-part or dispensing specification and unresolved risks recorded.

ASTM D5470 provides a controlled thermal-impedance measurement framework; its idealized heat flow does not directly reproduce most practical assemblies. Keep fixture comparisons separate from representative server validation. See the [ASTM method scope](https://store.astm.org/standards/d5470).

The published [Case 001 internal benchmark]({{ '/benchmark-evidence/ft-bn035-vs-sp2000-reference-sample/' | relative_url }}) illustrates condition-labelled reporting. It is not AI server qualification evidence and its results must not be transferred to a server interface.

## Start with the information you already have

Send the **current material name or TDS, interface location, approximate gap and the problem to solve**. Missing a parameter is fine: identify it as unknown. Do not send confidential drawings or customer information without permission.

<aside class="cta contextual-cta"><strong>Evaluating an AI server TIM second source?</strong><p>Ask Owen to help define a benchmark and sample plan for one interface before committing to a larger qualification programme.</p><p><a class="button-link" href="{{ '/benchmark-your-current-tim/' | relative_url }}">Discuss a TIM Benchmark</a> <a class="button-link" href="{{ '/request-sample/' | relative_url }}">Request a Sample</a></p><p><a href="https://wa.me/8613367909790?text={{ page.contact_message | url_encode }}">WhatsApp Owen</a> · <a href="mailto:5672306@gmail.com?subject={{ page.email_subject | url_encode }}">Email Owen</a> · <a href="{{ '/discuss-your-application/' | relative_url }}">Send a Private Question</a></p></aside>

## Questions before sample evaluation

<details><summary>Can the same W/m·K rating qualify a replacement?</summary><p>No. Installed thickness, both contact surfaces, mounting load, electrical requirements and aging can change the result. Align test conditions and validate the actual assembly.</p></details>
<details><summary>Should every server interface use the same pad or gel?</summary><p>No. Treat each interface as a separate requirement. A processor interface, a variable-height component field and an electrically isolated power stage can need different material classes and controls.</p></details>
<details><summary>What if we do not yet know the installed BLT?</summary><p>Share the nominal gap and available tolerance information. Agree how installed thickness and compression will be measured before interpreting a comparison; do not substitute the uncompressed sheet thickness for measured BLT.</p></details>
<details><summary>When is a second source ready for RFQ?</summary><p>When the specification, acceptance tests, sample findings, pilot-build controls and remaining qualification risks are documented. An RFQ is a sourcing step, not proof that reliability validation has passed.</p></details>

## AI server engineering guides

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "server" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
