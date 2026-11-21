# DTC NEXIS — الدفعة 79: تحقق تقاطعي من فهرس قطع Ascent 2022 وتحديثات الاستبدال

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / DEALER_CATALOG_2022_FITMENT_LEAD / NO_VIN_APPROVAL
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_ASSEMBLY_VALIDATION_BATCH78_AR.md
source_row=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_015.csv:43

## 2022 Ascent — دليل كتالوج قطع بحسب الفئة
- 2022 Subaru Ascent Base with EyeSight, 2.4L H4: third-party Subaru OEM parts catalog lists **31000AK140**, description **Transmission Assembly / TR690G61DA**.
  https://www.subarupartsdeal.com/parts-list/2022-subaru-ascent--2_4l_h4-base_eyesight/automatic_transmission/automatic_transmission_assembly.html
- 2022 Subaru Ascent Limited 8-passenger EyeSight, 2.4L H4: catalog indicates **31000AK130**, description **TR690S61DA**.
  https://www.subarupartsdeal.com/parts-list/2022-subaru-ascent--2_4l_h4-limited_8_passenger_eyesight/automatic_transmission/automatic_transmission_assembly.html
- Genuine Subaru dealership product listing also identifies **31000AK130 / TR690S61DA** and **31000AK140 / TR690G61DA**, though some catalog vehicle-fitment grids were unavailable at reading time.
  https://parts.ertlesubaru.com/oem-parts/subaru-trans-axle-31000ak130
  https://parts.subaruonlineparts.com/oem-parts/subaru-trans-axle-31000ak140

## 2025 replacement notice — supersession caution
- An archive of Subaru service campaign WRK-21_22R dated September 4, 2025 reports updated **with-CVTF-cooler replacement part 31000AK130R1**, compared with **31000AK140 without cooler**. This was found in the industry bulletin mirror; independent first-party 2025 PDF not yet verified. Treat as supersession lead and not as a universal replacing-part recommendation.
  https://oemdtc.com/tsb/11023504/
- For direct manufacturer-confirmed 2022-era replacement part numbers, use the NHTSA-hosted Subaru WRK-21R original document and its visual table:
  https://static.nhtsa.gov/odi/tsbs/2022/MC-10216971-0001.pdf
- This 2019–2020MY campaign document cannot establish 2022MY recall applicability. 2022 catalog references provide model/trim support, but require authoritative VIN-specific current EPC check before a definitive part assignment.

## Explicit evidence grading
- TR690 family for 2022 Ascent: OEM technical evidence available.
- 31000AK130 & 31000AK140: genuine manufacturer campaign assembly numbers confirmed (recall MY 2019–2020).
- 31000AK140 / TR690G61DA: 2022 Base model/trim association from parts catalog, NOT VIN-certified.
- 31000AK130 / TR690S61DA: 2022 Limited model/trim association from parts catalog, NOT VIN-certified.
- 31000AK130R1: later replacement revision secondary-source lead only; pending authoritative service campaign or Subaru EPC check.
- Cooling equipment: Base versus Limited trim can suggest a difference, but should NOT substitute for checking actual hardware and VIN.

## Results
existing_vehicle_source_rows_reexamined=1
new_2022_trim_specific_part_association_leads=2
new_secondary_supersession_leads=1
new_approved_exact_VIN_vehicle_transmission_assignments=0
new_ECU_DTC_links=0
new_library_vehicle_imports=0
raw_records_modified=0
hint_cases_still_pending_final_approval=32
next_batch=80
next_workstream=RECONCILE_CURRENT_SUBARU_EPC_VIN_SUPERSESSION_AND_VALIDATE_REMAINING_31_HINT_ROWS

## Protection
Review report only. Do not change source files, established reviews, main, stable, DTC catalog, website, Windows RC channels, or any existing media.
