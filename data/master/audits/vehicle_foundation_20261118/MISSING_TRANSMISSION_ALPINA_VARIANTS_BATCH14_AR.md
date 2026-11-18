# DTC NEXIS — الدفعة 14: اختلافات Alpina B3/B4 في الناقل المفقود

التاريخ: 2026-11-18 | REVIEW_ONLY | NO_OEM_APPROVAL
متابعة Commit f4b24835c02d4d170efd1d9c162d6459c650ce31 على فرع review/vehicle-foundation-audit-20261118.
المصدران اللذان تمت مراجعتهما دون تعديل:
data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_001.csv
النطاق: 34 صفاً سابقاً من Alpina، source_line 567–600، مقروءة من المصدر الخام ومتتبعات قائمة المراجعة.

## حالات موثقة من البيانات الخام وليست تصديقات OEM
- 574/575: B3 Limousine، سنة بداية جيل 2020، سعة 2993cc في السجلين لكن قدرة 340 مقابل 364kW. لا يُدمجان ولا يُمنحان ناقلاً واحداً استنتاجياً.
- 578/579: B3 S BITURBO، 2010، 2979cc، 294 مقابل 324kW.
- 580/581: B3 S BITURBO ALLRAD، 2011، 2979cc، 301 مقابل 324kW.
- 582/583: B3 S BITURBO TOURIN، 2014، 2979cc، 301 مقابل 324kW؛ «TOURIN» قد تكون تسمية مبتورة مقارنة «TOURING»، ولا توحد بلا تطابق كامل.
- 585/586: B3 S BITURBO TOURING ALLRAD، 2011، 2979cc، 294 مقابل 324kW.
- 587/589: B3 TOURING، 2001، stationwagen، 3.3L لكن 3346 مقابل 3300cc؛ duplicate_candidate_only لا تطابق حرفي.
- 590/591: B3 TOURING، سنة بداية جيل 2001، سعة 2993cc، قدرة 340/364kW (462.4/495 horsepower in source). يجب عدم فهم سنة بداية الجيل كسنة إنتاج هذه القدرة دون تحقق السوق والموديل والنسخة.
- 592–594: B4، 2014، القدرات 364/301/324kW والسعات 2993/2979cc؛ يحتفظ بالنسخ المنفصلة.
- 598/599: B4 BITURBO COUPE AL مقابل ALLRAD، 2015، السعة والقدرة متساويتان في المصدر؛ possible_truncated_alias فقط، وليس تطابقاً قانونياً أو مصنعياً.
- 600: B4 GRAN COUP? يحوي علامة استفهام في raw model، ما يثير احتمال تلف encoding، دون تغيير الأصل.

## النتائج المحفوظة
previous_rows_examined=34; approved_OEM_gearbox_fitments=0; new_imported_records=0; reviewed_but_deferred=34; confirmed_exact_duplicates=0 from the highlighted pairs; modified_original_records=0.
تراكم الصفوف التي تم تدقيقها مباشرة ضمن مجموعة OTHER في الدفعات 11–14: 17+17+21+34 = 89؛ التعداد المرجعي الإجمالي الناقص 1,469 لم يتغير ولا يُعد إنجازاً فنياً.
آخر صف خام مُدقق: engines_part_001.csv:600. الاستئناف التالي: engines_part_001.csv:601.
الترقية إلى OEM تحتاج مواصفة من الشركة مرتبطة بالموديل والنسخة وVIN/سنة السوق ورمز الناقل، ولا يجوز الاستدلال عليها من السعة فقط.
لا دمج main ولا تعديل DTC أو برنامج Windows أو RC3.8.0/RC3.8.2 ولا نشر.
