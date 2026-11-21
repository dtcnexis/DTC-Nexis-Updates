# DTC NEXIS — الدفعة 91: Dacia Sandero Easy-R وJogger Hybrid 140 — تعارضات سنة الموديل والناقل والقدرة

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_FAMILY_EVIDENCE / NO_RAW_MUTATIONS / NOT_PUBLISHED
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_OEM_TRIAGE_BATCH90_AR.md
source_original_review=data/master/reviews/vehicle_catalog_full_20261118/review_queue/engine_transmission_internal_conflicts_batch03.csv

## 1. Dacia Sandero Stepway — engines_part_005.csv:163
- Raw source label «Sandero Stepway (2016), 1.5L dCi 5MT FWD (95 HP)», 2016–2020 generation, 1461cc, structured 5-speed automatic; Git source blob c6c4861abab91c5d694bcec10fab21934ab36136.
- Renault Group/Dacia 2015 manufacturer announcement: **Easy-R five-speed automated manual** first available in early 2016 on Sandero/Stepway with **TCe 90 petrol** and Stop & Start, not with the diesel application described by this row.
  OEM: https://nl.media.renaultgroup.com/automatische-easy-r-transmissie-en-dacia-duster-edition-2016-debuteren-op-iaa-frankfurt/
- Renault Group/Dacia late 2016 new Sandero range announcement: **TCe 90 Easy-R** is a gasoline offering. A later **Blue dCi 95** became available in subsequent model years and may be confused with the earlier 2016 generation start.
  OEM: https://nl.media.renaultgroup.com/dacia-introduceert-nieuwe-range/
  Further Dacia 2019: https://be.media.renaultgroup.com/een-speciale-reeks-anniversary-voor-het-vijftienjarige-bestaan-van-dacia/?lang=nld
- Finding: no proof that a 2016-model Stepway 1.5 dCi95 used automated 5-speed; label **5MT** and field **5-speed automatic** are likely blended variant specifications. Since the row spans 2016–2020 and does not specify actual MY/market, not possible to select a corrected gearbox from these docs alone.
- Status=HIGH_PRIORITY_DIESEL_MANUAL_VS_PETROL_EASY_R_BLEND_LEAD / YEAR_MARKET_EPC_PENDING.

## 2–3. Dacia Jogger Hybrid — engines_part_005.csv:50 and :51
- Both raw rows «Jogger (2022) 1.6L FHEV FWD (141 HP)», second marked 7 Seats. Both fields: fuel Hybrid Gasoline, 1598cc, structured **94hp**, multi-mode automatic. Source Git blob c6c4861abab91c5d694bcec10fab21934ab36136.
- Dacia/Renault official launch (Nov 2022) says **Jogger HYBRID 140** orders Jan 2023, deliveries March 2023. Technology: **1.6L gasoline engine 90 ch** plus electric motor 50 ch and starter generator; 4 modes/gears for ICE and 2 for EV in the unique clutchless multi-mode gearbox.
  OEM: https://be.media.renaultgroup.com/jogger-hybrid-140-la-premiere-motorisation-hybride-de-dacia/?lang=bel
- Later Dacia Duster Hybrid 140 OEM document says same family 1.6L combustion **94 ch** plus 49 ch electric, demonstrating possible market/model-year ratings variation; it does **not** directly prove Jogger MY2022/2023 gasoline engine 94.
  OEM: https://nl.media.renaultgroup.com/meer-duster-dan-ooit/
- Raw 141 vs model-brand 140 and raw 94 vs earlier Renault 90 should be recorded as unit/year/market discrepancies. The **engine-vs-system** power difference is likely semantic, not simply wrong; manufacturer data cannot yet fully support each raw number for the exact MY/7 seats.
- Strong signal: raw generation start **2022** is NOT proof of an actual 2022 Jogger Hybrid retail MY; official manufacturer sale starts 2023. Do not change source year or power without OEM identity.
- Status=HYBRID_SYSTEM_VS_ICE_POWER_PLUS_GENERATION_YEAR_GATE / OEM_GEARBOX_FAMILY_MULTI_MODE / VIN_CODE_PENDING.

## Outcomes
existing_unique_source_conflict_rows_reexamined_this_batch=3
reviewed_unique_conflict_rows_all_audits_batches88_89_91=10
original_conflict_queue_rows=1166
conflict_rows_finally_resolved_and_approved=0
original_files_modified=0
new_ECU_DTC_mappings=0
next_batch=92
next_workstream=WRITE_CHECKPOINT_AND_REVIEW_REMAINING_POWERTRAIN_BLEND_CASES_WITH_TIERED_SOURCE_PROVENANCE

## Protection
No change to original CSV, existing review queues, main/stable, website, Windows RC updates, images or approved DTC library.
