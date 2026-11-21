# DTC NEXIS — الدفعة 40: Mercedes-Benz A/B/C/CLA/EQE/EQS/GLA/GLE (30 حالة)

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/MISSING_TRANSMISSION_LIGIER_MERCEDES_BATCH39_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_sources=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_009.csv;data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_010.csv

## نطاق مطابق لقائمة OTHER
- part_009: Mercedes-Benz A-Klasse Saloon 825–829 (5)، B-Klasse 831–837 (7)، C-Class 919/920/922 (3)، CLA Klasse 1446 (1) = 16.
- part_010: EQE 563، EQS SUV Maybach 580، EQV 582 (3)، GLA 708–711 و714–715 (6)، GLE 804/805/808 و821/822 (5) = 14.
- العدد 30. طوبقت السطور مع المصدر الخام. صفوف 830/921/581/712–713/806–807 خارج قائمة OTHER المحددة؛ بعض هذه الصفوف المجاورة تعرض ناقلًا في الخام، ولا يجوز نسخه تلقائيًا إلى الحالات المفحوصة.

## الملاحظات الفنية
- A-Klasse Saloon 2022 (825–829): بنزين 1991cc 220/250 4MATIC، ديزل 1950cc 180d/200d/220d؛ لا تعيين لأي ناقل OEM بمجرد اسم التكوين.
- B-Klasse 2022 (831–837): بنزين 1332/1991cc وديزل 1950cc، 180/200/220/250؛ يحتفظ اختلاف 4MATIC عن الإصدارات الأخرى، ولا يُشتق ناقل A-Klasse من المحرك المشترك.
- C-Class 2018 (919–920): C200 1497cc في AWD مقابل RWD؛ الصف 922 C220d 1951cc. وجود 9G-TRONIC في C400 المجاور 921 لا يثبت انطباقه على C200/C220d.
- CLA 250e PHEV FWD 2023 (1446): 1332cc، ناقل النظام الهجين غير مثبت.
- EQE 2021 (563): Electric 215kW، EQS SUV Maybach 2023 (580) Electric AWD/658HP، EQV 2019 (582) Electric/150kW؛ لا تعبئة ناقل تقليدي دون مواصفات مجموعة الدفع المختصة.
- GLA 2023 (708–711): 180d و200d و220d ديزل 1950cc، مع FWD أو 4MATIC AWD؛ حالتا 714–715 بنزين Mild Hybrid بسعة 1991cc مع AWD، لا توحيد لعلب ICE/Hybrid.
- GLE 2023 (804/805/808): Mild Hybrid Diesel 1993/2989cc وميلد هايبرد بنزين 2999cc؛ GLE 2026 (821–822) Mild Hybrid Diesel 2989cc؛ اختلاف سنة الجيل والسوق والوقود والقدرة يتطلب مصدرًا محددًا للناقل.
- جميع السجلات موسومة NOT_OEM_VERIFIED؛ ولا تُعد هذه المراجعة اعتمادًا لوحدة ECU أو DTC.

## نتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_40=769
last_examined=engines_part_010.csv:822
next_record=engines_part_010.csv:823 (confirmed queue)
remaining_OTHER_unreviewed_based_on_initial_1162=393

## الحماية
- تقرير تدقيق فقط؛ لا تغيير للخام أو main أو stable أو الموقع أو برنامج Windows أو الصور أو المكتبة المعتمدة.
