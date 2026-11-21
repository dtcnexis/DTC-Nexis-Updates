# DTC NEXIS — الدفعة 89: Acura MDX Sport Hybrid وNSX — كشف خلط المحركات والقدرات

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_POWERTRAIN_MISATTRIBUTION_FLAG / NO_AUTOMATIC_REWRITE / NO_RELEASE
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_OEM_RECLASSIFICATION_BATCH88_AR.md
queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/engine_transmission_internal_conflicts_batch02.csv

## الأصل الفني: Acura official data
**2018 MDX USA official specifications** separate *non-hybrid MDX SH-AWD* from *Sport Hybrid SH-AWD*:
- conventional **3.5L V6, 290hp**, **9-speed automatic**.
- Sport Hybrid **3.0L V6, 257hp combustion only**, **321hp total system**, **motor-integrated 7-speed DCT** (plus independent rear electric motor drivetrain).
- OEM: https://acuranews.com/en-US/releases/release-f0252be5c15a47eeab2c587019a90921-2018-acura-mdx-specifications-1-31-18
- 2016 MY conventional MDX official: **3.5L V6 290hp with 9-speed automatic**; it was not advertised as the later MY2017+ Sport Hybrid 321hp version.
- OEM 2016: https://acuranews.com/en-US/releases/release-97ad21e7cf904818ad72162988d0097f-2016-acura-mdx-specifications-features
- Acura corporate technology press says MDX Sport Hybrid appeared MY2017–2020 with **3.0L V6, seven-speed DCT**; hybrid total 321hp:
  https://acuranews.com/en-US/releases/acura-sport-hybrid-super-handling-all-wheel-drive

## Suspicious raw rows
1. engines_part_001.csv:55 «MDX (2018) 3.5L V6 9AT AWD (321 HP)», fuel=Hybrid, structured 3500cc 260hp, 9-Speed automatic. This **combines** non-hybrid 3.5L+9AT with hybrid total 321hp; structured 260hp is not same as official hybrid 257hp and may reflect engine-vs-system or unit source. Cannot treat as valid single OEM MY2018 variant without another market-specific manufacturer document.
2. engines_part_001.csv:58 «MDX (2016) 3.5L V6 9AT AWD (321 HP)», fuel=Hybrid, structured 3500cc 260.6hp, 9-speed automatic. Official MY2016 specs refer to 290hp conventional 3.5L+9AT; 321hp Sport Hybrid exists on later generation years with **3.0L+7DCT**. Very high priority year/powertrain blending.
Raw Git blob for both = 8a2e350c18a0f067aee4f6d03d2c5d7be964cffc.

## Acura NSX hybrid 9DCT
- engines_part_001.csv:66 «NSX (2016) 3.5L V6 9AT AWD (573 HP)», Hybrid, structured 3493cc, 506.9hp, transmission «9-speed automatic DCT».
- Acura OEM 2017 NSX press materials: **3.5L twin-turbo V6 500hp ICE + three motor assistance**, **573hp hybrid system**, **9-speed dual clutch**. Source field «506.9» plausibly reflects metric conversion of ~500 mechanical hp to PS, but source unit/market needs proof. It must NOT automatically be flagged as a genuine power discrepancy; paired ICE/system power may be legitimate.
- OEM: https://acuranews.com/en-US/releases/release-ccbf6f92b0414ce5abf653f74d1169de-2017-acura-nsx-technical-introduction
- OEM: https://acuranews.com/en-US/releases/release-7ad899f8a7aa4077a8e875ccd6bdb518-2017-acura-nsx-press-kit-power-unit
- Status=HYBRID_ICE_VS_SYSTEM_POWER_SEMANTICS_CANDIDATE / RAW_506_9_UNIT_UNVERIFIED / YEAR_SCOPE_NEEDS_CHECK; no link to ECU or new DTC.

## Root cause and model rule
- A single row with fields 'power_hp' and 'engine_label(...HP)' cannot safely represent both **power_engine_ice_hp** and **power_system_combined_hp**; hybrid drivetrain additionally cannot inherit nonhybrid gearbox from same make/model.
- Future derived normalized table should include power_source_type (ICE or system), units (hp/PS/kW), powertrain_variant, transmission_architecture, market, valid_model_years, provenance and fitment flag, but no existing schema changes are authorized by this audit.

## Counts
existing_conflict_records_reexamined=3
new_OEM_powertrain_identity_merge_candidates=2
new_power_semantic_false_positive_candidates=1
fully_corrected_and_reimported_rows=0
approved_ECU_DTC_links=0
original_1166_conflict_rows_remaining_for_final_resolution=1166
next_batch=90
next_workstream=ADDITIONAL_OEM_CONFLICT_SAMPLES_AND_STRUCTURED_REVIEW_DECISION_MATRIX

## Preservation
Review report only. No change to gor3a source, queue, main/stable, website, RC Windows, photos or released DTC library.
