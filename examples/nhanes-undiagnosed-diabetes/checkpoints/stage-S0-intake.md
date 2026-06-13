# S0 Intake：NHANES 慢病风险数据分析与文章写作

## 当前任务

用户希望使用 `academic-research-suite` checkpoint-first 工作流，基于本地 raw 数据目录分析 NHANES 2017-2018 慢病相关数据，并最终写成一篇以 SCI 期刊投稿为目标的论文。

## 已确认输入

- 项目目录：仓库根目录
- raw 数据目录：`data/nhanes_2017_2018/raw`
- 数据文件数量：12 个 `.xpt`
- 数据文件：
  - `DEMO_J.xpt`
  - `BMX_J.xpt`
  - `BPX_J.xpt`
  - `DIQ_J.xpt`
  - `GHB_J.xpt`
  - `GLU_J.xpt`
  - `BPQ_J.xpt`
  - `TCHOL_J.xpt`
  - `HDL_J.xpt`
  - `PAQ_J.xpt`
  - `SMQ_J.xpt`
  - `SLQ_J.xpt`

## 初步任务类型判断

这是一个跨多个 ARS 阶段的研究到文章任务，建议走：

1. S1 Research Question：确认文章研究问题、用途、目标读者和范围。
2. S1b Target Journal & Comparator Corpus：推荐 5 个目标期刊候选，用户确定目标期刊后，用至少 5 篇同刊相似原文校准体裁、字数和表图策略。
3. S2 Method / Analysis Plan：确认变量、统计方法、输出表格和文章结构需要的数据。
4. S3 Evidence / Data Execution：执行本地数据分析和必要官方来源核验。
5. S4 Interpretation：解释结果、限制和可写入文章的结论。
6. S5 Outline：确认文章大纲。
7. S6 Draft：写文章草稿。
8. S7 Integrity / Citation Check：检查数据、引用、统计和表述边界。
9. S8 Review / Revision：如需要，做审稿式修订。
10. S9 Finalize / Closeout：定稿与记忆收尾。

## 当前仍需用户确认的关键点

1. 文章用途：已更新为 SCI 论文投稿目标。
2. 目标读者：医生/医院管理者、医学生/研究生、AI 工程师，还是医疗 AI 培训学员？
3. 主线重点：NHANES 公共数据库介绍、糖尿病/慢病风险分析、医疗 AI 建模流程，还是数据合规与可解释 AI？
4. 输出停止点：建议至少到“完整性检查后的投稿前版本”，但具体期刊、格式和 cover letter 需后续阶段确认。

## 本阶段边界

- 本阶段不运行数据分析。
- 本阶段不写文章正文。
- 本阶段不确认具体研究问题，也不承诺现有数据与题目一定达到 SCI 发表标准。
- 本阶段只完成输入确认、任务归类和下一阶段建议。

## 下一阶段建议

进入 S1 Research Question，优先评估哪些研究问题可能具备 SCI 投稿价值，包括新颖性、可回答性、可用变量、统计可行性和潜在目标期刊方向。S1 确认后必须进入 S1b，不能直接进入方法定稿或正文写作。
