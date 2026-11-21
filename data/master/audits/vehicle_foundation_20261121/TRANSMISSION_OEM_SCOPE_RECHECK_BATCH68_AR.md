# DTC NEXIS — الدفعة 68: أربع حالات تلميح ناقل ومراجعة OEM / مصدر متخصص

date=2026-11-21 | REVIEW_ONLY / OEM_EVIDENCE_NOT_A_FINAL_GEARBOX_ID / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_SCOPE_RECHECK_BATCH67_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## الضوابط
لا تُستخدم عبارة عدد السرعات في engine_label اعتمادًا كافيًا لتحديد علبة التروس. يلزم ربط الصانع/سنة الموديل/السوق/المحرك/نسخة الدفع ورمز صندوق التروس وECU قبل أي تغيير للمكتبة. كل حالة أدناه تبقى NOT_APPROVED.

## 1. Audi SQ5 TDI — engines_part_002.csv:761
- raw_source: SQ5 (2020), year_start=2020, year_end=2024, 3.0L TDI V6 8AT AWD (341 HP), Mild Hybrid Diesel; source_git_blob_sha=3a281ebfce241e7849e4db09dcaa9e385986274e.
- Audi 2020-11-12 تذكر النسخة المحدثة 3.0L V6 TDI بقوة 251 kW/341 PS وتؤكد **eight-speed tiptronic**؛ إطلاق أوروبي مطلع 2021. تماثل وصف القدرة وعائلة المحرك يساعد كثيرًا، لكنه لا يغطي تلقائيًا سنوات 2020–2024 أو كل الأسواق، ولا يكشف كود ناقل المصنع.
- OEM_SOURCE: https://www.audi.com/en/media-releases/sporty-powerful-and-efficientaudi-presents-the-new-generation-of-the-sq5-tdi-13344
- status=OEM_POWERTRAIN_AND_8_SPEED_FAMILY_LEAD / MODEL_YEAR_MARKET_CODE_PENDING.

## 2. GMC Terrain — engines_part_006.csv:1549
- raw_source: Terrain (2021), years 2021–2024, 1.5L 9AT (170 HP) Gasoline; source_git_blob_sha=2622eaa2d8a10316d2e7a9561d3182061f51ffce.
- كتالوج GMC الرسمي الخاص بموديل 2021 يذكر 1.5L Turbo بقوة 170HP وعزم 203 lb-ft وناقل **9-speed automatic**. يتطابق عام 2021 مع سنة بداية الصف الخام، خلافًا لمقارنة الجيل المختلف 2025 المسجلة في الدفعة 66؛ الكتالوج لا يثبت كل 2022–2024 ولا اسم القطعة/الرمز OEM.
- OEM_SOURCE_PDF: https://www.gmc.com/content/dam/gmc/na/us/english/index/about/download-brochures/2021-models/GMTN21CT000_2021_GMC%20Terrain_Catalog_DIGITAL_8321.pdf
- OEM_PDF_SECTION: page 9, «Terrain Capability and Performance», verified visually via PDF screenshot; original equipment list also names nine-speed automatic.
- status=OEM_SAME_MODEL_YEAR_ENGINE_POWER_GEAR_COUNT_FAMILY_LEAD / EXACT_GEARBOX_CODE_AND_FULL_YEAR_SCOPE_PENDING.

## 3. Lotus Exige — engines_part_008.csv:1827
- raw_source: Exige (2021), 2021–2021, 3.5L V6 6MT (420 HP), Gasoline, RWD; source_git_blob_sha=88dcf7945b863564a06acb1de5f9676d401bba49.
- صفحة Lotus الرسمية لتاريخ Exige تذكر جيل 2011–2021 بمحرك 3456cc V6 supercharged وناقل **six-speed manual transaxle**، وتذكر نسخة Sport 420 Final Edition الأخيرة. هذا دليل أصلي قوي لعائلة الناقل وعدد السرعات، لكنه لا يقدم رقم جزء صندوق التروس المصنعّي أو VIN ولا يربط قدرة 420HP بمواصفات أسواق كل نسخة.
- OEM_SOURCE: https://www.lotuscars.com/sv-SE/lotus-story/road-cars/exige
- status=OEM_ENGINE_GENERATION_6MT_FAMILY_EVIDENCE / GEARBOX_PART_NUMBER_AND_MARKET_PENDING.

## 4. Lincoln Zephyr — engines_part_008.csv:1758
- raw_source: Zephyr (2021), 2021+, 2.0L 8AT، مع غياب نوع الوقود والقدرة؛ source_git_blob_sha=88dcf7945b863564a06acb1de5f9676d401bba49.
- MarkLines أفادت بتاريخ 2021-11-23 أن Zephyr الصينية عُرضت في نوفمبر 2021 مع محرك 2.0L وناقل 8 سرعات، على أن يبدأ تسويقها في الربع الأول من **2022**. هذا مصدر صحفي متخصص ثانوي، وليس وثيقة مواصفة OEM مباشرة ولا دليلًا على إنتاج/تسليم موديل 2021.
- SPECIALIST_NEWS_SOURCE: https://www.marklines.com/en/news/261735
- status=SECONDARY_8_SPEED_MARKET_LEAD / OEM_PRIMARY_MISSING / 2021_LAUNCH_VS_2022_SALES_APPLICABILITY_GATE.
- لا يجوز نسخ نوع ناقل من Corsair أو Nautilus أو Ford بدعوى قرابة الشركة.

## نتيجة الدفعة
existing_hint_cases_reexamined=4
OEM_primary_model_family_evidence=3
secondary_industry_lead_only=1
new_approved_OEM_gearbox_code_assignments=0
new_ECU_DTC_links=0
new_vehicle_imports=0
raw_rows_modified=0
hint_cases_still_unapproved=32
last_reexamined=engines_part_008.csv:1827
next_workstream=IDENTIFY_OEM_GEARBOX_PART_NUMBER_AND_EXACT_APPLICABILITY_FOR_AUDI_GMC_LOTUS_AND_LINCOLN

## سلامة المكتبة
هذه وثيقة أدلة تكميلية لا تعديل للصفوف المصدرية أو تقارير/قوائم OEM القديمة، ولا دمج إلى main أو stable، ولا نشر للموقع أو Windows أو تغيير لملفات DTC أو الصور.
