# DTC NEXIS — الدفعة 20: خمس حالات Audi ذات ناقل مفقود

date=2026-11-19
branch=review/vehicle-foundation-audit-20261118
base_commit=10f17cdb74a2bfcfb0a791044abe3b84d5a6f00c
status=REVIEW_ONLY / NO_RAW_MODIFICATION / NO_FULL_OEM_FITMENT_APPROVAL
original_list=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_source=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_002.csv
existing_keys: engines_part_002.csv:88,279,398,399,400 (five records)

## Verified scope, not an unconditional import
- :88 Audi A6 Avant (2025), 2.0L TFSI FWD (204 HP), 1984cc, 204 horsepower_numeric, transmission blank. Audi manufacturer 2025 A6 Avant 150 kW (204 PS) FWD paired with 7-speed S tronic. OEM official launch technical material and 2025 model price list: https://www.audi-mediacenter.com/de/publikationen/preislisten/preisliste-audi-a6-avant-modelljahr-2025-1606/download ; https://uploads.audi-mediacenter.com/system/production/uploaded_files/34346/file/ca3329d8541c52a0a7d8ff14e40f441905630a4e/20250304_Audi_A6_Avant_long_EN.pdf?disposition=attachment . Status OEM_FAMILY_2025_7S_TRONIC_EVIDENCE_LEAD, PS/HP unit mismatch unresolved and market/version/gearbox code not yet formally matched. PDF visual confirmation pending; no promotion.
- :279 Audi A8 (2021), 55 TFSI quattro AWD (340 HP), manufacturer refreshed A8 release describes A8 55 TFSI quattro, 3.0 TFSI 250 kW (340 PS) paired to 8-speed tiptronic across engines. Source https://www.audi-mediacenter.com/de/pressemitteilungen/geschaerftes-design-und-innovative-technologien-fuer-das-flaggschiff-der-aufgewertete-audi-a8-14500 . Status OEM_MODEL_FAMILY_8_TIPTRONIC_EVIDENCE, year/sales market and power units still require scoped 2021 document, NOT_APPROVED.
- :398 Audi e-tron Sportback (2019), «S 370 KW (503 HP)», Electric, horsepower_numeric=370 rather than 503 in label. Critical field semantics conflict: 370 appears kW but stored numeric power field, 503 is PS-equivalent approximate; model-year and e-tron S version availability not confirmed. Status POWER_UNIT_AND_MODEL_YEAR_REVIEW, not eligible for gearbox inference.
- :399 Audi RS e-tron GT (2024), raw 856 HP. Audi 2024 facelift announcement and motorsport trim require precise variant and performance rating; not yet proven whether 856 in raw label is HP or PS. https://www.audi-mediacenter.com/en/press-releases/the-new-audi-e-tron-gtan-electrifying-masterpiece-16054 . Status POWER_UNIT_VARIANT_SCOPE_REVIEW, no gearbox finalization.
- :400 Audi RS e-tron GT performance (2024), raw 925 HP; Audi 2024 manufacturer release specifies **925 PS / 680 kW** for performance model, not 925 mechanical bhp. Distinguish electric driveline and two-speed rear axle transmission from a generic 1AT label; no unscoped type fill. Same source. Status POWER_UNIT_PS_HP_MISMATCH_OEM_REVIEW.

## Count and continuation
prior_records_examined=5; new_imports=0; fully_OEM_approved=0; deferred=5; exact_duplicate_rows_removed=0; raw_rows_modified=0; ECU_DTC_links_approved=0.
Reviewed across OTHER batches 11–20: 213 existing records.
last_examined=engines_part_002.csv:400
next_queue_record=engines_part_002.csv:864 Austin 10
Next: compare Austin historic candidates 864+ to original raw fields before deduplication and require OEM evidence for gearboxes. Avoid interpreting generation start as variant production date.
No main merge or Windows/RC changes, no stable channel edits, no publication.
