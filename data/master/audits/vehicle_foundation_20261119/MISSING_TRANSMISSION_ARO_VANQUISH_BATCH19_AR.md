# DTC NEXIS — الدفعة 19: Aro M Series وAston Martin Vanquish

2026-11-19 | REVIEW_ONLY / NO_RAW_CHANGE / NOT_PUBLISHED
base_commit=b75033f1341593c8575e4c45dd752a3b7e5a9c10
branch=review/vehicle-foundation-audit-20261118
queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_001.csv

## نطاق ومصدر
- engines_part_001.csv:763 — Aro M Series (1963), 1963–1975, 2.5, Gasoline, displacement_cc=2512, AWD؛ ناقل مفقود. OEM source for gearbox and version/year not established; NOT_APPROVED.
- engines_part_001.csv:764 — Aro M Series (1959), 1959–1963, 3.2, Diesel, displacement_cc=3260, AWD؛ ناقل مفقود. Distinct generation, year, fuel, and displacement; do not deduplicate with 763; NOT_APPROVED.
- engines_part_001.csv:854 — Aston Martin Vanquish (2024), engine_label «5.2L V12 RWD (835 HP)», source horsepower_numeric=835, raw transmission blank.
  Primary manufacturer launch release dated 2024-09-02:
  https://www.astonmartin.com/en/our-world/news/2024/9/2/aston-martin-vanquish-an-icon-returns-to-reign-supreme
  Manufacturer official specification:
  https://www.astonmartin.com/en-us/models/vanquish
  Supports a 5.2L twin-turbo V12, rear-wheel drive, **ZF eight-speed automatic transmission**, and **835 PS (824 bhp)**. The raw label says 835 **HP**: unit equivalence is not assumed. Manufacturer announcement launched the third-generation Vanquish in 2024; exact market and VIN/specific transmission part number remain unverified.
  status=OEM_MODEL_YEAR_FAMILY_8AT_SUPPORTED_POWER_UNIT_CONFLICT_REVIEW, NOT_FULLY_APPROVED; do not populate source field or manufacturer code automatically.

## Result
previous_rows_examined=3
newly_documented_scoped_manufacturer_evidence=1
newly_approved_full_fitment_records=0
newly_imported_records=0
duplicates_removed=0
deferred=3
original_rows_modified=0
ECU_DTC_links_approved=0
Cumulative reviewed from OTHER list across batches 11–19: 208 existing rows, no full OEM approvals.
last_reviewed_record=engines_part_001.csv:854
next_review_queue_record=engines_part_002.csv:88 Audi A6 Avant (2025)
Next priority: Audi A6 Avant, A8, e-tron, e-tron GT source rows, then Austin historical duplicate candidates. Keep review evidence separate; no merge into main or stable update feed.
