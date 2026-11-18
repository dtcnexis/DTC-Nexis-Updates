# DTC NEXIS — تدقيق 32 وصف ناقل مفقود مع أدلة OEM — 2026-11-18

**الحالة:** REVIEW_ONLY / NO_MASTER_IMPORT / NO_ECU_DTC_APPROVAL / NO_RELEASE.

## البيانات المستأنفة
- سجلات gor3a للمحركات: **31,520**.
- صفوف حقل `transmission` الفارغ: **1,469**. لا تغيير في هذا العدد ولا في البيانات الخام.
- منها **32** تحمل مؤشرًا لنوع ناقل الحركة في تسمية المحرك: **20** مرشح AT و**7** مرشحات MT و**5** مرشحات CVT/e-CVT.
- ليست الأوصاف نصوصًا مصنعية مستقلة كافية لتعبئة `transmission` أو `transmission_code_oem`.

## العمل المنجز
- إعادة فحص السجلات الـ32 في `review_queue/missing_transmission_label_hints_batch01.csv`.
- حفظ **5 روابط إلى بيانات OEM منشورة** مرتبطة بسجلات محددة، دون إعلان اعتماد الانطباق الكامل:
  1. Alpine A110 (2024): مصدر Alpine لسوق تركيا يصف محرك 1.8L وناقل Getrag ذي 7 سرعات بقابض مزدوج رطب. يحتاج تأكيد نسخة القدرة 345 HP والسوق.
  2. Ford Transit Connect Passenger Wagon (2019): كتيب Ford الأمريكي يذكر محرك 2.0L GDI وناقل 8 سرعات. يحتاج ضبط القوة ورقم الناقل وسنوات 2018–2023.
  3. Lexus ES 250 AWD (2023): بيان Lexus Canada يذكر 203 HP مع ناقل أوتوماتيكي 8 سرعات؛ النطاق 2023 وسوق كندا، لا اعتماد تلقائيًا لكل 2023–2025.
  4. Toyota Corolla Sedan 1.8 (2022): بيان Toyota USA يوضح وجود المحرك 1.8L مع تجهيزات معينة؛ لا يستنتج منه موافقة تلقائية على 140 HP أو كل أسواق Corolla.
  5. Toyota Corolla Sedan 2.0 (2022): بيان Toyota USA يذكر Dynamic Shift CVT في تجهيزات 2.0L؛ قدرة 196 HP المسجلة في المصدر تتطلب مراجعة سوق ومحرك/منظومة هجينة.
- حفظ جميع أدلة البحث في `review_queue/missing_transmission_oem_evidence_batch02.csv`.
- حفظ الأولوية لكل **32** سجلًا في `review_queue/missing_transmission_32_prioritized_batch02.csv`: 5 سجلات ذات مصدر OEM أولي، و27 بلا دليل مباشر في هذه الدفعة.

## ضوابط منع الادعاء
- لا يكفي دليل اسم الموديل؛ يجب مطابقة السنة والسوق/النسخة، قدرة ومُعرّف المحرك، ورقم علبة السرعة حيث توفر.
- `2022 Corolla 2.0 (196 HP)` ليست مثبتة بتلك القدرة في المصدر المذكور، ولذلك تبقى موقوفة عن التطبيع.
- e-CVT في أنظمة هجينة ليس بالضرورة مكافئًا ميكانيكيًا لـ CVT بالحزام.
- لا يُستنتج ECU أو DTC أو رقم قطعة من مواصفة ناقل عامة.

## الحفظ والمتبقي
- الملفات الأصلية و3 ملفات استعادة لكل السجلات المفقودة بقيت دون تعديل.
- **DTC الجديدة: 0**؛ **ECU/DTC المعتمدة الجديدة: 0**؛ الملفات المؤكدة هنا للبحث والمراجعة فقط.
- التالية: تدقيق بقية 27 حالة بمراجع OEM مرتبطة بموديل/سنة/سوق محددة، ثم فرز 1,437 صفًا لا تحتوي تسمية محركها على دليل صريح، واستخراج رموز OEM فقط متى ظهر المصدر المناسب.
- تبقى مراجعة 1,166 اختلافًا سابقًا من ناحية اختلاف قدرة النظام الهجين/المحرك.
- لا تعديل `main` ولا البرنامج أو الصور أو قناة التحديث.

## مصادر OEM
- Alpine: https://media.alpinecars.com/alpine-comes-to-turkiye-with-its-first-point-of-sale-in-istanbul/?lang=eng
- Ford: https://media.ford.com/content/dam/fordmedia/North%20America/US/product/2019/transit-connect-van/19-Transit-Connect-Passenger-Van.pdf
- Lexus: https://media.lexus.ca/en/releases/2022/striking-design-meets-commanding-performance-the-2023-lexus-es-series-luxury-sedans.html
- Toyota: https://pressroom.toyota.com/corolla-keeps-the-fun-rolling-with-2022-apex-nightshade-editions/
