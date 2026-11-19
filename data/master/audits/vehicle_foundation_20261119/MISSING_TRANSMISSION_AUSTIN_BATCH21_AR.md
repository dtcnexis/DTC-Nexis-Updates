# DTC NEXIS — الدفعة 21: Austin 864–889، منع حذف فروق السعة

date=2026-11-19 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
base_commit=3416906722f3a142c94951972675f6bf7c89325b
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_source=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_002.csv
existing_records_examined=26 (engines_part_002.csv:864–889); raw and review list were compared; no newly imported original rows.

## Cases requiring exact OEM identity
- 864/865: Austin 10 / 1931 / sedan / 1.1L: 1124cc vs 1125cc. Candidate partial match only, not literal duplicate.
- 868/869: 1300 GLIDER / 1968: source displacements 2175cc vs 1275cc, different engine labels 2.2L / 1.3L. Both retained; strong motor/fitment anomaly lead; name alone cannot merge.
- 875/877/878: Austin 7 / 1928 / coupe / 0.7L: 748, 747, 746cc respectively. Row 876 is 0.9L / 885cc; do not collapse group by rounded engine label.
- 879/880: «A 30» / 1952 / 0.8L: 800 vs 803cc. 881 is 0.9L / 948cc; preserve.
- 885/886/887: «A30» / 1952 / 0.8L: 803, 808, 800cc and body source «gesloten opbouw»; label possibly alias of «A 30» but body metadata differs. All remain separately scoped.
- 888/889: A30 SEVEN / 1953 / 0.8L: 803 vs 800cc.
- 872/873/874 are distinct Austin 1800 BALANZA, 3000 MK II and 3000 MK III, no deduplication based only on rounded displacement.
- Original body label «Niet geregistreerd» appears in several rows. This is not an engine type and must not be normalized into a real body style without a new source.

## Decision
All 26 cases remain NOT_OEM_VERIFIED pending model/engine/year/market and gearbox OEM evidence; no new OEM gearbox codes and no ECU/DTC links.
prior_records_examined=26
records_deferred=26
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
Cumulative OTHER records directly reviewed batches 11–21: 239; these are triage counts, not mechanically complete vehicles.
last_examined=engines_part_002.csv:889
next_record=first queue entry following engines_part_002.csv:889 (must read queue, do not assume line number)
No branch merge, release, or modifications to program/site/media.
