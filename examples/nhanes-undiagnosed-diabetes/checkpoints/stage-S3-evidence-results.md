# S3 Evidence / Data Execution：NHANES 未诊断糖尿病主分析

## 阶段目标

执行 S2 已确认的数据分析方案，生成可复现结果文件。本阶段只报告执行结果和数据证据，不做论文讨论或最终解释。

## 执行环境

- R：4.5.1
- 主分析包：`survey` 4.5
- `survey` 安装位置：项目本地 `r-lib/`
- 分析脚本：`artifacts/s3_nhanes_undiagnosed_diabetes_analysis.R`
- 结果目录：`results/S3/`

## 生成文件

| 文件 | 内容 |
|---|---|
| `analytic_all.csv` | 合并后的全体数据 |
| `analysis_sample.csv` | 主分析样本 |
| `flow_counts.csv` | 样本筛选流程 |
| `weighted_prevalence_overall.csv` | 未诊断糖尿病和糖尿病前期加权比例 |
| `weighted_prevalence_subgroups.csv` | 分层加权比例 |
| `table1_weighted_by_outcome.csv` | 按未诊断糖尿病状态分组的加权特征 |
| `weighted_logistic_models.csv` | 加权 logistic 回归 OR 表 |
| `sensitivity_fpg_or_a1c_prevalence.csv` | HbA1c 或空腹血糖组合定义敏感性分析 |
| `analysis_summary.csv` | 核心结果摘要 |
| `analysis_log.txt` | 执行日志 |

## 样本流程

| 步骤 | n |
|---|---:|
| NHANES 2017-2018 interview participants | 9,254 |
| Adults aged >=20 years | 5,569 |
| Adults with diabetes questionnaire | 5,569 |
| Self-reported no diabetes | 4,517 |
| Self-reported no diabetes and HbA1c available | 4,051 |
| After excluding pregnant participants | 4,004 |

## 主结局加权比例

| 结局 | 未加权 n | 病例 n | 加权比例 | 95% CI |
|---|---:|---:|---:|---:|
| HbA1c-defined undiagnosed diabetes | 4,004 | 150 | 2.17% | 1.74%-2.70% |
| HbA1c-defined prediabetes | 4,004 | 1,254 | 24.76% | 22.63%-27.02% |

## 敏感性分析

使用 HbA1c >= 6.5% 或空腹血糖 >=126 mg/dL 的组合定义：

| 结局 | 未加权 n | 病例 n | 加权比例 | 95% CI |
|---|---:|---:|---:|---:|
| HbA1c or fasting glucose-defined undiagnosed diabetes | 4,004 | 211 | 3.26% | 2.66%-3.98% |

## 分层加权比例

| 分层变量 | 分组 | 未诊断糖尿病加权比例 | 95% CI |
|---|---|---:|---:|
| Sex | Male | 1.59% | 0.94%-2.24% |
| Sex | Female | 2.69% | 1.86%-3.53% |
| Age group | 20-39 | 0.97% | 0.40%-1.53% |
| Age group | 40-59 | 2.92% | 1.92%-3.91% |
| Age group | 60+ | 3.02% | 1.98%-4.07% |
| Race/ethnicity | Non-Hispanic White | 1.35% | 0.65%-2.05% |
| Race/ethnicity | Mexican American | 2.85% | 1.32%-4.39% |
| Race/ethnicity | Non-Hispanic Asian | 4.22% | 2.51%-5.94% |
| Race/ethnicity | Non-Hispanic Black | 4.75% | 3.33%-6.17% |
| Obesity | No | 0.85% | 0.54%-1.16% |
| Obesity | Yes | 4.08% | 3.16%-5.00% |

## Table 1 关键执行结果

按加权均值/比例观察，未诊断糖尿病组与非未诊断组在以下变量上有明显差异，后续 S4 再解释：

| 变量 | 非未诊断糖尿病 | 未诊断糖尿病 |
|---|---:|---:|
| 年龄，岁 | 46.51 | 54.71 |
| 肥胖，% | 38.80% | 75.81% |
| BMI，kg/m2 | 29.16 | 35.07 |
| 腰围，cm | 98.94 | 112.89 |
| 平均收缩压，mmHg | 122.39 | 135.90 |
| HbA1c，% | 5.42 | 7.50 |
| 总胆固醇，mg/dL | 190.32 | 211.39 |
| HDL-C，mg/dL | 54.75 | 46.53 |
| non-HDL-C，mg/dL | 135.56 | 164.85 |
| 当前吸烟，% | 18.23% | 14.75% |
| 短睡眠，% | 24.80% | 30.24% |
| 任一体力活动，% | 81.00% | 56.10% |

## 加权 logistic 回归执行结果

结果文件：`weighted_logistic_models.csv`

已成功生成三组模型：

1. Model 1：人口学变量。
2. Model 2：人口学 + 社会经济 + 体测变量。
3. Model 3：完整模型。

### 技术注意

单周期 NHANES 2017-2018 的设计自由度有限。Model 3 纳入参数较多，`survey` 对部分 P 值返回 `NA`。OR 和 95% CI 已生成，但 S4 解释阶段必须处理这一点：

- 方案 A：保留 Model 3，但主要报告 OR 和 95% CI，不强调 P 值。
- 方案 B：将主模型收窄为更少参数的 parsimonious model。
- 方案 C：补充更多 NHANES 周期，提高样本量和设计自由度。

## S3 执行结论

主分析已经完成，结果支持进入 S4 Interpretation。但 S4 需要重点处理两个方法风险：

1. 单周期数据和复杂抽样设计自由度有限。
2. 完整模型参数偏多，SCI 稿件可能需要更简洁的主模型或补充周期。

本阶段不做最终学术解释，不写讨论。
