# DTC NEXIS — الدفعة 101: Mercedes-Benz 4MATIC ومشكلة تداخل RWD/AWD

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / 4MATIC_OEM_ARCHITECTURE_EVIDENCE / EXACT_VARIANT_FITMENT_PENDING / NO_RELEASE
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/VEHICLE_DRIVETRAIN_OEM_CHECKPOINT_BATCH100_AR.md
input_source=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_009.csv
source_blob_sha=40e1c3019328b6375e0b367759ad6836d9af61bb
input_queue=data/master/audits/vehicle_foundation_20261121/DRIVETRAIN_LITERAL_MISMATCH_REVIEW_BATCH94.csv

## OEM manufacturer context
- Mercedes-Benz official 2018 C-Class Saloon/Estate launch separates C 200 (1.5L/184hp/9G-TRONIC) and C 200 **4MATIC** (same 184hp/9G-TRONIC), specifying that the latter has **permanent all-wheel drive**, with default torque distribution front/rear 45/55. Both variant names matter. OEM:
  https://media.mercedes-benz.com/en/article/8fd535c5-db8c-4979-8668-0479918cbd43
- Mercedes-Benz 2021 C-Class All-Terrain brochure verifies 4MATIC as all-wheel drive plus 9G-TRONIC; model year and body style differ and cannot prove 2018 cabriolet/2026 variants:
  https://media.mercedes-benz.com/en/article/32fe50af-5011-4792-b09c-2de5d5bfd1fa
- Mercedes-Benz 2024 official 4MATIC technology roundup again treats 4MATIC as all-wheel drive, across powertrains:
  https://media.mercedes-benz.com/en/press-kit/9d01948e-c320-4680-a71e-26be1d1b382c

## Eight existing source rows and controlled findings
1. engines_part_009.csv:716; A-Klasse (2012–2015), «220 4MATIC 7AT FWD (183 HP)», structured All Wheel Drive. **Label contains both 4MATIC AWD and FWD**. 4MATIC means AWD, but exact A 220 MY2012 gear, market and power output not checked. Status=LABEL_SELF_CONTRADICTION_OEM_BRAND_ARCHITECTURE_ONLY.
2. engines_part_009.csv:920; C-Class Cabriolet (2018–2022), «C 200 RWD (184 HP)», structured All Wheel Drive. 2018 manufacturer distinguishes C 200 non-4MATIC versus C 200 4MATIC: cannot decide from generic C 200 name alone whether field AWD belongs to specific cabriolet. Status=MODEL_VARIANT_4MATIC_FLAG_MISSING_OR_FIELD_MIX_PENDING.
3. engines_part_009.csv:923; C-Class Cabriolet (2018–2022), «C 300d 4MATIC ... AWD (245 HP)», structured Rear Wheel Drive. **4MATIC vs RWD** conflict; 2018 source proves 4MATIC architecture in C-Class, but not exactly this engine/body market and year. Status=4MATIC_BRAND_TYPE_CONFLICT_NEEDS_VARIANT_FITMENT.
4. engines_part_009.csv:970; C-Klasse (2026), «C 250 4MATIC EQ Boost MHEV 9AT RWD (218 HP)», structured Rear Wheel Drive. Self-contradictory label 4MATIC vs RWD. No direct manufacturer evidence for 2026 C250 4MATIC 218hp matched in this batch. Status=HIGH_PRIORITY_2026_MODEL_IDENTITY_AND_AWD_SELF_CONTRADICTION.
5. engines_part_009.csv:973; C-Klasse (2026), «C 250d MHEV EQ Boost 4MATIC 9AT RWD (200 HP)», structured Rear Wheel Drive. Self-contradictory 4MATIC/RWD; no exact 2026 C250d trim/engine OEM source. Status=HIGH_PRIORITY_OEM_MODEL_NAME_AND_MARKET_GATE.
6. engines_part_009.csv:983; C-Klasse (2018–2021), «C 200 9AT 4MATIC AWD (184 HP)», structured Rear Wheel Drive. 2018 manufacturer *specifically* names **C200 4MATIC 1.5L 184hp 9G-TRONIC AWD**; stronger same powertrain + year evidence, though exact body country and VIN remain absent. Status=OEM_MY2018_C200_4MATIC_FAMILY_MATCH / FIELD_RWD_SUSPECT.
7. engines_part_009.csv:986; C-Klasse (2018–2021), «C 400 4MATIC 9AT AWD (333 HP)», structured Rear Wheel Drive. 4MATIC is AWD; exact 333hp C400 model year/market may be earlier than start year 2018; cannot assume 2018 model. Status=O_E_M_IDENTITY_YEAR_CHECK.
8. engines_part_009.csv:992; C-Klasse (2018–2021), «C 300d 9AT 4MATIC AWD (245 HP)», structured Rear Wheel Drive. 4MATIC AWD architecture confirmed in same model family; particular diesel powertrain and MY require exact source. Status=O_E_M_VARIANT_YEAR_MATCH_PENDING.

## Results
existing_drive_source_rows_reviewed=8
label_self_contradictions_in_this_batch=3
new_final_approved_VIN_drivetrain_corrections=0
new_OEM_gearbox_assembly_assignments=0
new_ECU_DTC_links=0
source_rows_modified=0
next_batch=102
next_workstream=RECONCILE_ALL_NEW_8_MERCEDES_WITH_PREVIOUS_SIDE_CARS; PRODUCE_DETERMINISTIC_CHECKPOINT

## Preservation
No changes to original gor3a CSV, old 1166 conflict queues, raw vehicle catalogs, main, stable, Windows RC3.8.0/RC3.8.2, website, images or approved DTC records.
