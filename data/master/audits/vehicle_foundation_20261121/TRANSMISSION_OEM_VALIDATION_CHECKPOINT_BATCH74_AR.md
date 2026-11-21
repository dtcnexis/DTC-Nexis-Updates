# DTC NEXIS — نقطة الاستئناف المؤكدة حتى الدفعة 74

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=OEM_DOCUMENT_RESEARCH_IN_PROGRESS / NO_APPROVED_GEARBOX_IMPORTS / NO_RELEASE
base_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH71_AR.md

## تقارير جديدة
- batch72: TRANSMISSION_OEM_SCOPE_RECHECK_BATCH72_AR.md, commit 4d52a3e14328f4f00c0dca9753659ad1eb76e8a9, verified Git blob 59ac54c9bc23c8914c0e2cc8ad6d24d1f2c421a3.
- batch73: TRANSMISSION_OEM_SCOPE_RECHECK_BATCH73_AR.md, commit 751f0bb0a617c1e72b057b2c0459f209e4610e5c, verified Git blob e98c7d7daefec4ee763dcd1038c6d508cb93a5e5.
- batch74: TRANSMISSION_OEM_SCOPE_RECHECK_BATCH74_AR.md, commit 321283061e51f322f522fea88f19d653035288f1, verified Git blob 034bf16a96211292e6ec545bd3ae1d4408688cb5.

## ملخص التغطية
original_missing_transmission_source_records=1469
original_hint_review_cases=32
source_review_completed_previous_batches=true
distinct_existing_hint_rows_reexamined_batch72_to74=13
new_OEM_gearbox_family_identifiers=2
new_approved_exact_vehicle_gearbox_assignments=0
new_ECU_DTC_links=0
new_raw_vehicle_imports=0
raw_source_edits=0
remaining_hint_cases_needing_part_and_application_verification=32

## الأدلة ذات الأولوية
1. Ford Transit Connect 2019–2020 owner manual gives 8F35 for some 8-speed configurations; raw begins 2018; 2018 model code may differ and cannot be overwritten.
2. Cadillac XT4 MY2024 2.0L /235hp /350Nm official Hydra-Matic 9T50; raw 238hp and 2023–2025 covers broader scope.
3. Alpine A110 raw model «2024» 345HP/420Nm numerically resembles **A110 R Ultime** announced 2024, with an OEM **DW6** revised gearbox; generic 2024 A110/GT/S Getrag 7-speed must not be assigned to 345hp automatically.
4. Toyota Corolla Sedan raw 1.8L/140hp and 2.0L/196hp declared 2022 hybrid. UK OEM MY2023 Corolla hatchback/estate new hybrid generation reports 138bhp (~140PS) and 193bhp (~196PS), along with 9.2s and 7.5s; exact MY2022 sedan and market identity unverified.
5. Lexus ES 250 AWD 2023 203hp/8-speed and ES 300h 2023 215hp/CVT confirmed by Lexus Canada; gearbox assembly IDs and VIN applicability pending.
6. Citroën C4 PureTech100 6MT, PureTech130 S&S EAT8 and BlueHDi130 S&S EAT8 OEM family confirmed, but full 2022–2024 market application and non-S&S raw variant ambiguous.
7. Subaru Ascent 2022 Subaru official brochure PDF search shows 2.4L/260hp/High Torque Lineartronic CVT; web PDF screenshot failed, so this is an **unverified extracted lead** here rather than a visually validated OEM document. Retry authorized source HTML or PDF screenshot before grading.

## المرحلة التالية
next_batch=75
next_workstream=IDENTIFY_OEM_GEARBOX_ASSEMBLY_CODE_VIN_MARKET_AND_MODEL_YEAR_FOR_FORD_CADILLAC_ALPINE_LEXUS_CITROEN; VERIFY_SUBARU_2022_BROCHURE_VISUALLY; RESOLVE_TOYOTA_SEDAN_HATCHBACK_POWER_GENERATION_CONFLICT
pending_cases=32
technical_OEM_completion=false
merged_to_main=false
stable_updated=false

## حماية
حفظنا تقارير فرع المراجعة فقط. لم تتغير CSV الخام أو قوائم المراجعة القديمة، ولا main أو stable أو الموقع أو البرنامج أو الصور أو ملفات DTC.
