# DTC NEXIS — الدفعة 55: فحص شريحة HYBRID ذات ناقل حركة مفقود (28 حالة)

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_hybrid_batch01.csv

## المنهج
فُحصت جميع إدخالات HYBRID_TEXT_ONLY وعددها 28 مقابل السطر الأصلي من ملفات gor3a، بالموديل والشركة والسنة ووصف المحرك وحقل transmission الخالي. هذه مجموعة تصنيف لغوي وليست إثباتًا فنيًا أن المنظومة Hybrid معتمدة من OEM؛ يجب توثيق نوع MHEV/PHEV/HEV وأي ناقل أو transaxle وفق نسخة السيارة والسوق قبل ترقية الحالة.

## ملفات المصدر
- engines_part_002.csv: lines 61, 89, 90, 91; Git_blob_sha=3a281ebfce241e7849e4db09dcaa9e385986274e
- engines_part_004.csv: lines 1793; Git_blob_sha=a62309aa7556a1ffbc89573c42cdfab1cb27c1f5
- engines_part_009.csv: lines 369, 370, 371, 682, 830; Git_blob_sha=40e1c3019328b6375e0b367759ad6836d9af61bb
- engines_part_010.csv: lines 712, 713, 716, 806, 807, 824, 827, 828; Git_blob_sha=190ce6216c3301de8f289611dad37202cc86180d
- engines_part_011.csv: lines 391; Git_blob_sha=b8b395630356ba2157957abdc425847ff6218774
- engines_part_012.csv: lines 194, 1621; Git_blob_sha=bbcd1f604d7405c0c79dad7b08120b2b86ef38b2
- engines_part_013.csv: lines 1031; Git_blob_sha=d6fe7f5f1d6d6e695bb73e30c5b94234afb2ae01
- engines_part_014.csv: lines 44; Git_blob_sha=d16faa05277fc868bb2ed1eb9c890d4275983b77
- engines_part_015.csv: lines 449, 1224, 1225; Git_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36
- engines_part_016.csv: lines 1285; Git_blob_sha=8a5e0799e8cfaaddf2bdeef431f31dce7b582622
- engines_part_017.csv: lines 573; Git_blob_sha=2e7d952d6b67894720adf67613a819b92cdc48cf

