# DTC NEXIS — Bilingual Explanations Audit / جرد الشروحات
Date: 2026-11-22
Branch: research/dtc-bilingual-explanations-audit-20261122
Baseline: main tree 2df439b7b13fae8381a20c3faf5819ea8ee56f3e

## Verified baseline
- Authoritative source/application rows: 9,589 across 53 collections; source: data/master/all_collected_catalog_manifest.json. This is **not** a distinct-code count, not a translation-quality count and not a complete explanation count.
- main tree: 324 blobs; 58 under data/master/brands, 158 under data/master/reviews; includes archives and VW staging files not part of the 53-count inventory.
- Main status report: data/master/STATUS_20261106_AR.md.
- Earlier translations review: data/master/reviews/continuation_20261106_batch03/SELECTED_TRANSLATIONS.json has 7 narrowly scoped reviewed labels, none fully technically approved.

## Verified schema differences / existing reusable materials
- data/master/dtc_text_catalog.json: 26 multilingual generic **definitions** (EN/AR/SV), independent OEM review pending.
- data/master/brands/bmw.json: 98 manufacturer records; EN/AR definitions, legacy_requires_revalidation, not a complete repair manual.
- data/master/brands/nissan.json: 495 records with scope and ECU metadata; exact fitment not established by index alone.
- data/master/brands/toyota_exp002_dtc_part01.json: technical detail including symptoms, causes, diagnostic_steps, related source context for at least one inspected record (P0A0F); requires VIN/OEM review.
- data/master/legacy_enhanced_diagnostics.json: original detailed causes and testing information, explicitly REQUIRES_OEM_VERIFICATION.
- Drive accessible folder: DTC NEXIS Upload (181OSRfNRbBz9JOPu6ZMMRxXxqqt5qFRI). Found VW001 and Mercedes Batch01 readmes and archived-artifacts subfolder; no file contents were imported or overwritten in this pass.

## Unresolved and important numerical limitations
- Exact per-field EN/AR/diagnostic/repair/source omissions among 9,589 source rows: NOT YET COMPUTED. A mass per-file read encountered tool-call limits; do not substitute guessed totals.
- Distinct DTC+brand+model+engine+ECU+market variants: NOT YET COMPUTED.
- Verified complete bilingual explanation records: NOT YET ESTABLISHED.
- Recovered Drive source records: 0 imported in this pass (pending content+SHA checks).
- New verified technical explanation entries: 0. No unsupported content added.
- Duplicate removals: 0; originals untouched.
- Unconfirmed records must remain in existing data/master/reviews structures, not published as approved.

## Proposed canonical explanation overlay (do not break existing schemas)
For each entry: source_record_path, source_record_sha, raw_code, brand, model, model_year_range, market, engine, transmission, ecu, ecu_calibration, subcode, definition_en, definition_ar, symptoms_en/ar, causes_en/ar, diagnostic_steps_en/ar, repair_steps_en/ar, verification_steps_en/ar, technical_sources (document, page, OEM applicability), evidence_status, translation_review_status, scope_status, review_reason.
Deduplication key: (brand, normalized raw_code, subcode/INF, model/generation, year range, market, engine, ECU, calibration). Preserve legitimate variants. Never turn general training advice into OEM-approved repair instructions.

## Next checkpoint
1. Read and aggregate all 53 manifest files **in manageable batches**; validate the total row count and field-by-field completeness by schema, including nested previous_batch_row/details.
2. Read detailed legacy diagnostics, archive readmes and relevant Drive archives; compare by ID, source blob SHA and semantic key.
3. Build bilingual explanations only where diagnosis/repair and source scope match; put other content in existing review queue.
4. Commit verified overlays exclusively on the work branch, check commit+file contents, optionally open PR; do not merge or publish.
No site/UI/Windows/stable changes.
