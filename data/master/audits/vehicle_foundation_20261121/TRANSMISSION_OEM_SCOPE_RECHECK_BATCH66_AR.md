# DTC NEXIS — الدفعة 66: تدقيق نطاق مصادر OEM لست حالات ناقل حركة

date=2026-11-21 | REVIEW_ONLY / OEM_FAMILY_EVIDENCE_NOT_CODE_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_SOURCE_REVIEW_CHECKPOINT_20261121_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## المنهج
رُوجعت ست حالات موجودة مسبقًا (ليست سجلات جديدة) مع نشرات الشركات المصنعة المتاحة على مواقعها. يُفصل بين إثبات عائلة ناقل ضمن سوق/سنة معينة وبين المطابقة الدقيقة لصف المصدر، ولا يُعتمد رقم علبة التروس أو ECU أو DTC بلا تطابق السنة والسوق والنسخة ونظام الدفع. جميع الحالات ما زالت NOT_APPROVED. لا احتساب لهذه الستة كاعتماد جديد أو كزيادة في الـ1469.

## سجل الأدلة الجديد

### 1. Cadillac XT4 — engines_part_003.csv:1846
- raw: XT4 (2023–2025), 2.0L Turbocharged 9AT FWD (238 HP).
- المصدر الرسمي GM، إطلاق XT4 موديل 2024، أمريكا الشمالية: محرك 2.0L بقوة 235 hp وناقل Hydra-Matic **9T50** أوتوماتيكي 9 سرعات. ذكر صانع السيارة رقم العائلة 9T50 بوضوح.
- OEM_URL: https://news.gm.com/home.detail.html/Pages/news/us/en/2023/feb/0220-xt4.html
- النتيجة: NEW_OEM_GEARBOX_FAMILY_LEAD / MODEL_YEAR_AND_POWER_SCOPE_MISMATCH. لا يثبت أن مواصفة 238hp في الصف الخام وأسواق/سنوات 2023–2025 هي ذات نسخة 2024، ولا يُنسخ 9T50 إلى الصف دون دليل انطباق.

### 2. Peugeot 408 — engines_part_012.csv:1620
- raw: 408 Fastback (2026), 1.2L MHEV 6AT FWD (143 HP).
- بيجو/Stellantis تؤكد MY2026 408 Hybrid 145 بنظام 1.2L مع ناقل **e-DCS6** بست سرعات مزدوج القابض، ونظام P2 الكهربائي (بيان سوق تايوان 2026، وأيضًا بيان بريطاني 2026).
- OEM_URL: https://www.media.stellantis.com/as-en/peugeot/press/the-all-new-peugeot-408-launches-in-taiwan-with-evolved-design-hybrid-powertrain-and-technology
- SECONDARY_OEM_URL: https://www.media.stellantis.com/uk-en/peugeot/press/peugeot-reveals-uk-pricing-and-specification-for-new-408
- النتيجة: OEM_VARIANT_LEAD / POWER_UNITS_MARKET_GATE. الخام يقول 143 HP بينما المرجع 145 PS/hp ضمن تباين وحدات ومعيار قياس؛ لا تطبيع أعمى ولا اعتماد قطعة ناقل/VIN/ECU.

### 3. Renault Clio — engines_part_013.csv:1060
- raw: Clio 5 Doors (2025), 1.2L TCe 5MT FWD (115 HP).
- رينو تؤكد من 2025–2026 أن TCe 115 متاح بناقل يدوي أو EDC، لكن الإعلان لا يُثبت بالضرورة العدد **5MT** المذكور في المصدر.
- OEM_URL: https://media.renault.com/new-renault-clio-orders-open-in-france/?lang=eng
- SECONDARY_OEM_URL: https://media.renault.com/clio-expands-its-range-with-the-new-ecog-120-hp-edc-powertrain/?lang=eng
- النتيجة: MANUAL_FAMILY_CONFIRMED / GEAR_COUNT_NOT_ESTABLISHED. لا ترقية لاسم 5MT إلى مواصفة معتمدة.

### 4–5. Toyota Corolla — engines_part_015.csv:1004 و1005
- raw 1004: Corolla Sedan (2022), 1.8L CVT FWD (140 HP), Hybrid Gasoline.
- raw 1005: Corolla Sedan (2022), 2.0L CVT FWD (196 HP), Hybrid Gasoline.
- نشرات Toyota USA عن 2022 و2023 تذكر 2022 Corolla بنزين 2.0L/169 hp وDynamic Shift CVT في فئات معينة، بينما 2023 Corolla Hybrid بمحرك 1.8L وقدرة نظام 138 hp في السوق الأمريكية. اختلافات السنة والسوق ونوع الدفع تجعلها **أدلة نطاق مقارنة** وليست تطابقًا مع صفّي هجين 140/196hp من سنة 2022.
- OEM_URL_2022: https://pressroom.toyota.com/corolla-keeps-the-fun-rolling-with-2022-apex-nightshade-editions/
- OEM_URL_2023: https://pressroom.toyota.com/toyota-boosts-2023-corolla-hybrid-with-four-new-infrared-edition-new-grades-and-available-awd/
- النتيجة: MARKET_YEAR_POWERTRAIN_CONFLICT_REVIEW / BOTH_NOT_APPROVED. ينبغي البحث عن الكتالوج الأصلي للسوق المقصود قبل تحديد CVT مقابل e-CVT وموديل الناقل.

### 6. GMC Terrain — engines_part_006.csv:1549
- raw: Terrain (2021–2024) 1.5L 9AT (170 HP).
- GM تعلن عن الجيل الجديد **2025** بمحرك 1.5L/175hp، CVT للدفع الأمامي و8AT للدفع الكلي. مصدر 2025 **غير مطابق** لسنة 2021–2024 الخام ولا ينبغي استخدامه لنفي 9AT التاريخية أو إثبات ناقلها.
- OEM_URL: https://news.gm.com/home.detail.html/Pages/news/us/en/2024/aug/0812-25terrain.html
- النتيجة: DIFFERENT_GENERATION_NEGATIVE_SCOPE_ONLY. يتطلب مرجع 2021–2024 لنفس السوق.

## نتيجة الدفعة
previous_32_hint_cases=32
distinct_existing_cases_reexamined=6
new_approved_OEM_gearbox_assignments=0
new_ECU_DTC_links=0
new_raw_vehicle_imports=0
raw_rows_modified=0
records_remaining_not_OEM_approved=32
new_specific_OEM_transmission_family_lead=1
source_scope_comparisons=6
last_reexamined=engines_part_006.csv:1549
next_workstream=FIND_OEM_SOURCES_FOR_UNCOVERED_HINT_CASES_AND_VALIDATE_SAME_YEAR_MARKET_APPLICATION

## حماية
هذه وثيقة مراجعة ملحقة بالتقارير القديمة ولا تحل محلها. لم تُعدَّل قوائم OEM السابقة أو CSV الخام، ولا main أو stable أو Windows أو الموقع أو الصور.
