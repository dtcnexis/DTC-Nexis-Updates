"""Measure the review-only upstream tables separately from the signed catalogue."""
import csv
import hashlib
import io
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

inventory = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
repo = "repos/dtcnexis/DTC-Nexis-Updates"
heads = json.loads(subprocess.check_output(["gh", "api", repo + "/branches?per_page=100"]))
assert {branch["name"]: branch["commit"]["sha"] for branch in heads} == inventory["branchHeads"], "Refresh the source inventory"
branch = "research/vehicle-catalog-full-staging-20261118"
tree = inventory["branchFiles"][branch]
base = "data/master/reviews/vehicle_catalog_full_20261118/"
tables = defaultdict(dict)
files = []
car_slugs = defaultdict(set)

def blob(name):
    sha = tree[base + name]
    data = subprocess.check_output(["gh", "api", "-H", "Accept: application/vnd.github.raw+json", repo + "/git/blobs/" + sha])
    assert hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == sha, name
    return data.decode("utf-8-sig")

manifest = json.loads(blob("SOURCE_MANIFEST.json"))
for path in sorted(tree):
    if not path.startswith((base+"gor3a/", base+"vehiclesdb/")) or not path.endswith(".csv"):
        continue
    name = path[len(base):]
    rows = csv.DictReader(io.StringIO(blob(name)))
    count = 0
    for row in rows:
        count += 1
        if row.get("kind", "car") != "car":
            continue
        dataset = "VehiclesDB" if "make_slug" in row else "gor3a"
        make = row.get("make_name") or row["make"]
        if dataset == "VehiclesDB":
            car_slugs[row["make_slug"]].add(make)
        stats = tables[dataset].setdefault(make, {"models": set(), "engineRows": 0, "modelRows": 0, "yearLabels": set(), "files": set()})
        stats["models"].add(row.get("model_name") or row["model"])
        stats["files"].add(name)
        stats["engineRows" if "engine_label" in row else "modelRows"] += 1
        for key in ("gen_year_start", "gen_year_end", "year_start", "year_end"):
            if row.get(key):
                stats["yearLabels"].add(row[key])
    assert count == inventory["blobs"][tree[path]]["csvDataRows"]
    files.append({"file": path, "blob": tree[path], "rows": count})
for table in tables.values():
    for stats in table.values():
        for key in ("models", "yearLabels", "files"):
            stats[key] = sorted(stats[key])
report = {"commit": inventory["branchHeads"][branch], "verifiedBranchHeads": len(heads),
          "vehiclesDbCarMakeSlugs": len(car_slugs),
          "vehiclesDbSharedSlugs": {k: sorted(v) for k, v in car_slugs.items() if len(v) > 1},
          "manifest": manifest, "files": files, "bySourceAndMake": tables}
Path(sys.argv[2]).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print({source: (len(table), sum(s["modelRows"] for s in table.values()), sum(s["engineRows"] for s in table.values())) for source, table in tables.items()})
