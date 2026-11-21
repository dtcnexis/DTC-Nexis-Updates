# DTC NEXIS — الدفعة 97: BMW — سبعة سجلات نظام دفع ورمز محرك وتواريخ أجيال

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / BMW_MANUFACTURER_FAMILY_VERIFICATION / NOT_PUBLISHED
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/DRIVETRAIN_OEM_TRIAGE_BATCH96.csv
input_queue=data/master/audits/vehicle_foundation_20261121/DRIVETRAIN_LITERAL_MISMATCH_REVIEW_BATCH94.csv
raw_source=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_002.csv
raw_git_blob_sha=3a281ebfce241e7849e4db09dcaa9e385986274e

## BMW 1 Series M135 xDrive — engines_part_002.csv:1148
- Raw MY-generation 2024, «M135 xDrive 7AT AWD (300 HP)», structured drivetrain=Front Wheel Drive.
- BMW official worldwide 2024 1 Series technical press confirms **300 hp M135 xDrive**, **standard intelligent all-wheel-drive**, **7-speed Steptronic dual-clutch**.
- OEM https://www.press.bmwgroup.com/global/article/detail/T0442625EN/the-all-new-bmw-1-series?language=en
- Finding=EXACT_MY2024_OEM_AWD_FAMILY_PROOF / RAW_FWD_FIELD_MISMATCH. Brand 7AT is broad, actual 7-speed DCT should remain explicit; no VIN gearbox or ECU part yet.

## BMW 1 Series 128ti — engines_part_002.csv:1152
- Raw generation 2019–2024, «128ti 8AT FWD (265 HP)», structured drivetrain=Rear Wheel Drive.
- BMW official October 2020 128ti release identifies **265 hp, exclusively front-wheel drive, eight-speed Steptronic Sport** and November 2020 launch.
- OEM https://www.press.bmwgroup.com/global/article/detail/T0318069EN/the-new-bmw-128ti
- Finding=OEM_2020_FWD / RAW_RWD_CONTRADICTION / 2019_YEAR_START_NOT_PROVEN_VARIANT_LAUNCH.

## BMW 2 Series Gran Coupe 218i — engines_part_002.csv:1485 and 1486
- Raw 1485 «218i 6MT RWD (140 HP)», field Front Wheel Drive, cylinders=4, cc=1499.
- Raw 1486 «218i 7AT RWD (140 HP)», field Front Wheel Drive, cylinders=4, cc=1499, transmission structured 7-speed DCT.
- BMW worldwide 2019 launch release confirms **FWD platform**, **1.5L three-cylinder 140hp** engine in 218i with **six-speed manual or optional seven-speed Steptronic DCT**, depending on region.
- OEM https://www.press.bmwgroup.com/global/article/detail/T0301580EN/the-first-ever-bmw-2-series-gran-coupe?language=en
- OEM technical docs https://www.press.bmwgroup.com/global/article/attachment/T0322638EN/468207
- Findings=RAW_RWD_LABEL_SUSPECT / RAW_STRUCTURED_FWD_FAMILY_CONSISTENT; **cylinder-count field 4 vs official 3 is a separate source discrepancy** that must NOT be rewritten without exact same-market MY engine variant.
- 2019 raw generation start may be announcement date; deliveries began in early 2020. Never infer that all 2019–2024 markets offered both transmissions.

## BMW 2 Series Gran Coupe M235i xDrive — engines_part_002.csv:1487
- Raw «M235i xDrive 8AT AWD (306 HP)», structured Front Wheel Drive.
- BMW original 2019 world launch: **M235i xDrive** 306hp with **BMW xDrive AWD**, eight-speed Steptronic. FWD platform architecture does NOT mean this top-performance *xDrive variant* is FWD.
- OEM https://www.press.bmwgroup.com/global/article/detail/T0301580EN/the-first-ever-bmw-2-series-gran-coupe?language=en
- OEM NZ market https://www.press.bmwgroup.com/new-zealand/article/detail/T0306244EN/first-ever-bmw-2-series-gran-coup%C3%A9-launches-in-new-zealand
- Finding=HIGH_CONFIDENCE_MODEL_FAMILY_AWD / RAW_DRIVE_FWD_FIELD_SUSPECT / VIN_SCOPE_PENDING.

## BMW 3 Series Touring 320i 2019 — engines_part_002.csv:1549
- Raw «320i 8AT RWD (184 HP)», structured Front Wheel Drive.
- BMW official June 2019 3 Series Touring release specifies 320i 184hp 2.0L and classic rear-drive layout for non-xDrive trims. xDrive AWD is separate and offered for specified versions.
- OEM https://www.press.bmwgroup.com/ireland/article/detail/T0297368EN/the-new-bmw-3-series-touring?language=en
- OEM detailed model variant description https://www.press.bmwgroup.com/global/article/detail/T0297109EN/specifications-of-the-new-bmw-3-series-touring-valid-from-06/2019?language=en
- Finding=OEM_PLATFORM_RWD_FAMILY / RAW_FIELD_FWD_CONTRADICTION / MARKET_AND_MY_SCOPE_PENDING.

## BMW 318d xDrive Touring 2012/2013 — engines_part_002.csv:1604
- Raw «318d xDrive 6MT AWD (143 HP)», structured Rear Wheel Drive, generation 2012–2016.
- BMW official summer 2013 release confirms the **BMW 318d xDrive Touring** with **105kW/143hp diesel, xDrive four-wheel-drive**. Raw year start 2012 may be generation, not xDrive trim availability.
- OEM https://www.press.bmwgroup.com/global/article/detail/T0141144EN/bmw-model-upgrade-measures-taking-effect-from-the-summer-of-2013
- Finding=OEM_MY2013_DRIVETRAIN_4WD / RAW_RWD_FIELD_CONFLICT / RELEASE_YEAR_SCOPE_NEEDS_VALIDATION.

## Aggregate for this report
distinct_original_source_rows_reexamined=7
new_BMW_cylinder_count_anomaly_flags=2
new_approved_exact_market_VIN_vehicle_corrections=0
new_approved_gearbox_ECU_DTC_links=0
raw_originals_modified=0
next_batch=98
next_workstream=SAVE_BMW_OEM_EVIDENCE_SIDE_CAR_AND_COMMIT_CROSS_QUEUE_CHECKPOINT

## Protection
Only append source-linked review reports; no data edits or main/stable/Windows/website/assets/DTC release.
