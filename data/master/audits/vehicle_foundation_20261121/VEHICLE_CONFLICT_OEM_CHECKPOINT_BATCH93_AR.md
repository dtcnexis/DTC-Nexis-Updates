# DTC NEXIS — نقطة استئناف تدقيق التعارضات حتى الدفعة 93

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_REVIEW_RECORDS_SAVED / NO_APPROVED_SOURCE_CORRECTIONS / NOT_PUBLISHED
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH86_AR.md

## 1. مكان قائمة التعارضات الأصلي: تم التأكد
- Original audit: data/master/reviews/vehicle_catalog_full_20261118/ENGINE_TRANSMISSION_CONFLICT_AUDIT_AR.md.
- Four originals under data/master/reviews/vehicle_catalog_full_20261118/review_queue/engine_transmission_internal_conflicts_batch01.csv through batch04.csv.
- Counts from actual parsed CSVs: batch01=1; batch02=247; batch03=510; batch04=408; total **1166 unique (source_file+source_line)**, zero duplicate keys across four original queues.
- Original model review: **1194 potential indicators** in 1166 original rows: 371 gearbox wording/type hints, 81 cc discrepancies, 742 hp discrepancies, non-exclusive due to overlaps.
- Source conflict queue original files are intact, not rewritten.
- Reason earlier GitHub search returned no results: code search targets default branch, whereas files exist on review branch; explicit review branch Git tree recursive returned full 575-entry tree and identified queue.

## 2. Files created this session (all new, verified by refetch)
1. data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_QUEUE_RECOVERY_BATCH87_AR.md; commit 4e078171e7f014fc4eaf78c5897812093fca3b90
2. data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_OEM_RECLASSIFICATION_BATCH88_AR.md; commit af08d49238b4211cc86ea5d270488effd795c914
3. data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_ACURA_POWERTRAIN_BATCH89_AR.md; commit 2a9f5f8b88db0d8339334e87f6d1221e22e42e81
4. data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_OEM_TRIAGE_BATCH90.csv; **7 records**, commit c85fb5da85db9da4c91cfd9d463b69f3c01a05c7
5. data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_OEM_TRIAGE_BATCH90_AR.md; commit 4617bfda667ee1cbd26297f66afe7ec368d46749
6. data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_DACIA_SANDERO_JOGGER_BATCH91_AR.md; commit 8c71bbb005429346e73b8de17e4aff4fea7878ff
7. data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_DACIA_TRIAGE_BATCH91.csv; **3 records**, commit 7255ca7a120106242cda7956e0c0688fcc6ad9f8
8. data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_TOYOTA_AQUA_CHR_BATCH92_AR.md; commit 602e84386f0a2f7f653344cb864eb2099316c372
9. data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_TOYOTA_TRIAGE_BATCH93.csv; **6 records**, commit 63bb61846ff2eb7e8713376f7c83a1f96efa8a3c
- GitHub compare from last known commit 5109bf8c3ebf945d0dfeceb2d0486410cd5d8ba7 to 63bb61846ff2eb7e8713376f7c83a1f96efa8a3c shows **9 commits, 9 added files, 0 modified/deleted**. No original CSV changed.

## 3. Cumulative audited cases
- **16 distinct original conflict rows** now have structured OEM review observations:
  - 7 rows in batch90 sidecar: Duster 1, Bigster 1, Corsa 1, Alfa MiTo 1, Acura MDX 2, Acura NSX 1.
  - 3 additional in batch91 sidecar: Sandero Stepway 1, Dacia Jogger 2.
  - 6 additional in batch93 sidecar: Toyota Aqua 2, Toyota C-HR 4.
- **1150 of 1166** original conflict rows are **not yet in this new structured OEM-triage sidecar**; this does NOT claim no other earlier reviews have examined those rows.
- **0/1166 technically resolved with authorized master-field edits**; no schema updates, no ECU/DTC approvals, no direct VIN gearbox assignments.
- Missing transmission source-review status separately remains **1469/1469 source-reviewed but OEM technical approval pending**, including **32 hint cases** requiring exact gearbox application.

## 4. Key manufacturer-evidenced findings
- Acura MDX 2016/2018 raw combines 3.5L+9AT gasoline configuration with 321hp 3.0L+7DCT Sport Hybrid system, strong identity merge suspect.
- Opel Corsa 1.2 MHEV six-speed electrified DCT vs nonhybrid eight-speed automatic is a variant mix, 2023 label 110 vs 100 needs year/market.
- Alfa MiTo 140hp TB MultiAir in MY2014 uses six-speed TCT twin-clutch, not simply 6-speed foot-clutch manual; raw starts 2013.
- Dacia Duster/Jogger/Bigster hybrid total output must be distinguished from ICE rated power; avoid false-positive 'power corruption' judgments.
- Dacia Sandero 2016 Easy-R five-speed originally marketed with TCe90 gasoline, not proof for raw dCi95 diesel automatic; engine-version and launch-year mixed.
- Toyota Aqua E-Four 2021 is electric 4WD and is distinct from FWD; source row line714 says both E-Four and FWD, a confirmed textual contradiction, while exact variant remains unknown.
- Toyota C-HR source line937 says AWD in label but FWD in structured field; MY2023 Toyota OEM confirms Hybrid200 AWD-i and FWD variants exist. PHEV source line939 223 system vs 152 gasoline ICE is directly compatible with OEM 2024 PHEV ratings.
- In these cases no raw source field may be overwritten without same-market/year/trim/VIN evidence and verified schema compatibility.

## 5. Deterministic resumption
last_completed_batch=93
last_file=data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_TOYOTA_TRIAGE_BATCH93.csv
last_commit_before_checkpoint=63bb61846ff2eb7e8713376f7c83a1f96efa8a3c
next_batch=94
next_workstream=CONTINUE_OEM_CONFLICT_TRIAGE_FROM_16_CASES; PRIORITIZE_ADDITIONAL_DRIVE_LABEL_VS_FIELD_AND_HYBRID_POWER_ICE_MIXES; EXTEND_SIDECAR_APPEND_ONLY; PRESERVE_ALL_ORIGINALS
remaining_unreviewed_in_this_OEM_sidecar=1150
exact_part_and_ECU_DTC_approval=0
technical_completion=false
main_merged=false
stable_updated=false

## Preservation
Do not alter gor3a originals, original 1166 conflict queue, raw vehicle indexes, main or stable, Windows RC3.8.0 / RC3.8.2, website, image/media corpus or approved DTC records.
