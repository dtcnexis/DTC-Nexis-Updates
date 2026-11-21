# DTC NEXIS — الدفعة 32: Daimler / De Tomaso / Deepal / DFSK (30 حالة)

date=2026-11-21 | REVIEW_ONLY / NOT_OEM_VERIFIED / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/MISSING_TRANSMISSION_DAIMLER_BATCH31_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_source=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_005.csv

## نطاق التحقق
- Daimler: الصف 394 (1).
- De Tomaso: الصفوف 405–422 (18).
- Deepal: الصف 423 (1).
- DFSK: الصفوف 424–433 (10).
- الإجمالي 30 إدخالًا متطابق الهوية مع قائمة OTHER وصفوف CSV الخام؛ لا تشمل هذه الدفعة الصفوف 395–404 غير الموجودة في قائمة OTHER. حقل ناقل الحركة غير موثق مصنعيًا لجميع الصفوف.

## ملاحظات المراجعة
- 394: Daimler V8  250 / 1963 / 3442cc، اختلاف كبير عن السعات 2500/2504/2548cc في الصفوف السابقة ذات الاسم نفسه؛ مراجعة هوية النسخة والسعة أولوية، ولا تصحيح دون مرجع.
- 405–408: De Tomaso Deauville 1975، 5764/5751/5763/5818cc؛ لا دمج للسعات القريبة تحت وصف 5.8L.
- 409–410: De Tomaso Longchamp 2+2 1975، 5763/5689cc، وتسمية 5.8L مقابل 5.7L؛ يلزم تحديد المحرك والناقل حسب الإصدار.
- 411–419: De Tomaso Pantera 1971، 5751/5763/5739/5689/5700/5766/5796/6849/5800cc؛ صف 418 بسعة 6849cc مرشح مراجعة مرتفع الأولوية، و«Niet geregistreerd» ليس نوع هيكل مثبتًا.
- 420–422: Pantera GTS 1972، 5763/5689/5766cc؛ لا تعميم ناقل Pantera على GTS.
- 423: Deepal S05 سنة بداية مصدرية 2026، 1497cc، وصف الهيكل stationwagen؛ يحتاج تحقق تطابق منظومة الدفع والسوق قبل أي اعتماد.
- 424: DFSK 0901 سنة 2020، 1499cc بنزين؛ اسم الطراز الرقمي يحتاج توثيقًا.
- 425–431: DFSK 580 سنة 2018، كلها 1499cc ولكن أوصاف القدرة والوقود مختلفة (Petrol/Lpg/Diesel/Ng-biomethane/Unknown، 69/106/107 kW). لا توحيد الهوية رغم تطابق السعة؛ الحالات المتعارضة خاصة بنوع الوقود تُراجع بمصدر مصنعي.
- 432: DFSK 580 LPG 2021، 1499cc؛ تظل منفصلة عن 580 القياسية.
- 433: DFSK AT-IX5 SFG15TA-LVZ سنة 2020، 1499cc؛ لا تُستنتج وحدة ناقل من رمز وصف المحرك.

## النتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_32=529
last_examined=engines_part_005.csv:433
next_record=engines_part_005.csv:434 (confirmed queue)
remaining_OTHER_unreviewed_based_on_initial_1162=633

## الحماية
- تدقيق قيم CSV ومؤشرات قائمة المراجعة فقط؛ بلا سند OEM جديد أو روابط ECU/DTC معتمدة.
- لم تتغير ملفات المصدر أو الصور أو main أو stable أو بيانات الموقع أو برنامج Windows.
