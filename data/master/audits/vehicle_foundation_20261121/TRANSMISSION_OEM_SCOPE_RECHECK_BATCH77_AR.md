# DTC NEXIS — الدفعة 77: Subaru Ascent 2022 — تفريق TR690 عن نسخ برمجيات TCM

date=2026-11-21
status=REVIEW_ONLY / OEM_TCM_VARIANT_LEADS / NO_APPROVED_VIN_PART_FITMENT / NO_RELEASE
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_SCOPE_RECHECK_BATCH76_AR.md
source_row=engines_part_015.csv:43
raw_engine_label=2.4L CVT AWD (260 HP)
source_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36

## مستند المصنع
- Subaru of America SERVICE BULLETIN 16-132-20R revised 2022-11-17, filed in NHTSA.
- OEM_TSB_URL: https://static.nhtsa.gov/odi/tsbs/2022/MC-10226904-0001.pdf
- PDF physical index=3 (printed page 4 of 10), visually verified using PDF screenshot.
- TSB applicability: 2019–2023 Subaru Ascent; transmission model TR690 confirmed using OEM bulletin.
- Important: TSB table lists 2022 Ascent 2.4L DIT CVT without CVTF cooler (air cool) and with CVTF cooler (air cool) as distinct TCM programming configurations.
- 2022 without cooler: programming file 30919AJ53B.pk2, old ECU/TCM part number 30919AJ53A, CID N2FEE600.
- 2022 with cooler: programming file 30919AJ54B.pk2, old ECU/TCM part number 30919AJ54A, CID N2FEE600.
- These 30919... values are software / control-unit identifiers as labelled in the TSB, NOT necessarily gearbox assembly part numbers. The files ending .pk2 are programming files, not vehicle fitment evidence.
- The bulletin documents conditional diagnostics and software updates, and does not imply a fault exists in any specific car.

## Data-quality and applicability findings
- TR690 family is supported by original Subaru 2022 brochure and TSB. Full fitment must distinguish cooler hardware option, calibration version, VIN, and market.
- Raw row engines_part_015.csv:43 lacks cooler configuration, VIN, calibration, and full assembly part number; cannot assign one of the two TCM references to any specific car.
- Preserve both variants as review evidence, never fill a transmission field from the software filename, and never generate ECU/DTC links without the applicable service manual.

## Batch results
existing_hint_cases_reexamined=1
new_OEM_TCM_configuration_branches_identified=2
new_approved_gearbox_assembly_numbers=0
new_approved_ECU_DTC_link_records=0
raw_source_rows_modified=0
queue_rows_modified=0
remaining_hint_cases_not_final_approved=32
next_batch=78
next_workstream=VERIFY_VIN_FITMENT_FOR_TR690_AND_8F35_9T50_DW6_AND_OEM_TRANSMISSION_PART_CODES

## Protection
Review report only; no change to master data, main/stable, website, RC3.8.0/RC3.8.2, assets or approved DTC records.
