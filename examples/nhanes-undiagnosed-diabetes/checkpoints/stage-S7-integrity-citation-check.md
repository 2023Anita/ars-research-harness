# S7 Integrity / Citation Check: NHANES Undiagnosed Diabetes Manuscript

## Stage Purpose

This S7 checkpoint audits the S6 English SCI manuscript draft for three submission-critical risks:

- internal consistency between manuscript claims and local analysis outputs;
- citation traceability and reference-list readiness;
- overclaiming, causal language, and clinical recommendation risk.

This stage does not revise the manuscript text. It determines whether the draft is ready to proceed to reviewer-style revision or requires a citation/fix substage first.

## Overall Verdict

**Conditional pass for data integrity; not ready for journal submission.**

The core numerical results in the S6 draft match the local CSV outputs generated in S3 and S3b. The manuscript is also appropriately cautious about cross-sectional inference and single-measure HbA1c definitions.

However, the citation layer is not yet submission-ready. The draft still contains a "Working References for S7 Verification" section and several generic candidate references. Some candidate papers were verified through PubMed/official pages, but several placeholders remain too vague to serve as citable references. Before S8 reviewer simulation or S9 finalization, the project should run **S7b: final reference verification and manuscript citation replacement**.

## Data Integrity Audit

| Manuscript claim | Source checked | Result |
|---|---|---|
| Initial NHANES 2017-2018 interview participants: 9,254 | `results/S3/flow_counts.csv` | Match |
| Adults aged >=20 years: 5,569 | `results/S3/flow_counts.csv` | Match |
| Self-reported no diabetes: 4,517 | `results/S3/flow_counts.csv` | Match |
| Self-reported no diabetes with HbA1c available: 4,051 | `results/S3/flow_counts.csv` | Match |
| Final analytic sample after excluding pregnancy: 4,004 | `results/S3/flow_counts.csv` | Match |
| HbA1c-defined undiagnosed diabetes cases: 150 | `results/S3/weighted_prevalence_overall.csv` | Match |
| Weighted HbA1c-defined undiagnosed diabetes prevalence: 2.17% (95% CI 1.74%-2.70%) | `results/S3/weighted_prevalence_overall.csv` | Match after rounding |
| HbA1c-defined prediabetes cases: 1,254 | `results/S3/weighted_prevalence_overall.csv` | Match |
| Weighted HbA1c-defined prediabetes prevalence: 24.76% (95% CI 22.63%-27.02%) | `results/S3/weighted_prevalence_overall.csv` | Match after rounding |
| HbA1c-or-FPG sensitivity prevalence: 3.26% (95% CI 2.66%-3.98%); cases 211 | `results/S3/sensitivity_fpg_or_a1c_prevalence.csv` | Match after rounding |
| Obesity subgroup prevalence: 4.08% vs 0.85% | `results/S3/weighted_prevalence_subgroups.csv` | Match after rounding |
| Non-Hispanic Asian subgroup prevalence: 4.22%; Non-Hispanic Black: 4.75% | `results/S3/weighted_prevalence_subgroups.csv` | Match after rounding |
| Main Table 2 waist circumference OR: 1.051 (95% CI 1.030-1.073) | `results/S3b/table2_final_main_waist_model.csv` | Match |
| Main Table 2 non-HDL cholesterol OR: 1.016 (95% CI 1.008-1.023) | `results/S3b/table2_final_main_waist_model.csv` | Match |
| Main Table 2 Non-Hispanic Asian OR: 5.986 (95% CI 1.859-19.276) | `results/S3b/table2_final_main_waist_model.csv` | Match |
| Main Table 2 Non-Hispanic Black OR: 4.099 (95% CI 1.334-12.600) | `results/S3b/table2_final_main_waist_model.csv` | Match |
| Main Table 2 any physical activity OR: 0.478 (95% CI 0.211-1.078) | `results/S3b/table2_final_main_waist_model.csv` | Match |
| BMI sensitivity OR: 1.106 (95% CI 1.064-1.150) | `results/S3b/table2_sensitivity_bmi_model.csv` | Match |

### Data Integrity Conclusion

