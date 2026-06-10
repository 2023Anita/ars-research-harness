# 06. 发布到 GitHub

## 推荐仓库信息

- Repository name: `ars-research-harness`
- Description: `Checkpoint-first academic research workflow harness with a reproducible NHANES research-to-paper example.`
- Topics: `academic-writing`, `research-workflow`, `nhanes`, `reproducible-research`, `ai-workflow`, `checkpoint-first`, `medical-ai`

## 发布前检查

```bash
python3 harness/scripts/validate_checkpoint_workflow.py examples/nhanes-undiagnosed-diabetes/workflow-run.json
python3 scripts/generate_handdrawn_diagrams.py
python3 scripts/build_submission_docx.py
git status --short
```

确认 `git status --short` 中只出现准备公开的项目文件。`.workflow/`、旧临时包、`.DS_Store` 和 Word 临时文件应被 `.gitignore` 排除。

## 推荐首版 release note

`v0.1.0`:

- Adds checkpoint-first research workflow harness.
- Adds S0-S9 NHANES undiagnosed diabetes case study.
- Adds validator, templates, data small pack, tables, figures, and DOCX manuscript package.
- Adds bilingual documentation and hand-drawn workflow diagrams.
