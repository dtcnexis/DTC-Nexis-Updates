# DTC NEXIS — الدفعة 83: Lexus ES 2023–2024 — دليل مباشر من كتالوج Lexus

date=2026-11-21
status=REVIEW_ONLY / OEM_GEARBOX_FAMILY_CONFIRMED / NO_VIN_SPECIFIC_IMPORT
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH82_AR.md

## مصدر الصفين
- engines_part_008.csv:1383 — ES 250 AWD, 2023–2025, 8AT, 203 HP.
- engines_part_008.csv:1385 — ES 300h FWD, 2023–2025, e-CVT, 215 HP.
- Original CSV, queue, and library records unchanged.

## أدلة مصنع أصلية
1. **2023 Lexus USA ES / ESh brochure** lists ES 250: 203 hp, 2.5 L, AWD, **8-speed Direct-Shift Automatic**, and ES 300h: 215 total system hp, 2.5 L hybrid, FWD, **ECVT**.
   https://www.lexus.com/content/dam/lexus/documents/brochures/models/2023/MY23-Lexus-ES-ESh-Brochure.pdf
   PDF textual evidence lines around 300–326; a screenshot at PDF page index 7 succeeded but showed a photograph rather than the specification spread. Thus numerical brochure text is available, but the exact relevant 2023 specification page was not visually verified in this batch.
2. **2024 Lexus USA ES / ESh brochure** contains exact same transmission-family differentiation and power ratings: ES 250 AWD, 203 hp, 8-speed Direct-Shift; ES 300h, 215 net system hp, e-CVT.
   https://www.lexus.com/content/dam/lexus/documents/brochures/models/2024/MY24-Lexus-ES-ESh-Brochure.pdf
   VERIFIED_VISUALLY: PDF page index 22, printed pages 42–43, model specifications.
3. **2025 Lexus Canada specification sheet**, previously visually verified: ES 250 AWD **UB80F**, ES 300h **P710**.
   https://toyotacanada.scene7.com/is/content/toyotacanada/2025%20Lexus%20ES%20specifications%20TCI%20ENpdf?%24%3Fcdh=attachment&bfc=off
4. **2022 manufacturer data** submitted in US NHTSA regulation proceedings mentions transmission code **UB80F** for ES250 AWD and **P710** for ES300h. 2022 OEM PDFs can be opened as extractable text; screenshots each returned 403, so mark them TEXT_ONLY_NO_VISUAL_CONFIRMATION.
   https://downloads.regulations.gov/NHTSA-2023-0022-0088/attachment_12.pdf
   https://downloads.regulations.gov/NHTSA-2023-0022-0088/attachment_13.pdf

## Audit decision
- ES250 MY2023, MY2024: **8-speed family OEM verified**. 2025 UB80F directly verified; 2022 UB80F only text-extracted and suggests model code continuity but does not replace direct MY2023–24/EPC/VIN proof.
- ES300h MY2023, MY2024: **hybrid ECVT family OEM verified**. 2025 P710 directly verified; 2022 P710 searchable text requires caution because screenshot failed.
- Manufacturer brochure is authoritative for variant and model year, but not for service transmission assembly orderable part or TCM calibration.
- Do NOT treat vehicle transmission family identification as exact VIN fitment nor publish any ECU/DTC mappings.

## Counts and checkpoint
existing_source_hint_cases_reexamined=2
new_approved_OEM_exact_VIN_transmission_assignments=0
new_approved_ECU_DTC_mappings=0
source_rows_modified=0
hint_cases_pending_final_approval=32
next_batch=84
next_workstream=VERIFY_MORE_2023_2024_LEXUS_CODE_DOCUMENTS_OR_MARK_UNRESOLVED_AND_ADVANCE_OTHER_HINT_ROWS

## Preserve
No raw data change, no modifications to main, stable, website, RC3.8.0/RC3.8.2, images, or DTC library.
