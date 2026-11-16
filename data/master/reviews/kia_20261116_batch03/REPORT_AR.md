# Kia — OEM bulletin source batch, 16 Nov 2026

- Main comparison: `data/master/brands/kia.json`, 63 original rows. Existing source content not altered.
- 42 code-context records from three Kia bulletins; **40 previously absent raw DTC codes relative to the 63-row GitHub Kia baseline**, 2 existing codes with a different source/application.
- 42 deferred review entries (lack of ECU/engine/EU/Sweden validation, and 38 CHA114 DTCs lacking individual definitions).
- CHA114 US Optima JF/JFa and Sorento UMa: 38 distinct C codes; code service paths are conditional on rack/column MDPS and KDS diagnosis, NOT an unconditional instruction to replace components.
- TRA109: P084500 and P084600, IVT-specific and restricted to bulletin vehicles. 'XX' is a variable suffix family, not a literal code.
- ELE376/SA609: C128387 and C164286, K5 DL3 2025MY, only production/VIN/ROM scope in bulletin.
- **Prior 125-code DRAFT:** original artifact not accessible in this session. Cannot claim net-new against that DRAFT; no claim of brand-wide coverage.
- No images, GitHub release, update channel, or Windows files modified. Nothing merged into main.

## References
- MDPS Warning Lamp Diagnostic Inspection & Single Parts Replacement (2022-03): https://static.nhtsa.gov/odi/tsbs/2022/MC-10209439-0001.pdf
- IVT Oil Pressure Sensor Replacement (2024-07): https://static.nhtsa.gov/odi/tsbs/2024/MC-11004930-0001.pdf
- ACU Operation Logic Improvement SA609 (2025-04): https://static.nhtsa.gov/odi/tsbs/2025/MC-11017242-0001.pdf
