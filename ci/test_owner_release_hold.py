"""No publishing: unit-test that each Windows release requires owner's explicit approval."""
import importlib.util
import os
from pathlib import Path
import unittest
from unittest.mock import patch

here = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("publisher_under_test", here / "publish_release.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

fingerprint = "A1" * 20
env_base = {
    "NEXIS_OWNER_APPROVED_REVISION": "8",
    "NEXIS_APPROVED_SIGNER_THUMBPRINT": fingerprint,
    "NEXIS_APPROVED_WINDOWS_FILE_VERSION": "0.10.6.0",
}


class OwnerGateTests(unittest.TestCase):
    def verify_block(self, overrides=None, revision=8):
        env = dict(env_base)
        env.update(overrides or {})
        with patch.dict(os.environ, env, clear=True):
            with self.assertRaisesRegex(RuntimeError, "^BLOCK RELEASE:"):
                module.require_owner_release_approval(revision)

    def test_no_owner_approval(self):
        self.verify_block({"NEXIS_OWNER_APPROVED_REVISION": ""})
        self.verify_block({"NEXIS_OWNER_APPROVED_REVISION": "7"})
        self.verify_block({"NEXIS_OWNER_APPROVED_REVISION": "9"})
        self.verify_block({"NEXIS_OWNER_APPROVED_REVISION": "8 "})
        self.verify_block(revision=9)

    def test_missing_or_unpinned_signer(self):
        self.verify_block({"NEXIS_APPROVED_SIGNER_THUMBPRINT": ""})
        self.verify_block({"NEXIS_APPROVED_SIGNER_THUMBPRINT": "UNKNOWN"})
        self.verify_block({"NEXIS_APPROVED_SIGNER_THUMBPRINT": "X" * 40})

    def test_missing_or_invalid_windows_version(self):
        self.verify_block({"NEXIS_APPROVED_WINDOWS_FILE_VERSION": ""})
        self.verify_block({"NEXIS_APPROVED_WINDOWS_FILE_VERSION": "0.0.0.0"})
        self.verify_block({"NEXIS_APPROVED_WINDOWS_FILE_VERSION": "rc382"})
        self.verify_block({"NEXIS_APPROVED_WINDOWS_FILE_VERSION": "3.8.2-release"})

    def test_valid_explicit_approval_does_not_publish(self):
        with patch.dict(os.environ, env_base, clear=True):
            thumbprint, version = module.require_owner_release_approval(8)
        self.assertEqual(thumbprint, fingerprint)
        self.assertEqual(version, "0.10.6.0")


if __name__ == "__main__":
    unittest.main()
