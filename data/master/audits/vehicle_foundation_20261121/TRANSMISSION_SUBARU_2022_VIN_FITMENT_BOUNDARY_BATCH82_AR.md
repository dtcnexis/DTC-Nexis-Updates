# DTC NEXIS — الدفعة 82: Subaru Ascent 2022 — فحص حدود إثبات رقم تجميع TR690

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / VIN_EPC_PENDING / NO_FINAL_PART_FITMENT
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_LEXUS_MY2023_2024_FAMILY_REVIEW_BATCH81_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv
source_record=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_015.csv:43

## البحث المقارن
1. Official **Subaru 2022 Ascent brochure** states 2.4L turbo 260hp and High Torque Lineartronic CVT. It confirms model-year/engine/transmission family but gives no gearbox assembly part number. Source:
https://www.subaru.com/content/dam/subaru/downloads/pdf/brochures/2022/ascent/2022_Ascent_Brochure_Final.pdf
2. Manufacturer campaign **WRK-21R**, published at NHTSA, identifies 31000AK130 with CVTF cooler and 31000AK140 without cooler, but the campaign explicitly covers 2019–2020MY Ascent and not 2022MY. Source:
https://static.nhtsa.gov/odi/tsbs/2022/MC-10216971-0001.pdf
3. Subaru original dealer recall bulletin from 2023 confirms the same **31000AK130 / 31000AK140** replacement family, instructing that the most up-to-date replacement part must be ordered by specific VIN; it remains a **recall-year/affected vehicle** remedy, not a blanket 2022 VIN match. Source:
https://static.nhtsa.gov/odi/tsbs/2023/MC-10231303-0001.pdf
4. Third-party Subaru OEM part reseller previously retrieved 2022 Base catalog links **31000AK140 / TR690G61DA** and 2022 Limited 8-passenger **31000AK130 / TR690S61DA**; both are trim-level catalog hints rather than current OEM VIN-filtered EPC confirmation. Source references:
https://www.subarupartsdeal.com/parts-list/2022-subaru-ascent--2_4l_h4-base_eyesight/automatic_transmission/automatic_transmission_assembly.html
https://www.subarupartsdeal.com/parts-list/2022-subaru-ascent--2_4l_h4-limited_8_passenger_eyesight/automatic_transmission/automatic_transmission_assembly.html
5. No primary Subaru 2022 VIN-specific assembly number and supersession table were established in this research batch. A current owner's window-sticker is not interchangeable with EPC part selection.

## Applied research gates
- TR690 transmission *model family* for Ascent MY2022: supported by primary Subaru technical documentation.
- CVT assemblies 31000AK130 and 31000AK140: authentic Subaru recall replacement identifiers, OEM source-scope 2019–2020.
- MY2022 trim-level 31000AK130 vs 31000AK140: third-party catalog association (review only), not definitive VIN assignment.
- Replacement revision and supersession after MY2022: uncertain, cannot rely on mirrors alone.
- Do not infer a recall or fault on an individual 2022 vehicle from unrelated recall MYs; do not assign service software or DTC links.

## Outcome
existing_hint_cases_reexamined=1
new_VIN_verified_OEM_assembly_codes_for_2022=0
new_approved_transmission_assignments=0
new_ECU_DTC_links=0
raw_records_changed=0
remaining_32_hint_cases_final_approval_pending=32
next_batch=83
next_workstream=LEXUS_MY2023_2024_DIRECT_OEM_CODE_OR_EPC_AND_OTHER_UNRESOLVED_HINT_APPLICATION_MATCHES

## Preservation
No changes to original CSV, queues, master data, main, stable, Windows, website, media or approved DTC database.
