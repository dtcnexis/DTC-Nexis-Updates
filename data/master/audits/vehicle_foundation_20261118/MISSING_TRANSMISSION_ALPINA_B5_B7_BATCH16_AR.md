# DTC NEXIS — الدفعة 16: Alpina B5/B6/B7 ورصد فروق القدرة

2026-11-18 | branch=review/vehicle-foundation-audit-20261118 | REVIEW_ONLY / NOT_PUBLISHED
base_commit=f74ef357ede64d7a7d491c56e9821b9471c8f213

## نطاق المراجعة
existing_records=21، جميعها في `engines_part_001.csv:635–655`.
جرى فحص الصفوف في `data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_001.csv` ومقارنة مع `review_queue/missing_transmission_no_hint_other_batch01.csv` ضمن المسار `data/master/reviews/vehicle_catalog_full_20261118/`.
لا توجد حقول ناقل OEM مؤهلة في هذه الصفوف.

## نتائج فنية أولية من المصدر لا تعني موافقة المصنع
- 638/639: Alpina B6 BITURBO / 2012 / Cabriolet / 4395cc، ولكن 397 و441kW. اختلاف قدرة يجب الاحتفاظ به.
- 641/642: Alpina B7 / 2006 / 4.4L، 4398cc مقابل 4395cc؛ السطر الثاني يذكر 447kW. اسم الموديل والسنة لا يكفيان لتوحيد الصفين.
- 643/644: Alpina B7 BITURBO / 2010 / 4395cc، قدرة 397/447kW؛ لا تُعد نسختا الناقل متطابقتين دون إثبات.
- 646/647: B7 BITURBO ALLRAD / 2011 / 4395cc، قدرة 447/373kW؛ يحفظ الاختلاف.
- 649–655: أسماء BMWALPINA غير المفصولة (BMWALPINAB3GT3، BMWALPINAB3SBITURBO، BMWALPINAB5BITURBO، BMWALPINAB6BITURBO، BMWALPINAB7BITURBO) تصلح لفتح قائمة تسمية بديلة محتملة، ولا يجوز ربطها تلقائياً بموديلات Alpina المسماة منفصلة.
- 651/652: BMWALPINAB5BITURBO / 2011 / 4395cc / 373 و397kW؛ لا تطابق حرفي.
- 654/655: BMWALPINAB7BITURBO / 2011 / 4395cc / 373 و397kW؛ لا تطابق حرفي.

## حصيلة
prior_records_checked=21; deferred_for_OEM=21; newly_approved=0; newly_imported=0; duplicate_rows_deleted=0; raw_rows_modified=0.
آخر سجل: engines_part_001.csv:655.
التالي: engines_part_001.csv:656 BMWALPINAD3BITURBO.
لا تغييرات main أو DTC أو ECU أو الصور أو تحديث Windows/RC3.8.0/RC3.8.2؛ لا نشر.
