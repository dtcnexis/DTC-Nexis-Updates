# DTC NEXIS — الدفعة 59: مراجعة 30 سجلًا من EV_TEXT_ONLY

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_ev_batch01.csv

## المنهج
طوبقت 30 حالة من EV_TEXT_ONLY مع CSV الخام بالموديل والماركة والسنة ووصف المحرك، مع خلو حقل ناقل الحركة المنظم وحالة NOT_OEM_VERIFIED. توصيف كهربائي محتمل لا يثبت أنه ناقل تقليدي أو أن وحدة الاختزال متطابقة بين الإصدارات، ويلزم مصدر OEM يحدد فئة المحرك/الدفع والسوق والجيل قبل اعتمادها.

## أصول الصفوف
- engines_part_008.csv: lines 339, 340, 341, 342, 649, 1110, 1585, 1897, 1911, 1962, 1963, 1964, 1965, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983; Git_blob_sha=88dcf7945b863564a06acb1de5f9676d401bba49

| المصدر:صف | الماركة | الموديل | السنة | الوصف | الوقود الخام | cc | النتيجة |
|---|---|---|---|---|---|---|---|
| engines_part_008.csv:339 | Kia | EV6 | 2021 | Long Range 77.4 KWh (228 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:340 | Kia | EV6 | 2021 | Long Range 77.4 KWh AWD (325 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:341 | Kia | EV6 | 2021 | Standard Range 58 KWh (170 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:342 | Kia | EV6 | 2021 | Standard Range 58 KWh AWD (235 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:649 | Kia | Soul | 2018 | EV 201 HP FWD (150 Kw) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1110 | Lancia | Ypsilon | 2024 | 51 KWh (156 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1585 | Lightyear | Lightyear 0 | 2022 | 60 kWh AWD (172 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1897 | Maserati | GranCabrio | 2024 | 92.5 KWh AWD (829 HP) | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1911 | Maserati | Grecale | 2023 | 105 KWh | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1962 | Maxus | E-DELIVER 3 | 2020 | 40 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1963 | Maxus | E-DELIVER 3 | 2020 | 90 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1964 | Maxus | ED60 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1965 | Maxus | eDELIVER | 2022 | 150 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1967 | Maxus | EDELIVER 9 | 2021 | 150 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1968 | Maxus | EG50 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1969 | Maxus | EG51 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1970 | Maxus | EG52 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1971 | Maxus | EG53 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1972 | Maxus | EG54 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1973 | Maxus | EG55 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1974 | Maxus | EG56 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1975 | Maxus | EG57 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1976 | Maxus | EG58 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1977 | Maxus | EG59 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1978 | Maxus | EG60 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1979 | Maxus | EG61 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1980 | Maxus | EG62 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1981 | Maxus | EG63 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1982 | Maxus | EG64 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |
| engines_part_008.csv:1983 | Maxus | EG65 | 2022 | 130 kW Electric | Electric | — | OEM_DRIVETRAIN_REQUIRED |

## النتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
raw_rows_modified=0
cumulative_EV_text_records_source_reviewed=120
last_examined=engines_part_008.csv:1983
next_record=engines_part_008.csv:1984
remaining_EV_text_unreviewed=127

## الحماية
لا تغيير للمصدر أو main أو stable أو الموقع أو Windows أو الوسائط أو مكتبة DTC المعتمدة.
