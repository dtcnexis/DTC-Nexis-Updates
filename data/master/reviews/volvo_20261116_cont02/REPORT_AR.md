# Volvo — DTC NEXIS — Continuation 02 — 2026-11-16

**DRAFT: not for release or merge.** Original Volvo brand file on main is unchanged.

## Validated counts
- 60 original full DTCs; 14 earlier branch additions; 33 new this batch => 107 unique full DTC/ECU values.
- 4 previously known codes gained additional TJ evidence without being re-counted.
- 0 duplicate full codes in 107.
- 25 earlier deferred review items + 36 newly queued = 61 review entries.
- 2 older brake review items lacked id; preserved originals and created stable ID mapping separately.
- 0 images generated; image gathering remains on hold.

## New-code groups
- CAM/VVT: 8 ECM codes.
- Crankcase ventilation: 3 ECM codes.
- 48V supply: 3 ISGM codes.
- EVAP/Lambda/oil pump: 3 ECM codes.
- PHEV battery: 1 BECM code.
- Thermostat/coolant: 2 ECM codes.
- Rear axle inverter: 2 IEM codes.
- CDD/EV module: 2 BECM/VCU1 codes.
- Hesitation/misfire: 9 ECM codes.

## Sources
Volvo Car USA Technical Journals 37618.3.8, 37710.2.2, 37103.3.0, 37236.1.0, 37166.3.0, 37316.1.0, 37373.8.0, 37288.4.0, 37495.2.0, 37771.2.0, 37935.2.0. Their URLs, status dates and application tables are inside the supplementary JSON.

## Unresolved technical checks
- Confirm full official VIDA definition and SAE/J2012DA classification, including Failure Type suffix.
- Confirm Swedish and European fitment by VIN, engine, year and ECU. Source technical journals are US/Canada scoped.
- Confirm current revisions and software eligibility in VIDA, including newer Volvo Bookstore TJ 37373.9.0.
- Expand ABS/SRS/Body/CAN/TCM and older/other drivetrain units.
- No image, wiring or voltage threshold invented or adopted; preserve previously collected media.

## Files
- data/master/brands/volvo_tj_20261116_cont02.json
- data/master/reviews/volvo_20261116_cont02/REVIEW_QUEUE.json
- data/master/reviews/volvo_20261116_cont02/LEGACY_REVIEW_ID_MAPPING.json
- data/master/reviews/volvo_20261116_cont02/CONSOLIDATED_QA.json

All files are on a draft Volvo branch, no application, stable feed, installer, program or main change.
