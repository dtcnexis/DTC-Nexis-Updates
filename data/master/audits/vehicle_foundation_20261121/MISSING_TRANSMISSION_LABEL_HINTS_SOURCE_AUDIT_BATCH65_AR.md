# DTC NEXIS — الدفعة 65: إعادة مطابقة 32 حالة ذات تلميح ناقل حركة

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## النطاق
طوبقت 32 حالة موجودة مسبقًا في قائمة المراجعة ذات تلميحات مثل 7AT/8AT/9AT على صفوف ملفات gor3a الأصلية بالماركة والموديل والجيل، مع خلو عمود transmission من تعريف OEM صريح ووجود حالة NOT_APPROVED. وجود تلميح في engine_label لا يشكّل توثيقًا لرمز ناقل معين ضمن سنة/سوق/محرك وECU. لا تُعاد هذه الحالات إلى قائمة OTHER أو EV أو HYBRID، منعًا للعد المزدوج.

## مصدر السجلات وبصمات Git Blob
- engines_part_001.csv: lines 717; blob_sha=8a2e350c18a0f067aee4f6d03d2c5d7be964cffc
- engines_part_002.csv: lines 761; blob_sha=3a281ebfce241e7849e4db09dcaa9e385986274e
- engines_part_003.csv: lines 1558, 1846; blob_sha=3796acc7f93b581a449480f958097be2937788bc
- engines_part_004.csv: lines 317, 1188, 1189, 1190, 1191; blob_sha=a62309aa7556a1ffbc89573c42cdfab1cb27c1f5
- engines_part_006.csv: lines 1276, 1512, 1549; blob_sha=2622eaa2d8a10316d2e7a9561d3182061f51ffce
- engines_part_007.csv: lines 834, 865, 866, 1119, 1166; blob_sha=0399f720f92849388bf3c3e33f92441d42b7416f
- engines_part_008.csv: lines 1383, 1385, 1758, 1827; blob_sha=88dcf7945b863564a06acb1de5f9676d401bba49
- engines_part_010.csv: lines 803; blob_sha=190ce6216c3301de8f289611dad37202cc86180d
- engines_part_012.csv: lines 1620; blob_sha=bbcd1f604d7405c0c79dad7b08120b2b86ef38b2
- engines_part_013.csv: lines 1060; blob_sha=d6fe7f5f1d6d6e695bb73e30c5b94234afb2ae01
- engines_part_014.csv: lines 1033; blob_sha=d16faa05277fc868bb2ed1eb9c890d4275983b77
- engines_part_015.csv: lines 43, 1004, 1005, 1359; blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36
- engines_part_016.csv: lines 274, 1728, 1729; blob_sha=8a5e0799e8cfaaddf2bdeef431f31dce7b582622

