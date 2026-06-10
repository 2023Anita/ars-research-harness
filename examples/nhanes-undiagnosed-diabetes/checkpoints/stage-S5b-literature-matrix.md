# S5b Literature Source Matrix：SCI 初稿文献来源矩阵

## 阶段目标

为 S6 英文 SCI 初稿准备文献支撑矩阵。本阶段只做检索策略、来源筛选、证据用途规划和引用风险标注，不写正文。

用户已更新 S6 目标：

- 初稿语言：英文 SCI 初稿。
- 目标长度：6,500-8,500 英文词。
- 写作前置：先补 S5b 文献来源矩阵。

## 检索策略

### 数据库与来源

- PubMed / PMC / Diabetes Care / CDC / NCHS / ADA / NIDDK。
- 优先级：官方方法与诊断标准 > NHANES 未诊断糖尿病研究 > HbA1c/FPG 一致性研究 > 腰围/肥胖指标研究 > non-HDL-C 与糖代谢研究 > 筛查和社会差异研究。

### 核心检索式

```text
("NHANES" AND "undiagnosed diabetes" AND "HbA1c")
("NHANES" AND "undiagnosed diabetes" AND "prevalence" AND adults)
("NHANES" AND "HbA1c" AND "fasting glucose" AND mismatch)
("NHANES" AND "waist circumference" AND diabetes AND adults)
("NHANES" AND "non-HDL cholesterol" AND diabetes)
("NHANES" AND "race ethnicity" AND "undiagnosed diabetes")
```

## 来源分级

| 等级 | 含义 | 当前用途 |
|---|---|---|
| A | 官方或权威方法来源，已可直接用于方法/阈值/背景 | Methods, outcome definition, survey design |
| B | 同主题 peer-reviewed 研究，适合 Introduction/Discussion | Background, comparison, gap |
| C | 相关但非核心，适合补充讨论或备选引用 | Discussion, limitations |
| Pending | 已识别但需 S7 做 DOI/全文核验 | 暂不写成关键论据 |

## 官方与方法来源

| # | 来源 | 证据用途 | 质量 | 用于章节 |
|---:|---|---|---|---|
| A1 | CDC/NCHS. NHANES Survey Methods and Analytic Guidelines. https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx | NHANES 复杂抽样、权重、方差估计、分析指南。 | A | Methods |
| A2 | CDC/NCHS. NHANES Weighting Module. https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx | 说明 NHANES 权重用于处理复杂抽样、非应答和后分层，使样本代表美国非机构化平民人群。 | A | Methods |
| A3 | CDC/NCHS. GHB_J Glycohemoglobin documentation. https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/GHB_J.htm | 确认 `LBXGH` 为 Glycohemoglobin (%)，并说明实验室检测并非所有参与者均有。 | A | Methods |
| A4 | CDC/NCHS. 2017-2018 Laboratory Data page. https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Laboratory&Cycle=2017-2018 | 说明 GHB_J、GLU_J 等 2017-2018 实验室文件来源。 | A | Methods |
| A5 | ADA. Diabetes Diagnosis. https://diabetes.org/about-diabetes/diagnosis | A1C ≥6.5%、prediabetes 5.7%-6.4%、FPG ≥126 mg/dL 阈值。 | A | Methods, Introduction |
| A6 | NIDDK. The A1C Test & Diabetes. https://www.niddk.nih.gov/health-information/diagnostic-tests/a1c-test | A1C 阈值，并强调诊断通常需第二次检测确认。 | A | Methods, Limitations |
| A7 | CDC/NCHS Data Brief No. 516. Prevalence of Total, Diagnosed, and Undiagnosed Diabetes in Adults. https://www.cdc.gov/nchs/products/databriefs/db516.htm | 最新 NHANES 数据背景：美国成人总糖尿病、诊断糖尿病、未诊断糖尿病负担；年龄和体重状态梯度。 | A | Introduction, Discussion |
| A8 | Healthy People 2030 objective D-02. https://odphp.health.gov/healthypeople/objectives-and-data/browse-objectives/diabetes/reduce-proportion-adults-who-dont-know-they-have-prediabetes-d-02/data-methodology | 未诊断糖尿病前期作为公共卫生目标，使用 NHANES。 | A | Introduction |

## 核心研究文献候选

