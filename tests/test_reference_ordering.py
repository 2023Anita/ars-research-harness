import unittest

from scripts.build_submission_docx import prepare_citation_ordered_lines


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


if __name__ == "__main__":
    unittest.main()
