# DTC NEXIS — الدفعة 36: Geo / Ginetta / GMC / Holden / Honda (30 حالة)

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/MISSING_TRANSMISSION_FAW_FIAT_FORD_GEO_BATCH35_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_sources=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_006.csv;data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_007.csv

## نطاق التدقيق وفق ترتيب قائمة OTHER
- engines_part_006.csv: Geo 1379–1390 (12)، Ginetta 1391–1393 (3)، GMC 1445 (1)، Holden 1807–1813 (7)، Honda 1915 و1918 (2) = 25.
- engines_part_007.csv: Honda Civic CRX 295–297 (3)، HR-V 394 (1)، Jazz / Fit 424 (1) = 5.
- المجموع 30 صفًا. جميعها موجودة في قائمة النواقص، وقد قورنت بالسطور الخام. لا تُحسب الصفوف المجاورة غير الموجودة في قائمة OTHER ضمن الدفعة.

## الفروق والتحذيرات المصدرية
- Geo Prizm 1379: Premium Gasoline 1.6L / 1600cc، منفصل عن Prizm Regular Gasoline 1377 السابق؛ لا تعميم لنوع الوقود أو الناقل.
- Geo Spectrum/Storm 1380–1382: 1.5L/1.6L/1.8L بنزين، موديلات مختلفة تحت Geo.
- Geo Tracker 1383–1390: 1.6L/1600cc في تنويعات 2WD/4WD/4x4، Convertible/Hardtop/Van وسنوات 1989–1996؛ الهيكل والدفع لا يثبتان علبة تروس معينة.
- Ginetta 1391–1393: اسم الموديل الخام «unknown»، 2011، سعات 1998/2000/3700cc؛ لا يمكن اعتماد انطباق الناقل دون حل هوية الموديل.
- GMC Hummer EV 1445: الوصف «Three-motor e4WD (1000 HP)»، لكن حقل fuel الخام Gasoline؛ تعارض مصدر مرتفع الأولوية بين توصيف EV ونوع الوقود، ولا نصلحه بالتخمين.
- Holden HJ 1807–1810: سنوات 1974–1976 وسعات 2835/3310/4146/5047cc؛ اختلاف الأسطوانات 6/8 كما ورد في الأصل ولا يثبت صندوقًا محددًا.
- Holden HZ 1811–1813: سنوات 1977–1980 وسعات 3310/4146/5047cc؛ استقلال نطاق الجيل مهم رغم تقارب محركات HJ.
- Honda Accord 1915: Hybrid Gasoline 2.0L Atkinson FWD (204 HP)، لكن عمود drivetrain الخام All Wheel Drive؛ تعارض FWD/AWD لا يجوز معالجته دون مصدر.
- Honda Accord 1918: Hybrid Gasoline 2.0L i-VTEC FWD (212 HP)، بلا قيمة ناقل؛ لا نسخ ناقل CVT أو 10AT من Accord المجاورة 1916–1917.
- Honda Civic CRX 295–297: 1983–1987، 1.3L (71 HP)، 1.5i AF (101 HP)، 1.6i AS (125 HP)؛ لا استنتاج لناقل واحد لجميع المحركات.
- Honda HR-V 394: 2021–2022، 1.5L i-VTEC (132 HP) Hybrid Gasoline، حقل drivetrain All Wheel Drive؛ يحتاج تحقق OEM.
- Honda Jazz / Fit 424: Hybrid 2020، 1496cc و98 HP، AWD؛ تُحفظ مستقلة عن صف FWD 425 التالي.

## الحصيلة
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_36=649
last_examined=engines_part_007.csv:424
next_record=engines_part_007.csv:425 (confirmed queue)
remaining_OTHER_unreviewed_based_on_initial_1162=513

## الضوابط
- المراجعة إثبات مطابقة للأصل واستخراج تعارضات، وليست اعتماد OEM أو إضافة ECU/DTC.
- لا تعديل لملفات CSV أو main أو stable أو الموقع أو Windows أو الصور أو مكتبة DTC المعتمدة.
