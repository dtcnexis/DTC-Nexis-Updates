# DTC NEXIS — الدفعة 72: Ford 8F35 / Cadillac 9T50 / Toyota Corolla Hybrid applicability

date=2026-11-21 | REVIEW_ONLY / OEM_SOURCE_VERIFIED_FAMILY / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH71_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## المبدأ
المراجعة تخص 4 صفوف موجودة في قائمة التلميحات 32، لا إضافات مكتبة جديدة. رمز عائلة ناقل مُثبت لوثيقة موديل محدد لا يعني رقم قطع متطابقًا مع كل VIN أو سنة أو سوق؛ يجب فصل الأدلة عن الإسناد النهائي.

## 1. Ford Transit Connect — engines_part_006.csv:1276
- RAW: Transit Connect Wagon (2018), 2018–2023, 2.0L GDI 8AT (150 HP), Gasoline 1999cc/4cyl; source_git_blob_sha=2622eaa2d8a10316d2e7a9561d3182061f51ffce.
- دليل مالك **2020 Transit Connect US** من Ford يحدد الرمز **8F35** للناقل الأوتوماتيكي 8 سرعات، ويعرض الكود «8» على Safety Compliance Certification Label. دليل موديل 2019 أيضًا يتضمن ناقل 8F35 حسب إصدار سوق/دليل آخر؛ يجب الانتباه إلى أن دليل 2018 المعيّن في أرشيف Ford يسرد 6F35 في إحدى نسخه.
- OEM_SOURCE_2020: https://www.fordservicecontent.com/Ford_Content/vdirsnet/OwnerManual/Home/Content?ProcUid=G1965212&Uid=G1965211&buildtype=web&countryCode=USA&div=f&languageCode=en&moidRef=G1405423&userMarket=USA&vFilteringEnabled=False&variantid=7408
- OEM_SOURCE_2018: https://www.fordservicecontent.com/Ford_Content/vdirsnet/OwnerManual/Home/Content?ProcUid=G1708465&Uid=G1608812&buildtype=web&countryCode=USA&div=f&languageCode=en&userMarket=usa&vFilteringEnabled=False&variantid=6040
- FINDING: OEM_8F35_TRANSMISSION_FAMILY_IDENTIFIED_FOR_2020_MODEL_GUIDE. RAW 2018–2023 GENERATION_SPAN_NOT_FULLY_VALIDATED. لا إسناد 8F35 إلى جميع المركبات أو تحديد مواصفات ECU/PCM دون VIN/البناء/السوق.

## 2. Cadillac XT4 — engines_part_003.csv:1846
- RAW: XT4 (2023), years 2023–2025, 2.0L Turbocharged 9AT FWD (238 HP), torque 350Nm; source_git_blob_sha=3796acc7f93b581a449480f958097be2937788bc.
- GM Cadillac **2024 USA** confirms **Hydra-Matic 9T50 nine-speed automatic** with 235hp/350Nm 2.0L turbo. Correlation with 350Nm and family is strong, but 235hp vs RAW 238hp and 2023–2025/specific market/FWD applicability need reconciliation.
- OEM_SOURCE: https://news.gm.com/home.detail.html/Pages/news/us/en/2023/feb/0220-xt4.html
- FINDING: OEM_9T50_FAMILY_IDENTIFIED_MY2024_ONLY / RAW_POWER_AND_YEAR_APPLICATION_PENDING.

## 3. Toyota Corolla Sedan — engines_part_015.csv:1004
- RAW: Corolla Sedan (2022), **Hybrid Gasoline** 1.8L «CVT FWD (140 HP)»; source_git_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36.
- Toyota USA press MY2022 reports **121hp combined hybrid system output** for 1.8L, and Toyota notes the hybrid uses an electronically controlled planetary transaxle/e-CVT family. 140hp RAW may reflect different global-market generation/specification, not a proven US-market 2022 vehicle. Nonhybrid CVT/e-CVT must not be conflated.
- OEM_SOURCE: https://pressroom.toyota.com/corolla-hybrid-legendary-value-epic-mpg/
- OEM_TRANSAXLE_CONTEXT: https://pressroom.toyota.com/vehicle/2020-toyota-corolla/
- FINDING: POWER_MARKET_AND_ECVT_FAMILY_REVIEW / RAW_140HP_NOT_MATCHED_TO_US_MY2022.

## 4. Toyota Corolla Sedan — engines_part_015.csv:1005
- RAW: Corolla Sedan (2022), **Hybrid Gasoline** 2.0L «CVT FWD (196 HP)»; source_git_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36.
- Toyota official US specifications for MY2022 distinguish gasoline 2.0L **Dynamic Shift CVT** on SE/XSE from hybrid 1.8L **ECVT** on Hybrid LE. The raw 2.0L/196hp/Hybrid combination therefore cannot be validated against this specific US brochure. In separate Toyota 2023 vehicles, 196hp appears for Corolla Cross Hybrid, which is a different body/model; does NOT justify relabeling RAW Corolla Sedan as Corolla Cross.
- OEM_SOURCE: https://www.toyota.com/content/dam/toyota/brochures/pdf/2022/corolla_ebrochure.pdf
- OEM_CROSS_BODY_REFERENCE: https://pressroom.toyota.com/sporty-efficient-toyota-corolla-cross-hybrid-heads-to-dealers-this-summer/
- FINDING: HIGH_PRIORITY_HYBRID_NONHYBRID_CVT_APPLICATION_CONFLICT / 2_0L_196HP_RAW_OEM_SCOPE_MISSING.

## نتيجة الدفعة
existing_cases_reexamined=4
OEM_transmission_family_names_found=2
new_approved_exact_vehicle_gearbox_assignments=0
new_ECU_DTC_links=0
new_library_vehicle_imports=0
raw_records_modified=0
hint_cases_still_unapproved=32
next_workstream=CHECK_2018_2023_FORD_8F35_YEAR_COVERAGE_AND_TOYOTA_GLOBAL_MARKET_HYBRID_CATALOGS

## الحماية
لا تغيير لمصادر CSV أو قوائم المراجعة أو main أو stable أو الموقع أو Windows أو الصور أو سجلات DTC.
