# DTC NEXIS — الدفعة 17: مراجعة Alpina D3–D5 وسجلات ناقل الحركة الناقصة

التاريخ: 2026-11-18 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
base_commit=aabf905ed34012a954188c3a3a7f93b4231ce7d9

## مصادر وسجل المراجعة
تمت مطابقة 35 سجلاً من قائمة `data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv` مع نظائرها الخام في `data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_001.csv`، حيث `source_line=656–690`. لا يوجد استيراد أو إنشاء صفوف أصلية جديدة، ولا تأكيد لناقل OEM.

## حالات الأولوية
- 656/657: BMWALPINAD3BITURBO / 2011، 1995cc ديزل، 155/157kW: اختلاف قدرة مع بقاء الاسم والسنة والسعة.
- 659–662: D3 / سنة بداية جيل 2006: يوجد 1995cc/155 و157kW وكذلك 2993cc/261 و257kW في سجلات الاسم نفسه. علامة YEAR_POWER_VARIANT_SCOPE_REVIEW؛ لا تُعامل سنة بداية الجيل كسنة إنتاج هذه القدرات.
- **663: Alpina D3 BITTURBO / 2019 مسجل 4.4L 447kW Petrol / 4395cc، بينما اسم D3 يوحي عادة بخط D3 الديزل؛ علامة عالية الأولوية `POWERTRAIN_IDENTITY_INCONSISTENCY_CANDIDATE`. لا نصححه إلى D3 ديزل أو B5 بنقل آلي؛ يحتاج مرجع تسجيل/صانع/VIN وتدقيق جودة المصدر.**
- 664/665: D3 BITURBO / سنة بداية الجيل 2009؛ 2.0L 157kW Diesel (1995cc) مقابل 3.0L 257kW Diesel (2993cc)؛ يجب فصل نطاق النسخ.
- 667/668: D3 BITURBO TOURING / 2010، 2993cc بلا قدرة مقابل 1995cc و157kW؛ لا حذف أو دمج.
- 673/674: D3 TOURING / 2014 / 2993cc، قدرة 261/257kW؛ اختلاف يُحفظ.
- 680–682: D5 / 2012 / 2993cc Diesel، قدرات 285/300/257kW؛ تحتاج سنة نسخة ومصدر OEM.
- 686–689: D5 S / 2017 / 2993cc Diesel، قدرات 240/255/285/300kW؛ لا يعكس ذلك بالضرورة أربع نواقل أو أربع نسخ OEM مثبتة.
- أسماء `BMWALPINAD...` و`D3/D4/D5` يمكن اختبارها كمرادفات مشروطة، ولا تُوحّد بلا دليل ينطبق على السنة والمحرك والسوق.

## القياس
previous_rows_examined=35
newly_imported=0
approved_OEM_gearbox_fitments=0
rows_deferred=35
duplicate_rows_deleted=0
original_rows_modified=0
validated_ECU_DTC_links=0
الدفعات 15–17 راجعت 34+21+35=90 صفاً إضافياً؛ الدفعات 11–17 مجتمعة راجعت 179 صفاً من مجموعة OTHER (إن لم توجد إعادة عدّ لاحقة). لا يُفسَّر ذلك كاكتمال تقني لأي صف.

آخر صف تمت مراجعته: engines_part_001.csv:690 (D5 S ALLRAD).
نقطة الاستئناف الدقيقة: engines_part_001.csv:691، ثم 692/693 لاختصارات D5 S TOU.ALLR، ثم بقية OTHER، وبعدها فئات EV وHybrid، وتوحيد 384 تسمية خام ومطابقة OEM.
Google Drive SHA-256 والتغطية الفنية الكاملة ما زالا غير مكتملين.
الحماية: لا دمج main ولا تعديل DTC/ECU أو الصور أو الموقع أو برنامج Windows أو RC3.8.0 / RC3.8.2 أو ملفات التحديث.
