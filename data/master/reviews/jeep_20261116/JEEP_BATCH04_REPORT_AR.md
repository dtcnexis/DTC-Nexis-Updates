# DTC NEXIS — Jeep Batch04 progress (2026-11-16)

**Non-release branch only.** Existing Jeep Batch01 originals, Expansion V2, and Batch03 have not been replaced. These records do not modify app or update feed.

## Real starting point
- GitHub main: `data/master/source_archives/jeep_dtc_batch1.json` contains 111 raw rows / 108 distinct DTCs; preservation split into two Jeep files 90+21.
- Local Expansion V2: 115 distinct codes and 127 applicability rows, including 7 codes not in Batch01.
- Pending draft PR #22: Batch03 adds 7 distinct codes, 11 manufacturer-bulletin-linked applications, 46 deferred review rows.
- Combined pre-Batch04 distinct code index: **122**.

## Batch04 actual additions
- **28 code definitions** from 7 FCA/Stellantis OEM bulletins/STAR items; an additional NHTSA communication index grounds the 2024 Wrangler model year for one STAR case.
- **29 application relationships**, including one new Wrangler 2024 relation to the **existing** V2 `U0415-00` record (`jeep_dtc_u0415_00`) without duplicating its definition.
- Categories: 14 U codes (WL 2021 BCM), 3 B codes (WL 2024 RFHM), 1 C code (JL 6.4L DTCM), 2 C codes (JT DTCM, years unknown), 3 C codes (Compass MV 2022 ABS), 1 B code (JL SRS, years unknown), 2 C + 2 U codes (Wrangler JL 2024 ABS companion codes).
- **7 diagnostic workflows** with procedures, tool names, bilingual Live Data labels and numeric thresholds marked `غير مؤكد` except programming support voltage explicitly from bulletin.
- **31 new review rows**: 28 new code records requiring VIN/engine/SAE/Live Data reviews + one pre-existing code's newly documented application + two secondary/unscoped candidate codes not counted.
- **0 exact new-code duplicates** relative to previous 122-code combined index. The pre-existing U0415-00 was reused by ID, not counted new.
- Cumulative distinct codes in Batch01 + Expansion V2 + Batch03 + Batch04: **150** (index arithmetic, not production-approved).
- Previous Batch03 review queue 46 rows untouched; combined review cases 46 + 31 = **77** (not necessarily 77 unique DTCs).

## Files added in this batch
1. `data/master/enrichment/jeep_batch04_20261116.json`
2. `data/master/reviews/jeep_20261116/JEEP_BATCH04_DEFERRED_20261116.json`
3. `data/master/reviews/jeep_20261116/JEEP_BATCH04_REPORT_AR.md`

## Key original source links
- BCM WL: FCA `08-050-22 Rev.B` 2022-10-25 https://static.nhtsa.gov/odi/tsbs/2022/MC-10227756-9999.pdf
- RFHM WL: Stellantis `08-169-24 Rev.C` 2024-12-14 https://static.nhtsa.gov/odi/tsbs/2024/MC-11011927-0001.pdf
- DTCM JL: Stellantis `08-162-24` 2024-07-11 https://static.nhtsa.gov/odi/tsbs/2024/MC-11004888-0001.pdf
- JT 4WD: FCA STAR `S2208000097` 2022-04 https://static.nhtsa.gov/odi/tsbs/2022/MC-10228000-9999.pdf
- ABS MV (EE/MEA): FCA `08-007-23` 2023-01-10 https://static.nhtsa.gov/odi/tsbs/2023/MC-10231774-9999.pdf
- Airbag JL: Stellantis STAR `S1908000122 Rev.A` 2022-06 https://static.nhtsa.gov/odi/tsbs/2022/MC-10221440-9999.pdf
- ABS JL: Stellantis STAR `S2408000084` 2024-08 https://static.nhtsa.gov/odi/tsbs/2024/MC-11005434-0001.pdf
- NHTSA 2024 Wrangler model-year index for above STAR case: https://dot.report/manufacturer-communications/11005434

## Technical limits and remaining work
- Model-year identification for JT 4WD and JL SRS cases is not present in the printed STAR texts. **Do not automatically infer the missing years.**
- Some OEM documents cover EE region; that does not independently prove Swedish VIN eligibility.
- VIN, exact ECU calibrations, code-specific SAE generic/manufacturer classification, engine fitment, numerical Live Data specifications, and schematic connector pinouts remain unverified where indicated.
- STAR cases document technician experiences and **do not guarantee causes or authorize warranty repairs**.
- 2 extra candidates (`B1751-11`, `C147B-92`) were queued for lack of exact Jeep OEM vehicle application/accessible primary bulletin.
- **No images were collected/generated/changed**, honoring project hold. Existing media is preserved.
- PR stays draft, no main merge, no software RC3.8.0/RC3.8.2/edit to update channel.
