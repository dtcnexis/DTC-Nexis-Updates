# DTC NEXIS — نقطة استئناف التحقق التقني حتى الدفعة 82

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / NO_VIN_MATCHED_GEARBOX_APPROVAL / NO_RELEASE
base_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH80_AR.md

## تقارير هذه الجلسة
- batch81: data/master/audits/vehicle_foundation_20261121/TRANSMISSION_LEXUS_MY2023_2024_FAMILY_REVIEW_BATCH81_AR.md; verified commit 54b0cd758930982c115bff3952409f5030eed0af; blob 82dbefa56846c1562422cb93b9b53ba640287db4.
- batch82: data/master/audits/vehicle_foundation_20261121/TRANSMISSION_SUBARU_2022_VIN_FITMENT_BOUNDARY_BATCH82_AR.md; verified commit c2b4bce9e6d057f7b5612af9a8a7a6c2d97396be; blob fbf96f9c209ecc0c6a07db0a244be607764e44ef.

## Lexus ES
- Source queue rows engines_part_008.csv:1383 and :1385 are Lexus ES 250 AWD 203hp 8AT and ES300h 215hp e-CVT, year scope 2023–2025.
- Lexus Canada official MY2023 and MY2024 press publications support exact model-year **transmission family/type** for these rows. MY2025 Lexus official chart names **UB80F** for ES250 AWD and **P710** for ES300h.
- A 2022 US Lexus manufacturer specification hosted at regulations.gov gives **UB80F** and engine A25A-FKS for ES250 AWD in searchable extracted text. PDF screenshot returned HTTP 403 and must NOT be called visually verified. Direct MY2023–2024 Lexus chart, gearbox assemblies and VIN fitment still needed.

## Subaru Ascent
- Original 2022 brochure confirms 2.4L/260hp High Torque Lineartronic CVT and AWD; OEM service bulletin identifies TR690 transmission family.
- Subaru official campaign WRK-21R parts 31000AK130 (cooler equipped) / 31000AK140 (without cooler) are valid recall replacement part numbers for **2019–2020MY Ascent**. The campaign does NOT establish that a 2022MY Ascent is recalled.
- Third-party 2022 Ascent model/trim catalog associates 31000AK130 / TR690S61DA with Limited 8-passenger, and 31000AK140 / TR690G61DA with Base. VIN-specific dealer EPC selection and supersessions remain unverified; no blanket part recommendation.
- Some recent bulletin supersession leads are from secondary mirrors only, not sufficient for automatic part import.

## Cross-batch reconciliation
original_missing_transmission_rows=1469
previous_source_reviewed=1469
original_label_hint_cases=32
new_distinct_existing_rows_reexamined_in_batch81_to82=3
new_approved_gearbox_vehicle_assignments=0
new_approved_ECU_DTC_mappings=0
new_source_vehicle_rows_imported=0
duplicates_deleted=0
raw_files_modified=0
hint_cases_still_exact_application_pending=32

## Resume exactly
last_completed_batch=82
last_file=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_SUBARU_2022_VIN_FITMENT_BOUNDARY_BATCH82_AR.md
next_batch=83
next_workstream=OEM_DIRECT_MY2023_2024_LEXUS_CODE_PROOF_AND_SOURCE_EVIDENCE_FOR_OTHER_HINT_CASES_AND_LONGER_TERM_1166_CONFLICT_QUEUE
needs=VIN,OEM_EPC,MARKET,YEAR,ENGINE,TRANSMISSION_ASSEMBLY,ECU_CALIBRATION
technical_completion=false
main_merged=false
stable_updated=false
originals_preserved=true

## Restrictions
No main/stable changes, no raw CSV or queue replacement, no website / Windows RC3.8.0/RC3.8.2 editing, no media collection, no DTC releases.
