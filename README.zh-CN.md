# ars-research-harness

一个把 AI 学术写作从“提示词输出”升级为“受控工程流程”的研究工作流项目。它以 NHANES 2017-2018 未诊断糖尿病论文为完整案例，展示如何从公共医学数据走到分析结果、表图、论文初稿、审稿模拟、修回和投稿前 Word 包。

![Research-to-Paper Harness](assets/diagrams/01-overview-japanese-handdrawn.png)

图 1 讲解：这张图适合放在课程开场。它把项目压缩成一条主线：公共健康数据不是直接交给 AI 写论文，而是依次经过研究问题、统计分析、论文写作、审稿修回，最后才形成投稿前包。讲课时可以强调：这个项目的重点不是“让 AI 快速写一篇文章”，而是“让 AI 在科研流程里按阶段留下证据”。

## 这个项目解决什么问题

普通 AI 写论文很容易一次性跳过关键步骤：还没确认研究问题就跑分析，还没核对引用就写结论，还没审稿就生成“最终稿”。`ars-research-harness` 的核心是 checkpoint-first：

- 每个阶段只完成一个明确任务。
- 每个阶段都留下可检查产物。
- 进入下一阶段前必须有人确认。
- 所有阶段状态写入 `workflow-run.json`。
- validator 检查流程是否越级或缺少确认。

这让 AI 工作流更像一个可审计的科研流水线，而不是一次性的聊天输出。

## 快速开始

安装 Python 依赖，并确保 R 中已有 `haven`、`dplyr`、`readr`、`survey`：

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

运行后重点查看：

- `examples/nhanes-undiagnosed-diabetes/workflow-run.json`
- `examples/nhanes-undiagnosed-diabetes/checkpoints/`
- `examples/nhanes-undiagnosed-diabetes/results/`
- `examples/nhanes-undiagnosed-diabetes/submission_package/manuscript_final_with_tables_figures.docx`

## S0-S9 工作流

![Checkpoint Loop](assets/diagrams/02-checkpoint-loop-japanese-handdrawn.png)

图 2 讲解：这是项目最核心的控制逻辑。每个阶段都要先计划，再产出一个可检查 artifact，然后运行校验，最后由人确认。只有确认后才能进入下一阶段。中间的 `STOP: no auto-continue` 是本项目和普通 AI 自动写作最大的区别：AI 不能凭惯性把研究问题、分析、写作、投稿包一次性做完。

| 阶段 | 目的 | 产物 |
|---|---|---|
| S0 | 明确目标、数据、边界 | intake checkpoint |
| S1 | 收敛研究问题 | research question |
| S1b | 确定目标期刊和相似文章体裁 | journal fit + comparator corpus |
| S2 | 制定方法和分析方案 | method plan |
| S3 | 执行数据分析 | results tables |
| S3b | 修正模型复杂度 | parsimonious model |
| S4 | 解释结果 | interpretation |
| S5 | 生成 IMRaD 大纲 | outline |
| S5b | 建立文献矩阵 | literature matrix |
| S6 | 写英文 SCI 初稿 | manuscript draft |
| S7 | 数据、引用、论断完整性核查 | integrity report |
| S7b | 清理引用和参考文献 | citation-clean draft |
| S8 | 模拟审稿和修回路线 | reviewer report |
| S8b | 实施 major revision | revised manuscript |
| S9 | 生成投稿前包 | DOCX, tables, figures, checklist |

教学时可以把这张表当作课堂主导航：每讲完一个阶段，就回到这张表，让学员知道当前处在研究链条的哪一环。

更详细的逐步讲解见：[docs/03-stage-by-stage.zh-CN.md](docs/03-stage-by-stage.zh-CN.md)。

## Harness 架构

![Harness Architecture](assets/diagrams/03-harness-architecture-japanese-handdrawn.png)

图 3 讲解：这张图适合面向工程师或高级学员解释“为什么它是 harness 工程”。Skill Router 决定进入哪类研究任务，Workflow 定义阶段，Stage Contract 规定每阶段能做什么，State JSON 记录状态，Validator 检查合规性，Artifacts 保存证据，Human Confirm 作为人工门禁。换句话说，它不是一个更长的 prompt，而是一个把 AI 包起来的执行框架。

这个项目把 Academic Research Suite 包装成一个本地 workflow harness：

- `harness/checkpoint-first-workflow.md`：阶段规则和执行边界。
- `harness/templates/workflow-run.template.json`：状态文件模板。
- `harness/scripts/validate_checkpoint_workflow.py`：检查阶段状态。
- `examples/nhanes-undiagnosed-diabetes/`：完整 NHANES 案例。
- `scripts/`：可复用执行入口。

## NHANES 案例

![NHANES Case Path](assets/diagrams/04-nhanes-case-path-japanese-handdrawn.png)

图 4 讲解：这张图适合进入实操部分时使用。NHANES 小包数据先通过 survey analysis 生成统计结果，再拆成论文里的表、图，最后合并进 Word 投稿包。它帮助学员理解：数据、结果、图表和论文不是分散文件，而是一条可以复刻的生产链。

示例研究问题：在自报无糖尿病的美国成年人中，HbA1c 定义的未诊断糖尿病患病率及其心代谢、生活方式相关因素是什么？

案例包括：

- NHANES 2017-2018 小包数据。
- R survey 加权分析。
- Table 1、Table 2、Figure 1、Figure 2。
- 引用核查和修回记录。
- 最终通用 SCI Word 稿。

## 与普通 prompt/skill 的区别

| 维度 | 普通 prompt | 普通 skill | workflow harness |
|---|---|---|---|
| 阶段边界 | 弱 | 中 | 强 |
| 状态记录 | 通常没有 | 不一定 | 必须有 |
| 人工确认 | 可选 | 可选 | 阶段门禁 |
| 可追溯性 | 弱 | 中 | 强 |
| 复刻性 | 依赖聊天上下文 | 依赖说明 | 依赖文件和状态机 |

## 作为教学课件使用

如果你要把本项目用于 AI 医学科研培训，建议按下面的 90-120 分钟结构讲：

1. 先用图 1 解释从数据到论文包的完整链条。
2. 用图 2 解释 checkpoint-first，强调每一步必须停下来确认。
3. 用图 3 解释 harness 工程：状态、验证、产物、人工门禁。
4. 用图 4 进入 NHANES 示例，展示真实数据如何变成表、图和 Word。
5. 打开 `examples/nhanes-undiagnosed-diabetes/workflow-run.json`，让学员看状态机。
6. 打开 `checkpoints/`，让学员看每一步留下的证据。
7. 打开最终 Word 文件，展示图表已经嵌入稿件。
8. 最后让学员复制示例目录，替换成自己的数据集。

完整教学讲义见：[docs/07-teaching-courseware.zh-CN.md](docs/07-teaching-courseware.zh-CN.md)。

## 重要声明

- 本项目是科研工作流和教学模板，不保证论文被 SCI 接收。
- NHANES 是复杂抽样调查；正式推断必须使用权重、分层和 PSU。
- AI 生成的研究文本需要人工统计、伦理、引用和期刊格式复核。
- NHANES 数据来自 CDC/NCHS public-use files，使用者应遵守原始数据来源说明和引用规范。

English documentation: [README.md](README.md)
