# NHANES 未诊断糖尿病案例

这是 `ars-research-harness` 的完整示例：使用 NHANES 2017-2018 public-use 小包数据，完成一篇关于 HbA1c 定义未诊断糖尿病的 SCI 投稿前包。

## 研究问题

在自报无糖尿病的美国成年人中，HbA1c 定义的未诊断糖尿病患病率是多少？它与人口学、体测、心代谢和生活方式因素有什么关联？

## 阶段路径

- S0：确认目标是 SCI 论文。
- S1：从泛泛慢病分析收敛到未诊断糖尿病。
- S1b：确定目标期刊，并用同刊相似 original research 校准字数和表图策略。
- S2：确定 NHANES survey 设计、权重、变量和敏感性分析。
- S3/S3b：执行主分析并简化模型。
- S4：解释结果边界。
- S5/S5b：生成 IMRaD 大纲和文献矩阵。
- S6：生成英文 SCI 初稿。
- S7/S7b：核查数据、引用和参考文献。
- S8/S8b：模拟审稿并实施修回。
- S9：生成投稿前包。

## 主要产物

- `workflow-run.json`：完整状态记录。
- `checkpoints/`：每阶段 checkpoint。
- `results/`：分析表、图、敏感性分析。
- `submission_package/`：最终 Word、表、图、cover letter、STROBE mapping。

## 重要边界

这是教学与复刻样例，不表示论文已经被 SCI 接收。所有结论应理解为基于 NHANES 单周期横断面数据的关联性结果。
