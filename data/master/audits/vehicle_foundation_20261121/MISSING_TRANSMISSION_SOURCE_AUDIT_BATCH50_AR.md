# DTC NEXIS — الدفعة 50: مراجعة المصدر للناقل المفقود

date=2026-11-21 | REVIEW_ONLY / NOT_OEM_VERIFIED / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv

## التدقيق
تمت مطابقة 30 إدخالًا مع CSV الخام بالموديل والماركة والسنة ووصف المحرك، وكلها ضمن قائمة OTHER، وحقل ناقل الحركة المنظم خالٍ. السعة والوقود من المصدر الخام وليسا مواصفات OEM معتمدة. أي خلافات تحتاج مراجع مصنع لتحديد الجيل والسوق ونظام الدفع والناقل؛ لا دمج أو تعديل للأصول.

## ملفات المصدر
- engines_part_015.csv: lines 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 634, 635, 636, 637, 638; Git_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36

| المصدر:صف | الماركة | الموديل | السنة | وصف المحرك | الوقود | cc | الحالة |
|---|---|---|---|---|---|---|---|
| engines_part_015.csv:569 | SWM | GRAN MILANO | 2016 | 0.4L | — | 445 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:570 | SWM | RS300R | 2016 | 0.3L | — | 298 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:571 | SWM | RS500R | 2016 | 0.5L | — | 501 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:572 | SWM | RS650R | 2015 | 0.6L | — | 600 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:573 | SWM | SILVER VASE | 2016 | 0.4L | — | 445 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:574 | SWM | SM650 | 2015 | 0.6L | — | 600 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:575 | SWM | SUPERDUAL T | 2018 | 0.6L | — | 600 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:576 | SWM | URBAN 525 | 2026 | 0.5L | — | 494 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:577 | Talbot | 1100 FOURGONNETTE | 1981 | 1.3L | — | 1299 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:578 | Talbot | HORIZON | 1981 | 1.4L | — | 1400 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:579 | Talbot | HORIZON | 1981 | 1.4L | — | 1442 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:580 | Talbot | HORIZON | 1981 | 1.1L | — | 1100 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:581 | Talbot | HORIZON | 1981 | 1.4L | — | 1424 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:582 | Talbot | HORIZON | 1981 | 1.5L | — | 1500 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:583 | Talbot | HORIZON 1.1 LS | 1981 | 1.1L | — | 1118 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:584 | Talbot | SAMBA | 1983 | 1.4L | — | 1400 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:585 | Talbot | SAMBA | 1983 | 1.0L | — | 954 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:586 | Talbot | SAMBA | 1983 | 1.4L | — | 1351 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:587 | Talbot | SAMBA CABRIOLET | 1982 | 1.4L | — | 1351 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:588 | Talbot | SAMBA CABRIOLET | 1982 | 1.4L | — | 1360 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:589 | Talbot | SAMBA RALLYE | 1984 | 1.2L | — | 1219 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:590 | Talbot | SOLARA 1.6 GLS | 1981 | 1.6L | — | 1592 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:591 | Talbot | SOLARA 1.6 SX | 1980 | 1.6L | — | 1577 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:592 | Talbot | SOLARA 1.6 SX | 1980 | 1.6L | — | 1592 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:593 | Talbot | TAGORA 2.2 GLS | 1981 | 2.2L | — | 2155 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:634 | Tatra | 2-603 | 1969 | 2.5L | — | 2472 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:635 | Tatra | 603 | 1959 | 2.5L | — | 2472 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:636 | Tatra | 8P6R33 | 2019 | 12.9L | — | 12902 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:637 | Tatra | 8P6R33 | 2019 | 10.8L | — | 10837 | OEM_GEARBOX_REQUIRED |
| engines_part_015.csv:638 | Tatra | 8P6R43 | 2019 | 10.8L | — | 10837 | OEM_GEARBOX_REQUIRED |

## التقرير
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_50=1069
last_examined=engines_part_015.csv:638
next_record=engines_part_015.csv:639
remaining_OTHER_unreviewed_based_on_initial_1162=93

## الحماية
بلا اعتماد OEM أو ECU/DTC؛ لا تعديل للملفات الأصلية أو main أو stable أو الموقع أو برنامج Windows أو الوسائط أو مكتبة الأكواد.
