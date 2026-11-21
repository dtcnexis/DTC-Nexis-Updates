# DTC NEXIS — الدفعة 58: مراجعة 30 سجلًا من EV_TEXT_ONLY

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_ev_batch01.csv

## المنهج
تدقيق 30 إدخالًا من فهرس EV النصي مقابل صفوف ملفات gor3a الخام، بمطابقة الشركة والموديل والسنة ووصف المحرك، مع التأكد من خلو الحقل المنظم transmission وحالة NOT_OEM_VERIFIED. تصنيف EV قائم على الألفاظ، لا يثبت التقنية ولا رقم وحدة الدفع. قد لا تحتاج السيارة الكهربائية صندوق تروس تقليديًا ولكن يجب التحقق من gear reduction / drive unit من OEM قبل الحسم.

## ملفات المصدر
- engines_part_005.csv: lines 893, 894, 1006, 1162, 1163, 1240, 1674, 1730, 1731; Git_blob_sha=c6c4861abab91c5d694bcec10fab21934ab36136
- engines_part_006.csv: lines 71, 72, 1338, 1355, 1357, 1358, 1371; Git_blob_sha=2622eaa2d8a10316d2e7a9561d3182061f51ffce
- engines_part_007.csv: lines 376, 1023, 1024, 1025, 1026, 1034, 1130; Git_blob_sha=0399f720f92849388bf3c3e33f92441d42b7416f
- engines_part_008.csv: lines 92, 320, 321, 322, 323, 324, 338; Git_blob_sha=88dcf7945b863564a06acb1de5f9676d401bba49

| المصدر:صف | الماركة | الموديل | سنة المصدر | وصف منظومة المحرك | fuel الخام | cc | حالة الاعتماد |
|---|---|---|---|---|---|---|---|
| engines_part_005.csv:893 | FAW | EHS9 | 2021 | 320 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:894 | FAW | EHS9 | 2021 | 405 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:1006 | Ferrari | Luce | 2026 | 122 kWh AWD (1050 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:1162 | Fiat | 500 3+1 | 2020 | 23.8 KWh FWD (93 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:1163 | Fiat | 500 3+1 | 2020 | 42 KWh FWD (118 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:1240 | Fiat | 600 | 2023 | 54 KWh (156 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:1674 | Fiat | Topolino | 2023 | 5.4 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:1730 | Fisker | Ocean | 2021 | Dual Motor AWD (540 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:1731 | Fisker | Ocean | 2021 | Dual Motor AWD (550 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_006.csv:71 | Ford | F-150 Super Cab | 2022 | Extended-Range Battery 131 KWh (571 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_006.csv:72 | Ford | F-150 Super Cab | 2022 | Standard-Range Battery 98 KWh (432 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_006.csv:1338 | Genesis | G80 | 2020 | EV 272 KW AWD (370 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_006.csv:1355 | Genesis | GV60 | 2022 | Performance 77.4 kWh AWD (435 Hp) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_006.csv:1357 | Genesis | GV60 | 2022 | Standard 77.4 kWh AWD (318 Hp) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_006.csv:1358 | Genesis | GV60 | 2022 | Standard 77.4 kWh RWD (228 Hp) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_006.csv:1371 | Genesis | GV90 | 2026 | 123.5 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_007.csv:376 | Honda | e:Ny1 | 2023 | 68.8 KWh (204 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_007.csv:1023 | Hyundai | Ioniq | 2021 | 58 KWh (170 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_007.csv:1024 | Hyundai | Ioniq | 2021 | 58 KWh AWD (235 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_007.csv:1025 | Hyundai | Ioniq | 2021 | 72.6 KWh (218 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_007.csv:1026 | Hyundai | Ioniq | 2021 | 72.6 KWh AWD (306 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_007.csv:1034 | Hyundai | Ioniq 5 | 2023 | 84 KWh (609 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_007.csv:1130 | Hyundai | Kona Electric | 2021 | 64 KWh (201 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:92 | Jeep | Wagoneer | 2024 | 100 KWh (600 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:320 | Kia | EV2 | 2026 | Standard Range 42.2 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:321 | Kia | EV3 | 2026 | Long Range 81.4 KWh AWD | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:322 | Kia | EV3 | 2026 | Standard Range 58.3 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:323 | Kia | EV3 | 2024 | 58.3 kWh (204 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:324 | Kia | EV3 | 2024 | 81.4 kWh (204 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:338 | Kia | EV6 | 2021 | GT Long Range 77.4 KWh AWD (585 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |

## النتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
raw_rows_modified=0
cumulative_EV_text_records_source_reviewed=90
last_examined=engines_part_008.csv:338
next_record=engines_part_008.csv:339
remaining_EV_text_unreviewed=157

## الحماية
لا تعديل للمصدر أو main أو stable أو الموقع أو برنامج Windows أو الصور أو مكتبة DTC المعتمدة.
