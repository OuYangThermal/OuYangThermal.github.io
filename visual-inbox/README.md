# OUYANG THERMAL Visual Inbox

Put completed source images in this folder. Then tell Codex only the Image ID, for example: `V01`.

Do not rename, optimize, convert, or publish an image before review. Original PNG, JPG, WebP, AVIF, SVG, or editable source files are acceptable here.

## Image ID map

| ID | Planned subject | Preferred final filename |
|---|---|---|
| V01 | Homepage hero application map | `thermal-interface-material-applications-obc-pcs-optical-ai-server` |
| V02 | Thermal material family | `thermal-material-family-pad-gel-grease-potting-adhesive` |
| V03 | Thermal pad compression | `thermal-pad-compression-gap-tolerance-diagram` |
| V04 | Thermal gel dispensing and assembly | `thermal-gel-dispensing-variable-gap-assembly` |
| V05 | Thermal grease thin bond line | `thermal-grease-thin-bond-line-interface` |
| V06 | Structural adhesive heat and load path | `thermally-conductive-structural-adhesive-joint` |
| V07 | Application heat-path matrix | `thermal-management-application-heat-path-matrix` |
| V08 | Thermal test conditions | `thermal-material-test-method-pressure-thickness` |
| V09 | Ouyang Xiaohui real professional photo | `ouyang-xiaohui-thermal-management-shenzhen` |
| V10 | OBC multiple TIM locations | `obc-multiple-thermal-interface-material-locations` |
| V11 | Battery pack liquid cooling plate | `battery-pack-thermal-gel-liquid-cooling-plate` |
| V12 | Optical transceiver TIM location | `optical-transceiver-thermal-interface-material-location` |

## Simple naming

The easiest upload name is just the ID plus the original extension:

- `V01.png`
- `V03.jpg`
- `V09.webp`

If there are several versions, use:

- `V01-a.png`
- `V01-b.png`
- `V01-final.png`

Codex will review the selected image, verify technical accuracy and rights/provenance, prepare responsive WebP/AVIF versions, add meaningful ALT text, and place it only after receiving an explicit instruction to do so.

## Required processing workflow

`visual-inbox` is a temporary intake directory, not a published asset library. Before using an image, read `data/image-library.json`, check content and provenance, assign a controlled authenticity value, choose a descriptive filename, compare SHA-256 hashes, prepare the production format, move the file into the formal asset directory, update both the JSON manifest and `docs/IMAGE_LIBRARY.md`, add the page reference, run `npm run audit:images`, test, and deploy.

After processing, do not keep the same binary in both this inbox and a formal directory. Move unique editable masters to `assets/images/source/` when they need to be retained.
