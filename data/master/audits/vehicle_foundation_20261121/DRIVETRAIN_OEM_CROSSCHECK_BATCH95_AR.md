# DTC NEXIS — الدفعة 95: تدقيق OEM لسبع حالات تعارض الدفع

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_DRIVELINE_FAMILY_PROOF / NO_SOURCE_EDIT / NO_RELEASE
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/DRIVETRAIN_SOURCE_WIDE_AUDIT_BATCH94_AR.md
input_sidecar=data/master/audits/vehicle_foundation_20261121/DRIVETRAIN_LITERAL_MISMATCH_REVIEW_BATCH94.csv

## Acura TLX — two distinct powertrain generations
**engines_part_001.csv:111**: raw TLX (2020), years 2020–2024, «2.0L 10AT FWD (272 HP)», structured drive=Rear Wheel Drive.
- Acura/Honda official 2021 TLX press kit: 2.0L turbo 272 SAE hp with **10-speed automatic**, offered as **FWD or SH-AWD**, not RWD. 2021MY marked all-new model; raw label '2020' may be platform/generation-start context, not exact model year.
- OEM https://acuranews.com/en-US/releases/2021-acura-tlx-press-kit
- FINDING: OEM_MODEL_MY2021_FWD_AND_AWD_ONLY / RAW_RWD_FIELD_CONTRADICTS_VALID_2021_VARIANT / FULL_2020_2024_YEAR_SCOPE_PENDING.
**engines_part_001.csv:112**: raw TLX (2020), years 2020–2024, «2.4L 8AT FWD (206 HP)», structured drive=Rear Wheel Drive.
- Acura official 2020 TLX product sheet: 2.4L i-VTEC 206hp **FWD**, **8-speed DCT** (dual clutch, not conventional planetary 8AT). The 2021MY TLX introduced a different 2.0T powertrain, so 2020–2024 raw combined year range should not be assumed to hold for 2.4L.
- OEM https://acuranews.com/en-US/releases/release-f95cc1bc592449a8aa3190578a450057-2020-acura-tlx-specifications
- OEM generation transition https://acuranews.com/en-US/releases/2021-acura-tlx-press-kit
- FINDING: OEM_MY2020_2_4_FWD_8DCT / RAW_RWD_FIELD_INCORRECT_FOR_DOCUMENTED_US_2020_VARIANT / MULTI_YEAR_MISATTRIBUTION_CANDIDATE.

## Alfa Romeo 75 — two engine variants, RWD platform
**engines_part_001.csv:365**: Alfa 75 (1985–1992), label 2.0 Twin Spark 5MT RWD (128hp), structured Front Wheel Drive, structured power=148hp. This row also appears in original 1,166 conflict queue due to a power discrepancy. Do NOT collapse its separate power and drive issues into only one.
**engines_part_001.csv:367**: Alfa 75 (1985–1992), 3.0 V6 5MT RWD (188hp), structured Front Wheel Drive.
- Stellantis official Heritage story identifies Alfa 75 as the last rear-wheel drive mainstream Alfa before Giulia; includes Twin Spark and 3.0 V6 engine versions. This is original-manufacturer evidence of platform drivetrain, not per-market HP or VIN/gearbox evidence.
- OEM https://www.heritagehubitaly.com/en-uk/heritage/stories/alfa-romeo-75
- FINDING: HIGH_CONFIDENCE_PLATFORM_RWD_NOT_FWD / EXACT_MY_ENGINE_HP_AND_TRANSMISSION_PART_PENDING; raw source never silently corrected.

## Toyota Corolla Sedan — MY2020 model, two gearbox variants
**engines_part_015.csv:1010**: Corolla Sedan (2019), years 2019–2022, 2.0L 6MT FWD (169hp), structured Rear Wheel Drive.
**engines_part_015.csv:1011**: Corolla Sedan (2019), same years, 2.0L CVT FWD (169hp), structured Rear Wheel Drive.
- Toyota official US MY2020 Corolla Sedan launch and US 2020 product specifications: 2.0L Dynamic Force **169hp**, **available six-speed iMT or Dynamic Shift CVT** with front-wheel drive platform. Raw generation start 2019 may reference launch, not necessarily US MY2019 Corolla powertrain.
- OEM https://pressroom.toyota.com/all-new-2020-toyota-corolla-ready-to-rock-the-sedan-world/
- OEM secondary MY2020 https://pressroom.toyota.com/driving-and-design-highlight-the-all-new-2020-toyota-corolla/
- FINDING: STRONG_US_MY2020_FWD_VS_RAW_RWD_FIELD_CONFLICT / RAW_2019_YEAR_GENERATION_SCOPE_UNVERIFIED.

## Audi 100/200 quattro — self contradictory label
**engines_part_001.csv:917**: 100/200 (1982), years 1982–1991, 2.2L **quattro** 5MT **FWD** (138hp), field All Wheel Drive.
- Audi official Quattro background defines quattro as its AWD technology. This is a self-contradictory raw label; the AWD field and quattro designation agree **in system family**, but a 2.2L variant's precise year-market/engine output and vehicle model code remain unverified.
- OEM https://www.audi-mediacenter.com/en/more-than-40-years-of-quattro-14240
- FINDING: LABEL_SELF_CONTRADICTION / OEM_QUATTRO_AWD_CONCEPT_CONFIRMED / RAW_SPECIFIC_APPLICATION_PENDING.

## Results and non-destructive rules
distinct_drive_candidate_rows_reexamined=7
overlap_with_original_1166_queue_among_these=1
new_exclusively_drive_only_candidates_oem_reviewed=6
new_approved_OEM_vehicle_master_corrections=0
new_approved_exact_gearbox_VIN_assignments=0
new_ECU_DTC_links=0
original_files_edited=0
next_batch=96
next_workstream=APPEND_SEVEN_OEM_DRIVE_CANDIDATES_TO_NEW_SIDE_CAR_AND_CONTINUE_PRIORITY_CASES

## Safety
These are research findings, not approved data corrections. Keep raw source and every prior review queue unchanged. No merge main/stable, no Windows/site edits or media collection.
