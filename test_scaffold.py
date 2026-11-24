from pathlib import Path
import runpy
import shutil
import unittest
from unittest.mock import patch
import uuid

import Js_Template


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(".scaffold-test-" + uuid.uuid4().hex)
        self.root.mkdir()
        self.addCleanup(shutil.rmtree, self.root)

    def test_nested_target_is_created_and_rerun_preserves_content(self):
        target = self.root / "nested" / "site"
        script = Path(__file__).with_name("Js_Template.py")
        with patch("builtins.input", return_value=str(target)), patch("builtins.print"):
            runpy.run_path(str(script), run_name="__main__")
        self.assertTrue((target / "index.html").is_file())
        (target / "index.html").write_text("keep my page")
        with patch("builtins.input", return_value=str(target)), patch("builtins.print"):
            runpy.run_path(str(script), run_name="__main__")
        self.assertEqual((target / "index.html").read_text(), "keep my page")
        self.assertTrue((target / "src" / "scss" / "main.scss").is_file())

    def test_directory_collision_is_reported_at_directory_creation(self):
        target = self.root / "assets"
        target.write_text("not a directory")
        with self.assertRaises(FileExistsError):
            Js_Template.createDir(str(target))
        self.assertEqual(target.read_text(), "not a directory")


if __name__ == "__main__":
    unittest.main()
