# 02. Quickstart

## 5 分钟理解项目

先看三个文件：

1. `README.zh-CN.md`
2. `examples/nhanes-undiagnosed-diabetes/workflow-run.json`
3. `examples/nhanes-undiagnosed-diabetes/checkpoints/stage-S9-finalize-closeout.md`

你会看到一个完整路径：公共数据进入分析脚本，生成结果表和图，再进入论文写作、审稿模拟、修回和投稿前包。

## 15 分钟复刻最小流程

先安装依赖：

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

如果只想看结果，不想重新运行分析，直接打开：

```text
examples/nhanes-undiagnosed-diabetes/submission_package/
```

推荐优先查看 `manuscript_final_with_tables_figures.docx`。
