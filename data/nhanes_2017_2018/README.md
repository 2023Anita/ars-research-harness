# NHANES 2017-2018 Public-Use Small Pack

本目录保存 `ars-research-harness` 示例使用的 NHANES 2017-2018 public-use 小包数据。数据来源为 CDC / NCHS National Health and Nutrition Examination Survey (NHANES) public-use files。

官方入口：

- NHANES data portal: https://wwwn.cdc.gov/nchs/nhanes/
- Demographics: https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Demographics&Cycle=2017-2018
- Examination: https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Examination&Cycle=2017-2018
- Laboratory: https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Laboratory&Cycle=2017-2018
- Questionnaire: https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Questionnaire&Cycle=2017-2018
- Analytic guidelines: https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx
- Suggested citation: https://wwwn.cdc.gov/nchs/nhanes/NhanesCitation.aspx

## 使用边界

- 这些文件是 NHANES public-use 数据，不是本项目原创数据。
- 本项目保留小包数据是为了教学和可复刻演示。
- 使用者应阅读并遵守 CDC/NCHS 的原始说明、分析指南和引用规范。
- 正式流行病学分析必须处理 NHANES 复杂抽样设计，包括权重、分层和 PSU。

## 文件清单

| 文件 | 模块 | 行数 | 主要用途 |
|---|---:|---:|---|
| `raw/DEMO_J.xpt` | Demographics | 9254 | 年龄、性别、种族、收入、抽样权重 |
| `raw/BMX_J.xpt` | Examination | 8704 | 身高、体重、BMI、腰围 |
| `raw/BPX_J.xpt` | Examination | 8704 | 血压、脉搏、多次测量 |
| `raw/DIQ_J.xpt` | Questionnaire | 8897 | 糖尿病史、用药、诊断问卷 |
| `raw/GHB_J.xpt` | Laboratory | 6401 | 糖化血红蛋白 HbA1c |
| `raw/GLU_J.xpt` | Laboratory | 3036 | 空腹血糖 |
| `raw/BPQ_J.xpt` | Questionnaire | 6161 | 高血压、高胆固醇认知与用药 |
| `raw/TCHOL_J.xpt` | Laboratory | 7435 | 总胆固醇 |
| `raw/HDL_J.xpt` | Laboratory | 7435 | HDL 胆固醇 |
| `raw/PAQ_J.xpt` | Questionnaire | 5856 | 体力活动 |
| `raw/SMQ_J.xpt` | Questionnaire | 6724 | 吸烟 |
| `raw/SLQ_J.xpt` | Questionnaire | 6161 | 睡眠 |

## 建议演示任务

1. 糖尿病风险预测：以 `DIQ010` 或 HbA1c 派生标签为目标，使用年龄、性别、BMI、血糖、活动、吸烟等变量。
2. 高血压风险分析：使用血压测量均值、BMI、年龄、性别、吸烟、活动变量。
3. 缺失值处理：实验室数据行数少于人口学数据，合并后天然适合演示缺失机制。
4. 可解释 AI：用特征重要性或 SHAP 展示年龄、BMI、HbA1c、血压等变量贡献。

## 读取示例

```python
from pathlib import Path
import pandas as pd

raw = Path("data/nhanes_2017_2018/raw")
demo = pd.read_sas(raw / "DEMO_J.xpt", format="xport", encoding="utf-8")
bmx = pd.read_sas(raw / "BMX_J.xpt", format="xport", encoding="utf-8")
ghb = pd.read_sas(raw / "GHB_J.xpt", format="xport", encoding="utf-8")

df = demo.merge(bmx, on="SEQN", how="left").merge(ghb, on="SEQN", how="left")
print(df.shape)
print(df[["SEQN", "RIDAGEYR", "RIAGENDR", "BMXBMI", "LBXGH"]].head())
```

## 注意事项

- `SEQN` 是跨表合并主键。
- NHANES 是复杂抽样调查，正式流行病学估计应使用抽样权重、分层和 PSU；AI 培训入门演示可以先做普通建模，再单独讲权重问题。
- 不同模块样本数不同，尤其空腹血糖等实验室项目通常只覆盖子样本。

## Suggested Citation

When using these files, cite CDC/NCHS NHANES according to the current CDC suggested citation page:

Centers for Disease Control and Prevention (CDC). National Center for Health Statistics (NCHS). National Health and Nutrition Examination Survey Data. Hyattsville, MD: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention.
