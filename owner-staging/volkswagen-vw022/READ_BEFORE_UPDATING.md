# Volkswagen VW022 — Owner staging, NOT an active update

**Status:** INVENTORY_ONLY / NOT_READY_FOR_UPDATE_BUTTON

This branch contains a file inventory and QA summary for a staged, unpublished Volkswagen catalog. It intentionally does **not** contain the raw private VW001–VW022 dataset, installer, workshop records, signing keys, OEM images or wiring diagrams.

## Files and readiness
- **151 files** are preserved in the ChatGPT project Library at `/DTC_Nexis_RC/Volkswagen/`.
- The consolidated VW022 RC archive has SHA-256 `edcd8bb9695ae4f9096e27b72db17970b1fb6e88d00a7d30235556445e3557e1`.
- An independent offline SQLite test passed, but **this did not test the installed Windows app**.
- **1,699 indexed entries** are not 1,699 VIN-verified car-specific records.
- **644 candidate VAG DTCs** must not be advertised as confirmed for every Volkswagen model.
- 5 release-blocking requirements remain unresolved.
- No licensed OEM diagrams or photos are included.

## Why the button must NOT be tested as a VW022 update yet
The currently published single-channel `main/update-feed.json` is a P-256 signed Windows R7 installer release. The owner RC3.8.2 catalog update mechanism expects compatible manifests and signed authorization. VW022 is a different private review schema, **not a valid signed feed**, and pushing ZIP bytes without an approved adapter and proper signature does not cause the installed program to load them.

The current feed, update key, signing identities and `main` remain unchanged. No release or public installer was created.

## Next release gate
1. Confirm the owner's desired distribution scope for this currently private workshop dataset, because **this GitHub repository and all its branches are public**.
2. Build an adapter targeted to the actual installed RC3.8.2 data-updater schema; test in a disposable environment.
3. Remove or quarantine all unverified DTC-to-VIN and ECU mappings, rights-restricted assets and pending wiring entries.
4. Sign the approved owner-only catalog with the **existing** trusted key (never generate a replacement key).
5. Verify the original 18 visits are backed up and owner-device preflight succeeds before owner-only activation.
6. Only then explicitly approve feed activation and click Update.

**Do not change `main/update-feed.json`, `update-public-key.json`, installer files, or GitHub Releases solely to deliver this staging catalog.**
