# DTC NEXIS — Windows storage cleanup audit (2026-11-23)

## Confirmed facts
- Central repository: dtcnexis/DTC-Nexis-Updates, default branch main.
- Commit [457f1b6](https://github.com/dtcnexis/DTC-Nexis-Updates/commit/457f1b6592647122eb6d55eaeb4b59730a588d9a) removed twenty installer parts under installer-parts/v7/ from the active branch, alongside Windows release workflow, legacy publication scripts and release-request.json.
- Historical release-request.json at commit [61e89e0](https://github.com/dtcnexis/DTC-Nexis-Updates/commit/61e89e0aef76447833a6b792ce36558620b24772) lists 20 parts totaling 60,776,288 bytes (57.96 MiB, about 60.78 MB decimal). Historical references remain in Git history, so this is NOT evidence of reclaimed space.
- Active main currently returns 404 for installer-parts/v7/part-01.bin, part-20.bin, release-request.json and .github/workflows/publish-windows.yml.
- Current repository size reported separately by GitHub is a repository-level figure, NOT reclaimable bytes from the removed bundle.

## Not yet verified
- Full current tree and exact sizes of other Windows binary files across all branches.
- GitHub Release assets and their download counts, if any.
- Historical Git objects, refs, tags and backup branches retaining old Windows bundles; removal of those may be destructive.
- Dependencies of any release/update clients on older binaries; do not delete without checking.

## Safety gate
Do not remove files, releases, tags, branches, or rewrite history until exact targets, backups, dependencies and actual savings are documented and reviewed. Preserve data/master, website integration, technical sources, original archives and all signed/stable feeds. This is an audit checkpoint only; no deletion, merge or release authorized.

## Resume point
Continue from main and inspect other historical Windows candidates and release assets by exact filename/size. Categorize as already removed / active dependency / review candidate. Then compare before-after repository size only after an approved cleanup; never count deleted paths as freed storage.

## Follow-up branch scan — 2026-11-23
- Enumerated 41 repository branches (as returned by branch search).
- Confirmed that historical `release-request.json` with exact blob SHA `0d21806679a4c6f4597589a5adf5d3c6376ff017` remains present on five checked branches: `owner-stable-data-channel`, `owner-test-batch01-20261018`, `fix/r7-authenticode-release-gate-20261018`, `test/rc382-recovery-signer-qa-20261019`, `staging/vw022-no-activation-20261024`.
- On `main` the same path returns 404. Identical SHA proves the five release-request files are the same blob, NOT that all twenty binary installer parts remain on each branch.
- Branch comparisons with `main` succeeded; they did not establish a full file tree or reclaimable-byte estimate. Releases and tags still need independent inventory.
- **No branches, assets, files or history deleted**. These five refs must not be deleted simply because they contain the old request: some may carry stable/channel state or unrelated reviews.

### Next precise check
Enumerate release assets and tags; inspect full trees for `installer-parts/v7/` on remaining refs; confirm backups and dependencies, then propose per-ref/per-asset deletions only where safe. Preserve signed feeds and branches carrying unique data.

## Verified binary payload and release follow-up — 2026-11-23
- GitHub REST Releases list confirms exactly **one currently listed release** (v7): `DTC_NEXIS_SETUP_R7.exe`, asset ID `653132256`, **60,776,288 bytes** (57.96 MiB), **23 recorded downloads**, published 2026-10-18. URL: https://github.com/dtcnexis/DTC-Nexis-Updates/releases/tag/v7
- Git tree of **main** returned complete (non-truncated), 364 entries; there are **no installer-parts/v7 entries in main**. No significant Windows installer among the largest main branch files.
- Complete Git trees of `owner-stable-data-channel` and `owner-test-batch01-20261018` each still carry all 20 parts at `installer-parts/v7/`, totaling **60,776,288 bytes per branch tree**. These are the same historical release payload by declared sizes; NOT 121,552,576 confirmed unique storage because Git deduplicates shared objects.
- This directly confirms old installer blobs are **still reachable from at least two branches**, so the former main-branch deletion cannot be treated as repository history cleanup.
- **Do not delete the stable branch or the published v7 release yet**: the public release has recorded downloads and release body describes a Windows upgrade/update route. Determine whether active users rely on its asset and whether other refs/tags preserve the installer.
- The release asset and Git objects represent different storage classes; removing a GitHub Release asset would only reclaim its release-asset storage (subject to GitHub's accounting), not Git objects kept alive by refs.
- Attempt to scan all 41 branch trees in one operation exceeded connector execution call limit. Inventory remains **partial**, not all branches have been audited.
- **No destructive action performed**; next resume step: scan remaining branch trees in smaller batches via REST `git/trees/{sha}?recursive=1`, then inspect tags and version-feed references. Separate approved removal of obsolete release assets from preserving original Git data and any live signed feed.

## Follow-up: tag and live-release dependency — 2026-11-23
- Exact v7 release endpoint: release ID `416369505`, asset `DTC_NEXIS_SETUP_R7.exe` ID `653132256`, 60,776,288 bytes, 23 downloads at inspection, and `prerelease=true` (`draft=false`). Release URL: https://github.com/dtcnexis/DTC-Nexis-Updates/releases/tag/v7
- Release description explicitly says the installer is needed once to migrate old Windows installations, and clients subsequently check updates from within the app. **Treat as a live-compatibility dependency until independently disproven.**
- The Git tag `refs/tags/v7` resolves to commit `61e89e0aef76447833a6b792ce36558620b24772`. Its complete tree retains 20 parts totaling 60,776,288 bytes.
- Complete Git trees also confirm 20 parts (same aggregate 60,776,288 bytes) on `fix/r7-authenticode-release-gate-20261018` and `test/rc382-recovery-signer-qa-20261019`, plus previously confirmed `owner-stable-data-channel`, `owner-test-batch01-20261018`.
- This is **one historical payload referenced by multiple refs**, not five independent 60.8 MB allocations. Removing files from only the default branch, or one old branch, cannot reclaim blobs still reachable from the v7 tag and other refs.
- Current main branch does not include an `update-feed.json` at repository root; older stable-related branches do. Do not equate root 404 with confirmation that existing installations have stopped using legacy update endpoints.
- **Cleanup action:** none. Storage actually reclaimed: **0 bytes verified**. Release asset and tag require separate, explicit compatibility review and recovery plan; avoid deleting any stable feeds/tags or rewriting history without verified backups and approval.
- Next: audit all remaining branches/tags and external references to the v7 download and signed feeds. Prioritize safe removal of genuinely abandoned CI artifacts/caches with expiration policies (separate from repository blobs), if applicable. Keep Windows installer removal pending while old Windows clients may still depend on it.

## Old Windows app repository audit — 2026-11-23
- `dtcnexis/DTC-Nexis-App` default `main` tree is complete, with 6 blob files totaling 3,718,860 bytes in the current tree.
- Largest file: `DTC_NEXIS_RC35_PRIVATE_SOURCE.zip` (3,706,058 bytes). **Preserve as original private-source recovery archive**, not an expendable build artifact.
- Other current files: `README.md` and four RC status documents. No current large disposable EXE installer found in this tree.
- Repository-reported size: 65,459 KiB, far larger than current checked-out tree (about 3.55 MiB), suggesting historical Git objects/refs must be audited; **not proof of the amount reclaimable**.
- `DTC-Nexis-Updates` repo-reported size: 62,993 KiB; `DTC-Nexis-Website`: 150,967 KiB. These are repository metadata sizes and must not be summed as recoverable Windows waste.
- Explicit user request to delete unimportant old Windows files recorded. **No current-tree Windows files positively identified as both unnecessary and safely reclaimable yet; no deletion performed.** The v7 release is a prerelease but its description states migration dependency, so removal remains a compatibility risk.
- GitHub connector's GitHub REST fetch does not permit the repository-wide Actions artifacts inventory endpoint in this environment; cache/artifact storage remains unverified. Do not claim these were deleted.
- Next: compare all old Windows refs against main and inventory external release dependencies. Remove only individually proven disposable objects after recovery archive verification and references check; identify whether repository history rewrite would actually be needed and keep it out of the live branch.

## Complete active branch tip scan — 2026-11-23
- Inspected the complete recursive Git tree for **all 41 currently listed branch tips**, in batches. All tree responses were `truncated=false`.
- **37 of 41 active branch tips** carry all 20 files in `installer-parts/v7/`, totaling **60,776,288 bytes per tree**. The **four without them** are `main`, `audit/windows-storage-cleanup-20261123`, `fix/opel-astra-h-z16xep-2006`, and `research/dtc-bilingual-explanations-audit-20261122`.
- This includes data/ and work/ branches for vehicle/DTC research. **Do not delete those branches**: they contain unique work product. Do not count their installer payload once per branch; Git deduplicates identical objects.
- The `v7` tag still references a complete 20-part bundle, as does the published Release installer asset. Therefore merely deleting installer files in the 37 branch *tips* would add deletion commits while leaving historical blobs reachable via the immutable tag and commit ancestry, and cannot be represented as freeing 37 x 60.8 MB.
- No safe destructive cleanup identified among current main and old Windows App tip trees. **No files deleted, no branches deleted, no history rewritten, no release assets removed. Confirmed reclaimed storage: 0 bytes.**
- Next decision gate: confirm whether any old Windows migration path still needs v7; preserve the installer archive and actual signed update feed references. Only consider separate repo migration/archive or coordinated history rewrite if there is a clearly quantified benefit, complete verified backups, a branch-preservation plan, and explicit review. Rewriting public history is high risk and not part of the authorized safe cleanup.
- Actionable non-destructive alternative: new *clean* data-only repository initialized without installer history, only if an architecture migration is approved later; do not silently create a parallel DTC library. Current central repository stays authoritative.

## Product retirement decision — 2026-11-23
- Owner explicitly instructed that the Windows desktop program is retired and the website is the priority. Remove obsolete Windows distribution components, but preserve original archives and all DTC/vehicle data and existing live website infrastructure.
- Website default-branch GitHub code searches for `DTC_NEXIS_SETUP_R7.exe`, `installer-parts`, and `update-feed.json` returned no results (negative code-search result is not an exhaustive dependency proof).
- This connector permits per-file deletion, but **does not expose deleting GitHub Releases, release assets, tags or branch refs**, nor an atomic Git-history rewrite. Those are the operations relevant to reclaiming 60.8 MB old Windows payload. Removing 20 parts from many data-bearing branch tips would not reclaim still-referenced Git objects.
- Do not delete original `DTC_NEXIS_RC35_PRIVATE_SOURCE.zip` until backed up and verified separately, as it is a recovery asset. Do not touch website or master data.
- **Confirmed deletions: none. Confirmed recovered storage: zero.** Retirement decision recorded; deletion of v7 release asset and release retirement must be performed using an authorized GitHub interface or suitable write-capable integration after preserving installer backup, if desired. Remove/update obsolete Windows download links, if discovered, but do not change stable data channels inadvertently.
