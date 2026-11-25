"""Generate a pointer-only review of the pinned library using existing Git objects."""

import argparse
import csv
import json
import subprocess
from collections import Counter
from pathlib import Path

DATA = "c450625e5e3b2dc41ce0892dcd9f3fb2750df6d8"
WEB = "b980c94c478b735413f258160ae8cbba1689bb87"
MAZDA = "79b0c385e2f138175d509253f9c19106347ea918"
MAZDA_FILE = "data/master/brands/mazda_20261116_oem_tsb_additions.json"
FIELDS = ("symptoms", "causes", "diagnostic_steps", "repair_steps")
OUT = Path(__file__).resolve().parent


def document(repo, revision, path):
    raw = subprocess.check_output(["git", "-C", str(repo), "show", f"{revision}:{path}"])
    return json.loads(raw)


def literal(row):
    for key in ("code", "raw_code", "code_raw"):
        if row.get(key):
            return str(row[key]).strip().upper()
    raise ValueError("Missing code field")


def ranges(indices):
    result = []
    for index in indices:
        if result and result[-1][1] == index - 1:
            result[-1][1] = index
        else:
            result.append([index, index])
    return ",".join(str(a) if a == b else f"{a}-{b}" for a, b in result)


def nested_fields(value):
    found = set()
    if isinstance(value, dict):
        found.update(k for k in FIELDS if value.get(k))
        value = list(value.values())
    if isinstance(value, list):
        for item in value:
            found.update(nested_fields(item))
    return found


def write_csv(name, records):
    with (OUT / name).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)


def run(website, mazda_repo):
    manifest = document(OUT, DATA, "data/master/all_collected_catalog_manifest.json")
    site = {literal(row) for row in document(website, WEB, "dist/data/definitions.json")}
    site.update(document(website, WEB, "dist/data/oem.json"))
    totals = Counter({field + suffix: 0 for field in FIELDS for suffix in ("_direct", "_nested_only")})
    all_codes, mazda_codes = set(), set()
    coverage = []
    for collection in manifest["collections"]:
        path = collection["path"]
        source = document(OUT, DATA, path)
        key = next(k for k in ("entries", "records", "items") if k in source)
        rows = source[key]
        assert len(rows) == collection["rows"], path
        absent, missing_en, no_fields, nested_only = [], [], [], []
        counts = Counter()
        for i, row in enumerate(rows):
            code = literal(row)
            all_codes.add(code)
            if path == "data/master/brands/mazda.json":
                mazda_codes.add(code)
            if code not in site:
                absent.append(i)
            if not (row.get("definition_en") or row.get("en")):
                missing_en.append(i)
            direct = {field for field in FIELDS if row.get(field)}
            found = nested_fields(row)
            if not found:
                no_fields.append(i)
            elif not direct:
                nested_only.append(i)
            for field in FIELDS:
                if field in direct:
                    counts[field + "_direct"] += 1
                elif field in found:
                    counts[field + "_nested_only"] += 1
        counts.update(rows=len(rows), absent_from_web_rows=len(absent),
                      missing_direct_english=len(missing_en), no_named_fields=len(no_fields),
                      only_nested_technical_rows=len(nested_only))
        totals.update(counts)
        coverage.append(dict(path=path, array=key, rows=len(rows),
                             absent_from_web_indices=ranges(absent), missing_direct_english_indices=ranges(missing_en),
                             no_named_technical_fields_indices=ranges(no_fields),
                             nested_technical_only_indices=ranges(nested_only),
                             **{field + suffix: counts[field + suffix] for field in FIELDS
                                for suffix in ("_direct", "_nested_only")}))
    assert totals["rows"] == manifest["current_saved_row_count"]
    assert len(set(r["path"] for r in coverage)) == len(coverage) == manifest["file_count"]
    write_csv("collection-gaps.csv", coverage)

    existing_batch = document(mazda_repo, MAZDA, MAZDA_FILE)
    queue = []
    for i, row in enumerate(existing_batch["records"]):
        code = literal(row)
        queue.append(dict(pointer=f"/records/{i}", source_record_id=row["record_id"], code=code,
                          ecu=row["ecu"], in_web=code in site, in_master=code in all_codes,
                          in_mazda_baseline=code in mazda_codes, source_ids=",".join(row["source_ids"]),
                          source_classification=row["verification_status"]))
    assert len({r["source_record_id"] for r in queue}) == len(queue)
    write_csv("mazda-review.csv", queue)
    summary = dict(library_commit=DATA, website_commit=WEB, collections=len(coverage),
                   web_literals=len(site), archive_literals=len(all_codes),
                   shared_literals=len(all_codes & site), archive_only_literals=len(all_codes - site),
                   web_only_literals=sorted(site - all_codes), row_counts=dict(sorted(totals.items())),
                   mazda_source_commit=MAZDA, mazda_source_file=MAZDA_FILE,
                   mazda_contexts=len(queue), mazda_literals=len({r["code"] for r in queue}),
                   mazda_absent_from_web=sorted({r["code"] for r in queue if not r["in_web"]}),
                   mazda_source_classes=dict(Counter(r["source_classification"] for r in queue)))
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("website", type=Path, help="Website checkout containing the pinned development commit")
    parser.add_argument("mazda_repo", type=Path, help="Updates checkout containing the existing Mazda review commit")
    args = parser.parse_args()
    run(args.website, args.mazda_repo)
