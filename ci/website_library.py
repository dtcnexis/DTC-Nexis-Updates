"""Build one deterministic website snapshot from explicitly selected public records."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTION = re.compile(r"[a-z][a-z0-9-]{0,63}")
CODE = re.compile(r"[PBCU][0-3][0-9A-F]{3}")
ARCHIVE = "data/master/brands/legacy_generic_pbu.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON property {key}")
        require(key not in {"__proto__", "constructor", "prototype"}, f"unsafe key {key}")
        result[key] = value
    return result


def parse(text):
    return json.loads(text, object_pairs_hook=unique_keys, parse_constant=lambda x: require(False, x))


def encode(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def read_snapshot(path):
    envelope = parse(path.read_text(encoding="utf8"))
    require(sha(envelope["payload"]) == envelope["sha256"], "previous snapshot digest mismatch")
    return parse(envelope["payload"])


def rows_for(file, root, read):
    data = read(file)
    if file == "website-library/sections/dtc/existing.json":
        require(data["source"] == ARCHIVE, "unrecognized baseline")
        archive = read(ARCHIVE)
        content = (root / ARCHIVE).read_bytes().replace(b"\r\n", b"\n")
        blob = hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()
        require(blob == data["blob"], "archive changed: review and repin baseline")
        excluded = set(data["exclude"])
        originals = archive["entries"]
        require(excluded <= {r['code'] for r in originals}, "unknown excluded code")
        return [dict(id=r["code"], en=r["en"], ar=r["ar"], source=ARCHIVE)
                for r in originals if r["code"] not in excluded]
    require(isinstance(data, list) and data, f"{file}: expected nonempty record array")
    return data


def validate(section, row):
    require(isinstance(row, dict) and set(row) <= {"id", "en", "ar", "sv", "source", "values"},
            f"{section}: unexpected fields")
    for field in ("id", "en", "source", *(k for k in ("ar", "sv") if k in row)):
        value = row.get(field)
        require(isinstance(value, str) and value.strip() == value and value, f"{section}: invalid {field}")
    require(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,159}", row["id"]), "invalid record ID")
    require(row["source"].startswith(("data/master/", "volkswagen/", "https://")), "missing source")
    values = row.get("values", {})
    require(isinstance(values, dict), "technical values must be an object")
    if section == "dtc":
        require(CODE.fullmatch(row["id"]), "generic DTC must use its uppercase standard code")
    if section in ("models", "years", "engines"):
        for key in ({"models": ["make", "model"], "years": ["make", "model", "market"],
                     "engines": ["make", "model", "name"]}[section]):
            require(isinstance(values.get(key), str) and values[key].strip(), f"{section}: missing {key}")
    for key in {"years": ["year"], "engines": ["yearStart", "yearEnd"]}.get(section, []):
        require(type(values.get(key)) is int and 1886 <= values[key] <= 2199, f"invalid {key}")
    if section == "engines":
        require(values["yearStart"] <= values["yearEnd"] and row["source"].startswith("https://"),
                "invalid engine years or source")


def preserve(old, new, where):
    if isinstance(old, dict):
        require(isinstance(new, dict), f"lost object {where}")
        for k, v in old.items():
            require(k in new, f"removed {where}/{k}")
            preserve(v, new[k], f"{where}/{k}")
    elif isinstance(old, list):
        require(isinstance(new, list) and all(x in new for x in old), f"removed value in {where}")
    else:
        require(type(old) is type(new), f"type changed at {where}")


def build(root, revision, previous=None):
    require(re.fullmatch(r"[0-9a-f]{40}", revision), "invalid source revision")
    files = {}

    def read(file):
        path = root / file
        require(not path.is_symlink() and path.resolve().is_relative_to(root.resolve()), "invalid path")
        text = path.read_text(encoding="utf8")
        files[file] = sha(text)
        return parse(text)

    registry = read("website-library/sections.json")
    require(isinstance(registry, list) and registry and all(SECTION.fullmatch(s) for s in registry)
            and len(set(registry)) == len(registry), "invalid section registry")
    sections = {name: {} for name in registry}
    checked_sources = set()
    identities = set()
    directory = root / "website-library/sections"
    for path in sorted(directory.rglob("*")):
        require(not path.is_symlink(), "links cannot be published")
        if path.is_dir():
            continue
        rel = path.relative_to(directory)
        require(len(rel.parts) == 2 and rel.parts[0] in sections and path.suffix == ".json",
                f"unregistered file {rel}")
        section = rel.parts[0]
        for row in rows_for(path.relative_to(root).as_posix(), root, read):
            validate(section, row)
            fields = {"makes": (), "models": ("make", "model"), "years": ("make", "model", "market", "year"),
                      "engines": ("make", "model", "name", "yearStart", "yearEnd")}
            if section in fields:
                identity = (section, *(str(row["values"][k]).casefold() for k in fields[section])) if fields[section] else (section, row["en"].casefold())
                require(identity not in identities, f"duplicate vehicle identity {identity}")
                identities.add(identity)
            if not row["source"].startswith("https://") and row["source"] not in checked_sources:
                source = (root / row["source"]).resolve()
                require(source.is_relative_to(root.resolve()) and source.is_file(), "missing local evidence")
                checked_sources.add(row["source"])
            key = row["id"]
            require(key not in sections[section], f"duplicate {section}/{key}")
            sections[section][key] = row
    old = previous or {"files": {}, "sections": {}}
    preserve(old["sections"], sections, "sections")
    changed = sorted(k for k in files.keys() | old["files"].keys() if files.get(k) != old["files"].get(k))
    return dict(format=1, revision=revision, publishedAt=datetime.now(timezone.utc).isoformat(),
                changedFiles=changed, files=files, sections=sections)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("revision")
    parser.add_argument("output", type=Path)
    parser.add_argument("--previous", type=Path)
    args = parser.parse_args()
    snap = build(ROOT, args.revision, read_snapshot(args.previous) if args.previous else None)
    payload = encode(snap)
    args.output.write_text(encode(dict(sha256=sha(payload), payload=payload)), encoding="utf8")
    print(f"{sum(map(len, snap['sections'].values()))} records; {len(snap['sections'])} sections; "
          f"content {sha(encode(snap['sections']))}; changed files {snap['changedFiles']}")
