# DTC NEXIS — الدفعة 99: 28 سجل smart fortwo / fortwo Cabrio ذات اختلاف FWD/RWD

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_PLATFORM_FAMILY_EVIDENCE / NO_VIN_OR_ENGINE_TRANSMISSION_APPROVAL
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/DRIVETRAIN_BMW_OEM_TRIAGE_BATCH98.csv
input_queue=data/master/audits/vehicle_foundation_20261121/DRIVETRAIN_LITERAL_MISMATCH_REVIEW_BATCH94.csv

## مصدر الحالات
- Source: data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_014.csv (part file).
- Exact source row keys preserved in batch94 CSV: **28** rows (smart fortwo 17 entries; smart fortwo Cabrio 11 entries).
- Relevant lines **1835–1852** (with gaps) and **1866–1876**. The sidecar stores precise line IDs; do not treat these as complete inclusive sequences.
- All 28 raw engine labels include **FWD**, and structured drive column contains **Rear Wheel Drive**. This is a source-text/structured-field conflict in 28 unique rows, not 28 separately OEM-verified individual transmission variants.
- Raw engine years span early fortwo models 1998, 2000, 2003/04, 2007 and 2012 by generation; the raw gearbox strings include 5AT, 5MT, 6AT, 6MT, which may blend automated manual versus foot-clutch manual terminology. Separate gearbox validation is needed.

## Official manufacturer heritage evidence
1. smart manufacturer heritage page explicitly describes the **first-generation smart fortwo**, from its 1998 commercial debut, as a car with a **rear-mounted engine and rear-wheel drive**. The next generation is described as the **451 fortwo (2007–2014)**. This supports the architecture lineage and raises confidence that applying generic FWD to early fortwo/fortwo Cabrio is a systematic source labeling error.
   OEM https://uk.smart.com/en/about-us/legacy-cars-fortwo/
2. smart Europe manufacturer December 2025 release on its new #2 says the new project retains the original fortwo's **rear-wheel-drive dynamics**, reinforcing the identity of the original two-seater as RWD (but this is a brand retrospective, NOT an OEM service-spec/VIN fiche for every 2000/2007/2012 fortwo variant).
   OEM https://media.smart.com/en-CEU/260174-smart-2-begins-testing-on-innovative-electric-platform/
3. smart official newsroom historical timeline catalogs 1998 and 2007 product generations and fortwo Cabrio. This helps separate the commercial history, not establish every local transmission or trim spec.
   OEM https://media.smart.com/en-INT/pages/heritage/

## Decisions and limits
- Evidence supports a **family-level RWD platform interpretation** for historical smart fortwo. Source label FWD is inconsistent with manufacturer history in the related generations; structured drive RWD should not be overwritten with FWD by an automated importer.
- An OEM heritage article cannot prove each of the 28 line-specific engine powers, gearbox type (automated manual vs manual), year and market. These 28 are platform-prioritized **REVIEW_ONLY**, not 28 individually certified product sheets or 28 approved rows.
- In particular, label 6MT does not prove a conventional three-pedal manual. Do not infer gearbox codes from the generic count alone.
- These 28 are from the **582** source drive mismatch queue and do not add 28 new vehicle records beyond the queue, nor are they all part of the earlier 1,166 queue.

## Batch counts
smart_source_conflict_rows_inspected=28
oem_platform_family_evidence_classification=28
new_approved_source_drivetrain_corrections=0
new_approved_gearbox_part_identifiers=0
new_ECU_DTC_links=0
raw_source_rows_modified=0
next_batch=100
next_workstream=SAVE_SMART_PLATFORM_TRIAGE_SIDECAR_OR_CONTINUE_OTHER_BRAND_OEM_QUALITY_FLAGS

## Protection
Append-only report; no changes to original gor3a CSV, existing review queues, main/stable, Windows, website, images or published DTC library.
