# DTC NEXIS — الدفعة 48: مراجعة المصدر للناقل المفقود

date=2026-11-21 | REVIEW_ONLY / NOT_OEM_VERIFIED / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv

## التدقيق
تمت مطابقة 30 إدخالًا مع CSV الخام بالموديل والماركة والسنة ووصف المحرك، وكلها ضمن قائمة OTHER، وحقل ناقل الحركة المنظم خالٍ. السعة والوقود من المصدر الخام وليسا مواصفات OEM معتمدة. أي خلافات تحتاج مراجع مصنع لتحديد الجيل والسوق ونظام الدفع والناقل؛ لا دمج أو تعديل للأصول.

## ملفات المصدر
- engines_part_013.csv: lines 799, 800, 801, 802, 803, 804, 805, 806, 807, 984, 985, 1029, 1033, 1061, 1063, 1066, 1073, 1225, 1869, 1870; Git_blob_sha=d6fe7f5f1d6d6e695bb73e30c5b94234afb2ae01
- engines_part_014.csv: lines 123, 148, 176, 178, 180, 181, 182, 183, 184, 185; Git_blob_sha=d16faa05277fc868bb2ed1eb9c890d4275983b77

| المصدر:صف | الماركة | الموديل | السنة | وصف المحرك | الوقود | cc | الحالة |
|---|---|---|---|---|---|---|---|
| engines_part_013.csv:799 | Reliant | SCIMITAR GTE | 1969 | 2.8L | — | 2792 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:800 | Reliant | SCIMITAR GTE | 1969 | 3.0L | — | 3000 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:801 | Reliant | SCIMITAR GTE AUTOMATIC | 1970 | 3.0L | — | 2994 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:802 | Reliant | SCIMITAR GTE AUTOMATIC | 1970 | 3.0L | — | 2996 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:803 | Reliant | SCIMITAR GTE AUTOMATIC | 1970 | 2.8L | — | 2792 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:804 | Reliant | SCIMITAR GTE OVERDRIVE | 1970 | 2.9L | — | 2945 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:805 | Reliant | SCIMITAR GTE OVERDRIVE | 1970 | 3.0L | — | 2994 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:806 | Reliant | SCIMITAR GTE OVERDRIVE | 1970 | 2.8L | — | 2792 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:807 | Reliant | SCIMITAR SABRE 1.4 | 1994 | 1.4L | — | 1396 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:984 | Renault | 5 E-Tech | 2024 | 120 HP | Electric | — | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:985 | Renault | 5 E-Tech | 2024 | 150 HP | Electric | — | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:1029 | Renault | Captur | 2024 | 1.3L TCE FWD (152 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:1033 | Renault | Captur | 2024 | 1.6L E-Tech FWD (147 HP) | Hybrid Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:1061 | Renault | Clio | 2025 | 1.8L FHEV FWD (160 HP) | Hybrid Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:1063 | Renault | Clio | 2023 | TCe 100 | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:1066 | Renault | Clio | 2023 | 1.6L E-Tech (145 HP) | Hybrid Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:1073 | Renault | Clio | 2019 | E-TECH | Hybrid | — | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:1225 | Renault | Espace | 2023 | 1.2L E-TECH (130 HP) | Hybrid Gasoline | 1199 | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:1869 | Renault | Megane E-Tech | 2021 | 160 KW (218 HP) | Electric | — | OEM_GEARBOX_REQUIRED |
| engines_part_013.csv:1870 | Renault | Megane E-Tech | 2021 | 96 KW (130 HP) | Electric | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:123 | Rivian | R1S | 2021 | (835 HP) | Electric | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:148 | Rolls-Royce | La Rose Noire | 2023 | 6.75L V12 AWD (593 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:176 | Rolls-Royce | Spectre | 2022 | 563 HP | Electric | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:178 | Rover | 100 Cabrio | 1994 | 111 FWD (60 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:180 | Rover | 100 Cabrio | 1994 | 114 1.4L FWD (102 HP) | Gasoline | — | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:181 | RUF | BERGMEISTER | 2022 | 3.6L 309 kW Petrol | Petrol | 3600 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:182 | RUF | CTR ANNIVERSARY | 2021 | 3.6L 522 kW Petrol | Petrol | 3600 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:183 | RUF | RT12 R | 2021 | 3.7L 537 kW Petrol | Petrol | 3746 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:184 | RUF | SCR | 2020 | 4.0L 375 kW Petrol | Petrol | 4000 | OEM_GEARBOX_REQUIRED |
| engines_part_014.csv:185 | RUF | SCR | 2020 | 4.0L 382 kW Petrol | Petrol | 4000 | OEM_GEARBOX_REQUIRED |

## التقرير
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_48=1009
last_examined=engines_part_014.csv:185
next_record=engines_part_014.csv:186
remaining_OTHER_unreviewed_based_on_initial_1162=153

## الحماية
بلا اعتماد OEM أو ECU/DTC؛ لا تعديل للملفات الأصلية أو main أو stable أو الموقع أو برنامج Windows أو الوسائط أو مكتبة الأكواد.
