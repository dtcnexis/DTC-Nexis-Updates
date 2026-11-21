# DTC NEXIS — الدفعة 33: DFSK / Fengon (434–463)

date=2026-11-21 | REVIEW_ONLY / NOT_OEM_VERIFIED / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/MISSING_TRANSMISSION_DAIMLER_DETOMASO_DFSK_BATCH32_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_source=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_005.csv

## مطابقة المصدر
- فُحصت صفوف DFSK الثلاثون المتتابعة 434–463، وجميعها ضمن قائمة OTHER وفي ملف CSV الخام بأسماء وصفية متوافقة، مع سنة بداية ونوع وقود وسعة متى توفر.
- لا سجل من هذه المجموعة يحتوي رمز ناقل حركة مؤكد. لا تماثل اسم تجاري أو سعة اسمية يكفي لإثبات تطابق منظومة نقل.

## حالات المراجعة
- 434–435: C32/C35 (2016)، 1493cc؛ الوقود غير مذكور في الحقل الخام؛ لا تفترض تطابق الإصدارات.
- 436–440: DXK6471AS3H مقابل DXK6471ASH (2020)، 1499cc، أوصاف Diesel/Lpg/Ng-biomethane/Petrol عند 101 kW؛ اختلاف الحرف «3» وتعدد الوقود يحتاج مراجعة المصدر المصنعي والسوق، ولا تُعد جميع نسخ الوقود صحيحة تلقائيًا.
- 441: E5 (2024) 1498cc بلا وصف وقود؛ يحتاج إثبات هوية النسخة ونظام الدفع.
- 442–443: FEGON 500 وFEGON 580 (2022)، 1498/1499cc وقدرة 78/107 kW؛ يحتمل التباين في تهجئة FEGON/FENGON ويجب إبقاء الأصل.
- 444–447: FENGON (2020)، 1498/1499cc وأوصاف Petrol/Lpg وقدرات 78/101/107 kW؛ لا تعميم نسخة واحدة.
- 448–452: FENGON 5 وFENGON 500 (2021)، 1498/1499cc، Petrol/Lpg، 78 أو 101 kW؛ فرق 1498/1499cc في صفّي 450/452 مع تطابق بعض الوصف يحتاج تحقق، ولا حذف باعتباره تكرارًا حرفيًا.
- 453–455: Fengon 580 (2021)، 1499cc، LPG 106/107 kW وPetrol 107 kW؛ هذه أوصاف وقود/قدرة منفصلة.
- 456: FENGON 7 (2022)، 1967cc/162 kW Petrol؛ يحتاج تعريف ناقل تطبيقه.
- 457–461: FENGON LPG وFengon5 (2021)، 1499cc، LPG/Ng-biomethane/Petrol و100/101 kW؛ صياغة Fengon5 مقابل FENGON 5 تحتاج مطابقة مصنع وليس دمجًا آليًا.
- 462–463: FENGON500 (2021)، 1498cc و78 kW، Diesel مقابل Petrol؛ لا تتساوى نسختا الوقود لمجرد تطابق سعة المحرك.

## نتائج الدفعة
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_33=559
last_examined=engines_part_005.csv:463
next_record=engines_part_005.csv:464 (confirmed queue)
remaining_OTHER_unreviewed_based_on_initial_1162=603

## القيود
- فحص تطابق بيانات المصدر وقائمة OTHER فقط، بلا شهادة OEM أو سجلات ECU/DTC جديدة.
- ملفات CSV الخام وmain وstable والموقع وبرنامج Windows والأصول والصور ومكتبة أكواد DTC المعتمدة لم تُعدل.