| # | 来源 | 主要内容 | 质量/状态 | 用于章节 | 备注 |
|---:|---|---|---|---|---|
| B1 | Menke et al. / NHANES trend study. "Identifying Trends in Undiagnosed Diabetes in U.S. Adults..." https://pmc.ncbi.nlm.nih.gov/articles/PMC5744859/ | NHANES 未诊断糖尿病趋势；涉及 HbA1c 和血糖测量。 | B / 页面遇到校验，需 S7 核验 | Introduction, Discussion | 可用于说明该主题已有趋势研究，本文需突出 2017-2018 和特征相关性。 |
| B2 | "Undiagnosed diabetes based on HbA1c by socioeconomic status..." https://pmc.ncbi.nlm.nih.gov/articles/PMC8593698/ | 以 HbA1c ≥6.5% 且无自报糖尿病定义未诊断糖尿病，并分析社会经济因素。 | B / 页面遇到校验，需 S7 核验 | Introduction, Discussion | 与本研究定义高度相关。 |
| B3 | "Undiagnosed Diabetes in U.S. Adults: Prevalence and Trends." Diabetes Care. https://diabetesjournals.org/care/article/45/9/1994/147216/Undiagnosed-Diabetes-in-U-S-Adults-Prevalence-and | 美国成人未诊断糖尿病患病率和趋势；使用确认型定义。 | B / 403，需 S7 核验 | Introduction, Discussion | 高相关，建议优先核验 DOI。 |
| B4 | "Trends in Undiagnosed Diabetes Mellitus Among United States Adults: Cross-Sectional Analyses from NHANES 2011-2020." https://pubmed.ncbi.nlm.nih.gov/35613950/ | NHANES 2011-2020 未诊断糖尿病趋势。 | B / PubMed 页面遇到校验，需 S7 核验 | Introduction | 可用于定位本文不是趋势研究，而是特征相关性研究。 |
| B5 | "Mismatched HbA1c and glucose in NHANES 2005-2016." https://pubmed.ncbi.nlm.nih.gov/35662612/ | HbA1c 与葡萄糖分类不一致问题，提示单一 HbA1c 定义有局限。 | B / PubMed 页面遇到校验，需 S7 核验 | Methods, Limitations | 支撑 HbA1c/FPG 敏感性分析。 |
| B6 | "Epidemiological Ramifications of Diagnosing Diabetes with HbA1c..." https://pmc.ncbi.nlm.nih.gov/articles/PMC4287398/ | 比较 HbA1c 与实验室血糖定义对糖尿病流行病学估计的影响。 | B / 需 S7 核验 | Methods, Discussion | 支撑不同定义会改变估计。 |
| B7 | "National patterns in diabetes screening: data from the..." https://pubmed.ncbi.nlm.nih.gov/25533392/ | 使用 HbA1c 和/或 fasting glucose 定义未诊断糖尿病，讨论筛查状态。 | B / 需 S7 核验 | Introduction, Discussion | 支撑筛查缺口叙事。 |

## 腰围、肥胖与体测指标文献候选

| # | 来源 | 主要内容 | 质量/状态 | 用于章节 | 备注 |
|---:|---|---|---|---|---|
| C1 | "Sagittal Abdominal Diameter, Waist Circumference, and BMI as ..." https://pubmed.ncbi.nlm.nih.gov/30018985/ | NHANES 成人中比较 SAD、腰围、BMI 与 HbA1c/HOMA-IR 等指标。 | B / 需 S7 核验 | Discussion | 支撑腰围作为糖代谢风险指标。 |
| C2 | "Is weight-adjusted waist index more strongly associated..." https://pubmed.ncbi.nlm.nih.gov/39325793/ | NHANES 2017-2020，WWI 与 diabetes 关联，提示腰围相关指标受到关注。 | C / 需 S7 核验 | Discussion | 可作为近期体测指标文献，不作为核心论据。 |
| C3 | "Association of body roundness index with diabetes and prediabetes..." https://pmc.ncbi.nlm.nih.gov/articles/PMC11330595/ | BRI 与 diabetes/prediabetes，反映体型指标在糖代谢研究中的趋势。 | C / 需 S7 核验 | Discussion | 可用于说明替代体测指标领域较拥挤。 |
| C4 | "Trends in obesity prevalence and cardiometabolic risk factor control..." https://pmc.ncbi.nlm.nih.gov/articles/PMC9974736/ | NHANES diagnosed diabetes 人群中肥胖和心血管代谢风险控制趋势；定义中心性肥胖阈值。 | C / 需 S7 核验 | Methods, Discussion | 可辅助腰围阈值背景，但本研究主模型用连续腰围。 |

## non-HDL-C / 血脂文献候选

| # | 来源 | 主要内容 | 质量/状态 | 用于章节 | 备注 |
|---:|---|---|---|---|---|
| D1 | "The association between non-HDL-cholesterol to HDL-cholesterol ratio..." https://pmc.ncbi.nlm.nih.gov/articles/PMC11106869/ | NHHR 与 T2DM 相关，提示 non-HDL/HDL 方向已有近年 NHANES 研究。 | B / 页面遇到校验，需 S7 核验 | Discussion | 说明血脂比值方向拥挤，本文使用 non-HDL-C 更保守。 |
| D2 | "Non-HDL cholesterol as a predictor for incident type 2 diabetes..." https://pubmed.ncbi.nlm.nih.gov/34979322/ | 非 NHANES 队列研究，non-HDL-C 与 incident T2DM。 | B / 需 S7 核验 | Discussion | 支撑 non-HDL-C 与糖代谢风险的外部一致性。 |
| D3 | "Utility of non-high-density lipoprotein cholesterol in assessing..." https://pubmed.ncbi.nlm.nih.gov/22510237/ | non-HDL-C 与 incident T2DM 风险预测相关。 | B / 需 S7 核验 | Discussion | 较早但可作为 foundational 支撑。 |
| D4 | "U-shaped relationship between the non-HDL to HDL cholesterol..." https://pmc.ncbi.nlm.nih.gov/articles/PMC12215365/ | NHANES 1999-2018，NHHR 与糖代谢相关方向。 | C / 需 S7 核验 | Discussion | 若使用 NHHR 背景可引用，但当前主暴露是 non-HDL-C。 |

