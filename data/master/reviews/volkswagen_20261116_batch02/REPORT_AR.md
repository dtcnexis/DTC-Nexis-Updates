# Volkswagen — OEM DTC continuation BATCH02 — 16 November 2026

## Preserved baseline
- Main VW022: 1,699 **mixed** source records; includes 644 legacy candidate DTC rows (642 distinct text values).
- Previous independent work branch BATCH01: 45 context records from four factory bulletins. **Not rewritten or duplicated**.

## New records
- New BATCH02 context records: 24.
- Unique raw DTC strings in batch: 17.
- Brand-new raw DTC strings relative to prior 644 + 45 and VW022 observed/reference: 15.
- Previously known raw codes enriched with **source-scoped fitment**: C10AC07 (6 records for VIN/model variants), P20EE (Touareg 7L CATA ODIS test record).
- Repeat raw code B200FF0 across 3 separate vehicle/TSB contexts is **intentional**, not a duplicated record.
- 14 codes in Golf R DSG TSB: 1 primary (P0C29) + 13 accompanying codes. Accompanying codes only count under this TSB if P0C29 is present.
- 24 context records in deferred review queue: documentation and European fitment incomplete. No general parts diagnosis approved.

## Sources
- VW-2070973-2 TSB 2070973/2, 2024-02-22, https://static.nhtsa.gov/odi/tsbs/2024/MC-10250796-0001.pdf — official_vw_bulletin_public_copy
- VW-2070973-1 TSB 2070973/1, 2023-08-10, https://static.nhtsa.gov/odi/tsbs/2023/MC-10241181-0001.pdf — official_vw_bulletin_public_copy
- VW-2056436-1 TSB 2056436/1, 2019-12-16, https://static.nhtsa.gov/odi/tsbs/2019/MC-10169517-0001.pdf — official_vw_bulletin_public_copy
- VW-2080198-1 TSB 2080198/1, 2025-12-03, https://static.oemdtc.com/NHTSA-PDFs/MC-11027266-0001.pdf — manufacturer_authored_technical_bulletin_third_party_mirror
- VW-2080430-2 TSB 2080430/2, 2026-09-01, https://oemdtc.com/tsb/11038151/ — third_party_transcription_of_vw_bulletin_not_official_pdf_verified
- VW-VOS-17-29 VOS-17-29, 2017-11-08, https://static.nhtsa.gov/odi/tsbs/2017/MC-10133489-9999.pdf — official_vw_service_information_public_copy

## Coverage and safety
- All fitments are US-bulletin scoped; the Touareg CATA note is a **diagnostic tester content update**, not a proof of engine defect.
- Jetta / Taos 2025 and Tiguan 2026 ACC documents are present in secondary mirrors/transcriptions; additional primary-host check required.
- No images, wiring diagrams, ECU pinout or photos were generated or reused.
- `main`, VW022, RC3.8.0/RC3.8.2 and all update-feed & release metadata remain unchanged. This branch is not an activated update.
