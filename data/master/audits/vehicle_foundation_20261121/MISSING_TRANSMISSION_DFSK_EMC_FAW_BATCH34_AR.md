# DTC NEXIS — الدفعة 34: DFSK / EMC / FAW (30 حالة)

date=2026-11-21 | REVIEW_ONLY / NOT_OEM_VERIFIED / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/MISSING_TRANSMISSION_DFSK_BATCH33_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_source=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_005.csv

## نطاق التدقيق
- DFSK: الصفوف 464–484 (21)، 489 (1)، 495–498 (4): 26 حالة.
- EMC: الصفوف 883–884 (حالتان).
- FAW: الصفوف 885–886 (حالتان).
- المجموع 30 من قائمة OTHER بعد تدقيق السجلات الخام. الصفوف 485–488 و490–494 ليست ضمن هذا النطاق ولو ظهرت في CSV؛ لا تعدّ سجلات ناقل مفقود في هذه الدفعة تلقائيًا.

## اختلافات مؤجلة
- 464–466: DFSK FENGON500 2021، 1499cc، LPG/Petrol بقدرة 78/85 kW؛ كل وصف محفوظ ولا يعين تلقائيًا رمز ناقل.
- 467–473: GLORY 580/IS5/IX5 سنة 2020، 1499cc، 101/107 kW، Gnl/Lpg/Ng-biomethane/Petrol؛ بعض هذه التسميات والوقود تتطلب تحقق OEM، ولا يُستبدل اسم IS5 باسم IX5 دون دليل.
- 474–479: DFSK K01/K01H 2011/2014، 1310/1012/1240/1200cc؛ يلزم تحقق هوية المحركات وسنواتها وناقلاتها لكل شاحنة.
- 480: مصدر DFSK KUGA 2020، 1995cc Diesel؛ التباس محتمل في نسبة اسم KUGA إلى الشركة يستلزم سندًا، ولا يعاد تصنيفه تلقائيًا تحت Ford.
- 481: MINI TRUCK 2012، 1310cc، «Niet geregistreerd» لا يثبت نوع الهيكل.
- 482–484: MOTOR CO LTD 2020، 1499cc، Petrol/Lpg 101/107kW؛ هذه صيغة عامة/اسم شركة غير كافٍ لتحديد موديل صالح للربط.
- 489: DFSK SERES 3 2020، وصف «55 kW Petrol» دون سعة محرك؛ اختلافه عن صفوف SERES الكهربائية المجاورة مؤشر تحقق أعلى الأولوية، مع عدم تحويله تلقائيًا.
- 495–498: DFSK V22/V25/V27/V27 4X4، 2012–2014، 1310cc؛ تسميات الدفع والهيكل لا تثبت علبة محددة.
- 883–884: EMC WAVE 3 GPL 2022، 1498/1499cc، 108/83 kW LPG؛ فرق القدرة والسعة محفوظ.
- 885–886: FAW Bestune T77 Pro / Premium 2021، 1498cc، 118kW Petrol مقابل 117kW LPG؛ يلزم تحديد نطاق التطبيق والناقل من مرجع مؤهل.

## الحصيلة
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_34=589
last_examined=engines_part_005.csv:886
next_record=engines_part_005.csv:887 (confirmed queue)
remaining_OTHER_unreviewed_based_on_initial_1162=573

## حدود التقرير
- تدقيق مطابقات المصدر لا يعني تحققًا فنيًا OEM ولا يضيف أي علاقة ECU/DTC.
- البيانات الخام وmain وstable وملفات الموقع والبرنامج والوسائط والمكتبة المعتمدة لم تتغير.
