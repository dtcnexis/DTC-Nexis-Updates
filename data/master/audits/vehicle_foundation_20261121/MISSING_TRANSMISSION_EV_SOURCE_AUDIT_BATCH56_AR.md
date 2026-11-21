# DTC NEXIS — الدفعة 56: مراجعة 30 سجلًا من EV_TEXT_ONLY

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_ev_batch01.csv

## المنهج
تدقيق 30 إدخالًا من فهرس EV النصي مقابل صفوف ملفات gor3a الخام، بمطابقة الشركة والموديل والسنة ووصف المحرك، مع التأكد من خلو الحقل المنظم transmission وحالة NOT_OEM_VERIFIED. تصنيف EV قائم على الألفاظ، لا يثبت التقنية ولا رقم وحدة الدفع. قد لا تحتاج السيارة الكهربائية صندوق تروس تقليديًا ولكن يجب التحقق من gear reduction / drive unit من OEM قبل الحسم.

## ملفات المصدر
- engines_part_001.csv: lines 124, 125, 127, 128, 129, 130, 131, 132, 133, 479, 480, 735, 736, 1069, 1070; Git_blob_sha=8a2e350c18a0f067aee4f6d03d2c5d7be964cffc
- engines_part_002.csv: lines 393, 403, 474, 475, 476, 477, 478, 479; Git_blob_sha=3a281ebfce241e7849e4db09dcaa9e385986274e
- engines_part_003.csv: lines 1060, 1075, 1079, 1080, 1081, 1092, 1713; Git_blob_sha=3796acc7f93b581a449480f958097be2937788bc

| المصدر:صف | الماركة | الموديل | سنة المصدر | وصف منظومة المحرك | fuel الخام | cc | حالة الاعتماد |
|---|---|---|---|---|---|---|---|
| engines_part_001.csv:124 | Acura | ZDX | 2023 | A-Spec 102 KWh (340 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:125 | Acura | ZDX | 2023 | Type S Dual motor 102 KWh (500 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:127 | Aiways | U5 | 2020 | 125 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:128 | Aiways | U5 | 2020 | 55 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:129 | Aiways | U5 | 2020 | 60 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:130 | Aiways | U5 | 2020 | 150 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:131 | Aiways | U5 | 2020 | 1506 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:132 | Aiways | U5 / / | 2021 | 60 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:133 | Aiways | U6 | 2022 | 65 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:479 | Alfa Romeo | Junior | 2024 | 54 KWh AWD (156 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:480 | Alfa Romeo | Junior | 2024 | 54 KWh AWD (240 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:735 | Alpine | A390 | 2025 | GT 89 KWh (400 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:736 | Alpine | A390 | 2025 | GTS 89 KWh (470 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:1069 | Audi | A2 e-tron | 2026 | 61 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_001.csv:1070 | Audi | A2 e-tron | 2026 | 84 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_002.csv:393 | Audi | e-tron | 2024 | S e-tron GT 105 KWh (679 HP) | Plug-in Hybrid | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_002.csv:403 | Audi | E5 | 2025 | 76 kWh RWD (299 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_002.csv:474 | Audi | Q4 e-tron | 2026 | 63 kWh RWD (204 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_002.csv:475 | Audi | Q4 e-tron | 2026 | 82 kWh quattro (299 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_002.csv:476 | Audi | Q4 e-tron | 2026 | Performance 82 kWh quattro (340 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_002.csv:477 | Audi | Q4 e-tron | 2021 | 35 e-tron 52 KWh (170 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_002.csv:478 | Audi | Q4 e-tron | 2021 | 40 e-tron 77 KWh (204 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_002.csv:479 | Audi | Q4 e-tron | 2021 | 50 e-tron quattro 82 KWh (299 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_003.csv:1060 | BMW | i3 | 2026 | 50 xDrive 108.7 KWh AWD (463 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_003.csv:1075 | BMW | i5 | 2024 | eDrive40 81.2 KWh (340 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_003.csv:1079 | BMW | i7 | 2026 | 50 xDrive 112.5 KWh AWD (455 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_003.csv:1080 | BMW | i7 | 2026 | 60 xDrive 112.5 KWh AWD (544 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_003.csv:1081 | BMW | i7 | 2026 | M70 xDrive 112.4 KWh AWD (680 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_003.csv:1092 | BMW | iX M | 2022 | 111.5 KWh (619 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_003.csv:1713 | Cadillac | Celestiq | 2023 | 111 KWh AWD (600 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |

## النتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
raw_rows_modified=0
cumulative_EV_text_records_source_reviewed=30
last_examined=engines_part_003.csv:1713
next_record=engines_part_003.csv:1789
remaining_EV_text_unreviewed=217

## الحماية
لا تعديل للمصدر أو main أو stable أو الموقع أو برنامج Windows أو الصور أو مكتبة DTC المعتمدة.
