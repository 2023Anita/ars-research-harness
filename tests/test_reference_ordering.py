import unittest
from tempfile import TemporaryDirectory
from pathlib import Path

from scripts.build_submission_docx import prepare_citation_ordered_lines, write_reference_order_report


class ReferenceOrderingTest(unittest.TestCase):
    def test_reorders_references_by_first_citation_and_rewrites_body(self):
        lines = [
            "# Title",
            "",
            "Opening cites surveillance before methods [7].",
            "Methods cite guidelines later [1,2].",
            "Clinical thresholds cite two sources [5,6].",
            "",
            "# References",
            "",
            "1. Methods guideline.",
            "2. Weighting tutorial.",
            "5. ADA threshold.",
            "6. NIDDK threshold.",
            "7. Surveillance report.",
        ]

        ordered = prepare_citation_ordered_lines(lines)

        self.assertEqual(ordered.lines[2], "Opening cites surveillance before methods [1].")
        self.assertEqual(ordered.lines[3], "Methods cite guidelines later [2-3].")
        self.assertEqual(ordered.lines[4], "Clinical thresholds cite two sources [4-5].")
        self.assertEqual(
            ordered.lines[8:13],
            [
                "1. Surveillance report.",
                "2. Methods guideline.",
                "3. Weighting tutorial.",
                "4. ADA threshold.",
                "5. NIDDK threshold.",
            ],
        )

    def test_raises_when_citation_has_no_reference_entry(self):
        with self.assertRaisesRegex(ValueError, "Missing reference entries: 9"):
            prepare_citation_ordered_lines(["Body [9].", "# References", "1. Only ref."])

    def test_preserves_trailing_sections_after_numbered_references(self):
        lines = [
            "# Title",
            "Body cites later reference [2].",
            "",
            "# References",
            "",
            "1. Uncited reference.",
            "2. Cited reference.",
            "",
            "---",
            "",
            "# Data Availability",
            "Data remain available.",
            "",
            "# Ethics Statement",
            "No additional participant contact occurred.",
        ]

        ordered = prepare_citation_ordered_lines(lines)

        self.assertIn("# Data Availability", ordered.lines)
        self.assertIn("Data remain available.", ordered.lines)
        self.assertIn("# Ethics Statement", ordered.lines)
        self.assertIn("No additional participant contact occurred.", ordered.lines)
        self.assertEqual(ordered.lines[5], "1. Cited reference.")

    def test_reference_order_report_uses_lf_line_endings(self):
        ordered = prepare_citation_ordered_lines(["Body [1].", "# References", "1. Ref."])

        with TemporaryDirectory() as tmpdir:
            write_reference_order_report(ordered, Path(tmpdir))
            data = (Path(tmpdir) / "reference_order_check.csv").read_bytes()

        self.assertNotIn(b"\r\n", data)
        self.assertIn(b"old_reference_number,new_reference_number,status\n", data)


if __name__ == "__main__":
    unittest.main()
