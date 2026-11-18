# DTC NEXIS — استكمال أدلة OEM للحالات الـ27 — الدفعة 03 — 2026-11-18

**الحالة:** REVIEW_ONLY / NO_MASTER_IMPORT / NO_ECU_DTC_LINK / NO_RELEASE

## نقطة الانطلاق
- 31,520 صف محرك في gor3a محفوظة دون تعديل.
- 1,469 صفًا بلا وصف في حقل transmission.
- 32 حالة باسم المحرك مؤشر إلى ناقل الحركة؛ 5 أدلة OEM أولية مسجلة سابقًا، وبقيت 27 حالة لم يصل لها الدليل المباشر.
- استُرجعت بيانات هذه الدفعة من GitHub؛ أي تطابق مسميات لم يُعدّل الأصل.

## نتائج جديدة
- تم إضافة **6 حالات** إلى `review_queue/missing_transmission_oem_evidence_batch03.csv`.
- **4 حالات Citroën C4** مع بيانات مصنع رسمية عن PureTech 100 6MT وPureTech 130 EAT8 وBlueHDi 130 EAT8 ضمن السياق البريطاني.
- **حالة Subaru Ascent (2022)**: Subaru Canada تؤكد 2.4L 260hp مع Lineartronic CVT.
- **حالة Toyota Land Cruiser / Prado (2024)**: **تعارض سوق/مجموعة دفع**. صفحة Toyota الأمريكية تصف 2.4L i-FORCE MAX بنظام مختلف عن 2.8L 204hp MHEV في صف المصدر؛ لا يجوز نقل بيانات سوق USA إلى صف الديزل.
- حتى الآن صار **11 من 32** يحمل روابط أدلة OEM أولية/أو دليل اختلاف موثق (5 سابقة + 6 حاليًا). من هذه الـ11، حالة واحدة موثقة كعدم تطابق السوق والمحرك؛ **21 من 32** لم تُضف لها أدلة جديدة.
- لا يعني وجود دليل OEM أولي أن تطابق النسخة والسنة والسوق والقدرة ورمز علبة السرعة اكتمل.

## المصادر الرسمية
1. Citroën UK 2022: https://www.media.stellantis.com/uk-en/citroen/press/citron-updates-new-c4-electric-and-new-c4-for-2022
2. Citroën UK C4 2020: https://www.media.stellantis.com/uk-en/citroen/press/new-c4-and-new-e-c4-100-electric-citroen-reinvents-the-compact-hatchback
3. Citroën UK specifications: https://www.media.stellantis.com/uk-en/citroen/press/citroen-uk-opens-orders-for-new-c4-and-e-c4-100-electric-prices-and-specifications-confirmed
4. Subaru Canada Ascent 2022: https://subaru.ca/WebPage.aspx?ArticleID=9825&WebPageID=4998&WebSiteID=282
5. Toyota USA 2024 Land Cruiser (counterexample): https://pressroom.toyota.com/2024-toyota-land-cruiser-returns-to-its-origin/

## سلامة المكتبة
- أُضيفت الأدلة إلى قائمة المراجعة فقط؛ لم يُستبدل الحقل الخام transmission.
- لا توجد رموز مصنع engine_code_oem/transmission_code_oem/ecu_identifier مستخرجة ومعتمدة من هذه الأدلة.
- روابط ECU/DTC المعتمدة الجديدة = **0**؛ لا تعديل في البرنامج أو main أو update-feed.

## نقطة الاستئناف
1. تدقيق **21 حالة متبقية** من مجموعة الـ32، كل واحدة بمصدر OEM خاص بالجيل والمحرك والسوق.
2. فرز اختلافات قدرة المحرك/النظام الهجين ضمن 1,166 صف اشتباه وعدم وصفها أخطاء مؤكدة.
3. استخراج raw JSON specs مع فحص الترخيص وتوافق مخطط البيانات، وعدم استنتاج ECU من ناقل الحركة.
4. مراجعة التراخيص والفرع قبل أي دمج.
