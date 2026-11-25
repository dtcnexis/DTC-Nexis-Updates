# Diagnostic website library gap review, 25 November 2026

The website uses 2,142 code strings. The pinned central manifest contains 5,969 distinct strings across 9,589 rows in 53 collections. The two sets share 2,141 strings. The archive has 3,828 strings absent from the website baseline. One website code, `C1203`, has no literal match in those 53 collections. Retain its existing website definition and reconcile its origin before changing it. [Counts and source revisions](summary.json)

## Reuse the inventory

[Collection gaps](collection-gaps.csv) identifies original rows by file, JSON array and zero-based index. Ranges include both endpoints. For example, the first record of an `entries` array has JSON pointer `/entries/0`. An empty range means zero matching rows. This index stores pointers instead of duplicating definitions, translations or technical procedures.

The comparison trims whitespace around each code and uppercases it. It preserves leading zeros, punctuation, suffixes and internal spaces. A matching string measures search coverage only. To decide applicability, use the original manufacturer, ECU, model, market, year, suffix and bulletin scope. A shared literal can still need a new context. A missing literal can be an alias, family pattern or index entry that should never be exposed as a scanner result.

## Explanation coverage

The 22 November field audit was based on the same library content. The 25 November review carries its 1,956 rows without a populated direct `definition_en` or legacy `en` field forward as source pointers. English labels in provisional fields require separate review. [Previous field audit](https://github.com/dtcnexis/DTC-Nexis-Updates/blob/d736732c91911e9fd3ea931b1d729685af68a4ef/data/master/reviews/bilingual_explanations_20261122/FULL_FIELD_AUDIT.md)

The scan checks four exact field names anywhere within each manifest row. It counts a row once per field, even when multiple nested objects contain that field. It finds 257 rows with technical material only in nested fields. There are 8,223 rows without populated fields under these four names. This is a structural count across languages. A populated field can contain a provisional note. A row with no match can have technical information in a linked supplement, a differently named field or an original source.

| Field | Rows with a direct value | Additional rows with a nested value |
|---|---:|---:|
| `symptoms` | 901 | 257 |
| `causes` | 973 | 221 |
| `diagnostic_steps` | 1,109 | 257 |
| `repair_steps` | 0 | 0 |

For the next explanation batch, inspect the original rows indexed in `nested_technical_only_indices` first. Preserve the relationship between the nested record and its vehicle context. Consult the existing enrichment files and the twelve legacy diagnostic notes before marking any explanation missing. [Existing supplements](https://github.com/dtcnexis/DTC-Nexis-Updates/tree/c450625e5e3b2dc41ce0892dcd9f3fb2750df6d8/data/master/enrichment) · [Legacy diagnostic notes](https://github.com/dtcnexis/DTC-Nexis-Updates/blob/c450625e5e3b2dc41ce0892dcd9f3fb2750df6d8/data/master/legacy_enhanced_diagnostics.json)

## First code review batch

[Mazda review queue](mazda-review.csv) points to 22 existing context records for 20 code strings absent from the website. The original review classifies 16 contexts as having bulletin-specific definitions and six as mentions with a definition still pending. Its source file retains the English text, bulletin IDs, model coverage, ECU and eligibility restrictions. Each queue entry keeps its original record ID and JSON pointer.

Review the 16 definition-bearing contexts first against their listed bulletins, the archive and pending brand batches. Preserve distinct scopes even when two rows have the same code. Keep the six mention-only contexts pending and verify VIN, model-year and ECU restrictions before promoting any record. The queue adds no runtime data and grants no technical approval. [Original Mazda batch](https://github.com/dtcnexis/DTC-Nexis-Updates/blob/79b0c385e2f138175d509253f9c19106347ea918/data/master/brands/mazda_20261116_oem_tsb_additions.json)

## Reproduce

Run `python inventory.py PATH_TO_WEBSITE PATH_TO_UPDATES_WITH_MAZDA_REVIEW` from this directory. The script reads the pinned Git objects, checks the manifest row counts and writes the summary and two CSV files here. Its inputs and outputs are independent of any release channel.
