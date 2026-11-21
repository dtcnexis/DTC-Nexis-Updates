# DTC NEXIS — الدفعة 60: مراجعة 30 سجلًا من EV_TEXT_ONLY

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_ev_batch01.csv

## المنهج
طوبقت 30 حالة من EV_TEXT_ONLY مع CSV الخام بالموديل والماركة والسنة ووصف المحرك، مع خلو حقل ناقل الحركة المنظم وحالة NOT_OEM_VERIFIED. توصيف كهربائي محتمل لا يثبت أنه ناقل تقليدي أو أن وحدة الاختزال متطابقة بين الإصدارات، ويلزم مصدر OEM يحدد فئة المحرك/الدفع والسوق والجيل قبل اعتمادها.

## أصول الصفوف
- engines_part_008.csv: lines 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991; Git_blob_sha=88dcf7945b863564a06acb1de5f9676d401bba49
- engines_part_009.csv: lines 256, 257, 527, 869; Git_blob_sha=40e1c3019328b6375e0b367759ad6836d9af61bb
- engines_part_010.csv: lines 562, 564, 565, 566, 586, 1339, 1396, 1397, 1398, 1399; Git_blob_sha=190ce6216c3301de8f289611dad37202cc86180d
- engines_part_011.csv: lines 4, 5, 33, 34, 164, 248, 934, 935; Git_blob_sha=b8b395630356ba2157957abdc425847ff6218774

| المصدر:صف | الماركة | الموديل | السنة | الوصف | الوقود الخام | cc | النتيجة |
|---|---|---|---|---|---|---|---|
| engines_part_008.csv:1984 | Maxus | Einiq 5 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1985 | Maxus | EUINIQ 5 | 2021 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1986 | Maxus | EUNIQ | 2021 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1987 | Maxus | EUNIQ 5 | 2020 | 65 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1988 | Maxus | EUNIQ 5 | 2020 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1989 | Maxus | EUNIQ 6 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1990 | Maxus | EV80 | 2017 | 72 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1991 | Maxus | MIFA 9 | 2022 | 180 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_009.csv:256 | Mazda | 6e | 2025 | 68.8 KWh RWD (258 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_009.csv:257 | Mazda | 6e | 2025 | 80 KWh RWD (244 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_009.csv:527 | Mercedes-AMG | CLA 45 Shooting Brake | 2026 | 94 kWh 4MATIC+ (680 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_009.csv:869 | Mercedes-Benz | MERCEDES BENZ B-Klasse | 2014 | Electric Drive (179 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_010.csv:562 | Mercedes-Benz | MERCEDES BENZ EQC | 2019 | 400 4MATIC 80 Kwh (408 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_010.csv:564 | Mercedes-Benz | MERCEDES BENZ EQE SUV | 2022 | 350 4MATIC AWD 90.6 KWh (292 HP) | Plug-in Hybrid | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_010.csv:565 | Mercedes-Benz | MERCEDES BENZ EQE SUV | 2022 | 350+ RWD 90.6 KWh (292 HP) | Plug-in Hybrid | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_010.csv:566 | Mercedes-Benz | MERCEDES BENZ EQE SUV | 2022 | 500 4MATIC AWD 90.6 KWh (408 HP) | Plug-in Hybrid | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_010.csv:586 | Mercedes-Benz | MERCEDES BENZ G-Klasse | 2024 | 116 KWh AWD (587 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_010.csv:1339 | Mercedes-Benz | MERCEDES BENZ Vito | 2020 | eVito 90 KWh (204 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_010.csv:1396 | MG | IM6 | 2025 | Long Range 100 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_010.csv:1397 | MG | IM6 | 2025 | Standard Range 75 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_010.csv:1398 | MG | Marvel R | 2021 | Comfort / Luxury 70 KWh (180 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_010.csv:1399 | MG | Marvel R | 2021 | Performance 70 KWh (288 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:4 | MG | MG 5 | 2021 | 50.3 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:5 | MG | MG 5 | 2021 | 61.1 KWh (154 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:33 | MG | ZS | 2021 | Long Range 70 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:34 | MG | ZS | 2021 | Standard Range 50.3 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:164 | MINI | Countryman | 2023 | 66.45 KWh AWD (313 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:248 | MINI | Hatch | 2023 | 54.2 KWh (218 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:934 | Nissan | Ariya | 2024 | 66 KWh B6 e-4ORCE AWD | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:935 | Nissan | Ariya | 2024 | 91 KWh B9 e-4ORCE AWD | Electric | — | OEM_DRIVETRAIN_REQUIRED |

## النتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
raw_rows_modified=0
cumulative_EV_text_records_source_reviewed=150
last_examined=engines_part_011.csv:935
next_record=engines_part_011.csv:936
remaining_EV_text_unreviewed=97

## الحماية
لا تغيير للمصدر أو main أو stable أو الموقع أو Windows أو الوسائط أو مكتبة DTC المعتمدة.
