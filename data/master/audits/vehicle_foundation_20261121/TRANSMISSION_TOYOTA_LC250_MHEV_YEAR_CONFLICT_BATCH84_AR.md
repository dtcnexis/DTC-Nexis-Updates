# DTC NEXIS — الدفعة 84: Toyota Land Cruiser 250 / Prado 2024 — تعارض سنة إدخال MHEV

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_EUROPE_MODEL_YEAR_POWERTRAIN_CONFLICT / NO_RELEASE
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_LEXUS_OFFICIAL_BROCHURE_BATCH83_AR.md
input_row=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_015.csv:1359
original_engine_label=2.8L MHEV 8AT AWD (204 HP)
original_model=Land Cruiser / Prado (2024)
original_fuel=Mild Hybrid Diesel
original_cc=2755
original_torque=500Nm
source_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36

## وثائق Toyota Europe الأصلية
1. World premiere 2023 / European new LC250: first European 2024 Land Cruiser has **2.8L turbo-diesel 204 DIN hp** and new **eight-speed Direct Shift automatic**; Toyota announced **48V mild hybrid variant in 2025**.
   https://newsroom.toyota.eu/going-back-to-its-origins-world-premiere-of-the-all-new-toyota-land-cruiser/
2. Toyota official detailed 2024 Land Cruiser launch article says 2.8L diesel / 204 DIN hp and 8-speed Direct Shift, and that **mild hybrid 48V would join European range late 2025**.
   https://newsroom.toyota.eu/the-all-new-toyota-land-cruiser-a-modern-icon-true-to-its-heritage/
3. Toyota official June 2025 Hybrid 48V launch explicitly connects the **existing 2.8L diesel engine and eight-speed Direct Shift transmission** to a mild hybrid motor-generator and 48V battery.
   https://newsroom.toyota.eu/introducing-the-land-cruiser-hybrid-48v-a-new-powertrain-for-toyotas-legendary-suv/
4. Australia September 2025 Toyota Prado technical table also offers a 48V system; this is a different market and publication date, cannot establish the 2024 European variant.
   https://www.toyota.com.au/-/media/toyota/main-site/vehicle-hubs/prado/files/20250924_landcruiser_prado_spec_table_gto009429.pdf?rev=bfa49fe083624edfa2c5dc5d51d20ff4

## Analysis
- Genuine MY2024 European Land Cruiser 250 diesel 2.8L 204 DIN hp **8AT family is supported by OEM**, but the raw row's **MHEV** drivetrain classification is **not** substantiated by Toyota Europe for the 2024 launch vehicle.
- The 2025 48V introduction matches the MHEV family and 8-speed Direct Shift but needs market, actual MY and VIN. The raw year=2024 may be a *generation start*, not an actual 2024 MHEV model year.
- IMPORTANT: Do not infer impossibility of 2024 mild hybrid in all markets from European launch documents. Toyota Australia and other markets must be reviewed separately.
- No exact gearbox assembly/model code has been established by these documents; 'Direct Shift' is a marketed gearbox family, not an OEM service parts ID.
- Do not automatically rewrite Mild Hybrid Diesel to Diesel or change year_start. First split **generation start year** from **powertrain availability start year** under a verified market/year model.

## Results
existing_hint_cases_reexamined=1
high_priority_year_powertrain_conflict_flags=1
new_approved_exact_gearbox_parts=0
new_approved_ECU_DTC_links=0
source_rows_modified=0
remaining_hint_cases_final_approval_pending=32
next_batch=85
next_workstream=VALIDATE_OTHER_UNAPPROVED_HINT_CASES_AND_RECONCILE_CONFLICT_QUEUES

## Safety
Original CSV, review queues, main, stable, website, Windows and DTC database remain unchanged. No images created or collected.
