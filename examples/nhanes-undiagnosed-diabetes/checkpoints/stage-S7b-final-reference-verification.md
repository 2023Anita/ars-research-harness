# S7b Final Reference Verification and Citation Replacement

## Stage Purpose

S7b is a substage of S7. Its purpose is to remove S6 working-reference placeholders, replace them with verified source metadata, add in-text citation numbers, and downgrade or remove claims that were not supported by verified sources.

This stage does not perform reviewer simulation, journal selection, table formatting, or final submission formatting.

## Deliverables

| Artifact | Path |
|---|---|
| Citation-clean manuscript draft | `checkpoints/stage-S7b-citation-clean-draft.md` |
| S7b checkpoint report | `checkpoints/stage-S7b-final-reference-verification.md` |

## Actions Completed

1. Created a new citation-clean draft without overwriting the original S6 draft.
2. Replaced the "Working References for S7 Verification" section with a 17-item Vancouver-style reference list.
3. Added numbered in-text citations for the main background, methods, diagnostic-threshold, NHANES design, HbA1c/FPG mismatch, waist circumference, non-HDL cholesterol, and screening-gap claims.
4. Removed or avoided unverified placeholder citations from S6 references 9-14.
5. Downgraded wording where source support was not sufficiently specific:
   - changed broad "machine learning" positioning to "prediction-oriented methods";
   - changed "public health risk stratification" to "population-level screening-oriented profiles";
   - replaced an uncited lower-BMI Asian-risk statement with a directly supported NHANES undiagnosed-diabetes comparison.

## Final Reference Decisions

### Retained Official Sources

| Ref | Source | Use |
|---:|---|---|
| 1 | CDC/NCHS NHANES Survey Methods and Analytic Guidelines | Survey design and analytic methods |
| 2 | CDC/NCHS NHANES Weighting Module | Survey weights and representative estimation |
| 3 | CDC/NCHS GHB_J documentation | Glycohemoglobin variable and documentation |
| 4 | CDC/NCHS 2017-2018 Laboratory Data page | Laboratory file provenance |
| 5 | ADA Diabetes Diagnosis | HbA1c, FPG, and prediabetes thresholds |
| 6 | NIDDK A1C Test & Diabetes | A1C interpretation and confirmatory testing |
| 7 | NCHS Data Brief No. 516 | Recent national diabetes/undiagnosed diabetes context |
| 8 | Healthy People 2030 D-02 | Prediabetes unawareness as a public health objective |

### Retained Research Literature

| Ref | Source | Use |
|---:|---|---|
| 9 | Menke et al., JAMA 2015 | NHANES diabetes prevalence/trends; racial/ethnic patterning |
| 10 | Fang et al., Diabetes Care 2022 | Undiagnosed diabetes prevalence/trends and confirmatory-definition context |
| 11 | Gupta et al., Am J Cardiol 2022 | NHANES 2011-2020 undiagnosed diabetes trend note |
| 12 | Kiefer et al., J Gen Intern Med 2015 | National diabetes screening patterns and screening gap |
| 13 | Staimez et al., Diabetes Res Clin Pract 2022 | HbA1c/glucose mismatch and misclassification risk |
| 14 | Firouzi et al., J Diabetes Res 2018 | Waist circumference / body-shape indicators and glycemic measures |
| 15 | Tan et al., Lipids Health Dis 2024 | NHANES non-HDL-to-HDL ratio and T2DM association |
| 16 | Seo et al., Transl Res 2022 | Non-HDL cholesterol and incident T2DM cohort evidence |
| 17 | Ley et al., Diabetes Obes Metab 2012 | Non-HDL cholesterol as incident T2DM risk predictor |

### Removed / Not Used as Written

| S6 placeholder | S7b action | Reason |
|---|---|---|
| "Identifying trends in undiagnosed diabetes in U.S. adults using NHANES" | Replaced by Menke et al. 2015, Fang et al. 2022, and Gupta et al. 2022 | Placeholder metadata was not precise enough. |
| "Undiagnosed diabetes based on HbA1c by socioeconomic status" | Removed | Exact source metadata was not verified to submission standard. |
| "Non-HDL cholesterol and diabetes risk literature" | Replaced by Tan et al. 2024, Seo et al. 2022, and Ley et al. 2012 | Original placeholder was not a citable reference. |

## Claim-to-Source Map

| Manuscript claim area | Supporting references |
|---|---|
| NHANES survey design and use of weights/strata/PSUs | 1, 2 |
| NHANES 2017-2018 glycohemoglobin and lab file provenance | 3, 4 |
| HbA1c >=6.5%, prediabetes 5.7%-6.4%, FPG >=126 mg/dL | 5, 6 |
| Recent national burden of diagnosed and undiagnosed diabetes | 7 |
| Prediabetes unawareness as public health target | 8 |
| Prior NHANES prevalence/trend and screening literature | 9-12 |
| HbA1c/FPG mismatch and single-test limitation | 13 |
| Waist circumference / body-shape indicators and glycemic outcomes | 14 |
| Non-HDL / non-HDL-to-HDL and diabetes literature | 15-17 |
| Race/ethnicity caution and uneven screening/detection patterns | 9, 10, 12 |

## Remaining Limitations Before Submission

The draft is now suitable for S8 reviewer-style critique, but it is still not a final submission package because:

- tables and figures remain placeholders;
- the reference list is Vancouver-style but not adapted to a specific target journal;
- official web references may need access dates or alternative formatting depending on journal rules;
- no plagiarism-similarity or journal checklist audit has been performed;
- no cover letter, title page, data availability statement, or reporting guideline checklist has been prepared.

## Verification Checks

| Check | Result |
|---|---|
| Residual `Working candidate` text | None detected |
| Residual `S7 verification needed` text | None detected |
| Approximate word count | 7,174 words by `wc -w` |
| Reference 1-17 represented in in-text citations | Yes, via direct citations or ranges |
| Original S6 draft preserved | Yes |

## S7b Decision

S7b is complete. The recommended next stage is **S8 - Review / Revision**, where the draft should be treated as a citation-clean manuscript for reviewer simulation and revision planning.

## ARS Checkpoint

阶段：S7b - Final reference verification and citation replacement  
状态：complete, awaiting user confirmation  
本阶段交付物：
- `checkpoints/stage-S7b-citation-clean-draft.md`
- `checkpoints/stage-S7b-final-reference-verification.md`

关键决定：
- 不覆盖 S6 原稿，生成 S7b 引用清理稿。
- 删除未核验占位文献，保留 17 条已核验来源。
- 进入 S8 前仍需接受表图占位和目标期刊格式未定的限制。

风险与限制：
- S7b 不是最终投稿格式。
- 未做审稿人模拟和修订路线图。
- 未生成正式表图、cover letter 或 checklist。

下一阶段建议：S8 - Review / Revision  
需要你确认：是否进入 S8？
