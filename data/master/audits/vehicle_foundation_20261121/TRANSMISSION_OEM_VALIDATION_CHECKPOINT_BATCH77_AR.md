# DTC NEXIS — نقطة استئناف التحقق من ناقل الحركة حتى الدفعة 77

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=RESEARCH_REVIEW_ONLY / NO_APPROVED_VEHICLE_GEARBOX_IMPORT / NO_RELEASE
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH74_AR.md

## التقارير الجديدة التي حُفظت وتحققنا من محتواها
- batch75 = TRANSMISSION_OEM_SCOPE_RECHECK_BATCH75_AR.md, commit 2408be5b7c3a43381254984129b560a4fee60f77.
- batch76 = TRANSMISSION_OEM_SCOPE_RECHECK_BATCH76_AR.md, commit b8199e46c245050117179b44c17acec8b86afba7.
- batch77 = TRANSMISSION_OEM_SCOPE_RECHECK_BATCH77_AR.md, commit e2e488f6dcdddbf33ee5bb8b9108340695649e82.

## نتائج OEM الجديدة
1. **Subaru Ascent 2022**, source engines_part_015.csv:43: 2022 official brochure physically verified, High Torque Lineartronic CVT, AWD, 2.4L 260hp; 2022 Subaru service bulletin 16-132-20R also physically verified, gives explicit **Ascent TR690** applicable from 2019MY. This raises confidence in **gearbox model family TR690**, not a specific assembled part or calibration.
2. Subaru TSB November 2022 revision separates **CVTF cooler-present vs absent**, and lists corresponding software/control-module references **30919AJ53B.pk2 / 30919AJ53A** versus **30919AJ54B.pk2 / 30919AJ54A**. They are **TCM programming and old controller part identifiers, not gearbox assembly part numbers**. Neither shall be attached to raw entry without VIN/cooling-system match.
3. **Ford Transit Connect** raw combined 2018–2023 row 8AT: manufacturer documentation of 2018 US 6F35 and 2019–2020 8F35 is evidence that raw year range cannot safely inherit one transmission ID without year/engine/VIN-specific segmentation.
4. **Toyota Corolla** raw 2022 Sedan Hybrid 140hp and 196hp with 9.2s/7.5s precisely resembles MY2023 Europe 1.8/2.0 hybrid power figures, but Toyota regional source lists Sedan Hybrid 140H 1.8, with 2.0 being available in other Corolla bodies. This is a provenance/body-generation warning, NOT a proven correction.

## Remaining validation
hint_cases_total=32
hint_cases_OEM_assembly_VIN_approval_pending=32
new_OEM_gearbox_family_name_leads_this_turn=1
new_TCM_software_configuration_branches_identified=2
new_approved_gearbox_vehicle_assignments=0
new_approved_ECU_DTC_links=0
raw_source_records_modified=0
main_merged=false
stable_released=false

## Next checkpoint
last_completed_batch=77
last_file=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_SCOPE_RECHECK_BATCH77_AR.md
next_batch=78
next_workstream=VERIFY_SUBARU_TR690_VIN_COOLER_CONFIG_AND_EXACT_ASSEMBLY_NUMBER_THEN_REMAINING_HINT_CASE_OEM_PART_FITMENT

## Protection
Never change original gor3a or review queue files, master data, main/stable, website, Windows RC3.8.0/RC3.8.2, media or DTC approvals without separate verified OEM + compatibility review.
