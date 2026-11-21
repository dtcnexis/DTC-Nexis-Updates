# DTC NEXIS — الدفعة 62: مراجعة 30 سجلات من EV_TEXT_ONLY

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_ev_batch01.csv

## المنهج
طوبقت 30 حالة من EV_TEXT_ONLY مع CSV الخام بالموديل والماركة والسنة ووصف المحرك، مع خلو حقل ناقل الحركة المنظم وحالة NOT_OEM_VERIFIED. توصيف EV نصي فقط ولا يؤكد طبيعة وحدة الاختزال أو رمزها OEM. تُحفظ الاختلافات دون اعتماد أو حذف، وتحتاج وثائق صانع للجيل والسنة والسوق والدفع.

## ملفات المصدر
- engines_part_013.csv: lines 589, 590, 591, 650, 651, 1059, 1313, 1913, 1914; Git_blob_sha=d6fe7f5f1d6d6e695bb73e30c5b94234afb2ae01
- engines_part_014.csv: lines 121, 124, 125, 126, 127, 128, 129, 175, 1140, 1141, 1143, 1144, 1186, 1187, 1188, 1189, 1190; Git_blob_sha=d16faa05277fc868bb2ed1eb9c890d4275983b77
- engines_part_015.csv: lines 103, 104, 285, 286; Git_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36

| المصدر:صف | الماركة | الموديل | السنة | وصف المحرك | الوقود الخام | cc | النتيجة |
|---|---|---|---|---|---|---|---|
| engines_part_013.csv:589 | Porsche | Taycan Sport Turismo | 2024 | 105 KWh (435 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:590 | Porsche | Taycan Turbo | 2024 | 105 KWh RWD (789 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:591 | Porsche | Taycan Turbo | 2024 | Weissach package 105 KWh RWD (789 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:650 | Ram | Trucks 1500 | 2023 | 229 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:651 | Ram | Trucks 1500 | 2023 | Standard 168 KWh AWD (654 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:1059 | Renault | City K-ZE | 2019 | 26.8 KWh (45 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:1313 | Renault | Grand Kangoo | 2023 | 45 KWh (122 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:1913 | Renault | Scenic | 2023 | 60 KWh (170 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:1914 | Renault | Scenic | 2023 | 87 KWh (220 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:121 | Rimac | Nevera | 2024 | 108 KWh AWD (2107 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:124 | Rivian | R1S | 2021 | 105 KWh AWD (408 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:125 | Rivian | R1S | 2021 | 135 KWh AWD (764 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:126 | Rivian | R1S | 2021 | 180 KWh AWD (710 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:127 | Rivian | R1T | 2021 | 105 KWh AWD (408 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:128 | Rivian | R1T | 2021 | 135 KWh AWD (764 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:129 | Rivian | R1T | 2021 | 180 KWh AWD (710 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:175 | Rolls-Royce | Spectre | 2025 | Dual Motor 120 KWh AWD (650 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:1140 | Seres | 3 | 2020 | 55 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:1141 | Seres | 3 | 2020 | 120 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:1143 | Seres | DFSK | 2020 | 55 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:1144 | Seres | DFSK | 2020 | 120 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:1186 | Škoda | SKODA Enyaq | 2020 | Enyaq 50 iV 109 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:1187 | Škoda | SKODA Enyaq | 2020 | Enyaq 60 iV 132 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:1188 | Škoda | SKODA Enyaq | 2020 | Enyaq 80 iV AWD 150 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:1189 | Škoda | SKODA Enyaq | 2020 | Enyaq 80x iV AWD 195 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_014.csv:1190 | Škoda | SKODA Enyaq | 2020 | Enyaq RS AWD 225 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:103 | Subaru | Getaway | 2026 | Long Range 95.8 KWh AWD (420 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:104 | Subaru | Getaway | 2026 | Standard Range 77 KWh AWD | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:285 | Subaru | Solterra | 2025 | 74.7 KWh AWD (338 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:286 | Subaru | Solterra | 2021 | 71.4 KWh AWD (218 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |

## النتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
raw_rows_modified=0
cumulative_EV_text_records_source_reviewed=210
last_examined=engines_part_015.csv:286
next_record=engines_part_015.csv:287
remaining_EV_text_unreviewed=37

## الحماية
لا تغيير للمصدر أو main أو stable أو الموقع أو Windows أو الوسائط أو مكتبة DTC المعتمدة.
