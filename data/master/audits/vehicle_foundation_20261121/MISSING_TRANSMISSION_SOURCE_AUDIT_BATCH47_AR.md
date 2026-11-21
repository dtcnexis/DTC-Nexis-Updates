# DTC NEXIS — الدفعة 47: تدقيق ناقل الحركة المفقود (30 سجلًا)

date=2026-11-21 | REVIEW_ONLY / NOT_OEM_VERIFIED / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv

## طريقة التدقيق
فُحصت 30 حالة وفق ترتيب القائمة المعتمدة، مع استرجاع صف كل حالة من ملف CSV الخام المطابق رقمياً. قورنت الماركة والموديل وسنة البداية ووصف المحرك وحالة قائمة المراجعة، وتأكد أن عمود ناقل الحركة المنظم خالٍ من تعريف مصنع. لا يُعتمد أي كود ناقل أو ECU/DTC من هذه المراجعة؛ وتبقى اختلافات السعة والوقود والنسخة محفوظة حرفياً.

## أصول الملفات وبصمات Git Blob
- engines_part_012.csv: 1980, 1981, 1982, 1983, 1984; raw_source_sha=bbcd1f604d7405c0c79dad7b08120b2b86ef38b2
- engines_part_013.csv: 2, 3, 4, 5, 105, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798; raw_source_sha=d6fe7f5f1d6d6e695bb73e30c5b94234afb2ae01

## كشف الحالات (قيم المصدر، ليست بيانات OEM معتمدة)
| صف المصدر | الماركة | الموديل | سنة المصدر | وصف المحرك الخام | الوقود | cc | النتيجة |
|---|---|---|---:|---|---|---:|---|
| engines_part_012.csv:1980 | Polaris | SPORTSMAN 850 E | 2009 | 0.8L | — | 850 | OEM_GEARBOX_REQUIRED |
| engines_part_012.csv:1981 | Polaris | SPORTSMAN ACE | 2014 | 0.3L | — | 325 | OEM_GEARBOX_REQUIRED |
| engines_part_012.csv:1982 | Polaris | SPORTSMAN FOREST 500 | 2011 | 0.5L | — | 498 | OEM_GEARBOX_REQUIRED |
| engines_part_012.csv:1983 | Polaris | SPORTSMAN FOREST 570 | 2013 | 0.6L | — | 567 | OEM_GEARBOX_REQUIRED |
| engines_part_012.csv:1984 | Polaris | SPORTSMAN FOREST 800 | 2012 | 0.8L | — | 760 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:2 | Polaris | SPORTSMAN FOREST 850 | 2011 | 0.8L | — | 850 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:3 | Polaris | SPORTSMAN XP 1000 S | 2022 | 1.0L | — | 952 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:4 | Polaris | TRAIL BOSS 330 E | 2005 | 0.3L | — | 329 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:5 | Polestar | 1 | 2019 | 2.0L (600 HP) | Hybrid | — | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:105 | Pontiac | GTO | 1967 | 6.4 V8 | Gasoline | 6362 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:779 | Reliant | CLI | 2011 | 1.1L 76 kW Petrol | Petrol | 1149 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:780 | Reliant | KITTEN ESTATE | 1977 | 0.8L | — | 848 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:781 | Reliant | MEGANE | 2011 | 1.9L 96 kW Diesel | Diesel | 1870 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:782 | Reliant | REGAL 3/30 | 1969 | 0.6L | — | 598 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:783 | Reliant | REGAL 3/30 | 1969 | 0.7L | — | 700 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:784 | Reliant | REGAL 3/30 | 1969 | 0.7L | — | 694 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:785 | Reliant | RIALTO GLS | 1983 | 0.8L | — | 848 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:786 | Reliant | RIALTO LX | 1995 | 0.8L | — | 848 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:787 | Reliant | ROBIN | 1974 | 0.8L | — | 848 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:788 | Reliant | ROBIN | 1974 | 0.8L | — | 750 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:789 | Reliant | ROBIN | 1974 | 0.7L | — | 749 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:790 | Reliant | ROBIN 850 | 1976 | 0.8L | — | 848 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:791 | Reliant | SCIMITAR | 1966 | 3.0L | — | 3000 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:792 | Reliant | SCIMITAR | 1966 | 3.0L | — | 2994 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:793 | Reliant | SCIMITAR | 1966 | 2.9L | — | 2945 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:794 | Reliant | SCIMITAR | 1966 | 2.6L | — | 2553 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:795 | Reliant | SCIMITAR | 1966 | 1.4L | — | 1368 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:796 | Reliant | SCIMITAR | 1966 | 1.4L | — | 1396 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:797 | Reliant | SCIMITAR 1800 TI | 1987 | 1.8L | — | 1809 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:798 | Reliant | SCIMITAR GTE | 1969 | 3.0L | — | 2994 | OEM_GEARBOX_REQUIRED |

## الحصيلة
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_47=979
last_examined=engines_part_013.csv:798
next_record=engines_part_013.csv:799
remaining_OTHER_unreviewed_based_on_initial_1162=183

## الثقة والحماية
تدل النتيجة على تطابق الصف مع المصدر فقط. أي قيمة غير منطقية في المصدر تظل مؤجلة للتحقق من كتالوج OEM مع تحديد الموديل والسوق والسنة والمحرك والناقل. لا تعديل على CSV الخام أو main أو stable أو الموقع أو برنامج Windows أو الصور أو المكتبة المعتمدة.
