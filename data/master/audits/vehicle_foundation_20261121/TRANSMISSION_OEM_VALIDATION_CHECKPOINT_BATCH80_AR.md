# DTC NEXIS — نقطة حفظ ناقل الحركة حتى الدفعة 80

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=OEM_FAMILY_AND_ASSEMBLY_EVIDENCE_REVIEW / NO_MASTER_DATA_APPROVAL / NOT_PUBLISHED
prior_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH77_AR.md

## عمليات الحفظ المتحقق منها
- batch78: TRANSMISSION_OEM_ASSEMBLY_VALIDATION_BATCH78_AR.md, commit 0c7b95cabb2f989d19744083a01a16167c955ff7, verified blob c4d8018410c344f6113d62132c1c83733f8a3a84.
- batch79: TRANSMISSION_OEM_ASSEMBLY_FITMENT_BATCH79_AR.md, commit 41d389d6aeb283e25c845496e853889e83c68fb9, verified after create.
- batch80: TRANSMISSION_LEXUS_CODE_VALIDATION_BATCH80_AR.md, commit 378ce5785e85fa7327aa0a3f3167ba906c471458, verified blob 8097cc0407c0a6449e377640dabc7731063d5163.

## نتائج جديدة مدققة
1. Genuine Subaru campaign WRK-21R, PDF visually checked p.1 and p.3, part number **31000AK130** for Ascent with CVTF cooler, **31000AK140** for Ascent without CVTF cooler. **Crucial scope: 2019–2020 MY Ascent recall, not 2022 MY recall.** These are legitimate OEM part numbers but a 2022 car requires proper application validation.
2. Genuine Subaru parts-catalog reseller lists 2022 Ascent Base as **TR690G61DA / 31000AK140** and Limited 8-passenger as **TR690S61DA / 31000AK130**. This is a strong 2022 trim-model lead, not manufacturer VIN-authorized final part assignment.
3. A secondary Subaru campaign bulletin mirror updated Sept 2025 shows **31000AK130R1** as a later replacement lead for cooler-equipped Ascent, with 31000AK140 without cooler. First-party Sept 2025 bulletin / current VIN EPC approval not verified; do not apply R1 universally.
4. LEXUS official Canada MY2025 technical PDF visually checked physical index 2: **ES250 AWD transmission code UB80F**, **ES350 code UA80E**, **ES300h hybrid e-CVT code P710**. Only ES250 and ES300h are raw queue rows; ES350 serves as comparison. Raw Lexus queue spans 2023–2025 and still requires same-year verification for 2023–2024 and exact transmission assembly part/VIN.
5. Previously, Subaru TCM bulletin identified two software branches depending on air CVTF cooler; these 30919... programming numbers are **not gearbox assembly numbers**. Not imported into DTC or ECU tables.

## Coverage versus approval
total_missing_transmission_source_rows=1469
source_rows_reviewed=1469
prior_hint_cases_total=32
distinct_hint_rows_reexamined_this_session=3
new_OEM_assembly_number_evidence_leads_subaru=2
new_OEM_model_code_evidence_leads_lexus=2
new_fully_approved_gearbox_assignments=0
new_ECU_DTC_links=0
source_records_changed=0
pending_hint_cases_exact_application_approval=32
main_merged=false
stable_updated=false

## Deterministic resume
last_completed_batch=80
last_file=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_LEXUS_CODE_VALIDATION_BATCH80_AR.md
next_batch=81
next_workstream=LEXUS_2023_2024_OEM_TECH_CODES_AND_SUBARU_2022_EPC_VIN_GEARBOX_PART_SELECTION_THEN_REMAINING_32_HINT_FITMENT
pending_issues=VIN_REQUIRED;MODEL_YEAR_SCOPE;COOLER_CONFIGURATION;GEARBOX_VS_TCM_IDENTIFIER;PART_SUPERSESSION
technical_completion=false

## Non-destructive constraints
No changes to gor3a original CSV or review queues, no main/stable merges or releases, no website/Windows RC3.8.0/RC3.8.2 edits, and no media or approved DTC library modifications.
