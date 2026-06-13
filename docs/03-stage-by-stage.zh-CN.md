# 03. S0-S9 分阶段说明

这一页可以直接作为课堂讲义使用。讲解重点不是背阶段名，而是让学员理解：每一阶段都有明确目标、输入、输出、停止点和质量风险。

| 阶段 | 关键问题 | 不允许做什么 |
|---|---|---|
| S0 | 目标是什么，边界是什么？ | 不直接写论文 |
| S1 | 研究问题是否可回答？ | 不直接跑分析 |
| S1b | 目标期刊和相似文章体裁是否确定？ | 不凭感觉定字数和表图数量 |
| S2 | 数据、变量、模型和敏感性分析怎么定？ | 不临时改口径 |
| S3 | 按方案执行分析 | 不过度解释 |
| S3b | 模型是否需要简化？ | 不硬塞过拟合模型 |
| S4 | 结果意味着什么？ | 不做因果夸大 |
| S5 | IMRaD 结构如何组织？ | 不写完整正文 |
| S5b | 文献矩阵是否够支撑论点？ | 不伪造引用 |
| S6 | 写完整初稿 | 不声称已投稿 |
| S7 | 核查数据、引用、论断 | 不忽略风险 |
| S7b | 清理引用和参考文献 | 不保留未核验占位文献 |
| S8 | 模拟审稿和修回路线 | 不直接定稿 |
| S8b | 实施修回 | 不跳过表图和统计细节 |
| S9 | 生成投稿前包 | 不承诺期刊接收 |

每一阶段都应该有一个 checkpoint 文件，并在 `workflow-run.json` 里记录状态。

## S0 Intake：先定义任务边界

S0 的目标是回答“我们到底要做什么”。在 NHANES 案例里，最初任务不是泛泛写一篇培训文章，而是明确为：用公共医学数据形成一篇 SCI 投稿前论文包。

课堂讲法：

- 让学员先说目标：教学演示、论文投稿、内部报告还是产品原型。
- 明确数据路径、输出形式和不做什么。
- 强调如果 S0 没做好，后面所有自动化都会跑偏。

产物示例：`checkpoints/stage-S0-intake.md`。

## S1 Research Question：把大方向变成可回答问题

S1 负责把“慢病分析”这种大题目收敛成一个数据能回答的问题。NHANES 案例最终选择了 RQ1：自报无糖尿病成年人中的 HbA1c 定义未诊断糖尿病。

课堂讲法：

- 大方向不等于研究问题。
- 好问题必须有清晰人群、暴露或特征、结局、数据来源。
- 不要急着跑模型，先判断问题是否值得做、能不能做。

产物示例：`checkpoints/stage-S1-research-question.md`。

## S1b Target Journal & Comparator Corpus：先定目标期刊和文章体裁

S1b 是投稿型任务的强制门禁。研究问题确认后，不能马上进入方法定稿或大纲写作，而要先推荐 5 个目标期刊候选，让用户确定 1 个 working target journal，再查询该目标期刊中至少 5 篇相似 original research 文章。

课堂讲法：

- 不是先写完文章再找期刊，而是先知道目标期刊接受什么体裁。
- 相似文章不是泛泛参考文献，而是用来校准文章长度、摘要结构、主文表图数量和 supplement 策略。
- 如果无法访问足够全文或网页正文信息，要停下来请用户提供 PDF、HTML 或可访问链接。

S1b checkpoint 至少记录：

- 5 个候选期刊及领域匹配、文章类型、投稿风险和 author guidelines。
- 用户选定的目标期刊。
- 至少 5 篇同目标期刊、相似研究主题 / 设计 / article type 的 comparator articles。
- 每篇 comparator 的 DOI/URL、年份、研究类型、可访问性、摘要结构、正文大致字数、main tables、main figures、supplementary items 和 IMRaD 特点。
- 从 comparator corpus 推导出的目标正文词数、主文表图数量和 supplement 策略。

产物示例：`checkpoints/stage-S1b-target-journal-fit.md`。

## S2 Method Plan：把研究问题翻译成分析方案

S2 确定数据周期、纳入排除标准、变量定义、权重处理、主分析和敏感性分析。NHANES 案例里，关键点是使用 2017-2018 单周期、R survey 包、HbA1c 主定义、空腹血糖敏感性分析。

课堂讲法：

- 统计方案要先于结果出现。
- NHANES 是复杂抽样数据，不能只当普通表格跑。
- 敏感性分析要提前定义，不能看到结果后临时找说法。

产物示例：`checkpoints/stage-S2-method-plan.md`。

## S3 Evidence Execution：执行分析但先不写故事

S3 只负责按方案跑数据，输出 prevalence、Table 1、回归模型和日志。这个阶段的关键是“让数据说话”，不是马上把结果包装成论文结论。

课堂讲法：

- 输出 CSV、日志和样本流程。
- 检查样本量、病例数、权重和变量缺失。
- 任何异常都先记录，不急着美化。

