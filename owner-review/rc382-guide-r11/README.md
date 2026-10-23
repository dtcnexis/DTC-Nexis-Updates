# DTC NEXIS RC3.8.2 — R11 private review, NOT delivered

This isolated candidate adds one `ecu_list` image/card to the four R10 Vehicle Guide cards. The ECU photo (352×272 WebP, 42,274 bytes, SHA-256 `a1a8ac63ab958a7160912c8a99ed494f909c15eb43ec437ffd7e66bd2f952cd7`) was approved by the owner for private testing.

**Do not merge or publish this folder.** The `guide-r11-unsigned-payload.json` is only signing-ready **metadata**, not a signed `envelope`. The exact owner-approved ECU WebP is staged at `owner-review/rc382-guide-r11/images/ecu_list.webp` (42,274 bytes; SHA-256 `a1a8ac63ab958a7160912c8a99ed494f909c15eb43ec437ffd7e66bd2f952cd7`). It is **not** in the live owner-stable channel. The URL in metadata points to a future owner-stable-channel path; it does not presently resolve to an authorized R11 asset.

Verification and release gates:
1. **Staged and verified:** exact owner-approved ECU WebP, with SHA-256 and real WebP dimensions/bytes matched; the four R10 photos remain unchanged.
2. **PASSED** R10→R11 in actual Microsoft Edge using all five SHA-verified owner-approved WebPs, through the existing single update button: https://github.com/dtcnexis/DTC-Nexis-App/actions/runs/40031328945 . This used **ephemeral ECDSA CI signatures**, not the owner's original signing key and NOT a public feed.
3. Produce the owner-authorized R11 signed guide envelope with the **existing P-256 owner signing workflow**; never place the private key in this repo.
4. Verify the signed feed's trust chain, single-button in-place update, anti-rollback, offline persistence, and absence of installer downloads.
5. Keep RC3.8.0 and `owner-stable-data-channel/owner-channel/update-feed.json` unchanged until explicit release approval.

The ECU List currently supports 39 reference ECU types, diagnostic-address searches and *external* exact part-number searches (no unverified ECU/vehicle fitment claims). Import of Auto Scan reports is **not** implemented.

QA screenshot (actual five approved WebPs): https://github.com/dtcnexis/DTC-Nexis-App/blob/review/rc382-owner-final-ui-update-20261023/ci/owner-design-qa/RC382_GUIDE_R11_FIVE_REAL_APPROVED_ECU_EDGE.png

**Visibility:** The Updates repository is public; this staging branch is not a GitHub Release or a live update, but its staged files are readable by anyone with their GitHub URLs. Do not upload secrets here.
