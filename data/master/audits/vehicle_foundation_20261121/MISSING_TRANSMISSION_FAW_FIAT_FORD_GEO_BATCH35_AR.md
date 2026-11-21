# DTC NEXIS — الدفعة 35: FAW / Fiat / Fisker / Ford / Genesis / Geo (30 حالة)

date=2026-11-21 | REVIEW_ONLY / NOT_OEM_VERIFIED / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/MISSING_TRANSMISSION_DFSK_EMC_FAW_BATCH34_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_sources=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_005.csv;data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_006.csv

## نطاق قائمة OTHER
- part_005: FAW 887 (1)؛ Fiat 1128،1195،1301–1302،1665–1667 (7)؛ Fisker 1732 (1): 9.
- part_006: Ford 1052–1055،1083–1084،1208–1209،1238،1248،1250،1252 (12)؛ Genesis 1369–1370 (2)؛ Geo 1372–1378 (7): 21.
- المجموع 30. طوبقت المعرّفات مع سطور المصدر الخام؛ الصفان 1251 (Ford Tourneo بوصف 6AT) و1371 (Genesis GV90) خارج قائمة OTHER المعنية، ولم يُحتسبا.

## ملاحظات مؤجلة
- FAW Bestune T77 Pro Premium 2021 (887): 1498cc /118 kW Petrol؛ مختلف الوقود عن الحالة 886 السابقة.
- Fiat 500 2020 (1128) Electric 42 KW و500e 2013–2020 (1195) Electric 83 kW؛ ليستا نفس الموديل/النطاق، ولا تُملأ حقول ناقل تقليدي افتراضيًا.
- Fiat Campagnola 1974–1979 (1301) 1995cc مقابل 1955–1968 (1302) 1901cc؛ الجيل والسنة والسعة فروق معتبرة.
- Fiat Tipo Cross 2020 (1665–1667): 1.0L GSE T3 100HP Petrol مقابل 1.6L MultiJet Diesel 130/95HP؛ تطبيقات منفصلة.
- Fisker Ocean 2021 (1732): Single Motor FWD /275HP Electric؛ نوع وحدة الاختزال المصنعية مجهول.
- Ford Mustang Mach-E (1052–1055): مدخلات 2020/2021 كهربائية، صيغ 358 Kw و98.8 Kw داخل وصف المحرك تحتاج مراجعة وحدة القياس وما إذا كانت قدرة أو سعة بطارية؛ لا اعتماد ناقل كهربائي.
- Ford Ranger Double Cab 2021 (1083–1084): محركا 2.0 Bi-Turbo Diesel و3.0 V6 Diesel؛ مجهول كود الناقل الخاص بكل تطبيق.
- Ford Super Duty 2021 (1208–1209): 7.3 V8 بنزين / 6.7 V8 ديزل؛ لا دمج للنسختين.
- Ford Thunderbird (1238/1248): موديل 1983–1988 بمحرك 3797cc مقابل 1972–1976 بمحرك 7538cc؛ ناقل كل نطاق مستقل.
- Ford Tourneo 2018–2023 (1250/1252): 2.0L Gasoline و1.5L EcoBlue Diesel؛ لا نقل ناقل 6AT من الصف المجاور 1251 دون سند.
- Genesis GV80 2023 (1369–1370): وصف 2.5L 300HP و3.5L 375HP، وعدد أسطوانات 4 في الصفين حسب المصدر؛ يستلزم التحقق من محرك 3.5 ونطاقه قبل الاعتماد.
- Geo Metro/Metro LSI/Convertible/XFI 1989–1990 (1372–1376): 1.0/1.3L، 3/4 أسطوانات حسب المصدر؛ لا تعميم حسب الاسم.
- Geo Prizm 1989 (1377–1378): 1.6/1.8L، اختلاف محرك رغم الموديل نفسه.

## نتيجة التدقيق
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_35=619
last_examined=engines_part_006.csv:1378
next_record=engines_part_006.csv:1379 (confirmed queue)
remaining_OTHER_unreviewed_based_on_initial_1162=543

## الضوابط
- حفظ حالات عدم اليقين فقط؛ لا تعديل لـmain أو stable أو الأصول أو الموقع أو البرنامج أو الوسائط أو مكتبة DTC.
