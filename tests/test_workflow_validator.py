import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from harness.scripts.validate_checkpoint_workflow import validate


EXPECTED_STAGE_KEYS = [
    "S0_intake",
    "S1_research_question",
    "S1b_target_journal_fit",
    "S2_method_analysis_plan",
    "S3_evidence_data_execution",
    "S4_interpretation",
    "S5_outline",
    "S6_draft",
    "S7_integrity_citation_check",
    "S8_review_revision",
    "S9_finalize_closeout",
]


def stage(status: str = "pending", artifact: str = "", confirmed: bool = False) -> dict:
    return {
        "status": status,
        "artifact": artifact,
        "userConfirmed": confirmed,
        "confirmedAt": "2026-06-13T00:00:00+0800" if confirmed else "",
    }


def workflow_state() -> dict:
    return {
        "workflow": "academic-research-suite-checkpoint-first",
        "topic": "SCI manuscript submission workflow",
        "currentStage": "S0",
        "checkpointFirst": True,
        "stages": {key: stage() for key in EXPECTED_STAGE_KEYS},
        "artifacts": {},
        "decisions": [],
    }


class WorkflowValidatorTest(unittest.TestCase):
    def validate_state(self, data: dict) -> dict:
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "workflow-run.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            return validate(path)

    def complete_through_s2(self, data: dict) -> None:
        for key in ["S0_intake", "S1_research_question", "S2_method_analysis_plan"]:
            data["stages"][key] = stage("complete", f"checkpoints/{key}.md", True)

    def test_missing_s1b_stage_fails(self):
        data = workflow_state()
        data["stages"].pop("S1b_target_journal_fit")

        result = self.validate_state(data)

        self.assertFalse(result["ok"])
        self.assertIn("S1b_target_journal_fit", result["error"])

    def test_s1b_pending_blocks_s2_completion(self):
        data = workflow_state()
        self.complete_through_s2(data)
        data["stages"]["S1b_target_journal_fit"] = stage("pending")

        result = self.validate_state(data)

        self.assertFalse(result["ok"])
        self.assertIn("target journal gate", result["error"])

    def test_s1b_complete_allows_submission_workflow_to_continue(self):
        data = workflow_state()
        self.complete_through_s2(data)
        data["stages"]["S1b_target_journal_fit"] = stage(
            "complete",
            "checkpoints/stage-S1b-target-journal-fit.md",
            True,
        )

        result = self.validate_state(data)

        self.assertTrue(result["ok"])

    def test_non_submission_workflow_can_skip_s1b_with_reason(self):
        data = workflow_state()
        data["topic"] = "internal teaching handout"
        data["targetJournalGateSkipped"] = True
        data["targetJournalGateSkipReason"] = "Non-submission teaching output."
        data["stages"]["S0_intake"] = stage("complete", "checkpoints/stage-S0-intake.md", True)
        data["stages"]["S1_research_question"] = stage(
            "complete",
            "checkpoints/stage-S1-research-question.md",
            True,
        )
        data["stages"]["S1b_target_journal_fit"] = stage(
            "skipped",
            "checkpoints/stage-S1b-target-journal-fit.md",
            True,
        )
        data["stages"]["S2_method_analysis_plan"] = stage(
            "complete",
            "checkpoints/stage-S2-method-plan.md",
            True,
        )

        result = self.validate_state(data)

        self.assertTrue(result["ok"])

    def test_skipped_s1b_requires_explicit_skip_reason(self):
        data = workflow_state()
        data["stages"]["S0_intake"] = stage("complete", "checkpoints/stage-S0-intake.md", True)
        data["stages"]["S1_research_question"] = stage(
            "complete",
            "checkpoints/stage-S1-research-question.md",
            True,
        )
        data["stages"]["S1b_target_journal_fit"] = stage(
            "skipped",
            "checkpoints/stage-S1b-target-journal-fit.md",
            True,
        )
        data["stages"]["S2_method_analysis_plan"] = stage(
            "complete",
            "checkpoints/stage-S2-method-plan.md",
            True,
        )

        result = self.validate_state(data)

        self.assertFalse(result["ok"])
        self.assertIn("targetJournalGateSkipReason", result["error"])


if __name__ == "__main__":
    unittest.main()
