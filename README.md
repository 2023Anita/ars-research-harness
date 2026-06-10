# ars-research-harness

A checkpoint-first academic research workflow harness. This repository turns an AI-assisted paper workflow into a traceable, reproducible, human-confirmed process.

The included case study uses the NHANES 2017-2018 public-use files to build a manuscript package on HbA1c-defined undiagnosed diabetes among self-reported non-diabetic U.S. adults.

![Research-to-Paper Harness](assets/diagrams/01-overview-japanese-handdrawn.png)

## Why This Exists

AI can draft quickly, but research work needs staged decisions: research question, methods, analysis, interpretation, drafting, citation checks, peer-review simulation, revision, and final packaging. This project keeps those stages separate.

Core properties:

- checkpoint-first stage gates
- explicit `workflow-run.json` state
- validator-backed workflow status
- artifact trail for every stage
- complete NHANES example that can be reused as a template

## Quick Start

Install Python dependencies and make sure the R packages `haven`, `dplyr`, `readr`, and `survey` are available:

```bash
python3 -m pip install -r requirements.txt
Rscript -e 'install.packages(c("haven", "dplyr", "readr", "survey"), repos="https://cloud.r-project.org")'
```

```bash
python3 scripts/download_nhanes_small_pack.py
Rscript scripts/run_nhanes_analysis.R
python3 scripts/generate_tables.py
Rscript scripts/generate_figures.R
python3 scripts/build_submission_docx.py
python3 harness/scripts/validate_checkpoint_workflow.py examples/nhanes-undiagnosed-diabetes/workflow-run.json
```

Key outputs:

- `examples/nhanes-undiagnosed-diabetes/workflow-run.json`
- `examples/nhanes-undiagnosed-diabetes/checkpoints/`
- `examples/nhanes-undiagnosed-diabetes/results/`
- `examples/nhanes-undiagnosed-diabetes/submission_package/manuscript_final_with_tables_figures.docx`

## Workflow

![Checkpoint Loop](assets/diagrams/02-checkpoint-loop-japanese-handdrawn.png)

S0-S9 covers intake, research-question framing, methods planning, data execution, interpretation, outline, draft, integrity checks, reviewer-style revision, and final package generation.

## Engineering View

![Harness Architecture](assets/diagrams/03-harness-architecture-japanese-handdrawn.png)

This is a workflow harness, not just a prompt library. The repository includes stage contracts, state artifacts, validation scripts, example outputs, and human confirmation gates.

## Case Study

![NHANES Case Path](assets/diagrams/04-nhanes-case-path-japanese-handdrawn.png)

The NHANES example demonstrates how a public health dataset becomes survey-weighted results, tables, figures, a manuscript draft, a simulated review trail, and a Word submission package.

## Disclaimer

This project is a research workflow and teaching template. It does not guarantee journal acceptance and does not replace statistical, ethical, clinical, or editorial review. NHANES data are from CDC/NCHS public-use files; users are responsible for following source citation and reuse guidance.

中文文档: [README.zh-CN.md](README.zh-CN.md)
