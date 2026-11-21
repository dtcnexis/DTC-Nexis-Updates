# DTC NEXIS — الدفعة 57: مراجعة 30 سجلًا من EV_TEXT_ONLY

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_ev_batch01.csv

## المنهج
تدقيق 30 إدخالًا من فهرس EV النصي مقابل صفوف ملفات gor3a الخام، بمطابقة الشركة والموديل والسنة ووصف المحرك، مع التأكد من خلو الحقل المنظم transmission وحالة NOT_OEM_VERIFIED. تصنيف EV قائم على الألفاظ، لا يثبت التقنية ولا رقم وحدة الدفع. قد لا تحتاج السيارة الكهربائية صندوق تروس تقليديًا ولكن يجب التحقق من gear reduction / drive unit من OEM قبل الحسم.

## ملفات المصدر
- engines_part_003.csv: lines 1789, 1813, 1814, 1817; Git_blob_sha=3796acc7f93b581a449480f958097be2937788bc
- engines_part_004.csv: lines 1805, 1806; Git_blob_sha=a62309aa7556a1ffbc89573c42cdfab1cb27c1f5
- engines_part_005.csv: lines 175, 485, 486, 487, 488, 490, 491, 492, 493, 494, 585, 586, 844, 863, 864, 865, 866, 867, 868, 888, 889, 890, 891, 892; Git_blob_sha=c6c4861abab91c5d694bcec10fab21934ab36136

| المصدر:صف | الماركة | الموديل | سنة المصدر | وصف منظومة المحرك | fuel الخام | cc | حالة الاعتماد |
|---|---|---|---|---|---|---|---|
| engines_part_003.csv:1789 | Cadillac | Escalade | 2023 | 200 KWh (680 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_003.csv:1813 | Cadillac | Lyriq | 2022 | 102 KWh (347 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_003.csv:1814 | Cadillac | Lyriq | 2022 | 102 KWh (507 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_003.csv:1817 | Cadillac | Optiq-V | 2025 | Dual Motor 85 KWh AWD (519 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_004.csv:1805 | Cupra | Raval | 2026 | 37 KWh FWD (115 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_004.csv:1806 | Cupra | Raval | 2026 | 37 KWh FWD (135 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:175 | Dacia | Spring | 2021 | 26.8 KWh (44 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:485 | DFSK | SERES | 2021 | 120 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:486 | DFSK | SERES 2 | 2021 | 55 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:487 | DFSK | SERES 3 | 2020 | 50 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:488 | DFSK | SERES 3 | 2020 | 55 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:490 | DFSK | SERES 3 | 2020 | 120 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:491 | DFSK | SERES 3 / | 2021 | 50 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:492 | DFSK | SERES-3 | 2021 | 55 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:493 | DFSK | SERES3 | 2021 | 55 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:494 | DFSK | SERES3 | 2021 | 120 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:585 | Dodge | Charger | 2024 | R/T 100.5 KWh AWD (496 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:586 | Dodge | Charger | 2024 | SCAT PACK 100.5 KWh AWD (670 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:844 | DS | AUTOMOBILES DS 7 | 2026 | Long Range 97.2 KWh FWD (245 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:863 | e.GO | E.WAVE X | 2022 | 44 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:864 | e.GO | LIFE | 2019 | Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:865 | e.GO | LIFE FIRST EDITION | 2019 | 53 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:866 | e.GO | LIFE FIRST EDITION | 2019 | 57 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:867 | e.GO | LIFE FIRST EDITION | 2019 | 41 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:868 | e.GO | LIFE FIRST EDITION | 2019 | 75 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:888 | FAW | E-HS9 | 2022 | 160 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:889 | FAW | E-HS9 | 2022 | 245 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:890 | FAW | E-HS9 | 2022 | 405 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:891 | FAW | EHS9 | 2021 | 160 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_005.csv:892 | FAW | EHS9 | 2021 | 245 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |

## النتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
raw_rows_modified=0
cumulative_EV_text_records_source_reviewed=60
last_examined=engines_part_005.csv:892
next_record=engines_part_005.csv:893
remaining_EV_text_unreviewed=187

## الحماية
لا تعديل للمصدر أو main أو stable أو الموقع أو برنامج Windows أو الصور أو مكتبة DTC المعتمدة.
