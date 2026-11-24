import tempfile
import unittest
from pathlib import Path

from repo_health.checks import run_checks


class RunChecksTests(unittest.TestCase):
    def test_detects_present_files_and_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("readme", encoding="utf-8")
            (root / "LICENSE").write_text("license", encoding="utf-8")
            (root / ".github" / "workflows").mkdir(parents=True)

            results = {result.name: result for result in run_checks(root)}

            self.assertTrue(results["README"].present)
            self.assertTrue(results["License"].present)
            self.assertTrue(results["CI workflow"].present)
            self.assertFalse(results["Contributing guide"].present)
            self.assertFalse(results["Security policy"].present)
            self.assertFalse(results["Issue templates"].present)

    def test_detects_security_policy_and_issue_templates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "SECURITY.md").write_text("security", encoding="utf-8")
            (root / ".github" / "ISSUE_TEMPLATE").mkdir(parents=True)

            results = {result.name: result for result in run_checks(root)}

            self.assertTrue(results["Security policy"].present)
            self.assertTrue(results["Issue templates"].present)

    def test_rejects_a_file_as_repository_path(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "file"
            path.write_text("not a directory", encoding="utf-8")
            with self.assertRaises(ValueError):
                run_checks(path)


if __name__ == "__main__":
    unittest.main()
