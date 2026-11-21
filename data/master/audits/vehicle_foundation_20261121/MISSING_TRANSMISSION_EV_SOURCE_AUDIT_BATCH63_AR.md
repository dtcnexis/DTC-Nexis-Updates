# DTC NEXIS — الدفعة 63: مراجعة 30 سجلات من EV_TEXT_ONLY

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_ev_batch01.csv

## المنهج
طوبقت 30 حالة من EV_TEXT_ONLY مع CSV الخام بالموديل والماركة والسنة ووصف المحرك، مع خلو حقل ناقل الحركة المنظم وحالة NOT_OEM_VERIFIED. توصيف EV نصي فقط ولا يؤكد طبيعة وحدة الاختزال أو رمزها OEM. تُحفظ الاختلافات دون اعتماد أو حذف، وتحتاج وثائق صانع للجيل والسنة والسوق والدفع.

## ملفات المصدر
- engines_part_015.csv: lines 287, 299, 645, 646, 647, 648, 649, 650, 651, 652, 681, 926, 927, 928, 929, 930, 933, 934, 935, 1283, 1284, 1285, 1624, 1625, 1626; Git_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36
- engines_part_016.csv: lines 945, 946, 956, 964, 971; Git_blob_sha=8a5e0799e8cfaaddf2bdeef431f31dce7b582622

| المصدر:صف | الماركة | الموديل | السنة | وصف المحرك | الوقود الخام | cc | النتيجة |
|---|---|---|---|---|---|---|---|
| engines_part_015.csv:287 | Subaru | Solterra | 2021 | 71.4 KWh FWD (204 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:299 | Subaru | Uncharted | 2025 | Premium 74.7 kWh FWD (224 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:645 | Tesla | Model 3 | 2023 | Dual Motor Standard Range AWD (444 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:646 | Tesla | Model 3 | 2023 | Dual Motor Standard Range RWD (279 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:647 | Tesla | Model 3 | 2017 | Long Range 75 KWh AWD (346 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:648 | Tesla | Model 3 | 2017 | Long Range 75 KWh RWD (283 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:649 | Tesla | Model 3 | 2017 | Mid Range 62 KWh RWD (283 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:650 | Tesla | Model 3 | 2017 | Performance 75 KWh AWD (450 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:651 | Tesla | Model 3 | 2017 | Standard Range 50 KWh RWD (283 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:652 | Tesla | Model 3 | 2017 | Standard Range Plus 54 KWh RWD (283 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:681 | Tesla | Model Y | 2019 | Y Standard Range 60 KWh (204 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:926 | Toyota | bZ4X | 2025 | 57.7 KWh FWD (167 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:927 | Toyota | bZ4X | 2025 | 73.1 KWh AWD (343 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:928 | Toyota | bZ4X | 2025 | 73.1 KWh FWD (224 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:929 | Toyota | bZ4X | 2022 | 71.4 KWh AWD (217 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:930 | Toyota | bZ4X | 2022 | 71.4 KWh FWD (204 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:933 | Toyota | C-HR | 2025 | 57.7 KWh FWD (167 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:934 | Toyota | C-HR | 2025 | 77 KWh AWD (343 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:935 | Toyota | C-HR | 2025 | 77 KWh FWD (224 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:1283 | Toyota | Highlander / Kluger | 2026 | 77 KWh AWD (338 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:1284 | Toyota | Highlander / Kluger | 2026 | 77 KWh FWD (221 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:1285 | Toyota | Highlander / Kluger | 2026 | 95.8 KWh AWD (338 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:1624 | Toyota | Urban Cruiser | 2025 | 49 KWh FWD (144 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:1625 | Toyota | Urban Cruiser | 2025 | 61 KWh AWD (184 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_015.csv:1626 | Toyota | Urban Cruiser | 2025 | 61 KWh FWD (174 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_016.csv:945 | Volkswagen | ID.3 | 2026 | 50 KWh (170 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_016.csv:946 | Volkswagen | ID.3 | 2026 | 79 KWh (190 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_016.csv:956 | Volkswagen | ID.4 | 2020 | 82 KWh (201 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_016.csv:964 | Volkswagen | ID.7 GTX Tourer | 2024 | 86 KWh 4MOTION | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_016.csv:971 | Volkswagen | ID.Polo GTI | 2026 | 52 KWh FWD (226 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |

## النتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
raw_rows_modified=0
cumulative_EV_text_records_source_reviewed=240
last_examined=engines_part_016.csv:971
next_record=engines_part_016.csv:1283
remaining_EV_text_unreviewed=7

## الحماية
لا تغيير للمصدر أو main أو stable أو الموقع أو Windows أو الوسائط أو مكتبة DTC المعتمدة.
