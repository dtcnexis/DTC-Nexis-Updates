# DTC NEXIS — الدفعة 73: Alpine A110 345HP وToyota Corolla Hybrid 140/196HP

date=2026-11-21 | REVIEW_ONLY / SOURCE_YEAR_TRIM_CONFLICT / NO_RELEASE
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_SCOPE_RECHECK_BATCH72_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## 1. Alpine A110 — engines_part_001.csv:717
- RAW: A110 (2024), 2024, «1.8L 7AT RWD (345 HP)», 1798cc, torque 420Nm; source_blob_sha=8a2e350c18a0f067aee4f6d03d2c5d7be964cffc.
- Alpine official March 2024 Turkish launch mentions regular A110/A110 GT/A110 S with 1.8 turbo and Getrag 7-speed double wet clutch, **but this is not 345HP evidence**:
  https://media.alpinecars.com/alpine-comes-to-turkiye-with-its-first-point-of-sale-in-istanbul/?lang=eng
- Alpine announced **A110 R Ultime** at October 2024 Paris Motor Show, with **345hp on RON102**, **420Nm**, and **a new DW6 gearbox with higher torque capacity**; later press materials 2025 anticipate deliveries in early 2026. This matches the raw 345HP/420Nm numerical fingerprint much more closely than ordinary A110 range, yet the raw model name lacks «R Ultime» and its «2024» may reflect unveiling date rather than production/market model year. Do not silently replace model/gearbox.
  https://media.alpinecars.com/alpine-a110-r-ultime-the-most-high-performance-production-car-a110-ever-created-by-alpine/?lang=fra
  https://media.alpinecars.com/alpine-a110-r-ultime-the-most-extreme-a110-ever-press-kit/?lang=eng
- FINDING=HIGH_PRIORITY_TRIM_AND_GEARBOX_ARCHITECTURE_MISATTRIBUTION_CANDIDATE; OEM_DW6_GEARBOX_LEAD_FOR_R_ULTIME_ONLY; RAW_A110_2024_NOT_APPROVED.
- Next: locate OEM parts/vehicle homologation for R Ultime and check gear count, production/model year, 345HP vs unit conversion, engine 1798cc, 420Nm, and country.

## 2. Toyota Corolla Sedan 1.8 Hybrid — engines_part_015.csv:1004
- RAW: Corolla Sedan (2022) Hybrid Gasoline 1.8L, CVT FWD, **140HP**, 9.2s 0–100, source_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36.
- Toyota UK official announcement of **new MY2023 Corolla** (Nov 2022) gives 5th generation 1.8-litre hybrid **138bhp** total output, 9.2s 0–62mph; 138bhp is about 140 DIN hp (PS), suggestive of a measure-conversion and generation mismatch rather than proven wrong power figure. Report addresses European Corolla range and **does not validate a particular Sedan** configuration.
  https://media.toyota.co.uk/toyota-announces-the-new-2023-corolla/
- FINDING=HIGH_PRIORITY_2022_VS_2023_MODEL_YEAR_AND_PS_BHP_CONVERSION_CANDIDATE / SEDAN_BODY_SCOPE_PENDING.

## 3. Toyota Corolla Sedan 2.0 Hybrid — engines_part_015.csv:1005
- RAW: Corolla Sedan (2022) Hybrid Gasoline 2.0L, CVT FWD, **196HP**, 7.5s 0–100.
- Toyota UK new MY2023 Corolla: 2.0L Hybrid 193 bhp (about **196 DIN hp**) and 0–62 mph 7.5s. These match the raw 196/7.5 numerical fingerprint, but Toyota UK marketing covered hatchback/Touring Sports; raw calls it Sedan (2022). An exact same-body, same-market, same-year OEM homologation has NOT been identified.
  https://media.toyota.co.uk/toyota-announces-the-new-2023-corolla/
- FINDING=HIGH_PRIORITY_2023_EUROPE_HATCHBACK_POWERTRAIN_ASSOCIATION_NOT_SEDAN_CONFIRMATION / YEAR_BODY_MARKET_UNRESOLVED.
- Do not interpret the 196HP number as necessarily Corolla Cross; Toyota UK source independently confirms 2.0L Corolla family with 196 DIN hp. Equally do not overwrite Sedan 2022 with Hatchback 2023.

## نتائج
existing_cases_reexamined=3
new_approved_exact_gearbox_vehicle_assignments=0
new_ECU_DTC_links=0
new_vehicle_imports=0
confirmed_duplicate_deletions=0
raw_rows_modified=0
priority_trim_generation_mismatch_cases=3
hint_cases_still_not_approved=32
next_workstream=RECONCILE_SOURCE_MODEL_YEAR_VS_ANNOUNCEMENT_YEAR_AND_VEHICLE_BODY_AND_MARKET_THEN_OEM_GEARBOX_ID

## سلامة المصدر
هذه مراجعة مراجع OEM للهوية، ولا تعدّل الصفوف الأصلية أو main أو stable أو الموقع أو برنامج Windows أو الصور أو مكتبة DTC المعتمدة.
