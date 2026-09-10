# OUYANG THERMAL Image Library

## Purpose

This library gives maintainers and Codex one authoritative, searchable inventory of visual assets. Before adding or changing page imagery, query [`data/image-library.json`](../data/image-library.json) by product, application, topic, authenticity, usage, and reuse policy. The goal is to reuse a relevant approved asset when appropriate without turning the same picture into a repetitive site-wide decoration.

## Directory structure

- `assets/images/visual-content/` — published V03–V12 engineering/application diagrams, portrait, and production reference.
- `assets/images/real-evidence/` — individual user-supplied real-photo references.
- `assets/images/source/` — non-rendered source masters used to derive optimized variants.
- `assets/images/` — published homepage V01/V02 assets.
- `assets/favicon.svg` — interface favicon.
- `visual-inbox/` — temporary intake only; never treat it as the production asset directory.
- `data/image-library.json` — machine-readable source of truth.
- `scripts/audit-image-library.js` — dependency-free integrity audit.

## Naming rules

Use lowercase descriptive English filenames with hyphens. Name the material, application, and visual purpose rather than a meaningless sequence. IDs such as V03 remain metadata; they do not need to be repeated in a published filename. Keep the original extension only when it is the chosen production format. Do not append `.webp` to a PNG filename.

## Real photos and engineering diagrams

`real-photo`, `real-photo-composite`, `portrait`, `product-sample`, and `production-reference` describe photographic material. They do not prove a customer relationship, material grade, performance, ownership, capacity, or test result. `engineering-diagram` and `application-diagram` explain a principle or representative assembly and are not evidence of an actual customer product.

## Authenticity wording

- Real user-supplied photos: use **Real Application Reference** or **Engineering Application Example**.
- Production imagery: use **Real Production Reference** or **Material and Process Evidence** and avoid ownership/capacity claims.
- Generated diagrams: use **Engineering Diagram**, **Representative Engineering Diagram**, or **Generic Engineering Diagram**.
- Never use **Customer Case**, **Validated Performance**, **Actual Customer Product**, or similar wording unless the manifest is updated with documented authorization and evidence.
- `rights_status: user-supplied-rights-not-independently-verified` means the file was supplied for this site but independent provenance/authorization evidence is not stored in this repository.

## Matching an image to a new article

1. Read the image manifest before drafting the visual section.
2. Filter by exact `products`, then `applications`, then `topics`.
3. Confirm `authenticity`, `rights_status`, `primary_page`, `used_on`, and `reuse_policy`.
4. Reuse only when the image materially explains the new context and the policy permits it.
5. If cropping is allowed, preserve technical meaning and update the crop as a distinct derivative record; do not overwrite the source.
6. If no suitable asset exists, prepare a new brief and send it through `visual-inbox`.

## visual-inbox workflow

```text
visual-inbox
→ inspect content and source
→ assign authenticity type
→ choose a descriptive English filename
→ check duplicate SHA-256
→ convert to an appropriate WebP when useful
→ move into the formal asset directory
→ update image-library.json
→ update IMAGE_LIBRARY.md
→ add to the page
→ run tests
→ deploy
```

Processed copies must not remain in both `visual-inbox` and a formal directory. A unique editable/source master belongs in `assets/images/source/`, not in the inbox.

## Duplicate checking

Run:

```bash
npm run audit:images
```

The audit scans WebP, PNG, JPG, JPEG, and SVG files, calculates SHA-256, reads real dimensions, detects duplicate binaries, checks manifest paths and metadata, finds referenced-but-unregistered and registered-but-unused images, validates `used_on`, and checks rendered image attributes. Duplicate binaries and consistency failures return a non-zero exit code.

## Updating ALT and usage

When page context changes, update the rendered ALT and the manifest `alt` together. ALT should describe what is visually meaningful in that context without keyword stuffing. After adding or removing a reference, update `used_on` to the exact public route and run the audit. Update `primary_page` only when the intended canonical visual placement changes.

## Restricted reuse

- V01 desktop/mobile are homepage-responsive assets; the PNG is a non-rendered source master.
- V02 is a homepage real-photo composite, not a customer case.
- V03–V08 and V10–V12 are primary-page-only diagrams.
- V09 portrait and production composite are About-page-only.
- V02 individual photos are primary-page-only unless `single-context-after-review` is explicitly recorded.
- No user-supplied real photo may be called a customer case under the current manifest.