| صف المصدر | الماركة | الموديل | سنة المصدر | النص الخام | التلميح | أولوية التحقق | الحالة |
|---|---|---|---|---|---|---|---|
| engines_part_001.csv:717 | Alpine | A110 | 2024 | 1.8L 7AT RWD (345 HP) | 7AT | HIGH_OEM_LEAD | NOT_APPROVED |
| engines_part_002.csv:761 | Audi | SQ5 | 2020 | 3.0L TDI V6 8AT AWD (341 HP) | 8AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_003.csv:1558 | Buick | Enclave | 2021 | 3.6L V6 9AT (310 HP) | 9AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_003.csv:1846 | Cadillac | XT4 | 2023 | 2.0L Turbocharged 9AT FWD (238 HP) | 9AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_004.csv:317 | Chevrolet | Corvette | 1983 | 5.7L V8 5MT RWD (249 HP) | 5MT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_004.csv:1188 | Citroën | CITROEN C4 | 2022 | PureTech 100 Start & Stop 6MT | 6MT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_004.csv:1189 | Citroën | CITROEN C4 | 2022 | PureTech 130 8AT | 8AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_004.csv:1190 | Citroën | CITROEN C4 | 2022 | PureTech 130 Start & Stop 8AT | 8AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_004.csv:1191 | Citroën | CITROEN C4 | 2022 | BlueHDi 130 Start & Stop 8AT | 8AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_006.csv:1276 | Ford | Transit Connect | 2018 | 2.0L GDI 8AT (150 HP) | 8AT | HIGH_OEM_LEAD | NOT_APPROVED |
| engines_part_006.csv:1512 | GMC | Sierra 2500HD | 2019 | 6.6L 10AT (445 HP) | 10AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_006.csv:1549 | GMC | Terrain | 2021 | 1.5L 9AT (170 HP) | 9AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_007.csv:834 | Hyundai | i20 | 2018 | 1.2L 5MT FWD (75 HP) | 5MT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_007.csv:865 | Hyundai | i20 Active | 2018 | 1.2L 5MT FWD (75 HP) | 5MT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_007.csv:866 | Hyundai | i20 Active | 2018 | 1.2L 5MT FWD (84 HP) | 5MT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_007.csv:1119 | Hyundai | Kona | 2021 | 2.0L CVT FWD (147 HP) | TEXT_TERM | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_007.csv:1166 | Hyundai | Mistra | 2014 | 1.8L 6AT (143 HP) | 6AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_008.csv:1383 | Lexus | ES | 2023 | 250 8AT AWD (203 HP) | 8AT | HIGH_OEM_LEAD | NOT_APPROVED |
| engines_part_008.csv:1385 | Lexus | ES | 2023 | 300h e-CVT FWD (215 HP) | TEXT_TERM | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_008.csv:1758 | Lincoln | Zephyr | 2021 | 2.0L 8AT | 8AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_008.csv:1827 | Lotus | Exige | 2021 | 3.5L V6 6MT (420 HP) | 6MT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_010.csv:803 | Mercedes-Benz | MERCEDES BENZ GLE-Class | 2026 | 4MATIC 9AT AWD (537 HP) | 9AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_012.csv:1620 | Peugeot | 408 | 2026 | 1.2L MHEV 6AT FWD (143 HP) | 6AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_013.csv:1060 | Renault | Clio | 2025 | 1.2L TCe 5MT FWD (115 HP) | 5MT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_014.csv:1033 | SEAT | Leon ST | 2020 | 1.4L TSI 6AT FWD (204 HP) | 6AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_015.csv:43 | Subaru | Ascent | 2022 | 2.4L CVT AWD (260 HP) | TEXT_TERM | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_015.csv:1004 | Toyota | Corolla | 2022 | 1.8L CVT FWD (140 HP) | TEXT_TERM | HIGH_OEM_LEAD | NOT_APPROVED |
| engines_part_015.csv:1005 | Toyota | Corolla | 2022 | 2.0L CVT FWD (196 HP) | TEXT_TERM | HIGH_OEM_LEAD | NOT_APPROVED |
| engines_part_015.csv:1359 | Toyota | Land Cruiser / Prado | 2024 | 2.8L MHEV 8AT AWD (204 HP) | 8AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_016.csv:274 | Volkswagen | Atlas Cross Sport | 2026 | 2.0L TSI 4MOTIN 8AT (286 HP) | 8AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_016.csv:1728 | Volkswagen | Tiguan | 2020 | 2.0L TSI 8AT (184 HP) | 8AT | MEDIUM_PENDING_OEM | NOT_APPROVED |
| engines_part_016.csv:1729 | Volkswagen | Tiguan | 2020 | 2.0L TSI 8AT (320 HP) | 8AT | MEDIUM_PENDING_OEM | NOT_APPROVED |

## نتيجة إعادة الفحص
existing_records_examined=32
records_deferred=32
new_imports=0
full_OEM_approvals=0
queue_source_mismatches=0
raw_rows_modified=0
label_hints_queue_total=32
label_hints_remaining_source_review=0
next_workstream=OEM_TRANSMISSION_EVIDENCE_REVIEW

## الحماية
لا تُغيّر أي من البيانات الخام أو main أو stable أو الموقع أو Windows أو الوسائط أو مكتبة DTC المعتمدة؛ موافقات OEM السابقة أو نقصها لا تتغير بمجرد مطابقة المصدر.
