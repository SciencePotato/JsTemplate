import contextlib
import io
from pathlib import Path
import shutil
import subprocess
import sys
import unittest
from unittest.mock import patch
import uuid

import Js_Template


class CliTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(".cli-contract-" + uuid.uuid4().hex)
        self.root.mkdir()
        self.addCleanup(shutil.rmtree, self.root)

    def test_scaffold_failure_sets_nonzero_exit_status(self):
        target = self.root / "file"
        target.write_text("unchanged")
        result = subprocess.run([sys.executable, "Js_Template.py"], input=str(target) + "\n",
                                text=True, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(target.read_text(), "unchanged")
        self.assertIn("Error", result.stderr)

    def test_directory_cannot_satisfy_file_placeholder(self):
        (self.root / "index.html").mkdir()
        with self.assertRaises(IsADirectoryError):
            Js_Template.createFile(str(self.root), "index.html")

    def test_file_placeholder_is_empty_and_existing_contents_are_kept(self):
        Js_Template.createFile(str(self.root), "index.html")
        target = self.root / "index.html"
        self.assertEqual(target.read_bytes(), b"")
        target.write_text("keep")
        with contextlib.redirect_stdout(io.StringIO()):
            Js_Template.createFile(str(self.root), "index.html")
        self.assertEqual(target.read_text(), "keep")

    def test_permission_error_reaches_helper_caller(self):
        with patch("builtins.open", side_effect=PermissionError("read only")):
            with self.assertRaises(PermissionError):
                Js_Template.createFile(str(self.root), "index.html")


if __name__ == "__main__":
    unittest.main()
