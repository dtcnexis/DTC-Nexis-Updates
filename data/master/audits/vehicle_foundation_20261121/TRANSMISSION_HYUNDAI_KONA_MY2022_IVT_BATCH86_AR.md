# DTC NEXIS — الدفعة 86: Hyundai Kona 2022 — إثبات عائلة IVT للسوق الأمريكية

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_2022_POWERTRAIN_FAMILY_PROVEN / VIN_PART_NUMBER_UNVERIFIED / NOT_PUBLISHED
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH85_AR.md
queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv
raw_source=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_007.csv:1119
raw_git_blob_sha=0399f720f92849388bf3c3e33f92441d42b7416f
raw_label=Hyundai Kona (2021), 2021–2022, 2.0L CVT FWD (147 HP), Gasoline, 4 cylinders, 179Nm
approval=NOT_APPROVED

## Evidence, MY2022
- Hyundai original MY2022 Kona sales brochure, United States, mirrored unchanged by a Hyundai dealer-document host:
  https://cdn.dealereprocess.org/cdn/brochures/hyundai/2022-kona.pdf
- Extracted brochure technical feature table lists **147 hp / 132 lb-ft, 2.0L MPI Atkinson Cycle four-cylinder** for **SE** and **SEL** trims and **Smartstream Intelligent Variable Transmission (IVT)** in exactly these two trims.
- Brochure distinguishes N Line and Limited **1.6L Turbo 195 hp / 7-speed dry DCT**; those must not be transferred to the 2.0L raw row.
- Original 2022 brochure PDF screenshot could not be returned by web (file > screenshot fetch size limit). Consequently classify brochure text verification as **PDF_EXTRACTED_TEXT_ONLY / SCREENSHOT_NOT_AVAILABLE**, not visual PDF verification.
- Independent text transcription of Hyundai Motor America MY2022 Kona product guide also lists 2.0L 147hp with IVT for SE/SEL, and distinct 1.6T/DCT:
  https://manuals.plus/m/39ab2aaf42bf0b79158e834fce527716689dc373f43bb917453808e1b051380a
- The above product guide is a third-party reproduction of manufacturer-origin specifications, not a first-party-hosted live page.
- Hyundai Motor's own first-party MY2021 model generation catalog confirms the **Smartstream G2.0 + IVT** combination in Hyundai's home market but does not establish US MY2022 part fitment:
  https://www.hyundai.com/contents/repn-car/catalog_en/kona-catalog.pdf

## Audit decision
- Strong model year **2022 US** engine/power + trim + gearbox-family support for the raw Kona 2.0 FWD (147 hp) variant.
- Previous batch85 OEM South Africa 2021 brochure confirms 2021 family 2.0 + IVT. Together sources support actual MY2021 and MY2022 model variants, though across separate markets.
- Raw label says CVT; Hyundai markets it as **IVT**, a continuously variable transmission. IVT should not be interpreted as traditional eight-speed automatic.
- Raw record contains no market, trim, VIN, gearbox assembly code, ECU calibration or parts revision. No exact gearbox ID was assigned or imported.
- 2023+ all-new Kona generation technical documents cannot be treated as MY2021–2022 OEM confirmation.

## Counts
existing_hint_cases_reexamined=1
new_same_model_year_transmission_family_confirmations=1
new_OEM_gearbox_assembly_part_numbers_approved=0
new_ECU_DTC_links=0
new_master_vehicle_imports=0
raw_source_rows_modified=0
hint_cases_still_awaiting_full_OEM_approval=32
next_batch=87
next_workstream=VALIDATE_OTHER_PRIORITIZED_HINT_ROWS_AND_LOCATE_CONFLICT_QUEUE_1166

## Protection
No original CSV / queues overwritten, no main or stable changes, no website or Windows RC update, no media and no approved DTC database changes.