## 生活方式与筛查文献候选

| # | 来源 | 主要内容 | 质量/状态 | 用于章节 | 备注 |
|---:|---|---|---|---|---|
| E1 | Healthy People 2030 D-02 | 未诊断糖尿病前期知晓率目标，强调公共卫生筛查缺口。 | A | Introduction, Discussion | 已列为 A8，可重复用于主线。 |
| E2 | ADA Diabetes Diagnosis page | Prediabetes 通常无明显症状，需检测发现；预防建议包含体重管理和运动。 | A | Introduction, Discussion | 可用于生活方式讨论，但不要夸大本研究活动结果。 |
| E3 | NCHS Data Brief No. 516 | 未诊断糖尿病随年龄和体重状态增加。 | A | Discussion | 可与本研究分层结果对照。 |

## Literature Matrix

| 主题 | 主要来源 | 支撑用途 | 当前证据强度 |
|---|---|---|---|
| NHANES 方法与权重 | A1, A2, A3, A4 | Methods 的 survey design、权重、实验室数据来源 | 强 |
| 诊断阈值 | A5, A6 | Outcome definition, sensitivity analysis | 强 |
| 未诊断糖尿病公共卫生负担 | A7, B1, B3, B4 | Introduction 背景和 Discussion 对照 | 强，但 B 类需 S7 核验 |
| HbA1c/FPG 定义差异 | A5, A6, B5, B6 | Methods 和 Limitations | 中强，B 类需核验 |
| 自报无糖尿病与筛查缺口 | B2, B7, A8 | Research gap 和 Discussion | 中强 |
| 腰围/腹型肥胖 | C1, C2, C3, C4 | Discussion 解释 waist circumference 结果 | 中 |
| non-HDL-C / 血脂风险 | D1, D2, D3, D4 | Discussion 解释 non-HDL-C 结果 | 中 |
| 种族/族裔差异 | A7 + 后续需补专门文献 | Discussion 边界与社会决定因素 | 当前不足，S6 前建议补 2-3 篇专门文献 |
| 生活方式 | A5, E2 + 后续需补专门文献 | Discussion 中谨慎解释 activity 方向性 | 当前不足，不适合作为强论点 |

## 章节引用规划

### Introduction

必须引用：

- A7：美国成人糖尿病和未诊断糖尿病负担。
- A5/A6：A1C 和 FPG 诊断阈值。
- A8：未诊断糖尿病前期或筛查缺口公共卫生目标。
- B1/B3/B4：NHANES 未诊断糖尿病既有研究，S7 核验后使用。

### Methods

必须引用：

- A1/A2：NHANES analytic guidelines / weighting。
- A3/A4：GHB_J、GLU_J 数据来源。
- A5/A6：HbA1c 和 FPG 阈值。

### Results

通常不需要外部文献，只引用本研究表图。

### Discussion

建议引用：

- A7：与最新 NCHS 数据简要对照。
- B5/B6：解释 HbA1c/FPG 敏感性分析。
- C1/C2/C3：解释腰围和体测指标。
- D1/D2/D3：解释 non-HDL-C。
- 种族/族裔社会决定因素文献：当前矩阵不足，建议 S5c 或 S7 前补充。

## 缺口与补充检索建议

进入 S6 前，建议再补 2 个小检索，不必阻塞大纲，但会提高 Discussion 质量：

1. **Race/ethnicity and undiagnosed diabetes / diabetes screening disparities**
   - 目的：避免种族/族裔结果解释过薄或本质化。
   - 推荐检索式：`("undiagnosed diabetes" OR "diabetes screening") AND race ethnicity AND NHANES`

2. **Physical activity and undiagnosed diabetes / prediabetes in NHANES**
   - 目的：当前活动结果 CI 跨 1，只能谨慎写；需要文献支持“方向性但非核心”。
   - 推荐检索式：`NHANES physical activity prediabetes diabetes adults`

## S5b 结论

当前来源矩阵足以支持 S6 写作的 Methods、Outcome definition 和主要背景，但 Introduction/Discussion 若按 6,500-8,500 英文词展开，建议在 S6 写作时继续补少量定向文献，尤其是种族/族裔筛查差异和生活方式部分。

进入 S6 前建议用户确认：

1. 是否接受 6,500-8,500 英文词目标。
2. 是否接受先写英文 SCI 初稿。
3. 是否允许 S6 写作过程中补充少量定向文献，但不改变研究问题和主结果。
4. 是否将未核验 B/C 文献标记为待 S7 citation check，而不在 S6 中作为关键论据过度使用。