产物示例：`results/S3/`。

## S3b Parsimonious Model：发现模型过重就回头修

S3b 是本案例的一个重要教学点：完整模型对单周期 NHANES 的设计自由度来说太重，所以回到 S3b 生成简化主模型。

课堂讲法：

- 工作流不是直线，有时要回到前一阶段修正。
- 简化模型不是偷懒，而是让推断更稳妥。
- 这一步体现了 harness 的质量控制价值。

产物示例：`checkpoints/stage-S3b-parsimonious-model.md`。

## S4 Interpretation：解释结果但不越界

S4 把统计结果转化为研究解释。这里要区分事实、推断和建议。NHANES 案例是横断面研究，所以不能写成因果结论或临床诊断规则。

课堂讲法：

- 关联不是因果。
- 单次 HbA1c 是流行病学定义，不是临床确诊。
- race/ethnicity 要作为社会分类谨慎解释，不能写成生物本质化。

产物示例：`checkpoints/stage-S4-interpretation.md`。

## S5 Outline：先搭 IMRaD 骨架

S5 只生成论文结构，不写完整正文。它决定 Introduction、Methods、Results、Discussion 如何承接研究问题。投稿型任务的 S5 必须引用 S1b 的目标期刊 guidelines 和 comparator corpus，不能凭经验直接给出 3,500-4,500 或 6,500-8,500 这类字数目标。

课堂讲法：

- 大纲是论文的施工图。
- 表和图的位置要在大纲阶段想清楚，但数量应由目标期刊规则、相似文章中位数和本研究数据复杂度共同决定。
- 不要把所有结果都塞进主线，补充分析可以放 Supplement。

产物示例：`checkpoints/stage-S5-outline.md`。

## S5b Literature Matrix：先建文献证据表

S5b 建立文献矩阵，明确哪些论点由哪些文献支撑。它防止 AI 用“看起来合理”的句子替代真实引用。

课堂讲法：

- 文献不是装饰，而是论点支撑。
- 未核验文献必须标注，不能直接进入投稿稿。
- 官方来源、指南和 NHANES 文档要优先核对。

产物示例：`checkpoints/stage-S5b-literature-matrix.md`。

## S6 Draft：写完整初稿

S6 才进入长文写作。此时已经有研究问题、目标期刊体裁矩阵、方法、结果、大纲和文献矩阵，所以 AI 写作是在受控材料内完成。

课堂讲法：

- 初稿不是最终稿。
- 字数、结构、语气和边界要来自 S1b + S5，而不是临时让 AI 自己决定。
- 让 AI 写之前，先给它足够干净的材料。

产物示例：`checkpoints/stage-S6-draft.md`。

## S7 Integrity Check：核查数据、引用和论断

S7 是投稿前最容易被忽略的一步。它检查正文数字是否来自本地结果，参考文献是否真实，论断是否超出证据。

课堂讲法：

- 论文最危险的不是写得慢，而是写得像真的但没核对。
- 所有关键数字都要能追到 CSV 或脚本。
- 引用不能靠模型记忆。

产物示例：`checkpoints/stage-S7-integrity-citation-check.md`。

## S7b Citation Clean：清理参考文献

S7b 把未核验引用删除、替换或降级，把参考文献整理成可投稿的 Vancouver-style 清单。

课堂讲法：

- 不确定的文献不要硬留。
- 引用清理是科研诚信的一部分。
- 引用越少但越准确，通常比堆砌更稳。

产物示例：`checkpoints/stage-S7b-final-reference-verification.md`。

## S8 Review：模拟审稿

S8 模拟编辑和审稿人，从 novelty、方法、报告完整性、解释边界等角度提出 major revision。

课堂讲法：

- 审稿模拟不是为了挑刺，而是提前发现投稿风险。
- “Major Revision” 不等于失败，它说明稿件可救但还不完整。
- 这一步帮助学员理解真实投稿逻辑。

产物示例：`checkpoints/stage-S8-review-revision.md`。

## S8b Revision：真正实施修回

S8b 根据审稿意见补表、补图、补 missingness、补设计自由度、修正空腹权重敏感性分析，并把图表放进稿件。

课堂讲法：

- 回复审稿意见不能只写“已修改”，必须有实际修改。
- 图表、样本量、权重和模型说明是医学统计论文的硬骨架。
- 这一阶段把“能看”变成“更像投稿稿”。

产物示例：`checkpoints/stage-S8b-revision-implementation.md`。

## S9 Finalize：生成投稿前包

S9 生成最终通用 SCI 稿、Word、表、图、cover letter、STROBE mapping 和 readiness checklist。

课堂讲法：

- S9 是投稿前包，不是期刊接收证明。
- 目标期刊格式、作者信息、利益冲突、基金和伦理声明仍需人工最终确认。
- 这一步适合向学员展示“文件夹级交付物”。

产物示例：`submission_package/manuscript_final_with_tables_figures.docx`。
