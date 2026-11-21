# DTC NEXIS — الدفعة 69: Buick Enclave / Chevrolet Corvette / GMC Sierra HD

date=2026-11-21 | REVIEW_ONLY / TECHNICAL_EVIDENCE_NOT_PRODUCTION_IMPORT / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_SCOPE_RECHECK_BATCH68_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## منهج الحفظ
ثلاثة صفوف أصلية موجودة مسبقًا ضمن قائمة التلميحات الـ32، لا إضافات جديدة. المصدر الرسمي قد يثبت سنة محددة ونوع ناقل، لكنه لا يثبت نطاق كل السنوات في الصف المجمع أو كود القطعة/ECU. تُسجَّل الاختلافات والأدلة ولا تُعدّل الأصول.

## 1. Buick Enclave — engines_part_003.csv:1558
- RAW: Enclave (2021), years 2021–2024, 3.6L V6 9AT (310 HP); raw_git_blob_sha=3796acc7f93b581a449480f958097be2937788bc.
- **وثيقة Buick الأصلية لسنة 2022** تؤكد محرك 3.6L V6 بقوة 310 hp وناقلًا أوتوماتيكيًا 9 سرعات؛ عام 2022 يقع داخل فترة 2021–2024 الخام. هذا دليل مطابق لعائلة المحرك/القوة/عدد السرعات، وليس رقم صندوق أو تغطية تلقائية لسنوات 2021 و2023 و2024.
- OEM_SOURCE_PDF: https://media.buick.com/content/dam/Media/images/US/Vehicles/Buick/Enclave/2022/Buick-Enclave-Infographic.pdf
- OEM_PDF_PAGE: 1; visually verified from PDF screenshot.
- status=OEM_SAME_ENGINE_POWER_GEAR_COUNT_MY2022 / OTHER_MODEL_YEARS_AND_PART_NUMBER_PENDING.

## 2. Chevrolet Corvette — engines_part_004.csv:317
- RAW: Corvette Coupe (1983), year_start=1983, year_end=1996, 5.7L V8 5MT RWD (249 HP), 5735cc; raw_git_blob_sha=a62309aa7556a1ffbc89573c42cdfab1cb27c1f5.
- أرشيف General Motors للمواصفات يسرد 1982 Corvette ثم 1984 Corvette من دون إصدار عام 1983، بما يتفق مع تاريخ تخطي موديل Corvette لعام 1983 رغم اختبار سيارات أولية. هناك خطر **مزج سنة بداية الجيل الهندسية مع سنة الموديل الرسمية**؛ ولا يجوز إسناد ناقل 5MT لجميع السيارات بين 1983 و1996. شهد هذا الجيل أنواع ناقل مختلفة عبر السنوات، وتحتاج صفوفًا مقسمة بحسب الموديل الفعلي.
- OEM_ARCHIVE_INDEX: https://www.gm.com/heritage/archive/vehicle-information-kits
- SECONDARY_CONTEXT: https://www.history.com/articles/missing-1983-corvette-model-year
- status=HIGH_PRIORITY_MODEL_YEAR_GEN_SCOPE_CONFLICT / SOURCE_CORRECTION_PENDING / GEARBOX_HINT_NOT_APPROVED.
- لا يُحذف أو يُحوّل إلى 1984 أو 5MT دون توثيق الصف المصنعي الذي انبثقت منه بيانات المصدر، ومراجعة السنوات والنوع والقدرة.

## 3. GMC Sierra 2500HD — engines_part_006.csv:1512
- RAW: Sierra 2500HD (2019), years 2019–2022, «6.6L 10AT (445 HP)»؛ حقل fuel والمحرك النوعي غير محددين بالملف؛ raw_git_blob_sha=2622eaa2d8a10316d2e7a9561d3182061f51ffce.
- GMC تعرض مواصفات **2020 Sierra HD Chassis Cab**: محرك Duramax 6.6L Turbo Diesel V8 بقوة 445hp مع Allison 10-speed automatic، وتفرّق عنه محرك البنزين 6.6L بقوة 401hp وناقل 6 سرعات. هذا دليل لنسخة ديزل محددة بفئة chassis cab وسنة 2020، وليس تطابقًا آليًا مع صف 2500HD مجمّع من 2019 إلى 2022.
- OEM_SOURCE: https://www.gmc.com/vehicles/2020/commercial/sierra-hd-chassis-cab/model-details
- status=OEM_2020_DIESEL_ENGINE_POWER_10AT_FAMILY_LEAD / BODY_APPLICATION_AND_2019_SCOPE_PENDING.
- يلزم تحديد ما إذا كانت سنة 2019 في المصدر سنة بدء الجيل أو سنة موديل فعلية، والهيكل (pickup/chassis cab) وRPO ناقل وRPO محرك.

## النتائج
existing_hint_cases_reexamined=3
new_approved_OEM_gearbox_code_assignments=0
new_ECU_DTC_links=0
new_vehicle_imports=0
raw_records_modified=0
hint_cases_still_unapproved=32
new_high_priority_generation_conflict_flags=1
next_workstream=CHECK_GM_HERITAGE_CORVETTE_GENERATION_AND_YEAR_SCOPING_AND_REMAINING_OEM_HINT_CASES

## الحماية
لا كتابة على raw CSV ولا قوائم OEM القديمة، ولا دمج إلى main ولا تعديل stable أو برنامج Windows أو الموقع أو الصور أو ملفات DTC المعتمدة.
