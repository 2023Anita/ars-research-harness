#!/usr/bin/env python3
"""Validate Anita's checkpoint-first ARS workflow state file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


STAGE_KEYS = [
    "S0_intake",
    "S1_research_question",
    "S2_method_analysis_plan",
    "S3_evidence_data_execution",
    "S4_interpretation",
    "S5_outline",
    "S6_draft",
    "S7_integrity_citation_check",
    "S8_review_revision",
    "S9_finalize_closeout",
]

TERMINAL_STATUSES = {"complete", "skipped"}
ACTIVE_STATUSES = {"pending", "in_progress", "blocked", "needs_user_decision"}
ALLOWED_STATUSES = TERMINAL_STATUSES | ACTIVE_STATUSES


def fail(message: str) -> dict:
    return {"ok": False, "error": message}


def validate(path: Path) -> dict:
    if not path.exists():
        return fail(f"state file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if data.get("workflow") != "academic-research-suite-checkpoint-first":
        return fail("workflow must be academic-research-suite-checkpoint-first")
    if data.get("checkpointFirst") is not True:
        return fail("checkpointFirst must be true")

    stages = data.get("stages")
    if not isinstance(stages, dict):
        return fail("missing stages object")

    missing = [key for key in STAGE_KEYS if key not in stages]
    if missing:
        return fail(f"missing stages: {', '.join(missing)}")

    completed_indices = []
    for idx, key in enumerate(STAGE_KEYS):
        stage = stages[key]
        status = stage.get("status")
        if status not in ALLOWED_STATUSES:
            return fail(f"{key} has invalid status: {status}")
        if status in TERMINAL_STATUSES:
            completed_indices.append(idx)
            artifact = stage.get("artifact", "")
            if status == "complete" and not artifact:
                return fail(f"{key} is complete but artifact is empty")
            if idx < len(STAGE_KEYS) - 1 and stage.get("userConfirmed") is not True:
                return fail(f"{key} is {status} but userConfirmed is not true")

    if completed_indices:
        max_completed = max(completed_indices)
        for idx in range(max_completed):
            key = STAGE_KEYS[idx]
            status = stages[key].get("status")
            if status not in TERMINAL_STATUSES:
                return fail(f"stage jump detected: {key} is {status} before later completed stage")

    current_stage = data.get("currentStage")
    if current_stage and current_stage not in [key.split("_", 1)[0] for key in STAGE_KEYS]:
        return fail(f"invalid currentStage: {current_stage}")

    return {
        "ok": True,
        "stageCount": len(STAGE_KEYS),
        "completedStages": len(completed_indices),
        "currentStage": current_stage,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("state_file", help="Path to workflow-run.json")
    args = parser.parse_args()
    result = validate(Path(args.state_file))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
