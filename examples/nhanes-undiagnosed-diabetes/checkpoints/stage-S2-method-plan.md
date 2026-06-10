# S2 Method / Analysis Plan：RQ1 未诊断糖尿病

## 阶段目标

为已确认的 SCI 主线制定可执行分析方案。本阶段只制定方法，不运行数据分析。

## 已确认研究问题

**Primary RQ:**  
Among U.S. adults without self-reported diabetes, what demographic, anthropometric, cardiometabolic, and lifestyle factors are associated with HbA1c-defined undiagnosed diabetes in NHANES 2017-2018?

**中文：**  
在自报未患糖尿病的美国成年人中，哪些人口学、体测、心血管代谢和生活方式因素与 HbA1c 定义的未诊断糖尿病相关？

## 研究设计

- 研究类型：复杂抽样横断面研究。
- 数据来源：NHANES 2017-2018 public-use data。
- 研究对象：20 岁及以上美国成年人。
- 分析目标：估计未诊断糖尿病的加权患病比例，并识别与未诊断糖尿病相关的可解释特征。

## 人群筛选

### 纳入标准

1. `RIDAGEYR >= 20`。
2. 有糖尿病问卷 `DIQ010`。
3. 自报未被医务人员告知患糖尿病：`DIQ010 == 2`。
4. 有 HbA1c 检测值：`LBXGH` 非缺失。

### 排除标准

1. 自报已诊断糖尿病：`DIQ010 == 1`。
2. `DIQ010` 为拒答、不知道或边界编码。
3. HbA1c 缺失。
4. 妊娠状态可考虑排除，但当前 raw 未纳入妊娠变量细化；S3 可检查 `RIDEXPRG` 是否可用并决定。

## 结局定义

### 主结局

**HbA1c-defined undiagnosed diabetes**

在自报未患糖尿病者中：

- `LBXGH >= 6.5%`：未诊断糖尿病。
- `LBXGH < 6.5%`：未达到糖尿病范围。

说明：该定义用于流行病学筛查研究，不等同于临床确诊。

### 次要结局，可选

**HbA1c-defined prediabetes**

- `5.7% <= LBXGH < 6.5%`：糖尿病前期范围。

建议作为补充分析，不作为主结局，避免论文主线变散。

## 暴露与协变量

### 人口学变量

- 年龄：`RIDAGEYR`，连续变量；可按 20-39、40-59、≥60 分层。
- 性别：`RIAGENDR`。
- 种族/族裔：`RIDRETH3`。
- 家庭收入贫困比：`INDFMPIR`，连续或分层。

### 体测变量

- BMI：`BMXBMI`。
- 肥胖：BMI ≥ 30。
- 腰围：`BMXWAIST`。
- 腹型肥胖：按性别阈值定义；建议 S3 查官方或常用阈值。

### 血压变量

- 平均收缩压：`BPXSY1-4` 非缺失均值。
- 平均舒张压：`BPXDI1-4` 非缺失均值。
- 测量性高血压：可用 ≥130/80 mmHg 定义，需在方法中说明为筛查阈值。

### 血脂变量

- 总胆固醇：`LBXTC`。
- HDL-C：`LBDHDD`。
- non-HDL-C：`LBXTC - LBDHDD`。
- non-HDL/HDL ratio：可作为探索性指标，但不建议抢主线。

### 生活方式变量

- 当前吸烟：基于 `SMQ020` 和 `SMQ040`。
- 睡眠时长：`SLD012`。
- 短睡眠：<7 小时。
- 体力活动：基于 `PAQ605`、`PAQ620`、`PAQ635`、`PAQ650`、`PAQ665`，可定义是否报告任一中高强度或通勤/休闲活动。

## 统计分析方案

### 1. 数据准备

1. 使用 `SEQN` 合并 12 个数据表。
2. 限定成人样本。
3. 限定自报未患糖尿病且 HbA1c 可用样本。
4. 构建主结局和协变量。
5. 记录每一步样本量，形成 Figure 1 flowchart。

### 2. 复杂抽样处理

SCI 稿件必须优先使用 NHANES survey design：

