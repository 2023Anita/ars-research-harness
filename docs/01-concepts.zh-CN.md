# 01. 核心概念：Skill、Workflow 与 Harness

## Skill

Skill 是一组能力说明和提示词路由。它告诉 AI：遇到某类任务时应该读哪些规则、用哪些工具、遵守哪些边界。

## Workflow

Workflow 是有阶段顺序的工作过程。研究论文不是一个动作，而是一串动作：提出问题、确认方法、执行分析、解释结果、写作、核查、修回和定稿。

## Harness

Harness 是把 workflow 变成可控工程系统的一层约束。它不仅告诉 AI “怎么做”，还规定：

- 当前只能做哪个阶段。
- 阶段产物保存在哪里。
- 状态如何记录。
- 什么时候必须停下来。
- 如何验证是否越级执行。

因此，本项目不是单纯的论文提示词，而是一个 research-to-paper workflow harness。
