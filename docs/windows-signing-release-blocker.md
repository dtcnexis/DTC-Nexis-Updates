# Windows installer signing: release blocker and owner handoff

Status: **BLOCKED until a trusted Windows code-signing identity is configured**.

## What the R7 evidence proves
- Windows 11 Smart App Control blocked the downloaded R7 installer.
- Windows Properties screenshot showed no embedded or catalog signature for that downloaded EXE.
- The signed `update-feed.json` authenticates the update metadata and includes a SHA-256 hash; it does **not** Authenticode-sign the installer.
- R7's file metadata shown on the owner's machine was FileVersion 0.0.0.0 and ProductVersion 0.10.6-rc3.6. This needs a separate build metadata fix.
- These observations do not establish that a certificate expired; an unsigned binary is the primary observed issue.

## Required before any new Windows release
1. Choose a publicly trusted Authenticode code-signing certificate or managed signing service eligible for the publisher. The owner must complete provider identity verification. Never commit private keys or passwords.
2. Sign the application EXE(s) and final installer **after all binary modifications**. Use SHA-256 and RFC 3161 timestamping. Confirm the signing service supports the selected CI environment and secure credential handling.
3. On Windows, run `ci/verify-windows-installer-signature.ps1 -Installer <path>` as a **mandatory prerequisite in the actual build-and-publish workflow**. A standalone manual workflow is only an audit and does not block publishing.
4. Compare the final signed installer SHA-256 to the hash in the signed update manifest; generate the manifest only **after** signing. Verify the feed signature separately using the app's existing verification key.
5. Verify installer and installed application version resources match the release tag; reject 0.0.0.0.
6. Validate on Windows 11 with Smart App Control enabled and test installation, update, rollback, and uninstall. A valid signature does not guarantee Smart App Control reputation or immediate acceptance.
7. Publish only after the owner explicitly approves the release.

## Current repository changes
- `ci/verify-windows-installer-signature.ps1`: fail-closed signature audit.
- `.github/workflows/verify-r7-signature.yml`: manually triggered R7 audit (not run, and not a release gate).
- Neither change modifies the stable RC3.8.0 or the current published R7 asset.

## Next technical dependency
Locate the actual installer-building and release-publishing workflow in `dtcnexis/DTC-Nexis-App`. Add signing **there**, before upload, with a fail-closed check. Do not merge this work or describe an installer as signed until verified. Never disable Windows security to work around signing.
