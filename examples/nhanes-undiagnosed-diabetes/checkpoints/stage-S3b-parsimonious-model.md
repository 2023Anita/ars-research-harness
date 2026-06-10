# S3b Parsimonious Model Revision：简化主模型与最终 Table 2

## 阶段目标

根据 S4 的方法风险判断，回到数据执行阶段生成更适合单周期 NHANES 复杂抽样设计的简化主模型。本阶段只生成最终 Table 2 和敏感性模型，不写大纲或正文。

## 执行文件

- 脚本：`artifacts/s3b_parsimonious_model.R`
- 输出目录：`results/S3b/`

## 输出文件

| 文件 | 用途 |
|---|---|
| `table2_final_main_waist_model.csv` | 推荐作为正文 Table 2 的主模型 |
| `table2_sensitivity_categorical_screening_model.csv` | 分类筛查模型，建议作为补充表 |
| `table2_sensitivity_bmi_model.csv` | BMI 替代模型，建议作为补充表 |
| `s3b_all_parsimonious_models.csv` | 三个模型合并结果 |
| `s3b_model_summary.csv` | 设计自由度与模型样本量 |
| `s3b_analysis_log.txt` | 执行日志 |

## 设计自由度与样本量

| 指标 | 数值 |
|---|---:|
| Survey design degrees of freedom | 15 |
| 主腰围模型样本量 | 3,621 |
| 分类筛查模型样本量 | 3,707 |
| BMI 替代模型样本量 | 3,707 |

## 推荐正文 Table 2：主腰围模型

主模型变量：

- 年龄。
- 性别。
- 种族/族裔。
- 腰围。
- 平均收缩压。
- non-HDL-C。
- 任一体力活动。

| 变量 | OR | 95% CI |
|---|---:|---:|
| Age, per year | 1.025 | 0.983-1.068 |
| Female vs male | 1.861 | 0.728-4.756 |
| Mexican American vs Non-Hispanic White | 3.072 | 0.608-15.538 |
| Non-Hispanic Asian vs Non-Hispanic White | 5.986 | 1.859-19.276 |
| Non-Hispanic Black vs Non-Hispanic White | 4.099 | 1.334-12.600 |
| Other Hispanic vs Non-Hispanic White | 3.737 | 0.665-20.989 |
| Other/Multiracial vs Non-Hispanic White | 1.774 | 0.390-8.077 |
| Waist circumference, per cm | 1.051 | 1.030-1.073 |
| Mean systolic BP, per mmHg | 1.012 | 0.985-1.040 |
| Non-HDL cholesterol, per mg/dL | 1.016 | 1.008-1.023 |
| Any reported physical activity vs none | 0.478 | 0.211-1.078 |

## 敏感性模型要点

### 分类筛查模型

- 肥胖 vs 非肥胖：OR 5.064，95% CI 2.574-9.963。
- 测量性高血压：OR 1.394，95% CI 0.599-3.245。
- non-HDL-C：OR 1.015，95% CI 1.008-1.022。
- 任一体力活动：OR 0.475，95% CI 0.208-1.085。

### BMI 替代模型

- BMI 每 1 kg/m2：OR 1.106，95% CI 1.064-1.150。
- non-HDL-C：OR 1.016，95% CI 1.008-1.024。
- 任一体力活动：OR 0.456，95% CI 0.200-1.037。

## 推荐写作策略

正文 Table 2 使用主腰围模型，理由：

1. 腰围比 BMI 更贴近腹型肥胖和糖代谢风险。
2. 模型变量更少，避免完整 Model 3 的参数过载。
3. 结果有清晰可解释性：腰围、non-HDL-C、部分种族/族裔差异。

补充材料：

- BMI 替代模型作为 robustness check。
- 分类筛查模型用于临床/公共卫生可解释性补充。

## 解释边界

可以写：

- 腰围和 non-HDL-C 与 HbA1c-defined undiagnosed diabetes 的更高 odds 相关。
- Non-Hispanic Asian 和 Non-Hispanic Black 参与者相较 Non-Hispanic White 参与者有更高 odds，但解释必须聚焦筛查差异、社会决定因素和代谢风险分布，避免本质化叙事。
- 任一体力活动呈较低 odds 方向，但 95% CI 跨 1，应作为方向性发现谨慎描述。

不建议写：

- “体力活动显著降低未诊断糖尿病风险。”
- “种族导致未诊断糖尿病。”
- “腰围/non-HDL-C 可诊断糖尿病。”

## S3b 结论

S3b 已解决 S4 指出的主要模型风险。当前结果可以进入 S5 文章大纲阶段。

推荐下一阶段：

- S5 Outline：基于 S3 + S3b 结果设计 SCI 论文 IMRaD 大纲。