| المصدر:صف | الماركة | الموديل | السنة | تسمية المحرك الخام | الوقود الخام | cc | القرار |
|---|---|---|---|---|---|---|---|
| engines_part_002.csv:61 | Audi | A6 allroad | 2026 | 2.0L TFSI PHEV quattro (367 HP) | Plug-in Hybrid | — | REVIEW |
| engines_part_002.csv:89 | Audi | A6 Avant | 2025 | 2.0L TFSI MHEV FWD (204 HP) | Mild Hybrid | 1968 | REVIEW |
| engines_part_002.csv:90 | Audi | A6 Avant | 2025 | 2.0L TFSI MHEV quattro AWD (204 HP) | Mild Hybrid | 1968 | REVIEW |
| engines_part_002.csv:91 | Audi | A6 Avant | 2025 | 3.0L TFSI MHEV AWD (367 HP) | Mild Hybrid | 2995 | REVIEW |
| engines_part_004.csv:1793 | Cupra | Leon | 2020 | 1.4L TSI PHEV FWD (245 HP) | Hybrid | 1395 | REVIEW |
| engines_part_009.csv:369 | Mazda | CX-70 | 2024 | 2.5L PHEV (327 HP0 | Plug-in Hybrid | — | REVIEW |
| engines_part_009.csv:370 | Mazda | CX-70 | 2024 | 3.3L MHEV (284 HP) | Mild Hybrid | — | REVIEW |
| engines_part_009.csv:371 | Mazda | CX-70 | 2024 | 3.3L MHEV (345 HP) | Mild Hybrid | — | REVIEW |
| engines_part_009.csv:682 | Mercedes-Benz | MERCEDES BENZ A-Klasse | 2022 | 250 e PHEV (218 HP) | Plug-in Hybrid | 1332 | REVIEW |
| engines_part_009.csv:830 | Mercedes-Benz | MERCEDES BENZ A-Klasse Saloon | 2022 | 250e PHEV (218 HP) | Plug-in Hybrid | 1332 | REVIEW |
| engines_part_010.csv:712 | Mercedes-Benz | MERCEDES BENZ GLA | 2023 | 180 MHEV FWD (136 HP) | Mild Hybrid | 1332 | REVIEW |
| engines_part_010.csv:713 | Mercedes-Benz | MERCEDES BENZ GLA | 2023 | 200 MHEV FWD (163 HP) | Mild Hybrid | 1332 | REVIEW |
| engines_part_010.csv:716 | Mercedes-Benz | MERCEDES BENZ GLA | 2023 | 250e PHEV (218 HP) | Plug-in Hybrid | 1332 | REVIEW |
| engines_part_010.csv:806 | Mercedes-Benz | MERCEDES BENZ GLE-Class | 2023 | 350 e PHEV 4MATIC AWD (245 HP) | Plug-in Hybrid | 1993 | REVIEW |
| engines_part_010.csv:807 | Mercedes-Benz | MERCEDES BENZ GLE-Class | 2023 | 400 e PHEV 4MATIC AWD (280 HP) | Plug-in Hybrid | 1999 | REVIEW |
| engines_part_010.csv:824 | Mercedes-Benz | MERCEDES BENZ GLE-Class | 2026 | 450e PHEV 4MATIC AWD (326 HP) | Plug-in Hybrid | 2999 | REVIEW |
| engines_part_010.csv:827 | Mercedes-Benz | MERCEDES BENZ GLE-Class | 2023 | 350 e PHEV 4MATIC AWD (245 HP) | Plug-in Hybrid | 1993 | REVIEW |
| engines_part_010.csv:828 | Mercedes-Benz | MERCEDES BENZ GLE-Class | 2023 | 400 e PHEV 4MATIC AWD (280 HP) | Plug-in Hybrid | 1999 | REVIEW |
| engines_part_011.csv:391 | Mitsubishi | Colt | 2023 | 1.6L Hybrid FWD | Hybrid Gasoline | — | REVIEW |
| engines_part_012.csv:194 | Opel | Frontera | 2024 | 1.2L Turbo Hybrid (136 HP) | Hybrid Gasoline | — | REVIEW |
| engines_part_012.csv:1621 | Peugeot | 408 | 2026 | 1.6L PHEV (237 HP) | Plug-in Hybrid | — | REVIEW |
| engines_part_013.csv:1031 | Renault | Captur | 2024 | 1.3L TCE MHEV FWD (162 HP) | Mild Hybrid | — | REVIEW |
| engines_part_014.csv:44 | Renault | Symbioz | 2024 | E-Tech hybrid 145 | Hybrid Gasoline | — | REVIEW |
| engines_part_015.csv:449 | Suzuki | Swift | 2023 | 1.2L MHEV | Mild Hybrid | — | REVIEW |
| engines_part_015.csv:1224 | Toyota | Crown | 2025 | 2.5L HEV | Hybrid Gasoline | — | REVIEW |
| engines_part_015.csv:1225 | Toyota | Crown | 2025 | 2.5L PHEV | Plug-in Hybrid | — | REVIEW |
| engines_part_016.csv:1285 | Volkswagen | Passat Variant | 2023 | 1.5L eTSI MHEV 48V (150 HP) | Mild Hybrid | — | REVIEW |
| engines_part_017.csv:573 | Volvo | S90 | 2025 | 2.0L MHEV FWD (250 HP) | Mild Hybrid | — | REVIEW |

## النتائج
existing_records_examined=28
records_deferred=28
new_imports=0
queue_source_mismatches=0
full_OEM_approvals=0
raw_rows_modified=0
HYBRID_queue_total=28
HYBRID_queue_remaining_source_review=0
next_workstream=EV_TEXT_ONLY_247_CASES

## القيود
لا تعديل للخام أو main أو stable أو الموقع أو Windows أو الصور أو الأكواد المعتمدة. هذه مراجعة بيانات المصدر لا إصدار شهادة OEM.