No numeric mismatch was detected in the audited primary claims. The draft's main statistical claims are internally traceable to local outputs.

## Citation Verification Audit

### Official / Methods Sources

| Reference | Verification result | Evidence |
|---|---|---|
| CDC/NCHS NHANES Survey Methods and Analytic Guidelines | Verified | Official CDC/NCHS page documents NHANES sample design, estimation/weighting, variance estimation, and analytic guidelines: https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx |
| CDC/NCHS NHANES Weighting Module | Verified | Official CDC/NCHS tutorial explains the importance of weights for representative estimates and cycle-combination decisions: https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx |
| NHANES GHB_J 2017-2018 documentation | Verified | Official codebook identifies `LBXGH` as Glycohemoglobin (%), and notes use of `SDMVSTRA`/`SDMVPSU` for variance estimation: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/GHB_J.htm |
| NHANES 2017-2018 Laboratory Data page | Verified | Official CDC/NCHS page lists GHB_J and related laboratory data files for the 2017-2018 cycle: https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Laboratory&Cycle=2017-2018 |
| ADA Diabetes Diagnosis | Verified | ADA page supports A1C >=6.5%, prediabetes 5.7%-6.4%, and fasting plasma glucose threshold use: https://diabetes.org/about-diabetes/diagnosis |
| NIDDK A1C Test & Diabetes | Verified | NIDDK page supports A1C threshold interpretation and confirmatory testing language: https://www.niddk.nih.gov/health-information/diagnostic-tests/a1c-test |
| NCHS Data Brief No. 516 | Verified | NCHS Data Brief reports August 2021-August 2023 total, diagnosed, and undiagnosed diabetes prevalence: https://www.cdc.gov/nchs/products/databriefs/db516.htm |
| Healthy People 2030 D-02 | Verified | Official Healthy People page uses NHANES for the objective on reducing unawareness of prediabetes: https://odphp.health.gov/healthypeople/objectives-and-data/browse-objectives/diabetes/reduce-proportion-adults-who-dont-know-they-have-prediabetes-d-02/data-methodology |

### Research Literature Candidates

| S6 candidate | S7 result | Action needed |
|---|---|---|
| "Undiagnosed Diabetes in U.S. Adults: Prevalence and Trends" | Verified as real publication. PubMed ID 35817030; Fang M, Wang D, Coresh J, Selvin E. Diabetes Care. 2022;45(9):1994-2002. DOI: 10.2337/dc22-0242. | Replace candidate wording with full reference and cite in Introduction/Discussion. |
| "Mismatched HbA1c and glucose in NHANES 2005-2016" | Verified as real publication. PubMed ID 35662612; Staimez LR et al. Diabetes Res Clin Pract. 2022;189:109935. DOI: 10.1016/j.diabres.2022.109935. | Replace candidate wording with full reference and cite for HbA1c/FPG definition sensitivity. |
| "Sagittal Abdominal Diameter, Waist Circumference, and BMI..." | Verified as real publication. PubMed ID 30018985; Firouzi SA et al. J Diabetes Res. 2018;2018:3604108. DOI: 10.1155/2018/3604108. | Replace candidate wording with full reference and cite for anthropometric context. |
| "Undiagnosed diabetes based on HbA1c by socioeconomic status" | Not verified to submission standard from current S6 placeholder. A broad PubMed search returned related but not clearly identical records. | Do not cite as written. Either verify the exact PMC article metadata or remove. |
| "Identifying trends in undiagnosed diabetes in U.S. adults using NHANES" | Not verified to submission standard from current S6 placeholder. S5b points to a PMC page, but S7 did not establish full metadata. | Do not cite as written. Verify exact article title/authors/DOI or replace with Fang et al. 2022 and/or NCHS Data Brief. |
| "Trends in Undiagnosed Diabetes Mellitus Among United States Adults: NHANES 2011-2020" | Mentioned in S5b but not included precisely in S6 references. Not verified in this S7 pass. | Optional. Verify only if needed for Introduction; otherwise omit to keep reference list tight. |
| "Non-HDL cholesterol and diabetes risk literature" | Too generic. S7 identified related non-HDL/non-HDL-to-HDL publications, including NHANES-related work, but the S6 reference is not a valid citation. | Replace with 1-2 precise references or reduce the discussion claim to the present study's findings only. |

