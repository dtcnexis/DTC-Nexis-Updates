# DTC NEXIS — الدفعة 76: Subaru Ascent 2022 — إثبات رمز TR690 من نشرة خدمة OEM

date=2026-11-21
status=REVIEW_ONLY / OEM_TRANSMISSION_MODEL_FAMILY_VERIFIED / EXACT_ASSEMBLY_AND_ECU_PENDING / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_SCOPE_RECHECK_BATCH75_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## السجل الخام
- source_file=engines_part_015.csv
- source_line=43
- make=Subaru
- model=Ascent (2022)
- engine_label=2.4L CVT AWD (260 HP)
- source_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36
- structured_transmission=EMPTY (do not fill without approval workflow)

## إثبات فني من Subaru
1. Subaru USA, official 2022 Ascent brochure, printed page 19 / PDF index 10: 2.4L DIT turbo Boxer 260hp, **High Torque Lineartronic CVT**, Symmetrical AWD, and an eight-step *manual simulation mode*, not conventional eight-speed planetary automatic.
   - OEM_BROCHURE_URL=https://www.subaru.com/content/dam/subaru/downloads/pdf/brochures/2022/ascent/2022_Ascent_Brochure_Final.pdf
   - VERIFIED=PDF_SCREENSHOT_PAGE_10.
2. Subaru of America service bulletin **16-132-20R**, revised January 10, 2022, «Diagnostic Information for Alleged Chain Slip Condition on TR580 / TR690 Transmissions»:
   - OEM_TSB_URL=https://static.nhtsa.gov/odi/tsbs/2022/MC-10207174-0001.pdf
   - TSB page 1 identifies 2019–2022MY Ascent in applicability list.
   - TSB page 2 (PDF index 1) contains explicit **«Ascent- TR690: 19MY -»** in the Model/TCM Replacement table.
   - VERIFIED=PDF_SCREENSHOT_PAGE_1.
3. The bulletin's diagnostic instructions refer to SSM, TCM, CVT chain slip; these are maintenance bulletins, NOT evidence that any specific vehicle has a failure and NOT permission to generate DTC mappings.

## نتيجة تحقق نموذج ناقل الحركة
OEM_transmission_model_family=TR690
OEM_fully_verified_same_model_year_powertrain_family=true
VIN_specific_transmission_assembly_part_number=UNVERIFIED
TCM_variant_calibration_identification=UNVERIFIED
exact_engine_code_variant=UNVERIFIED
status=TR690_FAMILY_OEM_CONFIRMED_PENDING_GEARBOX_ASSEMBLY_VIN_AND_TCM

## نطاق الحفظ
existing_cases_reexamined=1
new_OEM_transmission_model_family_codes_identified=1
new_approved_exact_vehicle_gearbox_imports=0
new_approved_ECU_DTC_links=0
raw_source_rows_modified=0
prior_queue_modified=0
remaining_32_hint_cases_not_final_approved=32
next_batch=77
next_workstream=SUBARU_2022_ASCENT_TR690_ASSEMBLY_ID_AND_TCM_OR_OTHER_HIGH_PRIORITY_GEARBOX_VARIANTS

## الحماية
This report does not authorize edits to raw CSV, review queue, main, stable, website, RC3.8.0/RC3.8.2, media or released DTC library.
