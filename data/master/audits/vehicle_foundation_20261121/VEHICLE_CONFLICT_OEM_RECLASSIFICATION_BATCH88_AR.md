# DTC NEXIS — الدفعة 88: تدقيق أربع حالات تعارض بمراجع الشركات المصنّعة

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_EVIDENCE_GRADED / NO_AUTOMATIC_CORRECTIONS / NOT_PUBLISHED
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_QUEUE_RECOVERY_BATCH87_AR.md
input_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/engine_transmission_internal_conflicts_batch02.csv;batch03.csv;batch04.csv

## منهج
تمت مطابقة الصفوف الأربعة مع الصف الأصلي للمحرك في gor3a ومع منشورات الشركات. حالة «تعارض مؤشر» لا تعني خطأ حقيقيًا، ولا يُجرى تصحيح من استنتاج غير مرتبط بالسوق وسنة الموديل ورقم المحرك والناقل.

### 1 — Dacia Duster FHEV 140: power not necessarily contradictory
- RAW_REF: engines_part_005.csv:11; Duster (2023), label «1.6L FHEV 140 Multi-Mode AT FWD (140 HP)»; fuel=Hybrid Gasoline; structured power=94hp; transmission=Automatic transmission Multi-Mode; raw Git blob c6c4861abab91c5d694bcec10fab21934ab36136.
- Dacia/Renault Group manufacturer press: Duster hybrid 140 combines **1.6 L 4-cylinder combustion engine 94hp** with electric motors in a total-output **140hp** hybrid powertrain and clutchless electrified automatic gearbox.
- OEM: https://be.media.renaultgroup.com/plus-duster-que-jamais/?lang=bel
- FINDING: **SOURCE_POWER_FIELD_SEMANTICS_MIXED**, 94 vs 140 is a plausible correct distinction between combustion and combined system. Model generation launch year 2023 vs actual MY requires separate verification.
- REVIEW_DECISION: CANDIDATE_FALSE_POSITIVE_POWER_CONFLICT; OEM_FAMILY_SUPPORT; NO_RAW_MUTATION.

### 2 — Dacia Bigster Hybrid: engine vs combined output and transmission architecture
- RAW_REF: engines_part_004.csv:1844; Bigster (2024), «1.8L 4AT FWD (156 HP)»; fuel=Hybrid Gasoline; structured power=109hp, displacement 1793cc; raw Git blob a62309aa7556a1ffbc89573c42cdfab1cb27c1f5.
- Dacia UK manufacturer page confirms Bigster full Hybrid 155 consists of **109hp 4-cylinder 1.8 L combustion engine** and **49hp electric motor**, with clutchless **multi-mode automatic**. A Bigster hybrid 155 launch description gives the total-output family, but raw label **156HP** is not an exact OEM-marketing power match and calendar/generation 2024 may reflect unveiling, not model-year sales.
- OEM: https://www.dacia.co.uk/hybrid-and-electric-range/bigster-suv/engines.html
- OEM ARCHITECTURE: https://www.dacia.co.uk/hybrid-and-electric-range/bigster-suv/hybrid-technology.html
- OEM MODEL LAUNCH: https://be.media.renaultgroup.com/bigster-ouverture-des-commandes/?lang=bel
- FINDING: LIKELY_ENGINE_VS_TOTAL_HYBRID_OUTPUT_FALSE_POSITIVE; **4AT** cannot be automatically interpreted as simple four-speed automatic; full-hybrid multi-mode architecture is more nuanced; MY and 155/156 power unit to validate.
- REVIEW_DECISION: YEAR_MARKET_TRIM_AND_TRANSAXLE_CODE_PENDING, NOT_APPROVED.

### 3 — Opel Corsa MHEV 2023: six-speed electrified dual clutch vs unrelated eight-speed automatic
- RAW_REF: engines_part_012.csv:51; «Corsa 5 Doors (2023) 1.2L MHEV 6AT FWD (110 HP)», structured power=100hp and transmission=8-speed automatic, fuel field=Gasoline; raw blob bbcd1f604d7405c0c79dad7b08120b2b86ef38b2.
- Opel/Stellantis release of 2023-11-30: 48V Corsa Hybrid **100 hp and 136 hp**, new electrified **six-speed dual clutch**, explicitly contrasts it with a **non-electrified 1.2L eight-speed automatic** version.
- OEM: https://www.media.stellantis.com/em-en/opel/press/debut-new-opel-corsa-with-48v-hybrid-drive-for-first-time
- Opel official 2025 UK launch references Hybrid **110PS e-DCT6** plus non-hybrid 100PS 8-speed automatic, suggesting 110 label could come from later MY variant, not proof of a 2023 MY.
- OEM 2025 UK: https://www.media.stellantis.com/uk-en/vauxhall/press/vauxhall-corsa-yes-2025-special-edition-offers-customers-more-choice-with-new-powertrain-option
- FINDING: **HIGH_PRIORITY_POWERTRAIN_MIXING**: raw label MHEV 6AT vs structured 8AT very likely combines hybrid 6DCT and conventional gasoline 8AT configurations. Structured fuel label Gasoline also omits MHEV classification. Model year exactness unresolved.
- REVIEW_DECISION: AWAIT_MY_TRIM_MARKET_OEM_SOURCE; DO_NOT_REPLACE_SOURCE_AUTO.

### 4 — Alfa Romeo MiTo 1.4 Turbo MultiAir 140
- RAW_REF: engines_part_001.csv:489; «MiTo (2013), 1.4L Turbo MultiAir 6AT FWD (140 HP)»; structured transmission 6-speed manual; raw blob 8a2e350c18a0f067aee4f6d03d2c5d7be964cffc.
- Alfa Romeo/Stellantis official UK 2014 launch: **1.4 TB MultiAir 140 hp** with **ALFA TCT twin dry-clutch** as standard; German official press also confirms MY2014 140 PS TCT, which is an automated 6-speed dual-clutch gearbox family and NOT a standard foot-clutch manual.
- OEM: https://www.media.stellantis.com/uk-en/alfa-romeo/press/2014-alfa-romeo-range-successfully-launched-to-the-media-on-the-isle-of-man
- OEM DE: https://www.media.stellantis.com/de-de/alfa-romeo/press/neu-alfa-romeo-mito-jetzt-mit-140-ps-multiair-motor
- Alfa original TCT design description: https://www.media.stellantis.com/uk-en/alfa-romeo/press/alfa-romeo-launches-alfa-tct-transmission-in-mito
- FINDING: strong OEM 140 hp TCT family evidence for MY2014, but raw source says MY/generation 2013. Requires trim, market and exact MY before marking manual value as an error.
- REVIEW_DECISION: LIKELY_MANUAL_VS_TCT_SOURCE_BLEND; NOT_APPROVED.

## حالة مميزة / لا مضاعفة للأعداد
existing_unique_conflict_queue_rows_reexamined=4
known_conflict_queue_rows_total=1166
new_OEM_confirmed_same_row_VIN_corrections=0
new_finally_resolved_conflict_rows=0
candidates_for_false_positive_system_vs_engine_power=2
candidates_for_gearbox_variant_field_mix=2
original_rows_changed=0
new_ECU_DTC_links=0
next_batch=89
next_workstream=VERIFY_ACURA_MDX_HYBRID_AND_OTHER_HYBRID_SYSTEM_VS_ICE_POWER_FLAGS_FROM_OEM_DOCS

## حماية
إضافة تقرير مراجعة مستقل فقط؛ لا تعديل raw CSV أو قوائم queue أو main أو stable أو RC Windows أو الموقع أو صور أو مكتبة DTC.
