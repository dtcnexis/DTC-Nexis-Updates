# Website library channel

The public data channel belongs to this repository. The website server reads `website-data:current.json` over HTTPS without credentials. Google Drive can store backup archives. Visitors never write to either service.

The initial channel has zero active technical records. The selection in `review/existing.json` references 2,042 public archive definitions whose code, system, English and Arabic match the existing website. To activate them, propose moving that file into `sections/dtc/existing.json` for independent review. Their original review status stays in the source archive.

## Submit a change

Register a section name in `sections.json` and add one or more JSON arrays under `sections/<section>/`. Each record has a stable ASCII `id`, original English `en` and a `source` (an existing public archive path or an HTTPS source). Optional `ar` and `sv` belong to that same record. Put measurements, pin identifiers, technical symbols, codes and applicability in the shared `values` object. The section endpoint returns those values verbatim alongside the selected text. Missing translations fall back to English. For non-generic DTCs use a dedicated section and stable IDs incorporating manufacturer, control unit and applicability.

Generic DTCs use the uppercase code as ID. Model records specify `values.make` and `model`. Years specify `make, model, market, year`. Engine variants specify `make, model, name, yearStart, yearEnd` and their HTTPS source. Vehicle-specific references must retain their scope. Keep one ID across corrections and translations. New sections become readable through the website section API without a publisher change. Displaying a new card is a separate website change.

Open a PR against main and have a different contributor with write access approve its final head. Merge with the base up to date. The publisher checks the reviewed tree, merged PR, reviewer, changed paths, JSON structure, past record IDs and field preservation. Direct content changes fail closed. Check the Actions log before referring to any release. Only an empty initial channel can be created without content approval.

## Operate and restore

The `Central website library` workflow writes one self-contained, checksummed snapshot in a fast-forward commit on `website-data`. It records the source revision, UTC timestamp, source digests and changed paths. A publication failure leaves the existing ref in place. Logs include the changed files and rejection reason. To switch back one published version, run this workflow from main and choose `rollback`. The channel keeps the replaced snapshot as `previous.json` and earlier snapshots remain in Git. On the first publication the website's existing bundled data is the initial fallback. To resume after a rollback, submit a reviewed change accounting for the full difference from the reactivated version. No signing key, Drive credential, cross-repository token or site deployment is required by the data workflow.
