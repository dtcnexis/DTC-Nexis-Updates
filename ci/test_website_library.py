import json
import hashlib
import shutil
import tempfile
import unittest
from pathlib import Path

from website_library import ARCHIVE, ROOT, build, encode, sha


class WebsiteLibraryTest(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        archive = self.root / ARCHIVE
        archive.parent.mkdir(parents=True)
        shutil.copyfile(ROOT / ARCHIVE, archive)
        self.registry = self.root / "website-library/sections.json"
        self.folder = self.root / "website-library/sections/dtc"
        self.folder.mkdir(parents=True)
        self.registry.write_text('["dtc"]', encoding="utf8")
        contents = archive.read_bytes().replace(b"\r\n", b"\n")
        blob = hashlib.sha1(b"blob " + str(len(contents)).encode() + b"\0" + contents).hexdigest()
        rows = json.loads(contents)["entries"]
        trilingual = json.loads((ROOT / "data/master/dtc_text_catalog.json").read_text(encoding="utf8"))
        keep = {r["code"] for r in trilingual["entries"]}
        selector = {"source": ARCHIVE, "blob": blob, "exclude": [r["code"] for r in rows if r["code"] not in keep]}
        (self.folder / "existing.json").write_text(encode(selector), encoding="utf8")
        self.old = self.build()

    def build(self, previous=None):
        return build(self.root, "0" * 40, previous)

    def test_new_file_same_record_and_real_translation(self):
        catalog_path = "data/master/dtc_text_catalog.json"
        catalog = json.loads((ROOT / catalog_path).read_text(encoding="utf8"))
        row = next(r for r in catalog["entries"] if r["code"] in self.old["sections"]["dtc"])
        key = row["code"]
        selector = self.folder / "existing.json"
        config = json.loads(selector.read_text())
        config["exclude"].append(key)
        selector.write_text(encode(config), encoding="utf8")
        moved = self.old["sections"]["dtc"][key].copy()
        batch = self.folder / "moved.json"
        batch.write_text(encode([moved]), encoding="utf8")
        next_release = self.build(self.old)
        self.assertEqual(next_release["sections"], self.old["sections"])
        moved["sv"] = row["translation_sv"]
        batch.write_text(encode([moved]), encoding="utf8")
        updated = self.build(next_release)
        self.assertEqual(updated["changedFiles"], ["website-library/sections/dtc/moved.json"])
        self.assertEqual(updated["sections"]["dtc"][key]["sv"], row["translation_sv"])
        self.assertEqual(len(updated["sections"]["dtc"]), len(self.old["sections"]["dtc"]))
        del moved["sv"]
        batch.write_text(encode([moved]), encoding="utf8")
        with self.assertRaisesRegex(ValueError, "removed"):
            self.build(updated)

    def test_duplicate_malformed_and_loss(self):
        batch = self.folder / "duplicate.json"
        batch.write_text(encode([next(iter(self.old["sections"]["dtc"].values()))]), encoding="utf8")
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.build()
        batch.write_text("{", encoding="utf8")
        with self.assertRaises(ValueError):
            self.build()
        batch.unlink()
        (self.folder / "existing.json").unlink()
        with self.assertRaisesRegex(ValueError, "removed"):
            self.build(self.old)

    def test_new_section_and_empty_english(self):
        name = "diagnostic-references"
        registry = json.loads(self.registry.read_text())
        self.registry.write_text(encode([*registry, name]), encoding="utf8")
        folder = self.folder.parent / name
        folder.mkdir()
        file = folder / "existing.json"
        record = next(iter(self.old["sections"]["dtc"].values())).copy()
        file.write_text(encode([record]), encoding="utf8")
        self.assertEqual(self.build(self.old)["sections"][name][record["id"]], record)
        record["en"] = ""
        file.write_text(encode([record]), encoding="utf8")
        with self.assertRaisesRegex(ValueError, "invalid en"):
            self.build()
