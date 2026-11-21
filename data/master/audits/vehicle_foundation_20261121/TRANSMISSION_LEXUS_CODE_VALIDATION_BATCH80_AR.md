# DTC NEXIS — الدفعة 80: Lexus ES 250 / ES 300h — رموز نواقل Lexus الأصلية

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=OEM_MODEL_YEAR_2025_CODE_PROVEN / RAW_2023_SCOPE_PENDING / REVIEW_ONLY / NO_RELEASE
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_ASSEMBLY_FITMENT_BATCH79_AR.md
prior_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## الصفوف الخام
- Lexus ES 250 AWD, engines_part_008.csv:1383, years 2023–2025, 250 8AT AWD (203 HP).
- Lexus ES 300h FWD, engines_part_008.csv:1385, years 2023–2025, 300h e-CVT FWD (215 HP).
- Both original rows have empty structured transmission and no exact OEM model IDs. Source blob=88dcf7945b863564a06acb1de5f9676d401bba49.

## وثيقة Lexus Canada الرسمية، MY2025
- LEXUS 2025 ES Product Information technical PDF, chart «Chassis and Body — Transmission — Code Name».
- OEM source: https://toyotacanada.scene7.com/is/content/toyotacanada/2025%20Lexus%20ES%20specifications%20TCI%20ENpdf?%24%3Fcdh=attachment&bfc=off
- PDF physical page index 2 visually verified using source screenshot.
- **ES 250 AWD:** transmission **UB80F**, 8-speed Direct Shift automatic.
- **ES 350:** transmission **UA80E**, 8-speed Direct Shift automatic. This is a distinct ES 350 application, NOT the ES 250 code; preserve distinction.
- **ES 300h:** hybrid transmission **P710**, e-CVT.
- The official chart further identifies 2025 engine types A25A-FKS (ES250) and A25A-FXS (ES300h). Power table distinguishes ES250 engine output (204 hp in 2025 table) from 203 hp in the earlier 2023 Lexus Canada press release; this small market/measure/year difference is not automatically a mistake.

## مقارنة دليل سنة 2023
- Lexus Canada MY2023 launch confirms ES250 AWD 2.5L/203 peak hp plus 8-speed automatic, and ES300h 2.5L/215 net hp plus CVT:
  https://media.lexus.ca/en/releases/2022/striking-design-meets-commanding-performance-the-2023-lexus-es-series-luxury-sedans.html
- This source does NOT give UB80F/P710 codes explicitly for 2023. The MY2025 technical sheet verifies 2025 end-year of raw range but must not be blindly expanded backwards to 2023–2024 or every market.
- VIN and market-specific transaxle assembly part number remain unverified. Code name (UB80F/P710) is not an EPC parts order number.

## Review decisions
- 1383: OEM_CODE_UB80F_CONFIRMED_FOR_2025_CANADA_ES250_AWD / 2023_2024_MARKET_AND_VIN_GATE_PENDING / NOT_APPROVED_IN_MASTER.
- 1385: OEM_CODE_P710_CONFIRMED_FOR_2025_CANADA_ES300H / 2023_2024_MARKET_AND_VIN_GATE_PENDING / NOT_APPROVED_IN_MASTER.
- ES350 UA80E is supporting differential comparison, not part of these two raw rows.
- Never overwrite the two original queue rows or infer shared ECU/DTC calibrations between non-hybrid 8-speed and e-CVT hybrid.

## Results
existing_hint_cases_reexamined=2
new_2025_OEM_transmission_model_codes_evidence=2
new_exact_2023_2025_all_year_vehicle_gearbox_approvals=0
new_ECU_DTC_links=0
new_source_imports=0
raw_records_modified=0
hint_cases_pending_final_approval=32
next_batch=81
next_workstream=FIND_MY2023_2024_LEXUS_TECH_SHEETS_AND_SUBARU_VIN_EPC_CONFIRMATION

## Protection
Review-only report; no modifications to main, stable, original CSV, source reviews, Windows or website, media or published DTC database.
