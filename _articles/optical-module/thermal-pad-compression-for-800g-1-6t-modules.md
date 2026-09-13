---
title: "Thermal Pad Compression Ratio for 800G and 1.6T Optical Modules"
description: "Define an optical-module thermal-pad compression window from gap tolerances, force, contact resistance and reliability—not a universal percentage."
category: "Optical Module"
category_slug: "optical-module"
category_url: "/optical-module/"
author: "Ouyang Xiaohui"
date: 2026-09-13
updated: 2026-09-13
primary_keyword: "thermal pad compression ratio for optical modules"
search_demand: "Unknown"
---

<div class="quick"><strong>Answer first</strong><p>There is no universal best compression percentage for an 800G or 1.6T optical-module pad. Define a valid window: enough deflection to maintain full contact at maximum gap, but low enough force to protect the module, PCB, package, housing and insertion system at minimum gap.</p></div>

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/800g-1-6t-optical-module-thermal-pad-compression.webp' | relative_url }}" width="1439" height="810" loading="lazy" decoding="async" alt="Under-compressed, controlled and over-compressed thermal pad conditions in 800G and 1.6T optical module interfaces"><figcaption><strong>Representative Engineering Diagram.</strong> Under-compression can leave poor contact; excessive compression can increase mechanical stress. Product-specific limits require validation.</figcaption></figure>

## Calculate the installed state

If initial thickness is `t0` and compressed thickness is `tc`:

**Compression ratio = (t0 − tc) / t0 × 100%**

Run the calculation at minimum, nominal and maximum gaps. Do not confuse compression ratio with compression set: the first describes installed deflection; the second evaluates residual deformation after load removal and a defined recovery period.

## What determines the acceptable window?

| Boundary | Under-compression risk | Over-compression risk |
| --- | --- | --- |
| Contact | Partial contact and higher contact resistance | Pad extrusion or local stress concentration |
| Thermal | Unstable interface and hot spots | Thicker-than-expected or distorted heat path |
| Mechanical | Movement or intermittent contact | PCB bow, package load, housing distortion |
| Production | Sensitivity to gap variation | Difficult assembly, insertion or rework |
| Reliability | Contact loss after cycling | Permanent deformation or material damage |

Hardness is a method-dependent indentation result. Use compression-deflection data and actual loaded area to estimate force. Total force depends on stress multiplied by contact area, so a soft pad over a large area can still create significant load.

## Validation method

1. Measure actual stack components and build a tolerance model.
2. Select candidate thicknesses that cover the gap range.
3. Test force versus displacement at relevant temperature and rate.
4. Measure thermal impedance with pressure and compressed thickness recorded.
5. Assemble worst-case gap fixtures or modules.
6. Check critical temperatures, contact evidence, insertion and retention behavior.
7. Apply relevant cycling, humidity or vibration.
8. Recheck pad position, thickness, contact and thermal response.

ASTM D5470 can support controlled comparison of thermal impedance, but its idealized heat flow does not directly reproduce most assemblies. Hardware validation remains necessary.

## Common mistakes

- Publishing one compression percentage as universal.
- Calculating from nominal sheet thickness without measuring it.
- Using hardness as a substitute for force-deflection data.
- Checking maximum gap contact but not minimum gap load.
- Comparing thermal results at different pressure or thickness.
- Ignoring repeated insertion, liner handling and pad shift.

## FAQ

<details><summary>Does more compression always lower contact resistance?</summary><p>No. Initial contact may improve, but benefit can level off while mechanical load and material distortion continue increasing.</p></details>
<details><summary>Should 800G and 1.6T use the same compression window?</summary><p>Not by default. Compare geometry, heat sources, contact area, housing, host cooling and mechanical limits.</p></details>
<details><summary>How should a supplier state the recommendation?</summary><p>Request a product-specific range tied to thickness, temperature, area and force-deflection evidence, then validate it in your assembly.</p></details>

## Related engineering resources

- [800G supplier qualification]({{ '/optical-module/thermal-pad-supplier-for-800g-optical-modules/' | relative_url }})
- [1.6T thermal-pad selection]({{ '/optical-module/thermal-pad-for-1-6t-optical-modules/' | relative_url }})
- [Compression ratio explained]({{ '/thermal-pad/thermal-pad-compression-ratio-explained/' | relative_url }})
- [Compression set explained]({{ '/thermal-pad/thermal-pad-compression-set-explained/' | relative_url }})

[Ask Ouyang]({{ '/discuss-your-application/' | relative_url }}) with the gap distribution, area and force limit, or [benchmark the current pad]({{ '/benchmark-your-current-tim/' | relative_url }}).

## Reference

- [ASTM D5470-17(2024)](https://store.astm.org/standards/d5470), thermal transmission testing for thermally conductive electrical insulation materials.