### Citation Compliance Findings

| Issue | Severity | Explanation |
|---|---|---|
| S6 uses named source descriptions rather than a finalized citation style | Major | The draft is not yet APA/Vancouver compliant and cannot be submitted as-is. |
| Working references 9-14 are placeholders | Major | Placeholder references are not acceptable in a submission draft. |
| In-text citation system is mixed and non-numbered | Major | The manuscript uses source names in prose, not a coherent journal style. |
| Some background claims lack precise citations | Medium | Especially non-HDL cholesterol, race/ethnicity interpretation, and lifestyle discussion. |
| Official web sources are traceable but require journal-specific formatting | Medium | CDC, ADA, NIDDK, and Healthy People entries need consistent formatting. |

## Claim Integrity Audit

### Causal Language

The draft generally avoids causal overclaiming. It repeatedly states that:

- the analysis is cross-sectional;
- results are associations rather than causal effects;
- single HbA1c values are epidemiologic definitions rather than clinical diagnoses;
- no clinical decision rule or deployable prediction model is being proposed.

### Wording Requiring Caution in S7b/S8

| Draft wording pattern | Risk | Recommended handling |
|---|---|---|
| "may help characterize screening gaps" | Acceptable if kept cautious | Retain, but avoid "identify patients" or "guide clinical decisions" without validation. |
| "screening-relevant correlates" | Acceptable | Retain as epidemiologic framing. |
| "risk stratification" | Moderate | Use "population risk description" or "screening-oriented profile" unless a validated model is developed. |
| "predict" in AI/data science discussion | Acceptable as a future-research contrast | Keep clearly framed as future work requiring validation. |
| race/ethnicity odds | Sensitive | Maintain social/structural interpretation and avoid biological essentialism. |

### Clinical / Diagnostic Boundary

The manuscript correctly distinguishes HbA1c-defined undiagnosed diabetes from clinically confirmed diabetes. This distinction should remain in the Abstract, Methods, Discussion, and Limitations.

## Required Fixes Before Submission

1. Replace the "Working References for S7 Verification" section with a finalized, journal-style reference list.
2. Convert all in-text citations to the selected target style, preferably Vancouver if the eventual target journal uses numbered biomedical references.
3. Remove or replace unverified placeholders:
   - "Identifying trends..."
   - "socioeconomic status..."
   - generic "non-HDL cholesterol and diabetes risk literature"
4. Add precise citations for:
   - race/ethnicity and screening inequity interpretation;
   - non-HDL cholesterol / non-HDL-to-HDL ratio and diabetes literature;
   - HbA1c/FPG mismatch and confirmatory testing limitations.
5. Generate actual Table 1, Table 2, Figure 1, and Figure 2 files or insert formatted tables before final review.
6. Keep the manuscript's claims as association-based and avoid clinical recommendation language.

## S7 Decision

S7 is complete as an integrity checkpoint, but the paper is **not ready for S8 reviewer simulation or S9 finalization** unless the user explicitly accepts reviewing a citation-incomplete draft.

Recommended next stage:

- **S7b - Final reference verification and citation replacement**.

S7b should produce:

- a clean reference list;
- a citation map showing each major claim and supporting source;
- a revised S6 draft with placeholders removed;
- a short log of any removed or downgraded claims.

## ARS Checkpoint

阶段：S7 - Integrity / Citation Check  
状态：complete, awaiting user confirmation  
本阶段交付物：
- `checkpoints/stage-S7-integrity-citation-check.md`

关键决定：
- 数据完整性通过本阶段核查。
- 引用完整性未达到投稿标准。
- 建议先进入 S7b，而不是直接进入 S8。

风险与限制：
- 仍需目标期刊格式决定后统一引用格式。
- S7 未改写正文，只判定风险与修复优先级。
- 部分 B/C 文献候选需要被删除或替换为已核验条目。

下一阶段建议：S7b - Final reference verification and citation replacement  
需要你确认：是否进入 S7b？
