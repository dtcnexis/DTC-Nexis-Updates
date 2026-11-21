# DTC NEXIS — الدفعة 41: Mercedes-Benz / MG / MINI / Morgan / Morris (30 سجلًا)

date=2026-11-21 | REVIEW_ONLY / NOT_OEM_VERIFIED / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/MISSING_TRANSMISSION_MERCEDES_BATCH40_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_sources=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_010.csv;data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_011.csv

## نطاق السجلات
- engines_part_010.csv: Mercedes-Benz GLE 823/825/826/829 (4)، GLS Maybach 866 (1)، GLS 872–875 (4)، Pullman 919–920 و931–932 (4)، VLE 1340–1341 (2)، MG4 1406 (1) = 16.
- engines_part_011.csv: MINI Classic 75–76 (2)، MINI Countryman 165–166 (2)، Morgan Plus Six 714 (1)، Morris 719–727 (9) = 14.
- المجموع 30 صفًا مطابقًا لقائمة OTHER وCSV الخام. الصفوف 824/827/828 بين سجلات GLE ليست ضمن هذه القائمة ولا تُدرج في العدد.

## المراجعات المؤجلة
- Mercedes-Benz GLE 823/829 (2026/2023) 450 4MATIC mild hybrid 2999cc، وGLE 825/826 (2023) 300d/450d mild hybrid diesel 1993/2989cc؛ لا تعيين لناقل مشترك بمجرد وصف 4MATIC.
- Mercedes-Benz GLS Maybach 866 (2023) V8 3982cc مع حقل fuel فارغ؛ يحتاج إثبات نسخة المحرك والسوق. GLS 872–875 (2023) 450/580 بنزين 2999/3982cc مقابل 350d/450d ديزل 2989cc؛ نطاقات مستقلة.
- Mercedes-Benz Pullman 919–920 (2018/2015) V12 5980cc بقوتين 630/530HP؛ Pullman 931–932 (1938) 770 Kompressor 7655cc بصفة special protection في أحد الوصفين؛ لا افتراض ناقل أو دمج تجهيز خاص.
- Mercedes-Benz VLE 1340–1341 (2026) Electric 300 و400 4MATIC؛ لا إسناد ناقل احتراق داخلي.
- MG 4 1406 (2023) Electric 435HP؛ مواصفات وحدة الاختزال تتطلب OEM.
- MINI Classic 75–76 (2024) 156/204HP مع حقل Gasoline وسعة فارغة؛ يلزم إثبات تسمية النسخة والمحرك/الوقود.
- MINI Countryman 165 (2023) JCW ALL4 2.0L/1999cc و312HP ولكن fuel خام Electric؛ تعارض الوقود/محرك الاحتراق مؤشر مراجعة عالي. Countryman 166 (170HP) Mild Hybrid دون سعة، منفصل.
- Morgan Plus Six 714 (2022) 3.0L RWD 335HP؛ لا تحديد رمز ناقل.
- Morris 1/4 TON VAN 719 (1966) 1098cc؛ 10/4 720–722 (1933) 1140/1293/1100cc، و1000 Traveller 723 (1968) 1100cc، 1100 724 (1952) 1098cc، 1300 725–726 (1968) 1275/1300cc، 1300 GT 727 (1970) 1275cc؛ لا توحيد لاختلافات الاسم أو السعة أو السنة.

## نتائج الدفعة
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_41=799
last_examined=engines_part_011.csv:727
next_record=engines_part_011.csv:728 (confirmed queue)
remaining_OTHER_unreviewed_based_on_initial_1162=363

## حماية
- التقرير فحص لقائمة النواقص مقابل المصدر الخام وليس مصدرًا مصنعياً. لا تغيير لـmain أو stable أو البيانات الأصلية أو الموقع أو البرنامج أو الصور أو DTC المعتمدة.
