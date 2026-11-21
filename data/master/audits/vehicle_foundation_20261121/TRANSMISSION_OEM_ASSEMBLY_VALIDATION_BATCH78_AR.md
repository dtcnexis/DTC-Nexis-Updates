# DTC NEXIS — الدفعة 78: أرقام تجميع Subaru TR690 مع ضبط نطاق سنة الموديل

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_ASSEMBLY_NUMBER_EVIDENCE / VIN_FITMENT_PENDING / NO_RELEASE
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH77_AR.md
existing_source_row=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_015.csv:43
raw_label=Subaru Ascent (2022), 2.4L CVT AWD (260 HP)
raw_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36

## دليل OEM موثق بالصفحة الأصلية
- Subaru of America product campaign WRK-21R, revised 2022-07-18, hosted by NHTSA:
  https://static.nhtsa.gov/odi/tsbs/2022/MC-10216971-0001.pdf
- PDF physical page index=2, printed page 3/25. Verified with a visual PDF screenshot.
- Ascent **with CVTF cooler (air)**: CVT assembly **31000AK130**.
- Ascent **without CVTF cooler**: CVT assembly **31000AK140**.
- Manufacturer explicitly requires replacement parts to be selected based on each vehicle's VIN and stock/revision rules.
- **CRITICAL SCOPE**: PDF physical page index=0 (visually verified) states the WRK-21R recall applies to **2019–2020MY Ascent**, and certain 2020MY Legacy/Outback. It does **NOT** directly establish recall eligibility for **2022MY Ascent**, and must not be interpreted as a 2022 recall notice.

## Evidence separation
1. OEM original campaign parts (2019–2020MY affected Ascent) establish authentic assembly numbers and CVTF-cooler distinction.
2. Pre-existing Subaru official 2022 Ascent technical source and OEM TSB 16-132-20R identify the **TR690** transmission family for Ascent model-year 2022 but not one VIN-matched assembly number.
3. Dealer catalogue can provide a supporting 2022 model/trim association; it remains below OEM VIN-specific EPC confirmation and is not authority to apply a recall part number globally.
4. OEM table: with-cooler 31000AK130; without-cooler 31000AK140. TCM software numbers 30919AJ53*/30919AJ54* from prior batch are not gearbox assembly numbers.

## New review records
new_distinct_OEM_assembly_part_number_leads=2
part_lead_1=31000AK130;condition=CVTF_COOLER_PRESENT;scope=WRK-21R_2019_2020MY;status=SOURCE_CONFIRMED_APPLICABILITY_TO_2022_PENDING
part_lead_2=31000AK140;condition=CVTF_COOLER_ABSENT;scope=WRK-21R_2019_2020MY;status=SOURCE_CONFIRMED_APPLICABILITY_TO_2022_PENDING
new_approved_2022_gearbox_part_assignments=0
new_approved_DTC_or_ECU_links=0
raw_records_modified=0
other_32_hint_cases_unapproved=32
next_batch=79
next_workstream=CHECK_2022_ASCENT_DEALER_PARTS_CATALOG_BY_TRIM_AND_RECENT_SUBARU_REPLACEMENT_PART_REVISIONS

## Protect original
No changes to source CSV, review queues, main/stable, application, Windows releases, pictures or published DTC catalogue.
