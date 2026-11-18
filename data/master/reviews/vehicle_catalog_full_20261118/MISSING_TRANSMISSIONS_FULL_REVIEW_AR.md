# DTC NEXIS — تدقيق كامل للأوصاف الناقصة لناقل الحركة — 2026-11-18

**الحالة:** REVIEW_ONLY / ORIGINAL_DATA_UNCHANGED / NO_APP_RELEASE / NO_ECU_DTC_APPROVAL

## المصدر والمنهجية
- فُحصت كافة ملفات `gor3a/engines_part_001.csv` إلى `engines_part_017.csv` المخزّنة في فرع المراجعة، بإجمالي **31,520** صفًا.
- احتفظنا بـ **1,469** صفًا حقل `transmission` فيها فارغ، في ملفات تتبع تحتوي مسار الأصل والسطر واسم المحرك ونطاق سنة الجيل.
- سُجلت **32** حالة فيها إشارة واحدة صريحة أو مصطلح نوع ناقل في `engine_label`؛ لا تشكّل مواصفة مصنع معتمدة. لا توجد حالات متعددة التلميح وفق القاعدة.
- تبقى **1,437** حالة بلا إشارة صريحة اكتشفتها القاعدة؛ هذا لا يعني انعدام ناقل الحركة في السيارة.
- فُصلت الإشارات الـ32 في `review_queue/missing_transmission_label_hints_batch01.csv` لسهولة فحصها بالمراجع الأصلية.

## فرز بحسب ألفاظ اسم نسخة المحرك (تقسيم حصري اصطلاحي فقط)
| شريحة نصية | صفوف ناقصة |
|---|---:|
| ألفاظ كهربائية محتملة (electric/EV/BEV/kWh/dual motor/battery) | 247 |
| ألفاظ هجينة دون تحقق OEM (PHEV/HEV/hybrid/MHEV/e-Boxer) | 30 |
| الباقي دون تلك الإشارات | 1,192 |
| **الإجمالي** | **1,469** |

هذه الشرائح تعتمد فقط على كلمات الوصف. لا تعني إثبات هوية EV/HEV ولا تُستخدم لإسناد ناقل من نوع واحد.

## أشد الماركات ظهورًا بين الأوصاف المفقودة
Austin (188)، Alpina (171)، Morris (82)، DFSK (75)، Mercedes-Benz (71)، Westfield (71)، Polaris (69)، Daimler (60)، Ligier (45)، Aixam (34).

## الملفات المحفوظة
- `review_queue/missing_transmission_source_trace_part_001.csv`: 500 حالة.
- `review_queue/missing_transmission_source_trace_part_002.csv`: 500 حالة.
- `review_queue/missing_transmission_source_trace_part_003.csv`: 469 حالة.
- `review_queue/missing_transmission_label_hints_batch01.csv`: 32 حالة مشتقة من نفس الـ1,469، وليست حالات إضافية في العدد الإجمالي.

## ما لا يجوز استنتاجه
- رمز `7AT` في `engine_label` لا يثبت رقم صندوق التروس أو معرّف وحدة TCM ولا مواصفة السوق.
- وصف ناقل فارغ في سيارة كهربائية لا يثبت نقلًا أحادي السرعة.
- لا تُضاف روابط ECU/DTC لأي سجل دون مصدر فني مع نطاق التطبيق.
- عبارات `EV_HINT`/`HYBRID_HINT` ليست بيانات تركيبية معتمدة.

## نقطة الاستئناف
1. مطابقة عينات 32 حالة ذات تلميحات بالأدلة الفنية المصنعية حسب الجيل والسوق والسنة.
2. التحقق من نقص `transmission` في مركبات Austin/Alpina وبقية الماركات ذات الأعداد الكبيرة، من دون استكمال آلي متسرع.
3. البحث عن raw JSON specs المرخصة وتوثيق حقول `engine_code_oem` و`transmission_code_oem` و`ecu_identifier`، مع إبقاء الفارغ كما هو حتى إثباته.
4. مواصلة تدقيق حالات التعارض السابقة البالغ عددها 1,166 وتحديد أولويات التدقيق.
5. لا تعديل `main` ولا RC3.8.0/RC3.8.2 ولا update-feed أو الوسائط.

المصدر: [بيانات محركات gor3a الموثقة في مستودع المراجعة](https://github.com/dtcnexis/DTC-Nexis-Updates/tree/research/vehicle-catalog-full-staging-20261118/data/master/reviews/vehicle_catalog_full_20261118/gor3a).
