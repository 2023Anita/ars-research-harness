# S4 Interpretation：结果解释与 SCI 可写性判断

## 阶段目标

解释 S3 已生成的结果，判断哪些结论可以进入 SCI 论文，哪些需要谨慎处理，以及是否需要回到数据执行阶段做补充分析。本阶段不写正文，不生成论文大纲。

## 1. 主结果是否支持论文主线

S3 结果支持当前 RQ1 主线：

> 在自报未患糖尿病的美国成年人中，HbA1c 定义的未诊断糖尿病仍存在可测量的公共卫生负担，并呈现明显的人口学、体测、心血管代谢和生活方式差异。

核心证据：

- 主分析样本 4,004 人。
- HbA1c-defined undiagnosed diabetes 未加权病例 150 人。
- 加权比例 2.17%，95% CI 1.74%-2.70%。
- 使用 HbA1c 或空腹血糖组合定义时，加权比例升至 3.26%，95% CI 2.66%-3.98%。

可写入 Results：

- “Among self-reported non-diabetic U.S. adults, the weighted prevalence of HbA1c-defined undiagnosed diabetes was 2.17%.”
- “When fasting plasma glucose was additionally considered, the estimated prevalence increased to 3.26%.”

不能写成：

- “2.17% 的美国成年人患有未诊断糖尿病。”  
  原因：分母是自报未患糖尿病且 HbA1c 可用的成人，不是全体美国成年人。

## 2. 分层结果的解释价值

分层结果有较强可写性：

| 分层 | 关键模式 |
|---|---|
| 性别 | 女性 2.69%，男性 1.59%。 |
| 年龄 | 40 岁以上明显高于 20-39 岁。 |
| 种族/族裔 | Non-Hispanic Black 与 Non-Hispanic Asian 组较高。 |
| 肥胖 | 肥胖者 4.08%，非肥胖者 0.85%。 |

这些结果适合支撑论文中的“screening gap is unevenly distributed”这一论点。

写作边界：

- 可以说 “higher weighted prevalence was observed in...”
- 不应说 “sex/race/obesity caused undiagnosed diabetes”
- 种族/族裔结果必须谨慎，讨论结构性健康差异、筛查机会和社会决定因素，不写成生物本质差异。

## 3. Table 1 结果的解释价值

未诊断糖尿病组相比非未诊断组：

- 年龄更高：54.71 vs 46.51 岁。
- 肥胖比例更高：75.81% vs 38.80%。
- BMI 更高：35.07 vs 29.16 kg/m2。
- 腰围更高：112.89 vs 98.94 cm。
- 平均收缩压更高：135.90 vs 122.39 mmHg。
- 总胆固醇和 non-HDL-C 更高。
- HDL-C 更低。
- 报告任一体力活动比例更低：56.10% vs 81.00%。

这些结果形成了很清楚的“cardiometabolic and lifestyle profile”。

可写入 Results：

- “Participants with HbA1c-defined undiagnosed diabetes had higher weighted mean BMI, waist circumference, systolic blood pressure, total cholesterol and non-HDL cholesterol, and lower HDL cholesterol.”
- “They were also less likely to report any physical activity.”

解释限制：

- 当前是横断面，无法判断这些因素发生在未诊断糖尿病之前还是之后。
- 当前吸烟比例未呈现明显升高，不应强行解释。
- 短睡眠比例方向上较高，但标准误较大，不能作为核心发现。

## 4. 回归模型的 SCI 风险

当前加权 logistic 模型能生成 OR 和 95% CI，但存在一个重要问题：

- Model 3 参数较多。
- 单周期 NHANES 复杂抽样设计自由度有限。
- `survey` 对 Model 3 多个 P 值返回 `NA`。

这不是数据“错了”，而是当前模型与单周期设计自由度不匹配。SCI 审稿人可能会问：

1. 为什么单周期样本要放这么多分类变量和连续变量？
2. 模型是否过拟合或估计不稳定？
3. 为什么部分 P 值无法估计？
4. 是否应该使用更简洁模型，或合并多个 NHANES 周期？

## 5. 推荐的模型修正

进入 S5 之前，建议不要直接用当前 Model 3 作为最终主模型。

推荐做一个 S3b 补充分析，生成更简洁的主模型：

### Parsimonious Model A：最推荐

Outcome:
- HbA1c-defined undiagnosed diabetes。

Predictors:
- 年龄。
- 性别。
- 种族/族裔。
- BMI 或腰围二选一。
- 平均收缩压。
- non-HDL-C 或 HDL-C 二选一。
- 任一体力活动。

理由：
- 保留临床和公共卫生重点。
- 避免 BMI 与腰围、non-HDL 与 HDL 同时进入导致参数和共线性压力。
- 更适合单周期 NHANES。

### Parsimonious Model B：筛查框架

Predictors:
- 年龄组。
- 性别。
- 种族/族裔。
- 肥胖。
- 测量性高血压。
- non-HDL-C 高水平。
- 任一体力活动。

理由：
- 更适合“screening-oriented”论文叙事。
- OR 容易解释。
- 但连续变量信息损失较多。

### 不推荐

- 继续扩展机器学习模型。
- 增加更多行为变量。
- 在当前单周期数据上做复杂交互和中介分析。

## 6. 当前结果是否足够进入 SCI 初稿

判断：**可以进入 SCI 初稿，但建议先做 S3b 简化模型。**

理由：

- 研究问题清楚。
- 主结局有足够病例数，但不算很大。
- 加权患病率结果清楚。
- 分层和 Table 1 有可写性。
- 当前回归模型存在可修复的方法风险。

如果不做 S3b，论文在审稿时最容易被攻击的是“主模型不稳”。如果做 S3b，论文会更像一篇规范的 NHANES 横断面分析。

## 7. 可进入论文 Results 的结果

建议优先写：

1. 样本筛选流程。
2. 未诊断糖尿病和糖尿病前期加权比例。
3. HbA1c + 空腹血糖敏感性分析。
4. 分层患病率：年龄、性别、种族/族裔、肥胖。
5. Table 1 中体测、血压、血脂、活动差异。
6. 简化模型的 OR 结果，待 S3b 生成。

## 8. 不建议作为主结论的内容

1. 当前完整 Model 3 的所有变量。
2. 当前吸烟和短睡眠结果。
3. “生活方式导致未诊断糖尿病”。
4. “AI 模型可用于筛查”。
5. “NHANES 结果代表所有美国成年人中的真实未诊断糖尿病比例”，除非分母和权重解释非常精确。

## 9. S4 结论

当前结果支持 SCI 论文方向，但建议在进入 S5 大纲前先执行一个 **S3b parsimonious model**。这不是推翻 S3，而是让主模型更符合单周期 NHANES 的设计自由度和 SCI 审稿预期。

推荐下一步：

- 回到 S3b：生成简化主模型和最终可写 Table 2。

备选下一步：

- 若用户希望先看文章结构，也可进入 S5，但需要在大纲中标注 Table 2 尚需重跑。
