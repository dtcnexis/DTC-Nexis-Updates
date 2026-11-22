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
