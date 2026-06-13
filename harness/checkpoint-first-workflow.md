# Academic Research Suite Checkpoint-First Workflow

## 定位

这是 Anita 本机对 `academic-research-suite` 的强制执行覆盖层。它把 ARS 从“可调用 skill”提升为“有状态、有门禁、可验收的 workflow”。

触发条件：
- 用户调用 `academic-research-suite`
- 用户输入 `/Academic Research Suite`
- 用户输入 `$academic-research-suite`
- 用户输入 `ars-full`、`ars-plan`、`ars-outline`、`ars-lit-review` 等 ARS alias
- 用户明确说“用 ARS / Academic Research Suite 工作流”

## 铁律

1. 必须 checkpoint-first。
2. 每次只推进一个阶段。
3. 阶段完成后必须停下，等待用户明确确认。
4. 没有用户确认，不得进入下一阶段。
5. 不得把研究问题确认、分析方案、数据执行、结果解释、文章大纲、正文写作、引用检查、审稿和定稿压缩成一次性交付。
6. 如果研究问题、文章用途、目标读者或输出形态不清楚，必须先进入 Socratic narrowing。
7. SCI / 投稿型任务在 S1 研究问题确认后，必须完成 S1b 目标期刊与相似文章体裁门禁：先推荐 5 个目标期刊候选，用户确定目标期刊后，再记录至少 5 篇同目标期刊相似 original research 的链接 / DOI / 摘要 / 体裁矩阵。
8. 未完成 S1b 时，不得进入 S2 方法定稿、S5 大纲或 S6 正文写作；如果全文无法访问，必须停在 S1b 要求用户提供下载材料或可访问链接。
9. 只有用户明确说“全自动继续”“跳过 checkpoint”“一次性完成全部阶段”时，才允许弱化 checkpoint；即便如此，涉及数据解释、引用、审稿、发布、上传、提交、外部 API 或敏感内容时仍需停下确认。

## 强制状态机

| 阶段 | 名称 | 目标 | 交付物 | 进入下一阶段条件 |
|---|---|---|---|---|
| S0 | Intake | 明确任务类型、用途、读者、输出形态、停止点 | `stage-S0-intake.md` | 用户确认 |
| S1 | Research Question | 收敛研究问题、范围、假设/分析边界 | `stage-S1-research-question.md` | 用户确认 |
| S1b | Target Journal & Comparator Corpus | 确定目标期刊，并用至少 5 篇同刊相似原文校准体裁、字数和表图策略 | `stage-S1b-target-journal-fit.md` | 用户确认 |
| S2 | Method / Analysis Plan | 确认数据、变量、方法、统计/写作方案 | `stage-S2-method-plan.md` | 用户确认 |
| S3 | Evidence / Data Execution | 执行检索、数据分析或材料整理 | `stage-S3-evidence-results.md` | 用户确认 |
| S4 | Interpretation | 解释结果、限制、风险和可用结论 | `stage-S4-interpretation.md` | 用户确认 |
| S5 | Outline | 生成文章/报告结构和论证蓝图 | `stage-S5-outline.md` | 用户确认 |
| S6 | Draft | 写正文草稿或修订稿 | `stage-S6-draft.md` | 用户确认 |
| S7 | Integrity / Citation Check | 检查引用、数据、声明、统计解释 | `stage-S7-integrity-check.md` | 用户确认 |
| S8 | Review / Revision | 模拟审稿、修订路线图、回应 | `stage-S8-review-revision.md` | 用户确认 |
| S9 | Finalize / Closeout | 输出最终版本、过程记录、记忆收尾 | `stage-S9-final.md` | 完成 |

阶段可按任务缩短，但不能改变顺序。例如“只写摘要”仍需 S0 确认用途和边界，然后进入对应阶段；“只做 citation-check”仍需 S0 确认待检材料和引用格式，然后执行 S7。

## 运行目录

每次完整或重要 ARS 任务必须创建本地运行目录：

```text
.workflow/academic-research-suite/<slug>/
|-- workflow-run.json
|-- checkpoints/
|   |-- stage-S0-intake.md
|   |-- stage-S1-research-question.md
|   `-- ...
|-- artifacts/
|-- sources/
|-- results/
`-- final-report.md
```

如果当前项目没有 `.workflow/`，在当前工作目录创建。若只是短问答或单阶段咨询，可不创建目录，但仍必须在回复里给出 checkpoint 并等待确认。

## Checkpoint 输出格式

每个阶段结束时必须用以下格式收尾：

```markdown
**ARS Checkpoint**
阶段：Sx - 阶段名称
状态：complete / blocked / needs-user-decision
本阶段交付物：
- ...

关键决定：
- ...

风险与限制：
- ...

下一阶段建议：Sy - 阶段名称
需要你确认：是否进入下一阶段？
```

等待用户确认的词包括：`确认`、`继续`、`进入下一阶段`、`同意`、`可以`、`按这个走`。

## 禁止行为

- 禁止在 S0/S1 未完成时直接写全文。
- 禁止在 SCI / 投稿型任务未完成 S1b 时定稿方法、大纲、正文目标字数或表图数量。
- 禁止在 S2 未确认时执行数据分析或实验。
- 禁止在 S3 未确认时把结果写成定稿结论。
- 禁止在 S5 未确认时直接写完整正文。
- 禁止在 S7 未执行或明确跳过时宣称“文章完成”。
- 禁止把未验证引用写成确定来源。
- 禁止把横断面或观察性分析写成因果结论。

## 降级规则

如果无法创建文件、无法访问数据、无法联网核验、或缺少必要工具：

1. 停在当前阶段。
2. 说明阻塞原因。
3. 给出最小下一步。
4. 不得伪造下游阶段产物。
