# DTC NEXIS — الدفعة 85: Hyundai Kona MY2021 — دليل OEM لنوع ناقل IVT

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_SAME_MODEL_YEAR_TRANSMISSION_FAMILY_VERIFIED_FOR_SOUTH_AFRICA / NO_PART_NUMBER_APPROVAL
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_TOYOTA_LC250_MHEV_YEAR_CONFLICT_BATCH84_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv
input_source=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_007.csv:1119
raw=Hyundai Kona (2021), years 2021–2022, 2.0L CVT FWD (147 HP)
source_status=NOT_APPROVED

## 2021 manufacturer source — visual verification
- Hyundai South Africa official Kona OS MY21 specification sheet, dated **July 13, 2021**, PDF physical page index 0, screenshot visually verified:
  https://cdn.hyundai.co.za/Documents/KONA_Specifications.pdf
- **KONA 2.0 EXEC AT MY21**: 1999cc petrol engine, **109.5kW at 6200 rpm** (~147 bhp), 4 cylinders, FWD, transmission **IVT**, described on top table as **8-spd IVT**, which represents IVT simulated steps and does not establish conventional 8AT.
- Separate 1.6 TGDI trim has **7-spd DCT**, which must not be conflated with the 2.0 variant.
- Manufacturer gearbox **assembly model / part number and ECU calibration are not identified** by this brochure.
- Primary manufacturer global 2021 Kona facelift brochure also offers Smartstream G2.0 Atkinson at **149 PS**, which is approximately 147 mechanical hp, but does not give specific IVT gearbox part code or bind it to the same South African trim:
  https://www.hyundai.com/content/dam/hyundai/template_en/en/data/marketing/brochure/product/kona-2021/kona_2021.pdf

## Interpretation
- Raw label CVT describes a broad category; OEM description IVT is manufacturer-specific, for **South Africa MY2021 2.0 FWD**. The match on MY21, FWD and engine power is strong.
- The original queue covers 2021–2022 without market; **cannot** propagate South Africa MY21 IVT to all markets or MY2022, and cannot assign a service gearbox assembly code.
- Prior OEM Kona 2.0 lead referred to a **newer generation**; this new source directly covers MY2021 instead and is therefore stronger applicability evidence.
- Do not replace original 2021–2022 raw row, do not infer that IVT has 8 mechanical forward gears, and do not infer Hyundai-specific DTC/TCM mapping.

## Outcome
existing_hint_cases_reexamined=1
new_model_year_exact_OEM_transmission_family_evidence=1
new_approved_exact_gearbox_part_assignments=0
new_ECU_DTC_links=0
source_rows_modified=0
hint_cases_pending_final_approval=32
next_batch=86
next_workstream=VERIFY_2022_KONA_2_0_IVT_WITH_YEAR_MARKET_AND_OEM_CODE_THEN_OTHER_PENDING_HINTS_AND_1166_CONFLICT_QUEUE

## Data protection
No raw CSV, queue, master library, main/stable, website, Windows, media or DTC data changed.
