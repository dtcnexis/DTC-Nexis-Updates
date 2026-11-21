# DTC NEXIS — الدفعة 49: مراجعة المصدر للناقل المفقود

date=2026-11-21 | REVIEW_ONLY / NOT_OEM_VERIFIED / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv

## التدقيق
تمت مطابقة 30 إدخالًا مع CSV الخام بالموديل والماركة والسنة ووصف المحرك، وكلها ضمن قائمة OTHER، وحقل ناقل الحركة المنظم خالٍ. السعة والوقود من المصدر الخام وليسا مواصفات OEM معتمدة. أي خلافات تحتاج مراجع مصنع لتحديد الجيل والسوق ونظام الدفع والناقل؛ لا دمج أو تعديل للأصول.

## ملفات المصدر
- engines_part_014.csv: lines 186, 927, 928, 929, 930, 931, 932, 933, 934, 936, 937, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1034, 1035, 1036, 1073, 1142, 1816, 1829, 1856; Git_blob_sha=d16faa05277fc868bb2ed1eb9c890d4275983b77
- engines_part_015.csv: lines 565, 566, 567, 568; Git_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36

| المصدر:صف | الماركة | الموديل | السنة | وصف المحرك | الوقود | cc | الحالة |
|---|---|---|---|---|---|---|---|
| engines_part_014.csv:186 | RUF | TURBO FLORIO | 2022 | 3.0L 433 kW Petrol | Petrol | 2981 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:927 | SEAT | Leon | 2020 | 1.0L TSI FWD (110 HP) | Gasoline | 999 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:928 | SEAT | Leon | 2020 | 1.0L TSI FWD (90 HP) | Gasoline | 999 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:929 | SEAT | Leon | 2020 | 1.5L TSI FWD (130 HP) | Gasoline | 1498 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:930 | SEAT | Leon | 2020 | 1.5L TSI FWD (150 HP) | Gasoline | 1498 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:931 | SEAT | Leon | 2020 | 2.0L TSI FWD (190 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:932 | SEAT | Leon | 2020 | 2.0L TDI FWD (115 HP) | Diesel | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:933 | SEAT | Leon | 2020 | 2.0L TDI FWD (150 HP) | Diesel | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:934 | SEAT | Leon | 2020 | 1.0L eTSI FWD (110 HP) | Hybrid | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:936 | SEAT | Leon | 2020 | 1.5L eTSI FWD (150 HP) | Hybrid | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:937 | SEAT | Leon | 2020 | 1.5L TGI FWD (130 HP) | Natural Gas | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1026 | SEAT | Leon ST | 2020 | 1.0L TSI FWD (110 HP) | Gasoline | 999 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1027 | SEAT | Leon ST | 2020 | 1.0L TSI FWD (90 HP) | Gasoline | 999 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1028 | SEAT | Leon ST | 2020 | 1.5L TSI FWD (130 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1029 | SEAT | Leon ST | 2020 | 1.5L TSI FWD (150 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1030 | SEAT | Leon ST | 2020 | 2.0L TSI FWD (190 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1031 | SEAT | Leon ST | 2020 | 2.0L TDI FWD (115 HP) | Diesel | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1032 | SEAT | Leon ST | 2020 | 2.0L TDI FWD (150 HP) | Diesel | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1034 | SEAT | Leon ST | 2020 | 1.5L TGI FWD (130 HP) | Natural Gas | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1035 | SEAT | Leon ST | 2020 | 1.0L eTSI FWD (110 HP) | Mild Hybrid | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1036 | SEAT | Leon ST | 2020 | 1.5L eTSI FWD (150 HP) | Mild Hybrid | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1073 | SEAT | Mii | 2019 | 61 Kw (83 HP) | — | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1142 | Seres | 5 | 2023 | 1.5L | — | 1499 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1816 | Smart | forfour | 2019 | 41 Kw (82 HP) | Electric | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1829 | Smart | fortwo | 2019 | 41 Kw (82 HP) | Electric | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:1856 | Smart | fortwo Cabrio | 2019 | 41 Kw (82 HP) | Electric | — | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:565 | SWM | G01 | 2021 | 1.5L 98 kW Lpg | Lpg | 1499 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:566 | SWM | G01 | 2021 | 1.5L 98 kW Petrol | Petrol | 1499 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:567 | SWM | G01F | 2021 | 1.5L 98 kW Lpg | Lpg | 1499 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:568 | SWM | G01F | 2021 | 1.5L 98 kW Petrol | Petrol | 1499 | OEM_GEARBOX_REQUIRED |

## التقرير
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_49=1039
last_examined=engines_part_015.csv:568
next_record=engines_part_015.csv:569
remaining_OTHER_unreviewed_based_on_initial_1162=123

## الحماية
بلا اعتماد OEM أو ECU/DTC؛ لا تعديل للملفات الأصلية أو main أو stable أو الموقع أو برنامج Windows أو الوسائط أو مكتبة الأكواد.
