# DTC NEXIS — الدفعة 51: مراجعة المصدر للناقل المفقود

date=2026-11-21 | REVIEW_ONLY / NOT_OEM_VERIFIED / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv

## تدقيق المصدر
قورنت 30 حالة حسب قائمة OTHER مع CSV الخام: الماركة والموديل والسنة ووصف المحرك وحالة NOT_OEM_VERIFIED وحقل ناقل الحركة الفارغ. لا يعني تطابق الصف أن تطبيقه الفني ثبت مصنعيًا. لا حذف لأي اختلافات في السعة/الوقود/السوق.

## مرجع الملف وبصمته
- engines_part_015.csv: rows 639, 640, 641, 692, 1007, 1272, 1273, 1274, 1275, 1414; Git_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36
- engines_part_016.csv: rows 275, 384, 385, 386, 1278, 1279, 1280, 1281, 1282; Git_blob_sha=8a5e0799e8cfaaddf2bdeef431f31dce7b582622
- engines_part_017.csv: rows 356, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987; Git_blob_sha=2e7d952d6b67894720adf67613a819b92cdc48cf

| المصدر:صف | الماركة | الموديل | السنة | وصف المحرك | الوقود | cc | نتيجة المراجعة |
|---|---|---|---|---|---|---|---|
| engines_part_015.csv:639 | Tatra | 8P6R43 | 2019 | 12.9L | — | 12902 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:640 | Tatra | 8P6R53 | 2019 | 12.9L | — | 12902 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:641 | Tatra | T2-603 | 1965 | 2.5L | — | 2472 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:692 | Toyota | 4Runner | 2024 | 2.4L (282 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:1007 | Toyota | Corolla | 2020 | 1.6L VVT-i Multidrive S FWD (132 HP) | Gasoline | 1598 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:1272 | Toyota | Grand Highlander | 2023 | 2.4L AWD | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:1273 | Toyota | Grand Highlander | 2023 | 2.4L FWD | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:1274 | Toyota | Grand Highlander | 2023 | 2.5L AWD (367 HP) | Mild Hybrid | — | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:1275 | Toyota | Grand Highlander | 2023 | 2.5L FWD (367 HP) | Mild Hybrid | — | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:1414 | Toyota | Mirai | 2021 | 134 KW (174 HP) | Hybrid | — | OEM_GEARBOX_REQUIRED |
| engines_part_016.csv:275 | Volkswagen | Atlas Cross Sport | 2023 | 2.0L TSI (273 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_016.csv:384 | Volkswagen | Caddy | 2020 | TSI (114 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_016.csv:385 | Volkswagen | Caddy | 2020 | TDI (120 HP) | Diesel | — | OEM_GEARBOX_REQUIRED |
| engines_part_016.csv:386 | Volkswagen | Caddy | 2020 | TDI (74 HP) | Diesel | — | OEM_GEARBOX_REQUIRED |
| engines_part_016.csv:1278 | Volkswagen | Passat Variant | 2023 | 2.0L TSI 4MOTION AWD (265 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_016.csv:1279 | Volkswagen | Passat Variant | 2023 | 2.0L TSI FWD (204 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_016.csv:1280 | Volkswagen | Passat Variant | 2023 | 2.0L TDI 4MOTION AWD (193 HP) | Diesel | — | OEM_GEARBOX_REQUIRED |
| engines_part_016.csv:1281 | Volkswagen | Passat Variant | 2023 | 2.0L TDI FWD (122 HP) | Diesel | — | OEM_GEARBOX_REQUIRED |
| engines_part_016.csv:1282 | Volkswagen | Passat Variant | 2023 | 2.0L TDI FWD (150 HP) | Diesel | — | OEM_GEARBOX_REQUIRED |
| engines_part_017.csv:356 | Volvo | P1800 | 1961 | 1.8 | Gasoline | 1782 | OEM_GEARBOX_REQUIRED |
| engines_part_017.csv:978 | Westfield | 2,0 ZETEC SPORT | 2010 | 2.0L | — | 1998 | OEM_GEARBOX_REQUIRED |
| engines_part_017.csv:979 | Westfield | 2.0 ZETEC SPORT | 2009 | 2.0L | — | 1998 | OEM_GEARBOX_REQUIRED |
| engines_part_017.csv:980 | Westfield | CONVERTIBLE | 1987 | 1.8L | — | 1800 | OEM_GEARBOX_REQUIRED |
| engines_part_017.csv:981 | Westfield | CONVERTIBLE | 1987 | 2.0L | — | 2000 | OEM_GEARBOX_REQUIRED |
| engines_part_017.csv:982 | Westfield | CONVERTIBLE | 1987 | 2.0L | — | 1998 | OEM_GEARBOX_REQUIRED |
| engines_part_017.csv:983 | Westfield | CONVERTIBLE | 1987 | 1.6L | — | 1598 | OEM_GEARBOX_REQUIRED |
| engines_part_017.csv:984 | Westfield | N/A | 2011 | 1.6L 141 kW Petrol | Petrol | 1598 | OEM_GEARBOX_REQUIRED |
| engines_part_017.csv:985 | Westfield | Non renseignÃš | 2010 | 1.6L 141 kW Petrol | Petrol | 1598 | OEM_GEARBOX_REQUIRED |
| engines_part_017.csv:986 | Westfield | Non renseignÚ | 2010 | 1.6L Petrol | Petrol | 1598 | OEM_GEARBOX_REQUIRED |
| engines_part_017.csv:987 | Westfield | SE | 1977 | 1.7L | — | 1686 | OEM_GEARBOX_REQUIRED |

## نتيجة الدفعة
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_51=1099
last_examined=engines_part_017.csv:987
next_record=engines_part_017.csv:988
remaining_OTHER_unreviewed_based_on_initial_1162=63

## حدود الاعتماد
بلا سند ناقل OEM جديد أو إضافة روابط ECU/DTC. لا تعديل لملفات المصدر أو main أو stable أو الموقع أو برنامج Windows أو الصور أو مكتبة الأكواد المعتمدة.
