# DTC NEXIS RC3.8.2 — R11 private review, NOT delivered

This isolated candidate adds one `ecu_list` image/card to the four R10 Vehicle Guide cards. The ECU photo (352×272 WebP, 42,274 bytes, SHA-256 `a1a8ac63ab958a7160912c8a99ed494f909c15eb43ec437ffd7e66bd2f952cd7`) was approved by the owner for private testing.

**Do not merge or publish this folder.** The `guide-r11-unsigned-payload.json` is only signing-ready **metadata**, not a signed `envelope`. The ECU image binary is **not present** in the Updates repository yet. The URL in metadata points to a future owner-stable-channel path; it does not presently resolve to an authorized R11 asset.

Remaining gates:
1. Upload the **exact** owner-approved ECU WebP to a private staging location, verify SHA-256 and real WebP dimensions/bytes against the owner approval; preserve all four R10 images.
2. Test R10→R11 in Windows Edge using the five **actual approved** images from staging. The synthetic-ECDSA CI R11 test does not replace this.
3. Produce the owner-authorized R11 signed guide envelope with the **existing P-256 owner signing workflow**; never place the private key in this repo.
4. Verify the signed feed's trust chain, single-button in-place update, anti-rollback, offline persistence, and absence of installer downloads.
5. Keep RC3.8.0 and `owner-stable-data-channel/owner-channel/update-feed.json` unchanged until explicit release approval.

The ECU List currently supports 39 reference ECU types, diagnostic-address searches and *external* exact part-number searches (no unverified ECU/vehicle fitment claims). Import of Auto Scan reports is **not** implemented.
