# DTC NEXIS — الدفعة 15: Alpina B4 / B5 — ناقل الحركة المفقود

تاريخ المراجعة: 2026-11-18
branch: review/vehicle-foundation-audit-20261118
base_commit: bf4a7731c278a3c6e728e7bc3898679f0c302c67
status: REVIEW_ONLY / NOT_PUBLISHED / NO_OEM_GEARBOX_APPROVAL

## أصل البيانات
- قائمة المراجعة الموجودة: `data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv`
- المصدر الخام المطابق: `data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_001.csv`
- تم تدقيق 34 صفاً موجوداً: `engines_part_001.csv:601–634` بمقارنة القيم في القائمة مع الملفات الخام، دون إعادة استيراد أو تعديلها.
- جميع هذه الصفوف تبقى `OEM_GEARBOX_IDENTIFICATION_REQUIRED`؛ سنة بداية الجيل ليست بذاتها سنة إنتاج كل نسخة محرك.

## مؤشرات اختلاف الاحتفاظ الإلزامي
- B4 GRAN COUPE، الصفان 601/602: 2021، 2993cc، قدرتان 340/364kW؛ الاختلاف أصلي وليس تكراراً حرفياً.
- B4 S BITURBO 603/604 وCABRIO 605/606 وCOUPE 607/608: كل زوج يشترك في وصف الطراز والسعة (2979cc)، وتختلف القدرة 324/332kW.
- B4 S BITURBO COUPE ALLRA / COUPÉ ALLRA / ALLRAD، 609–612: اختلافات الاسم مع علامة تشكيل/نهاية مبتورة/سنة/قدرة. مرادفات مرشحة للمراجعة فقط؛ لا توحيد أو حذف.
- B5، 613–616: 2005، 4.4L اسميًا، لكن 4398cc في الصف 613 مقابل 4395cc في 614–616؛ وقدرات 373/447/457kW في الصفوف 614–616. اختلاف السعة والقدرة محفوظ.
- B5 BITURBO، 618–621: 2010، 4395cc، قدرات 373/397/441/447kW؛ لا تُفسَّر على أنها أربعة نواقل مؤكدة ولا تُدمج آلياً.
- B5 BITURBO AL / ALLRAD / (M3) / M3 / TO / Touring Allrad، الصفوف 622–630: تشابه اختصارات محتمل مع اختلاف السنة أو البنية أو القدرة؛ الالتباس لا يثبت تطابق الموديل.
- B5 TOURING، 631/632: 2006، 4.4L، `displacement_cc=4398` و`4400` على التوالي. ليسا تكرارًا حرفيًا؛ يلزم OEM للتحقق من قيمة السعة، وناقل كل نسخة.
- B5 TOURING AL / ALLRAD، 633/634: اسم جزئي محتمل ولا يُدمج تلقائياً بسبب اختلاف سنة بداية الجيل والهيكل النصي.

## حصيلة الدفعة
existing_rows_inspected=34
new_oem_verified_rows=0
new_imported_rows=0
confirmed_duplicate_rows_removed=0
rows_deferred=34
raw_rows_modified=0
ECU_DTC_links_approved=0

آخر سجل تمت مقارنته `engines_part_001.csv:634`.
الاستئناف: `engines_part_001.csv:635` (Alpina B5S)، ثم بقية OTHER، ومراجعة أدلة OEM المستقلة. لا تنقل أي قيمة ناقل إلى CSV الخام دون سنة/سوق/رمز ناقل مثبت.
الحماية: لا مساس بـ main أو الصور أو DTC أو RC3.8.0 / RC3.8.2 أو Windows أو قناة التحديث.
