# DTC NEXIS — الدفعة 71: Mercedes-Benz GLE / Volkswagen Atlas Cross Sport / Hyundai Mistra

date=2026-11-21 | REVIEW_ONLY / OEM_SCOPE_NOT_FINAL_GEARBOX_PART_MATCH / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_SCOPE_RECHECK_BATCH70_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## 1. Mercedes-Benz GLE-Class (2026) — engines_part_010.csv:803
- RAW: 2026, «4MATIC 9AT AWD (537 HP)», Gasoline V8، 750Nm، **بدون اسم GLE 580**؛ git_blob_sha=190ce6216c3301de8f289611dad37202cc86180d.
- Mercedes-Benz Germany official current GLE overview gives **GLE 580 4MATIC** V8 / 3982cc / 395kW (537 PS) / 750Nm / **9G-TRONIC**. This is a very strong candidate to match the 537/750 V8 raw row, but the official model/engine designation is absent from raw data and 537 PS is not strictly 537 mechanical hp.
- OEM_SOURCE: https://www.mercedes-benz.de/passengercars/models/suv/gle/overview.html
- status=HIGH_QUALITY_OEM_VARIANT_CANDIDATE / RAW_TRIM_AND_POWER_UNITS_AND_YEAR_APPLICATION_PENDING.
- لا يثبت رقم قطعة الناقل، رقم RPO، VIN أو ECU ولا يجوز تعديل الوصف العام للصف تلقائيًا.

## 2. Volkswagen Atlas Cross Sport (2026) — engines_part_016.csv:274
- RAW: 2026, «2.0L TSI 4MOTIN 8AT (286 HP)», Gasoline 4-cyl، 350Nm؛ git_blob_sha=8a5e0799e8cfaaddf2bdeef431f31dce7b582622.
- **Volkswagen Canada official MY2026 technical data**: Atlas Cross Sport 2.0 TSI gives **269 hp** at 5,500–6,500 rpm and **8-speed automatic**; 4MOTION AWD available. Power mismatch of 286 vs 269 and ambiguous original typo «4MOTIN». Same model year but market/power mismatch -> cannot approve the raw powertrain.
- OEM_SOURCE: https://www.vw.ca/en/models/new-vehicles/2026-atlas-cross-sport.html/__ui/technical-data.app
- OEM_SECONDARY_PAGE: https://www.vw.ca/en/models/new-vehicles/suv/2026-atlas-cross-sport.html
- status=OEM_8AT_SAME_MODEL_YEAR_MARKET_LEAD / RAW_HP_286_VS_269_CONFLICT / RAW_DRIVE_TEXT_TYPO.
- لا تصحح 286 إلى 269 دون تحديد مصدر 286 والسوق المقصود.

## 3. Hyundai Mistra (2014) — engines_part_007.csv:1166
- RAW: 2014–2017, «1.8L 6AT (143 HP)», Gasoline 4-cyl/1800cc، FWD؛ git_blob_sha=0399f720f92849388bf3c3e33f92441d42b7416f.
- تقرير صناعي تاريخي نشر نوفمبر 2013 عن إطلاق Mistra الصينية 2014 يذكر محرك 1.8L بقوة **146 hp** أو 2.0L بقوة 162hp وخيارات ناقل 6-speed manual أو automatic. بعض كتالوجات السيارات الصينية الثانوية تذكر 1.8L 143hp 6AT؛ قد تختلف القدرة بين مقاييس PS وhp أو النسخ، لكن هذا ليس مصدرًا مصنعياً.
- SECONDARY_NEWS_SOURCE: https://carnewschina.com/2013/11/20/hyundai-mistra-launched-on-the-china-car-market/
- SECONDARY_SPEC_SOURCE: https://en.17vin.com/model/obfax.html
- status=SECONDARY_CHINA_MODEL_6AT_LEAD / NO_PRIMARY_HYUNDAI_OEM_GEARBOX_PART_REFERENCE.
- لا يُعتمد 6AT أو 143hp للمكتبة حتى توفر مستند Hyundai/Beijing Hyundai الأصلي للنسخة/السوق.

## النتائج
existing_hint_cases_reexamined=3
new_approved_OEM_gearbox_code_assignments=0
new_ECU_DTC_links=0
new_vehicle_imports=0
raw_rows_modified=0
hint_cases_still_unapproved=32
next_workstream=REVIEW_OEM_PARTS_AND_APPLICABILITY_FOR_HIGH_CONFIDENCE_VARIANTS_AND_PRESERVE_CONFLICTS

## الحماية
تقارير الأدلة تُضاف فقط إلى فرع المراجعة، ولا تتغير main أو stable أو بيانات الموقع أو Windows أو الصور أو CSV الخام أو الأكواد المعتمدة.
