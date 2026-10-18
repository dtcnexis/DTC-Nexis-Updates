# DTC NEXIS — Windows certificate and release gate (owner-only hold, 18 Oct 2026)

**STATUS: BLOCKED for all public and beta-user distribution.** The only authorized human tester is the owner. An earlier proposal for 20 testers has **not** been approved. Never run the publish workflow, merge to production, edit the live update-feed, or distribute a new installer or data pack until the owner reviews the complete build and expressly says **«ارفع»**. Ordinary "تابع" or successful automated tests are not publication consent.

## Confirmed technical facts
- Historical public release **R7** contains an **unsigned** Windows setup EXE. Its public ECDSA/P-256-signed update-feed and SHA-256 checksum are NOT Windows Authenticode code signing.
- The unsigned file was blocked by Windows 11 Smart App Control. Disabling SAC or trusting a self-issued certificate is not an acceptable release solution.
- The original installer on the owner's machine reported FileVersion 0.0.0.0 and ProductVersion 0.10.6-rc3.6.
- In the **private trial app branch**, full Windows CI build **39143084723** succeeded with numeric FileVersion **0.10.6.0** on the PyInstaller EXE and Inno Setup EXE. The original installer application identity remains `0.10.6-rc3.6` to preserve upgrade tests.
- In a subsequent private app CI **39144277564, attempt 2**, Python/JS, Edge/UI, installer packaging, and the executable-update runtime signing guards passed. First attempt encountered an intermittent Edge startup timeout; retry used the same code. No real publisher-signed app has been produced.
- **No signing identity is configured**. Neither passing CI nor the signed feed proves a trusted Windows installer or Smart App Control approval.

## Experimental public-publisher PR, not merged
This draft branch `fix/r7-authenticode-release-gate-20261018` checks the **actual final setup EXE** before GitHub release creation and before editing `update-feed.json`.

The proposed production publisher is deliberately blocked unless all requirements are met:
1. A protected, owner-controlled `NEXIS_OWNER_APPROVED_REVISION` matches the exact release revision. It must be updated for **each separately approved release**, not granted permanently.
2. `NEXIS_APPROVED_SIGNER_THUMBPRINT` specifies the 40-hex SHA-1 fingerprint of the particular, owner-approved Authenticode signing certificate. Any other certificate, including a different otherwise-valid signer, is rejected.
3. `NEXIS_APPROVED_WINDOWS_FILE_VERSION` specifies the nonzero numeric version. Both the setup EXE and **installed app EXE** must match this version and approved signer.
4. Both EXE signatures must be **Valid**, with a trusted timestamp; the final signed installer must match the signed feed's exact SHA-256. Release bytes must be immutable.
5. Test normal install, updates, rollback and uninstall on a real Windows 11 device with Smart App Control enabled. A valid signature does not guarantee SAC reputation.

**These protected settings are not configured and must NOT be configured before owner's release authorisation.** Do not store a certificate private key, exportable PFX, passwords, identity scan, or identity-verification details in GitHub source, the update feed, app bundle, or chat.

The test-only workflow `.github/workflows/verify-r7-signature.yml` runs on Windows, verifies the publisher/owner gates, downloads only the known historical unsigned R7, and asserts refusal. It does not publish. Latest success: **GitHub Actions run 39145652154**.

## Remaining implementation and owner decisions
- Select direct Authenticode-signed EXE versus **accepted Microsoft Store MSIX** packaging, while respecting tester countries and avoiding identity/personal-data exposure where possible. Store MSIX package signing does not magically sign the direct-download Inno Setup EXE.
- Obtain an eligible legitimate publisher signing identity through the owner's explicit approval. Legal publisher name can be visible in authenticode certificate details; explain privacy implications before registration.
- Sign the PyInstaller app EXE after building it and before packaging it in Inno; then sign the final Inno Setup installer (both with timestamps). Verify and pin both publisher certificates.
- Compute signed installer digest only **after** signing, create/sign the new feed only once accepted, and publish only when explicitly authorised.
- Continue preparation and owner-only offline/private tests; do not modify the stable RC3.8.0 branch or currently published assets.

Private app changes are proposed separately in [app PR #5](https://github.com/dtcnexis/DTC-Nexis-App/pull/5). Public-publisher changes remain a **draft PR #1**.