## Index

| ID | Image | Type | Product | Application | Primary page | Status |
| -- | -- | -- | -- | -- | -- | -- |
| UI-FAVICON | favicon.svg | application-diagram | — | site interface | sitewide | published |
| V01 | thermal-interface-material-applications-obc-pcs-optical-ai-server.webp | application-diagram | thermal pad, thermal gel | OBC, PCS, ESS, optical, AI server | / | published |
| V01-MOBILE | thermal-interface-material-applications-mobile.webp | application-diagram | thermal pad, thermal gel | homepage mobile | / | published |
| V01-SOURCE | thermal-interface-material-applications-obc-pcs-optical-ai-server-source.png | application-diagram | thermal pad, thermal gel | source master | — | source-master |
| V02 | real-thermal-materials-and-applications-v02.webp | real-photo-composite | multiple TIMs | OBC, PCB, optical, power, battery | / | published |
| V02-01 | 01-thermal-material-samples.jpg | product-sample | thermal pad, gel, grease | material overview | — | available |
| V02-02 | 02-obc-thermal-pad-layout.jpg | real-photo | thermal pad | OBC | /thermal-pad/ | published |
| V02-03 | 03-pcb-thermal-gel-dispensing.jpg | real-photo | thermal gel | PCB | /thermal-gel/ | published |
| V02-04 | 04-thermal-gel-dot-pattern.jpg | real-photo | thermal gel | dispensing process | /thermal-gel/common-thermal-gel-dispensing-problems/ | published |
| V02-05 | 05-optical-transceiver-tim-opened.jpg | real-photo | TIM | optical transceiver | /optical-module/ | published |
| V02-06 | 06-optical-transceiver-tim-contact.jpg | real-photo | TIM | optical transceiver | /optical-module/thermal-interface-materials-for-optical-transceivers/ | published |
| V02-07 | 07-optical-transceiver-module-exterior.jpg | real-photo | TIM | optical transceiver | /applications/ | published |
| V02-08 | 08-power-device-insulation-pad.jpg | real-photo | insulation pad | power electronics | /thermal-insulator/ | published |
| V02-09 | 09-battery-pack-liquid-cooling-plate-dispensing.jpg | real-photo | thermal gel | battery pack | /battery-pack/ | published |
| V03 | thermal-pad-compression-gap-tolerance-diagram.webp | engineering-diagram | thermal pad | power electronics | /thermal-pad/ | published |
| V04 | thermal-gel-dispensing-variable-gap-assembly.webp | engineering-diagram | thermal gel | PCB, power electronics | /thermal-gel/ | published |
| V05 | thermal-grease-thin-bond-line-interface.webp | engineering-diagram | thermal grease | power electronics | /thermal-grease/ | published |
| V06 | thermally-conductive-structural-adhesive-joint.webp | engineering-diagram | structural adhesive | power electronics | /structural-adhesive/ | published |
| V07 | thermal-management-application-heat-path-matrix.webp | application-diagram | multiple TIMs | eight application families | /applications/ | published |
| V08 | thermal-material-test-method-pressure-thickness.webp | engineering-diagram | TIM | testing | /testing/ | published |
| V09-PORTRAIT | ouyang-xiaohui-thermal-management-shenzhen.webp | portrait | TIM | professional profile | /about/ | published |
| V09-PRODUCTION | thermal-material-real-production-support.webp | production-reference | TIM | production support | /about/ | published |
| V10 | obc-multiple-thermal-interface-material-locations.webp | engineering-diagram | multiple TIMs | OBC | /obc/why-does-an-obc-use-multiple-thermal-interface-materials/ | published |
| V11 | battery-pack-thermal-gel-liquid-cooling-plate.webp | engineering-diagram | thermal gel | battery pack | /battery-pack/thermal-gel-for-battery-pack-liquid-cooling-plates/ | published |
| V12 | optical-transceiver-thermal-interface-material-location.webp | engineering-diagram | TIM | optical transceiver | /optical-module/thermal-interface-materials-for-optical-transceivers/ | published |
