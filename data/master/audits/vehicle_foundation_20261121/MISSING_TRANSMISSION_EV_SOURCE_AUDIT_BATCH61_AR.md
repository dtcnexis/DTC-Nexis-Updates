# DTC NEXIS — الدفعة 61: مراجعة 30 سجلًا من EV_TEXT_ONLY

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_ev_batch01.csv

## المنهج
طوبقت 30 حالة من EV_TEXT_ONLY مع CSV الخام بالموديل والماركة والسنة ووصف المحرك، مع خلو حقل ناقل الحركة المنظم وحالة NOT_OEM_VERIFIED. توصيف كهربائي محتمل لا يثبت أنه ناقل تقليدي أو أن وحدة الاختزال متطابقة بين الإصدارات، ويلزم مصدر OEM يحدد فئة المحرك/الدفع والسوق والجيل قبل اعتمادها.

## أصول الصفوف
- engines_part_011.csv: lines 936, 937, 939, 940, 1011, 1012, 1358, 1596, 1947; Git_blob_sha=b8b395630356ba2157957abdc425847ff6218774
- engines_part_012.csv: lines 210, 598, 1619, 1891; Git_blob_sha=bbcd1f604d7405c0c79dad7b08120b2b86ef38b2
- engines_part_013.csv: lines 6, 7, 8, 9, 14, 15, 16, 17, 511, 524, 571, 572, 573, 578, 579, 580, 581; Git_blob_sha=d6fe7f5f1d6d6e695bb73e30c5b94234afb2ae01

| المصدر:صف | الماركة | الموديل | السنة | الوصف | الوقود الخام | cc | النتيجة |
|---|---|---|---|---|---|---|---|
| engines_part_011.csv:936 | Nissan | Ariya | 2020 | 63 KWh 2WD (218 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:937 | Nissan | Ariya | 2020 | 63 KWh AWD (340 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:939 | Nissan | Ariya | 2020 | 87 KWh 2WD (242 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:940 | Nissan | Ariya | 2020 | 87 KWh AWD (394 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:1011 | Nissan | Juke EV | 2026 | 52 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:1012 | Nissan | Juke EV | 2026 | 75 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:1358 | Nissan | Sakura | 2022 | 20 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:1596 | Opel | Astra | 2022 | 54 KWh (156 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_011.csv:1947 | Opel | Astra Sports Tourer | 2022 | 54 KWh (156 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_012.csv:210 | Opel | Grandland | 2024 | 98 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_012.csv:598 | Opel | Rocks-e | 2021 | 5.5 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_012.csv:1619 | Peugeot | 408 | 2026 | 58 KWh (210 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_012.csv:1891 | Pininfarina | B95 | 2023 | 120 KWh (1900 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:6 | Polestar | 2 | 2023 | Long range Dual motor 82 KWh AWD (421 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:7 | Polestar | 2 | 2023 | Long range Dual motor Performance Pack 82 KWh AWD (476 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:8 | Polestar | 2 | 2023 | Long range Single motor 82 KWh RWD (299 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:9 | Polestar | 2 | 2023 | Standard range Single motor 69 KWh RWD (272 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:14 | Polestar | 4 | 2023 | Long range Dual motor 102 KWh (544 HP) | — | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:15 | Polestar | 4 | 2023 | Long range Single motor 102 KWh (272 HP) | — | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:16 | Polestar | 5 | 2025 | Dual Motor 112 KWh (748 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:17 | Polestar | 5 | 2025 | Performance 112 KWh (884 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:511 | Porsche | Macan 4 Electric | 2024 | 100 KWh (408 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:524 | Porsche | Macan Turbo Electric | 2024 | 100 KWh (639 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:571 | Porsche | Taycan | 2024 | 4S 89 KWh (544 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:572 | Porsche | Taycan | 2024 | 89 KWh (408 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:573 | Porsche | Taycan | 2024 | Performance Battery Plus 97 KWh (435 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:578 | Porsche | Taycan Cross Turismo | 2024 | 4 105 KWh (435 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:579 | Porsche | Taycan Cross Turismo | 2024 | 4S 105 KWh (598 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:580 | Porsche | Taycan Cross Turismo | 2024 | Turbo 105 KWh (884 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_013.csv:581 | Porsche | Taycan Cross Turismo | 2024 | Turbo S 105 KWh (952 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |

## النتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
raw_rows_modified=0
cumulative_EV_text_records_source_reviewed=180
last_examined=engines_part_013.csv:581
next_record=engines_part_013.csv:589
remaining_EV_text_unreviewed=67

## الحماية
لا تغيير للمصدر أو main أو stable أو الموقع أو Windows أو الوسائط أو مكتبة DTC المعتمدة.
