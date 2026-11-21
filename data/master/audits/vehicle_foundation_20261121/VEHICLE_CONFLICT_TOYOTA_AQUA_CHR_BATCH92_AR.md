# DTC NEXIS — الدفعة 92: Toyota Aqua 2021 وC-HR 2023 — فحص AWD/E-Four مقابل قدرة النظام الهجين

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_JAPAN_EU_POWERTRAIN_SCOPE / NO_RAW_CORRECTION / NO_RELEASE
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_DACIA_SANDERO_JOGGER_BATCH91_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/engine_transmission_internal_conflicts_batch04.csv
source_file=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_015.csv
source_blob_sha=6ec436f6414f8d5557c6171555ed402fb0a11f36

## 1–2. Toyota Aqua (2021)
- Line 714 raw «1.5L FHEV E-Four eCVT FWD (116 HP)», structured transmission eCVT, structured DRIVE=Front Wheel Drive, 1490cc, power_hp=91.
- Line 715 raw «1.5L FHEV eCVT FWD (116 HP)», structured DRIVE=Front Wheel Drive, 1490cc, power_hp=91.
- Toyota Global **2021-07-19 Japan new Aqua launch** lists **FWD (2WD)** and **E-Four** as **distinct vehicle driveline choices** and defines E-Four as electric four-wheel drive, both paired with THS II based on **M15A-FXE 1.5L**.
- OEM_GLOBAL=https://global.toyota/en/newsroom/toyota/35584064.html
- Toyota Japan 2021 original catalog sheet and official certified-vehicle listing indicate **M15A-FXE 67kW / 91 PS** for the combustion engine; this explains raw field '91' as probable ICE output, while 116HP label is plausibly hybrid combined power. A **first-party source explicitly certifying 116 PS combined system** was not directly located in this audit, so do not claim that detail OEM-confirmed.
- OEM_JAPAN_SPEC=https://toyota.jp/pages/contents/carlineup/archive/aqua/2021-07/pdf/aqua_main_s_202107.pdf
- OEM_JAPAN_CATALOG=https://toyota.jp/ucar/catalog/brand-TOYOTA/car-AQUA/202107/10139543/
- **Line714 has mutually exclusive E-Four and FWD in the same raw label**, and the structured drive likewise says FWD. This is a confirmed *textual drivetrain self-conflict*, but the correct source variant (2WD versus E-Four) still must be determined from individual model/VIN. Line715 is a separate FWD variant and should not be merged with line714 without proof.
- Decision714=HIGH_PRIORITY_DRIVE_TAXONOMY_CONFLICT / ORIGINAL_VARIANT_ID_UNKNOWN / REVIEW_ONLY.
- Decision715=HYBRID_SYSTEM_VS_ICE_POWER_PROVENANCE / MODEL_CODE_VIN_PENDING / REVIEW_ONLY.

## 3–6. Toyota C-HR 2023
- Line 936: raw 1.8L CVT FWD (140 HP) Hybrid Gasoline, structured power=98 and DRIVE FWD.
- Line 937: raw 2.0L CVT AWD (198 HP) Hybrid Gasoline, structured power=152, yet structured DRIVE=Front Wheel Drive.
- Line 938: raw 2.0L CVT FWD (198 HP) Hybrid Gasoline, structured power=152, DRIVE FWD.
- Line 939: raw 2.0L CVT PHEV FWD (223 HP), Plug-in Hybrid, structured power=152, DRIVE FWD.
- Toyota Europe MY2023/2024 new C-HR official press: Hybrid 140 has 1.8L, Hybrid 200 has **2.0L 197 DIN hp** with both FWD and **AWD-i** version, PHEV 220 has 2.0L and **223 DIN hp total system output** with gasoline engine **152 DIN hp**. In Europe these are distinct physical configurations.
- OEM_EU_SOURCE=https://newsroom.toyota.eu/toyota-c-hr-plug-in-hybrid-220--a-concept-car-for-the-road-with-a-dual-dna/
- OEM_EU_PRODUCTION=https://newsroom.toyota.eu/production-of-the-all-new-toyota-c-hr-starts-including-a-plug-in-hybrid-variant-using-a-locally-assembled-battery/
- Lines936/938: label system power vs structured engine power is plausible, but engine-only 98 and 152 values for both HEV trims require specific Toyota technical sheets; difference 197 DIN vs raw 198 may be units/market rounding, not an approved correction.
- Line937 has a **direct AWD vs FWD contradiction in the same source row**, analogous to Aqua E-Four. OEM offers Hybrid 200 AWD-i, but without exact trim/market/VIN cannot decide the original row's intended drivetrain.
- Line939 is strongly explained by **OEM PHEV 152 hp gasoline vs 223 hp combined system**, so should not be considered an incorrect power reading by itself; correct ECU applicability remains a separate matter.
- All transmission codes remain broadly CVT/eCVT terms and cannot be treated as manufacturer assembly part number proof.

## Totals
distinct_original_conflict_cases_reexamined=6
new_direct_raw_drive_label_vs_field_mismatches_identified=2
new_OEM_model_market_proven_powertrain_distinctions=2
new_approved_transmission_VIN_assignments=0
new_approved_ECU_DTC_links=0
source_rows_modified=0
cumulative_unique_conflict_cases_OM_EVIDENCE_REEXAMINED_BATCH88_89_91_92=16
original_conflict_queue_total=1166
final_approved_conflict_row_corrections=0
next_batch=93
next_workstream=STRUCTURED_TOYOTA_REVIEW_SIDECAR_AND_FINAL_CHECKPOINT_OR_FURTHER_OEM_CONFLICT_SAMPLES

## Safety
Data and original review queues unchanged; no edits to main, stable, Windows, site, media, or approved DTC library.
