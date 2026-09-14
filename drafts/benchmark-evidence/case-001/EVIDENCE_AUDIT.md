# Case 001 evidence audit and publication plan

Status: final local production candidate prepared. Do not commit, push or deploy until the remaining validation gate is approved and passed.

## Evidence audit

All five supplied images were visually inspected against `README_FOR_CODEX.txt` and `CODEX_PROMPT.txt`.

- The formal ASTM D5470 table supports the five FT-BN035 thickness/resistance pairs and the single 0.25 mm SP2000 reference value.
- The report states a pressure of 50 psi. Individual displayed result rows are around 49.8–50 psi.
- The ASTM D149 table supports 4.93 kV at 0.20 mm, `>6 kV` at 0.25/0.31/0.38/0.47 mm and 5.37 kV for the 0.25 mm reference.
- The ASTM D257 table supports approximately 1.62 × 10^14 ohm at 500 V.
- The ASTM D792 table supports 1.833, 1.875 and 1.900 g/cm3 and a displayed rounded average of 1.87 g/cm3.
- A raw D5470 screen supports a separate run around 0.22 mm, 2.03 W/mK, 0.168 degC-in2/W and 49.9 psi. Its equivalence to the formal series is not established, so it is excluded from the formal dataset.

## Privacy and redaction

The report screenshots contain internal laboratory/company fields, an operator name, equipment or software identifiers, dates, instrument manufacturer references and an internal conclusion/approval restriction. Original images were removed from the repository workspace and remain only in controlled, repository-external storage.

Public-ready assets use newly drawn tables/charts without those identifiers. The optional raw-screen derivative is cropped, removes the operating-system/taskbar area and covers the software/device-identifying header. It is labeled raw-run evidence and is not used in the formal comparison.

Do not publish the original five images. The user's phase-two instructions authorize publication of the FT-BN035 name, the approved internal comparative values, and the wording `SP2000 reference sample`, subject to the exact limitations and non-affiliation statement used on the production candidate page.

## Proposed repository structure

```text
data/benchmark-evidence/case-001.json
assets/images/benchmark-evidence/case-001/
  case-001-thermal-resistance-vs-thickness.webp
  case-001-0-25mm-thermal-resistance-comparison.webp
  case-001-electrical-properties-summary.webp
  case-001-test-method-evidence-map.webp
  case-001-anonymized-raw-d5470-run.webp
benchmark-evidence/
  index.md
  ft-bn035-vs-sp2000-reference-sample/index.md
docs/benchmark-evidence/CASE_001_PROVENANCE.md
```

Source originals remain outside the public repository in controlled storage.

## CREATE versus UPDATE

Recommendation: **CREATE one evidence-node URL**, then add restrained links from existing guides after publication approval.

The existing `/sp2000-alternative-evaluation/` and `/comparison/sp2000-thermal-pad-alternative-what-parameters-should-engineers-compare/` pages answer selection and qualification questions. Neither publishes this original measured dataset. Updating either page with the full evidence package would mix a general commercial/selection intent with a source-led test record. One dedicated evidence URL is therefore distinct and avoids repeating the dataset across multiple pages.

Final candidate title: `FT-BN035 Thermal Resistance Benchmark with an SP2000 Reference Sample`

Proposed slug: `/benchmark-evidence/ft-bn035-vs-sp2000-reference-sample/`

Primary keyword/entity phrase: `FT-BN035 vs SP2000 thermal resistance benchmark`

Search demand is unknown. This is an original-evidence/GEO citation asset, not a volume-keyword page.

## Internal-link plan

Case 001 should link to:

- `/sp2000-alternative-evaluation/`
- `/comparison/sp2000-thermal-pad-alternative-what-parameters-should-engineers-compare/`
- `/comparison/thermal-conductivity-vs-thermal-resistance/`
- `/engineering-resources/thermal-pad-compression-calculator/`
- `/engineering-resources/tim-tds-comparison-tool/`
- `/engineering-resources/second-source-qualification-generator/`
- `/testing/why-can-the-same-thermal-material-produce-different-test-results/`
- `/benchmark-your-current-tim/`, `/request-sample/` and `/discuss-your-application/`

After approval, add one contextual link back to Case 001 from the two SP2000 pages, the thermal-conductivity-versus-resistance guide, and the test-results-differ guide. Consider links from supplier pages only where a measured-evidence example genuinely supports the paragraph. Do not force this specific thin-pad dataset into OBC, optical-module or power-electronics pages without matching application context.

## Approved publication boundaries

1. FT-BN035 may be identified with the approved internal comparative test values.
2. SP2000 is described only as the specific `SP2000 reference sample` that was tested; the page makes no broader product-family claim.
3. The formal series is described as tested at approximately 50 psi.
4. The evidence is explicitly described as internal comparative testing, not independent third-party certification.
5. Only one anonymized raw ASTM D5470 run image is included, and that separate run is not merged into the formal series.
6. The page states that SP2000 is used solely for comparative identification and that OUYANG THERMAL is not affiliated with or endorsed by the referenced brand.

## Local validation

- Source metadata and internal-path check: PASS, 105 source pages checked.
- Image-library audit: PASS, 40 files and 40 records, zero duplicate binary groups; two pre-existing unused-source warnings only.
- Five Case 001 derivatives: 1440 × 900 WebP, 40.8–117.5 KB each.
- A production candidate now exists at `/benchmark-evidence/ft-bn035-vs-sp2000-reference-sample/`; the superseded unpublished page draft was removed.
- Google verification, robots.txt, inquiry files, canonical logic and production URLs were not modified.
- Full Jekyll build: NOT RUN because this workstation has no Ruby, Bundler, Docker or WSL runtime. A build cannot be triggered through GitHub without pushing, which the user expressly prohibited. This remains a publication gate.

## Current recommendation

**READY FOR VALIDATION, NOT READY FOR PUBLICATION.** Evidence, disclosure wording and derived assets are prepared. A complete Jekyll build and rendered-page validation remain mandatory. The repository currently has no validation-only GitHub Actions workflow, so no remote build can be run without first adding an isolated validation workflow and pushing a dedicated non-production branch with user approval.
