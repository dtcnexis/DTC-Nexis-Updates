# DTC NEXIS — الدفعة 70: SEAT Leon ST / Volkswagen Tiguan 320HP / Toyota Prado

date=2026-11-21 | REVIEW_ONLY / OEM_SCOPE_AND_CONFLICT_CHECK / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_SCOPE_RECHECK_BATCH69_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## 1. SEAT Leon ST — engines_part_014.csv:1033
- RAW: Leon ST Estate (2020), 1.4L TSI 6AT FWD (204 HP), Hybrid، وثيقة المصدر لا تحتوي رمز ناقل؛ raw_git_blob_sha=d16faa05277fc868bb2ed1eb9c890d4275983b77.
- SEAT الرسمية توثق Leon Sportstourer 1.4 eHybrid PHEV 150kW/204PS مع ناقل **6-speed DSG**، وليس تعريفًا عامًا غير محدد 6AT. نص المصدر يستخدم Hybrid ولا يميز PHEV، ويسجل 3 أسطوانات بينما مصدر الشركة لعائلة 1.4 TSI يحتاج تطابق رمز المحرك والأسطوانات والتحقق من سنة وتطبيق السوق.
- OEM_SOURCE: https://www.seat.com/company/news/cars/first-model-offers-five-engines
- status=OEM_PHEV_6_SPEED_DSG_VARIANT_LEAD / RAW_HYBRID_TAXONOMY_AND_CYLINDER_SCOPE_PENDING.
- لا تُرقَّ علبة DSG إلى gearbox part ID ولا يُصحَّح حقل الأسطوانات دون كتالوج المصنع.

## 2. Volkswagen Tiguan — engines_part_016.csv:1729
- RAW: Tiguan (2020), 2.0L TSI 8AT (320 HP), Gasoline، دون تحديد Tiguan R أو الدفع؛ raw_git_blob_sha=8a5e0799e8cfaaddf2bdeef431f31dce7b582622.
- مواصفة Volkswagen R الرسمية الصادرة 2022 تميز Tiguan R بقوة **320 PS** وناقل **7-speed DSG** و4MOTION؛ وهذا يناقض **8AT** في الصف الخام إن كان المقصود Tiguan R الأوروبية. لا يجوز تحويل ذلك إلى يقين تعارض عالمي دون إثبات أن الصف يمثل Tiguan R لا Tiguan آخر في سوق مختلف.
- OEM_SOURCE: https://www.volkswagen-newsroom.com/en/the-volkswagen-r-models-15258/volkswagen-r-models-technical-data-15269
- OEM_LAUNCH_SOURCE: https://www.volkswagen-newsroom.com/en/press-releases/powerful-320-ps-performance-version-of-the-successful-suv-new-tiguan-r-now-available-to-order-6638
- status=HIGH_PRIORITY_GEAR_COUNT_CONFLICT_TIGUAN_R_CANDIDATE / ENGINE_TRIM_MARKET_YEAR_IDENTIFICATION_REQUIRED.
- الصف 1728 (184HP/8AT) حالة منفصلة، لا تُستخدم معلوماته لإثبات حالة 320HP.

## 3. Toyota Land Cruiser / Prado — engines_part_015.csv:1359
- RAW: Land Cruiser / Prado (2024), 2.8L MHEV 8AT AWD (204 HP), Mild Hybrid Diesel, 2755cc؛ raw_git_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36.
- المصدر السابق Toyota USA 2024 يتعلق بمحرك 2.4L i-FORCE MAX بقوة مختلفة، ولا يُثبت مواصفات هذا الديزل 2.8L. لم يُستخلص في هذه الدفعة مصدر OEM مطابق لعام 2024 وسوق محدد ونظام 48V والناقل 8AT لهذه الحالة؛ تبقى مؤجلة بلا تصحيح أو استبدال.
- OEM_US_DIFFERENT_POWERTRAIN_REFERENCE: https://pressroom.toyota.com/2024-toyota-land-cruiser-returns-to-its-origin/
- status=MARKET_AND_HYBRID_ARCHITECTURE_UNVERIFIED / NOT_APPROVED.

## الحصيلة
existing_hint_cases_reexamined=3
new_definitive_gearbox_code_assignments=0
new_ECU_DTC_links=0
new_vehicle_imports=0
high_priority_gear_count_conflict_candidates=1
raw_rows_modified=0
hint_cases_still_not_approved=32
last_reexamined=engines_part_015.csv:1359
next_workstream=VALIDATE_OTHER_2026_OR_UNSOURCED_GEARBOX_HINTS_WITH_PRIMARY_OEM_DOCUMENTS

## الحماية
تقرير ملحق فقط، لا تعديل لملفات المصدر أو main أو stable أو الموقع أو Windows أو الوسائط أو مكتبة DTC المعتمدة.