- 权重：以 MEC 权重 `WTMEC2YR` 为主，因为 HbA1c 属于 MEC/实验室相关检测。
- 分层：`SDMVSTRA`。
- PSU：`SDMVPSU`。

若后续使用 Python 无法可靠实现复杂抽样标准误，建议 S3 使用 R 的 `survey` 包进行主分析；Python 可作为数据整理辅助。

### 3. 描述性分析

输出 Table 1：

- 按未诊断糖尿病状态分组。
- 报告加权均值或加权比例。
- 变量包括年龄、性别、种族/族裔、PIR、BMI、腰围、血压、血脂、吸烟、睡眠、体力活动。

输出核心患病估计：

- 自报未患糖尿病成人中的 HbA1c-defined undiagnosed diabetes 加权比例。
- 可按性别、年龄、种族/族裔、肥胖状态分层。

### 4. 主模型

加权 logistic regression：

**Outcome:** HbA1c-defined undiagnosed diabetes。

**Model 1:**  
年龄、性别、种族/族裔。

**Model 2:**  
Model 1 + PIR、BMI、腰围。

**Model 3:**  
Model 2 + 平均收缩压、HDL-C、non-HDL-C、吸烟、睡眠、体力活动。

报告：

- OR。
- 95% CI。
- P 值。
- 加权样本量和未加权样本量。

### 5. 敏感性分析

建议至少做 3 个：

1. 将结局改为 HbA1c ≥6.5% 或空腹血糖 ≥126 mg/dL 的组合定义；当前 GLU 样本较小，应作为敏感性分析。
2. 排除妊娠者，如 `RIDEXPRG` 可用且适用。
3. 使用 BMI 分类替代连续 BMI。
4. 使用 waist circumference 替代 BMI 或同时检查多重共线性。

### 6. 亚组分析

建议做，但不要过多：

- 年龄：20-39、40-59、≥60。
- 性别。
- 肥胖状态。

重点看 BMI/腰围和生活方式因素在不同亚组中的方向是否一致。若样本量不足，不做过度解释。

### 7. 图表计划

**Figure 1:** 样本筛选流程图。  
**Figure 2:** 未诊断糖尿病加权患病比例，按年龄/性别/种族或肥胖状态分层。  
**Figure 3 可选:** adjusted OR forest plot。  

**Table 1:** 分组基线特征。  
**Table 2:** 多模型加权 logistic 回归结果。  
**Supplementary Table 1:** 变量定义。  
**Supplementary Table 2:** 敏感性分析结果。  

## SCI 写作策略

### 推荐标题

**英文暂定：**  
Cardiometabolic and lifestyle correlates of HbA1c-defined undiagnosed diabetes among self-reported non-diabetic U.S. adults: a cross-sectional analysis of NHANES 2017-2018

### 核心卖点

1. 聚焦未诊断糖尿病，而不是普通糖尿病风险因素。
2. 使用公开、代表性调查数据。
3. 将体测、血压、血脂和生活方式因素整合到筛查缺口框架。
4. 强调结果用于公共卫生筛查和风险分层，不用于临床诊断。

### 主要限制

1. 横断面设计不能推断因果。
2. 自报未诊断糖尿病可能受医疗可及性、回忆和知晓率影响。
3. HbA1c 单次测量不能替代临床确诊。
4. 单周期数据样本量有限，部分亚组不稳定。
5. 若只使用当前 raw 数据，不含药物、饮食、胰岛素、甘油三酯和死亡随访。

## S3 执行前检查清单

进入 S3 前建议确认：

1. 是否接受只用当前 2017-2018 单周期数据？
2. 是否允许用 R `survey` 包做主分析？这会更符合 SCI 审稿预期。
3. 是否将空腹血糖作为敏感性分析，而非主结局？
4. 是否排除妊娠者？
5. 是否将 prediabetes 放在补充分析，而不是主线？

## 本阶段结论

该方案可以进入 S3 数据执行。若目标是 SCI，建议主分析使用 R `survey` 包处理 NHANES 权重、分层和 PSU；Python 可用于数据整理和辅助检查。当前数据可以完成一篇横断面 SCI 初稿，但投稿竞争力属于“稳妥中等”，不是高创新方向。
