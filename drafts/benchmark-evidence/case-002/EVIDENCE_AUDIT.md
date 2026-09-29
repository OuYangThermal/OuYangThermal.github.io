# Case 002 evidence audit and publication record

Status: published. Public URL: /benchmark-evidence/ft-bn050-thermal-resistance-vs-thickness/
Published 2026-09-14 (commit 13ebdb3 "Publish Case 002 thin insulating TIM evidence").

This audit record was compiled 2026-09-29 from `docs/benchmark-evidence/CASE_002_PROVENANCE.md`
and from direct verification of the published page and its derived assets. The original
source-evidence JPEGs remain only in controlled, repository-external storage and were not
re-opened for this record; their contents are represented here exactly as recorded in the
provenance document, which was written at the time the images were inspected.

## Evidence audit

A user-supplied material pack containing a public-data summary and three source-evidence
JPEGs was used to verify the displayed method, conditions and numerical tables. The
provenance document records the following verification results:

- ASTM D5470: five FT-BN050 nominal/compressed thickness pairs and measured
  thermal-resistance values at 50 psi, in °C·in²/W:
  0.21 mm → 0.179 / 0.27 mm → 0.195 / 0.32 mm → 0.209 / 0.40 mm → 0.249 / 0.52 mm → 0.292.
- ASTM D149: five displayed breakdown-voltage limits for a stated 200 × 200 mm test area:
  >5 kV at 0.21 mm; >6 kV at 0.27 / 0.32 / 0.40 / 0.52 mm.
- Environment: 25 ± 3 °C and 65 ± 10% RH.
- Sample identifier and color: FT-BN050, white.
- The report section heading immediately above the raw thermal-result images contains an
  inconsistent `FT-BN035` label. The public summary, main data table and individual
  raw-result captions identify the sample as FT-BN050. The inconsistent heading is treated
  as a source-document typographical error and is not reproduced publicly.

No conductivity value is inferred or stated for the series. Derived graphics preserve the
displayed numerical values and greater-than limits only; they do not infer device
temperature or unreported performance.

## Privacy and redaction

The source JPEGs contain company, department, operator, equipment/software identifiers,
report ownership language, dates and device photographs. Original images were excluded
from the repository and remain only in controlled, repository-external storage.

Public-ready assets use newly drawn tables/charts without those identifiers. No original
test-report screenshot is published for Case 002. This is an intentional anonymization
decision, consistent with the Case 001 policy.

Do not publish the original three images.

## Approved publication boundaries

1. FT-BN050 may be identified with the approved internal test values (thermal resistance
   versus thickness series plus ASTM D149 breakdown-voltage limits).
2. The series is described as tested at 50 psi per ASTM D5470.
3. The evidence is explicitly described as internal testing, not independent third-party
   certification.
4. Results apply only to the stated samples and test conditions.
5. No customer endorsement, field reliability, certification or production approval is
   claimed.
6. Application decisions still require assembly-specific thermal, mechanical, electrical
   and reliability validation.

## Current state verification (2026-09-29)

- Public URL returns HTTP 200 with the full data table (five thickness rows),
  the ASTM D149 table, and three derived charts.
- The URL is listed in the production sitemap.xml and in the Benchmark Evidence Library
  as "Case 002 — Thin insulating TIM".
- Seven published pages reference Case 002; all reference the real published URL.
  No fabricated or dangling Case 002 reference exists.
- `data/benchmark-evidence/case-002.json` status now reads `published` with
  `published_date` 2026-09-14, consistent with the production state.
