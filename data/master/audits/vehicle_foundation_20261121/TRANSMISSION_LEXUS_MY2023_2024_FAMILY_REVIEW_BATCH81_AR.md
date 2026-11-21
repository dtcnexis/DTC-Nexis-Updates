# DTC NEXIS — الدفعة 81: مراجعة Lexus ES 2023 و2024 وعدم الخلط بين رموز العائلات وقطع VIN

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / OEM_MY2023_2024_FAMILY_VERIFICATION / TRANSMISSION_CODE_YEAR_SCOPE_PENDING / NOT_PUBLISHED
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH80_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## صفوف الإدخال الموجودة مسبقًا
- engines_part_008.csv:1383 — Lexus ES 250 AWD (2023–2025), «250 8AT AWD (203 HP)».
- engines_part_008.csv:1385 — Lexus ES 300h FWD (2023–2025), «300h e-CVT FWD (215 HP)».
- Original engine CSV unchanged; existing queue statuses NOT_APPROVED.

## Lexus Canada: إثبات العائلة بحسب سنة الموديل
1. **2023 MY**: Lexus Canada product press release states ES250 AWD 2.5L 203hp with eight-speed automatic; ES300h 2.5L 215 net hp hybrid with continuously variable transmission:
https://media.lexus.ca/en/releases/2022/striking-design-meets-commanding-performance-the-2023-lexus-es-series-luxury-sedans.html
2. **2024 MY**: Lexus Canada product press release states ES250 AWD 2.5L 203hp with eight-speed Direct Shift. ES300h is sold as hybrid in same MY, though press release is less explicit about hybrid transaxle designation:
https://media.lexus.ca/en/releases/2023/on-sale-now--2024-lexus-es-300h--es-350--es-250-awd.html
3. **2025 MY**: Lexus Canada original specification chart explicitly states ES250 AWD **UB80F** eight-speed and ES300h **P710** e-CVT; verified as primary 2025 OEM evidence in Batch80:
https://toyotacanada.scene7.com/is/content/toyotacanada/2025%20Lexus%20ES%20specifications%20TCI%20ENpdf?%24%3Fcdh=attachment&bfc=off

## Supplementary 2022 manufacturer spec hosted on public US regulations site
- Document describes 2022 Lexus ES250 AWD with engine **A25A-FKS**, 203hp and transmission designation **UB80F**:
https://downloads.regulations.gov/NHTSA-2023-0022-0088/attachment_12.pdf
- The searchable PDF text exposed the 2022 designation, but a direct screenshot attempt failed with 403 Forbidden; therefore **TEXT_EXTRACT_ONLY_VISUAL_VERIFICATION_FAILED**. Do NOT mark the 2022 document visually verified.
- While independent 2022 and 2025 endpoints support the stability of UB80F, 2023–2024 code-year attribution must still be checked with direct same-year technical PDFs / service manual and market fitment before promoting an approved record.

## Findings
- 1383: OEM_MY2023_2024_TRANSMISSION_EIGHT_SPEED_FAMILY_CONFIRMED; UB80F proven in OEM 2025, and textual 2022 OEM document; direct source linking exact UB80F to 2023/2024 not yet visually validated.
- 1385: OEM_MY2023_2024_HYBRID_CVT_FAMILY_SUPPORTED; P710 2025 confirmed; exact code for MY2023–2024 remains unverified.
- A model-year family specification or marketing news release cannot establish VIN-specific assembly part number or ECU/TCM calibration.
- Toyota Canada 2025 chart gives ES350 UA80E as different model; don't transfer ES350 transmission code to ES250 or ES300h.

## Counts
existing_queue_rows_reexamined=2
new_exact_MYA_2023_2024_transmission_code_approvals=0
new_approved_VIN_assembly_assignments=0
new_ECU_DTC_links=0
raw_rows_modified=0
hint_cases_pending_final_OEM_fitment=32
next_batch=82
next_workstream=SUBARU_CURRENT_2022_EPC_VIN_PART_SUPERSESSION_AND_YEAR_APPLICABILITY

## Controls
Audit-only file. No modification of original data, review queues, main, stable, site, Windows RC3.8.0/RC3.8.2, images, or released DTC library.
