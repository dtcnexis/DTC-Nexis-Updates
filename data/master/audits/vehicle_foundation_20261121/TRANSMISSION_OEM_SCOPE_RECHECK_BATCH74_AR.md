# DTC NEXIS — الدفعة 74: Lexus ES 250/300h وCitroën C4 بأربع نسخ

date=2026-11-21 | REVIEW_ONLY / OEM_POWERTRAIN_FAMILY_NOT_VIN_GEARBOX_PART_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_SCOPE_RECHECK_BATCH73_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## نطاق مطابقة المصدر الخام
1. engines_part_008.csv:1383, Lexus ES (2023), 250 8AT AWD (203 HP), Gasoline.
2. engines_part_008.csv:1385, Lexus ES (2023), 300h e-CVT FWD (215 HP), Hybrid Gasoline.
3. engines_part_004.csv:1188, Citroën C4 (2022–2024), PureTech 100 Start & Stop 6MT.
4. engines_part_004.csv:1189, Citroën C4 (2022–2024), PureTech 130 8AT.
5. engines_part_004.csv:1190, Citroën C4 (2022–2024), PureTech 130 Start & Stop 8AT.
6. engines_part_004.csv:1191, Citroën C4 (2022–2024), BlueHDi 130 Start & Stop 8AT.
- Raw file Git blob SHA Lexus: 88dcf7945b863564a06acb1de5f9676d401bba49.
- Raw file Git blob SHA Citroën: a62309aa7556a1ffbc89573c42cdfab1cb27c1f5.

## مراجع Lexus الأصلية
- Lexus Canada official MY2023 ES release states ES250 AWD has **2.5L 203 peak HP, eight-speed automatic**, and ES300h 2.5L Atkinson hybrid has **215 net HP and a continuously variable hybrid transaxle**, distinguishing gasoline automatic from hybrid transaxle.
- OEM_SOURCE: https://media.lexus.ca/en/releases/2022/striking-design-meets-commanding-performance-the-2023-lexus-es-series-luxury-sedans.html
- Lexus 2020 release explicitly explains electronically controlled CVT on ES300h:
  https://media.lexus.ca/en/releases/2019/rewarding-at-every-touch-and-turn-the-2020-lexus-es-series-takes-a-bold-step-forward.html
- Rows 1383/1385 each now have matching **MY2023 powertrain + power + drivetrain family evidence for Canada**, but exact transmission assembly/model code / full MY2023–2025 coverage / VIN applicability not verified.
- Finding=OEM_SAME_MODEL_YEAR_MARKET_POWERTRAIN_FAMILY_CONFIRMED / EXACT_GEARBOX_IDENTIFIER_PENDING.

## مراجع Citroën الأصلية
- Stellantis/Citroën official New C4 launch enumerates distinct family pairings: PureTech 100 S&S **6-speed manual**, PureTech 130 S&S **EAT8**, BlueHDi 130 S&S **EAT8**; it ALSO offers PureTech 130 S&S with manual six-speed in some market ranges.
- OEM_SOURCE: https://www.media.stellantis.com/em-en/citroen/press/new-c4-and-e-c4-100-electric-citroen-reinvents-the-compact-hatchback
- The distinctions prove 6MT/EAT8 **family descriptions**, not individual gearbox assembly numbers.
- For raw 1189 «PureTech 130 8AT» without «Start & Stop», manufacturer release only explicitly lists PureTech 130 **S&S EAT8**. This text difference cannot be silently assumed identical and needs market/year/engine-spec match.
- Raw years 2022–2024 not fully established from 2020 family launch alone.
- Finding=OEM_TRANSMISSION_FAMILY_FOR_1188_1190_1191 / PURETECH130_WITHOUT_S_S_1189_AMBIGUOUS / FULL_2022_2024_YEAR_SCOPE_PENDING.

## الحصيلة
existing_hint_cases_reexamined=6
new_OEM_same_model_year_Lexus_family_leads=2
new_OEM_Citroen_family_evidence_reviewed=4
new_approved_exact_gearbox_code_vehicle_assignments=0
new_ECU_DTC_links=0
new_vehicle_imports=0
raw_rows_modified=0
hint_cases_still_not_approved=32
next_workstream=OEM_ASSEMBLY_PART_NUMBER_AND_VIN_FITMENT_FOR_LEXUS_AND_CITROEN_THEN_OTHER_PENDING_HINTS

## الحماية
لا تعديل لمكتبة DTC أو ملف المحركات أو queue السابقة أو main أو stable أو الموقع أو برنامج Windows أو الوسائط.
