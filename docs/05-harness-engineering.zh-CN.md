# 05. 为什么这是 Harness 工程

这个项目的核心不是“AI 会写论文”，而是“AI 被约束在一个可验证的工程流程里”。

## 关键部件

- Router：根据任务进入 deep research、paper、review、pipeline 等路径。
- Stage contract：S0-S9 定义每个阶段的输入、输出和边界。
- Checkpoint gate：阶段结束必须停下来，等待人确认。
- State artifact：`workflow-run.json` 记录当前阶段、确认状态和产物。
- Validator：检查阶段数量、状态、越级执行和完成度。
- Artifact registry：每个阶段留下可审计文件。
- Human-in-the-loop：用户确认是执行边界，不是礼貌询问。

## 失败模式

如果 AI 一次性完成选题、分析、写作和定稿，说明 workflow gate 不够硬。正确做法是把下一阶段入口写成状态机约束，并用 validator 检查。

## 工程收益

- 可复现：同样数据和脚本可以重新生成结果。
- 可审计：每个阶段都有文件证据。
- 可教学：学员能看到完整研究路径。
- 可迁移：换数据集后仍能复用 S0-S9 框架。
- 可扩展：以后可以加 CLI、dashboard、CI 校验和更多模板。
