# S8b Revised Manuscript Draft

## Manuscript Title

**Cardiometabolic and lifestyle correlates of HbA1c-defined undiagnosed diabetes among self-reported non-diabetic U.S. adults: a cross-sectional analysis of NHANES 2017-2018**

## Draft Status

This is a Stage S8b revised manuscript draft. It implements the S8 major-revision roadmap by inserting manuscript tables and figures, clarifying missingness and model degrees of freedom, updating the fasting-glucose sensitivity analysis with fasting subsample weights, and tightening selected contribution and interpretation language. It still requires final target-journal formatting before S9 finalization.

---

# Abstract

## Background

Undiagnosed diabetes remains a public health concern because individuals may report no history of diabetes while laboratory measures indicate glycemic values in the diabetic range. The ability to identify cardiometabolic and lifestyle profiles associated with undiagnosed diabetes may support more targeted screening among adults who do not report diagnosed diabetes.

## Objective

This study estimated the weighted prevalence of HbA1c-defined undiagnosed diabetes among self-reported non-diabetic U.S. adults and examined demographic, anthropometric, cardiometabolic, and lifestyle correlates using National Health and Nutrition Examination Survey (NHANES) 2017-2018 data.

## Methods

This cross-sectional study used public-use NHANES 2017-2018 interview, examination, and laboratory files. Adults aged 20 years or older who self-reported no prior diabetes diagnosis and had available HbA1c data were included. Pregnant participants were excluded. The primary outcome was HbA1c-defined undiagnosed diabetes, defined as HbA1c >=6.5% among participants who self-reported no diabetes diagnosis. Prediabetes was defined as HbA1c 5.7%-6.4%. A fasting-subsample sensitivity definition used HbA1c >=6.5% or fasting plasma glucose >=126 mg/dL. Survey weights, strata, and primary sampling units were incorporated using the R `survey` package. Weighted prevalence estimates and survey-weighted logistic regression models were calculated.

## Results

The final analytic sample included 4,004 self-reported non-diabetic adults with available HbA1c data after excluding pregnant participants. The weighted prevalence of HbA1c-defined undiagnosed diabetes was 2.17% (95% CI, 1.74%-2.70%), and the weighted prevalence of HbA1c-defined prediabetes was 24.76% (95% CI, 22.63%-27.02%). In the fasting subsample, the fasting-weighted prevalence increased from 1.84% (95% CI, 1.29%-2.62%) using HbA1c alone to 4.06% (95% CI, 3.12%-5.28%) using HbA1c or fasting plasma glucose. Weighted prevalence was higher among participants with obesity than among those without obesity (4.08% vs 0.85%). In a parsimonious survey-weighted logistic model, waist circumference (OR per cm, 1.051; 95% CI, 1.030-1.073) and non-HDL cholesterol (OR per mg/dL, 1.016; 95% CI, 1.008-1.023) were associated with higher odds of HbA1c-defined undiagnosed diabetes. Compared with non-Hispanic White participants, non-Hispanic Asian participants (OR, 5.986; 95% CI, 1.859-19.276) and non-Hispanic Black participants (OR, 4.099; 95% CI, 1.334-12.600) had higher odds. Reporting any physical activity was associated with lower odds in direction, but the confidence interval included the null (OR, 0.478; 95% CI, 0.211-1.078).

## Conclusions

Among self-reported non-diabetic U.S. adults in NHANES 2017-2018, HbA1c-defined undiagnosed diabetes was present in approximately 2% of the weighted population and was patterned by obesity, waist circumference, non-HDL cholesterol, and race/ethnicity. These findings suggest that routine anthropometric and lipid measures may help characterize screening gaps among adults who do not report diagnosed diabetes. Because the analysis was cross-sectional and based on a single survey cycle, results should be interpreted as associations rather than causal effects or diagnostic recommendations.

**Keywords:** NHANES; undiagnosed diabetes; HbA1c; waist circumference; non-HDL cholesterol; diabetes screening; cross-sectional study

---

# Introduction

Diabetes remains a major chronic disease burden in the United States, but diagnosed disease represents only part of the glycemic risk landscape. National surveillance reports continue to distinguish total diabetes, diagnosed diabetes, and undiagnosed diabetes because a meaningful portion of adults have laboratory evidence of diabetes without a corresponding self-reported diagnosis. The National Center for Health Statistics reported that during August 2021-August 2023, the prevalence of total, diagnosed, and undiagnosed diabetes among U.S. adults was 15.8%, 11.3%, and 4.5%, respectively, with prevalence increasing by age and weight status [7]. This surveillance framing is important because diabetes detection is not only a matter of biology; it also depends on access to screening, health care contact, clinical follow-up, patient awareness, and the tests used to define disease.

Self-reported diabetes status is useful in population surveys, but it cannot fully capture glycemic abnormalities in people who have not been tested, have not received results, or do not recall a prior diagnosis. Laboratory-defined undiagnosed diabetes therefore has two linked meanings. Epidemiologically, it identifies a subgroup in which measured glycemia falls within the diabetes range. Clinically, it flags a screening gap rather than a definitive diagnosis, because diagnostic standards generally require confirmatory testing unless symptoms are present. The American Diabetes Association lists HbA1c >=6.5% as a diabetes-range threshold and HbA1c 5.7%-6.4% as a prediabetes range; fasting plasma glucose >=126 mg/dL is another diabetes-range criterion [5]. The National Institute of Diabetes and Digestive and Kidney Diseases similarly emphasizes that abnormal A1C results used for diagnosis usually require confirmation with a second measurement [6]. In population research, this distinction is essential: a single HbA1c value can define an epidemiologic category, but it should not be described as a clinical diagnosis.

The National Health and Nutrition Examination Survey (NHANES) is well suited to examine undiagnosed diabetes because it combines interviews, standardized physical examination, and laboratory measurements in a probability sample of the U.S. civilian noninstitutionalized population. NHANES provides demographic data, anthropometry, blood pressure, health questionnaires, and laboratory measures, including glycohemoglobin and fasting glucose in the 2017-2018 cycle. Its complex sampling design requires analytic weights, strata, and primary sampling units to produce representative estimates and valid variance estimates. NHANES analytic guidelines and weighting tutorials emphasize that weights account for unequal selection probabilities, oversampling, non-response, and post-stratification adjustment [1,2]. For studies of glycemic status in the general adult population, these design features allow researchers to move beyond convenience samples and estimate population-level patterns.

Prior NHANES-based studies have examined diabetes prevalence trends, undiagnosed diabetes definitions, population screening patterns, and discrepancies between HbA1c-based and glucose-based glycemic classification [9-13]. These studies provide important background but leave room for narrower analyses focused on the profile of people who self-report no diabetes diagnosis while meeting laboratory criteria for diabetes-range HbA1c. The research gap is not that undiagnosed diabetes has never been studied; rather, it is that screening-relevant cardiometabolic and lifestyle correlates can be described in a way that links routine measurements to the subgroup most likely to be missed by self-report alone. This framing is especially relevant for public health and primary care because variables such as waist circumference, blood pressure, and lipid measures are widely available or relatively inexpensive compared with advanced metabolic testing.

Anthropometric measures are central to this question. Body mass index is commonly used to categorize weight status, but waist circumference may capture central adiposity more directly. Central adiposity is closely related to insulin resistance and adverse cardiometabolic risk profiles, and NHANES-based studies have examined waist circumference and other body shape indices in relation to glycemic outcomes [14]. In the present analysis, waist circumference was selected for the primary parsimonious model because it was directly measured in NHANES, is interpretable in clinical and public health settings, and avoids overloading a single-cycle model with multiple correlated adiposity variables. BMI and categorical obesity were retained for descriptive and sensitivity analyses.

Lipid measures may also help characterize undiagnosed glycemic abnormalities. Non-HDL cholesterol, calculated as total cholesterol minus HDL cholesterol, captures cholesterol carried by atherogenic lipoproteins and is often easier to derive than more specialized lipid measures. Recent NHANES and cohort studies have reported associations between non-HDL cholesterol, non-HDL-to-HDL cholesterol ratio, and diabetes or incident diabetes risk [15-17]. The current study used non-HDL cholesterol rather than a more novel lipid ratio as a conservative and clinically interpretable marker. This choice supports the study's screening-oriented objective while avoiding overemphasis on a single derived index.

Lifestyle variables, including physical activity, smoking, and sleep duration, may be related to diabetes risk and detection patterns, but their interpretation in cross-sectional survey data is complex. Participants with undiagnosed diabetes may have altered lifestyle behaviors, unmeasured comorbidities, or differential health awareness. Therefore, lifestyle factors in this study are treated as correlates rather than causal exposures. The analysis emphasizes descriptive patterning and adjusted associations, with cautious interpretation of variables whose confidence intervals are wide.

The objective of this study was to estimate the weighted prevalence of HbA1c-defined undiagnosed diabetes among self-reported non-diabetic U.S. adults and to examine its demographic, anthropometric, cardiometabolic, and lifestyle correlates using NHANES 2017-2018 data. The study further evaluated HbA1c-defined prediabetes and a fasting-subsample sensitivity definition that incorporated fasting plasma glucose. The central premise is that a screening gap can be described using routine survey measures, while the conclusions must remain bounded by the cross-sectional design and the limitations of single-measure laboratory definitions.

This focus differs from a conventional diabetes risk-factor analysis in two ways. First, the denominator is not the general adult population or adults with diagnosed diabetes, but adults who report no diabetes diagnosis. This restriction better matches the practical screening problem: clinicians and public health programs often need to decide which apparently non-diabetic adults may warrant laboratory testing or closer follow-up. Second, the analysis emphasizes routinely available correlates rather than complex prediction algorithms. Many recent studies apply prediction-oriented methods to diabetes classification, but the present study deliberately avoids presenting a clinical prediction model because the available data are cross-sectional, single-cycle, and not externally validated. A transparent, survey-weighted epidemiologic analysis is more appropriate for the current evidence base and is less likely to overstate clinical utility.

The incremental contribution of this study is its deliberately parsimonious screening-gap profile for a recent pre-pandemic NHANES cycle: it separates undiagnosed diabetes burden, cardiometabolic profile, and screening implications in adults who self-report no diabetes diagnosis. Estimating prevalence describes the size of the screening gap. Comparing characteristics by outcome status describes the profile of adults who may be missed by self-report. Regression modeling evaluates whether selected measures remain associated after adjustment for major demographic factors. Keeping these aims distinct helps prevent overinterpretation. The analysis can identify associations that may guide future screening research, but it cannot determine whether modifying waist circumference, lipid levels, or physical activity would reduce undiagnosed diabetes in the observed population.

# Methods

## Study design and data source

This cross-sectional study used publicly available NHANES 2017-2018 data. NHANES is conducted by the National Center for Health Statistics and uses a complex, multistage probability sampling design to assess the health and nutritional status of the U.S. civilian noninstitutionalized population. Data are collected through household interviews, standardized physical examinations, and laboratory testing. The 2017-2018 cycle included demographic, examination, questionnaire, and laboratory components. Because the data are publicly released and de-identified, this secondary analysis did not involve direct contact with participants.

The present analysis used 12 NHANES files: demographic data (`DEMO_J`), body measures (`BMX_J`), blood pressure examination data (`BPX_J`), diabetes questionnaire data (`DIQ_J`), glycohemoglobin (`GHB_J`), fasting plasma glucose (`GLU_J`), blood pressure and cholesterol questionnaire data (`BPQ_J`), total cholesterol (`TCHOL_J`), HDL cholesterol (`HDL_J`), physical activity questionnaire data (`PAQ_J`), smoking questionnaire data (`SMQ_J`), and sleep questionnaire data (`SLQ_J`). Files were linked using the respondent sequence number (`SEQN`). Glycohemoglobin was identified using the NHANES variable `LBXGH`, documented as glycohemoglobin (%) in the 2017-2018 laboratory documentation [3,4].

## Study population

The analytic population was restricted to adults aged 20 years or older. Participants were eligible for the primary analysis if they self-reported no prior diabetes diagnosis and had available HbA1c data. Diabetes self-report was derived from the NHANES diabetes questionnaire item asking whether a doctor or health professional had ever told the participant that they had diabetes. Participants who self-reported diagnosed diabetes were excluded from the primary analytic sample because the research question focused on laboratory-defined diabetes-range HbA1c among people who reported no diabetes diagnosis.

Pregnant participants were excluded where pregnancy status was available because pregnancy can alter glycemic interpretation and because gestational diabetes is conceptually distinct from the nonpregnant adult diabetes screening question. The primary analytic sample included 4,004 participants. The final waist-circumference model included 3,621 participants after excluding observations with missing model covariates; the BMI and categorical sensitivity models included 3,707 participants. Key covariate missingness included waist circumference n=188, non-HDL cholesterol n=72, mean systolic blood pressure n=190, and physical activity n=0. The sample selection proceeded as follows: 9,254 NHANES 2017-2018 interview participants were available; 5,569 were aged 20 years or older; 4,517 adults self-reported no diabetes; 4,051 self-reported no diabetes and had available HbA1c data; and 4,004 remained after excluding pregnant participants. This final group constituted the primary analytic sample.

## Outcome definitions

The primary outcome was HbA1c-defined undiagnosed diabetes, defined as HbA1c >=6.5% among participants who self-reported no prior diabetes diagnosis. Participants who self-reported no diabetes and had HbA1c <6.5% were classified as not having HbA1c-defined undiagnosed diabetes for the primary binary outcome. HbA1c-defined prediabetes was defined as HbA1c 5.7%-6.4% among the same self-reported non-diabetic population.

A sensitivity definition of undiagnosed diabetes incorporated fasting plasma glucose. Participants were classified as having HbA1c- or fasting-glucose-defined undiagnosed diabetes if HbA1c was >=6.5% or fasting plasma glucose was >=126 mg/dL. Because fasting glucose data were available only for the fasting subsample, this definition was treated as a sensitivity analysis using fasting subsample weights (`WTSAF2YR`) rather than the primary outcome. The diagnostic thresholds were based on ADA and NIDDK criteria [5,6], but the study language treats these measures as epidemiologic definitions rather than clinical diagnoses because confirmatory testing was not available.

## Covariates

Demographic variables included age, sex, race/ethnicity, and family income-to-poverty ratio. Age was used as a continuous variable in regression models and categorized as 20-39, 40-59, and 60 years or older for subgroup prevalence. Sex was categorized as male or female. Race/ethnicity followed NHANES categories: Mexican American, other Hispanic, non-Hispanic White, non-Hispanic Black, non-Hispanic Asian, and other or multiracial. Family income-to-poverty ratio was used as a continuous socioeconomic measure in extended models and as a descriptive variable where appropriate.

Anthropometric measures included BMI and waist circumference. BMI was calculated and released by NHANES as `BMXBMI`. Obesity was defined as BMI >=30 kg/m2. Waist circumference was measured in centimeters (`BMXWAIST`) and used as the primary adiposity variable in the parsimonious regression model. Waist circumference was preferred for the primary model because it captures central adiposity and reduced the need to include multiple correlated adiposity measures.

Blood pressure measures were calculated from up to four systolic and diastolic readings. Mean systolic blood pressure and mean diastolic blood pressure were calculated from nonmissing values. A measured hypertension indicator was defined using mean systolic blood pressure >=130 mmHg or mean diastolic blood pressure >=80 mmHg for screening-oriented sensitivity analysis. This threshold was used for epidemiologic classification in a sensitivity model and was not intended as a clinical diagnosis.

Lipid measures included total cholesterol, HDL cholesterol, and non-HDL cholesterol. Non-HDL cholesterol was calculated as total cholesterol minus HDL cholesterol. Non-HDL cholesterol was selected for the primary regression model because it is clinically interpretable and derivable from routinely measured cholesterol components.

Lifestyle variables included current smoking, sleep duration, and physical activity. Current smoking was derived from smoking history and current smoking frequency variables. Short sleep was defined as self-reported sleep duration <7 hours. Physical activity was summarized as any reported activity based on NHANES physical activity questionnaire items covering vigorous or moderate work activity, walking or bicycling for transportation, and vigorous or moderate recreational activity.

## Statistical analysis

All analyses accounted for the NHANES complex sampling design. MEC examination weights (`WTMEC2YR`) were used because the primary outcome relied on examination and laboratory measures. Survey strata (`SDMVSTRA`) and primary sampling units (`SDMVPSU`) were incorporated. Analyses were conducted in R version 4.5.1 using the `survey` package version 4.5. The `survey.lonely.psu` option was set to adjust lonely primary sampling units. The final survey design had 15 design degrees of freedom; model parsimony was therefore prioritized over a broad covariate set.

Weighted prevalence estimates and 95% confidence intervals were calculated for HbA1c-defined undiagnosed diabetes and HbA1c-defined prediabetes. Subgroup prevalence estimates were calculated by sex, age group, race/ethnicity, and obesity status. Weighted descriptive characteristics were summarized by undiagnosed diabetes status using survey-weighted means for continuous variables and survey-weighted percentages for binary variables.

Survey-weighted logistic regression was used to estimate associations with HbA1c-defined undiagnosed diabetes. The final primary model was parsimonious and included age, sex, race/ethnicity, waist circumference, mean systolic blood pressure, non-HDL cholesterol, and any reported physical activity. This model was selected after a fuller model was found to be parameter-heavy relative to the design degrees of freedom in a single NHANES cycle. Two sensitivity models were generated: a BMI alternative model and a categorical screening model including obesity, measured hypertension, non-HDL cholesterol, and any reported physical activity. A fasting-weighted sensitivity prevalence analysis used `WTSAF2YR` among participants with fasting glucose data. Odds ratios (ORs) and 95% confidence intervals (CIs) are reported. Because the analysis was exploratory and cross-sectional, emphasis was placed on effect estimates and interval precision rather than binary significance claims.

# Results

## Study population

The analytic sample selection is summarized in Figure 1. Among 9,254 NHANES 2017-2018 interview participants, 5,569 were adults aged 20 years or older. All 5,569 adult participants had diabetes questionnaire data. Among them, 4,517 self-reported no diabetes diagnosis. Of those, 4,051 had available HbA1c data. After excluding pregnant participants, 4,004 adults remained in the primary analytic sample.

This analytic population represents adults who did not report diagnosed diabetes but had laboratory data sufficient to evaluate HbA1c-defined glycemic status. The exclusion of participants with self-reported diagnosed diabetes aligns the denominator with the study's central question: whether laboratory-defined diabetes-range HbA1c is present among adults who report no prior diabetes diagnosis.

## Weighted prevalence of HbA1c-defined undiagnosed diabetes and prediabetes

Among self-reported non-diabetic adults with available HbA1c data, 150 participants had HbA1c >=6.5%. The weighted prevalence of HbA1c-defined undiagnosed diabetes was 2.17% (95% CI, 1.74%-2.70%). HbA1c-defined prediabetes was more common: 1,254 participants had HbA1c 5.7%-6.4%, corresponding to a weighted prevalence of 24.76% (95% CI, 22.63%-27.02%).

In the fasting subsample, the sensitivity definition incorporating fasting plasma glucose identified 115 cases of HbA1c- or fasting-glucose-defined undiagnosed diabetes among 1,807 participants. The corresponding fasting-weighted prevalence was 4.06% (95% CI, 3.12%-5.28%). The higher prevalence under this definition is consistent with the expectation that HbA1c and fasting plasma glucose do not classify all participants identically. Because fasting glucose was available for a smaller subsample, the combined definition was retained as a sensitivity analysis rather than replacing the primary HbA1c-based definition.

## Subgroup prevalence patterns

The weighted prevalence of HbA1c-defined undiagnosed diabetes varied across demographic and anthropometric subgroups. By sex, the weighted prevalence was 1.59% (95% CI, 0.94%-2.24%) among men and 2.69% (95% CI, 1.86%-3.53%) among women. By age group, prevalence was 0.97% (95% CI, 0.40%-1.53%) among adults aged 20-39 years, 2.92% (95% CI, 1.92%-3.91%) among adults aged 40-59 years, and 3.02% (95% CI, 1.98%-4.07%) among adults aged 60 years or older.

Race/ethnicity patterns were also observed. The weighted prevalence was 1.35% (95% CI, 0.65%-2.05%) among non-Hispanic White participants, 2.85% (95% CI, 1.32%-4.39%) among Mexican American participants, 3.24% (95% CI, 0.50%-5.97%) among other Hispanic participants, 4.22% (95% CI, 2.51%-5.94%) among non-Hispanic Asian participants, 4.75% (95% CI, 3.33%-6.17%) among non-Hispanic Black participants, and 1.79% (95% CI, 0.61%-2.98%) among other or multiracial participants. These estimates should be interpreted carefully because some subgroup intervals were wide.

Weight status showed one of the clearest subgroup patterns. Among participants without obesity, the weighted prevalence of HbA1c-defined undiagnosed diabetes was 0.85% (95% CI, 0.54%-1.16%). Among participants with obesity, the weighted prevalence was 4.08% (95% CI, 3.16%-5.00%). This pattern supports the relevance of adiposity-related measures in characterizing undiagnosed glycemic abnormalities among adults who self-report no diabetes diagnosis.

## Weighted characteristics by undiagnosed diabetes status

Participants with HbA1c-defined undiagnosed diabetes differed from those without it across several cardiometabolic variables. The weighted mean age was 54.71 years among participants with undiagnosed diabetes and 46.51 years among those without undiagnosed diabetes. Weighted obesity prevalence was 75.81% in the undiagnosed diabetes group compared with 38.80% in the comparison group.

Anthropometric differences were pronounced. Weighted mean BMI was 35.07 kg/m2 among participants with undiagnosed diabetes and 29.16 kg/m2 among those without undiagnosed diabetes. Weighted mean waist circumference was 112.89 cm in the undiagnosed diabetes group and 98.94 cm in the comparison group. These differences indicate that central and general adiposity were more prominent among participants whose HbA1c met the diabetes-range threshold despite no self-reported diabetes diagnosis.

Blood pressure and lipid measures also differed. Weighted mean systolic blood pressure was 135.90 mmHg among participants with undiagnosed diabetes and 122.39 mmHg among those without undiagnosed diabetes. Weighted mean diastolic blood pressure was 77.05 mmHg and 72.89 mmHg, respectively. Weighted mean total cholesterol was 211.39 mg/dL in the undiagnosed diabetes group compared with 190.32 mg/dL in the comparison group. Weighted mean HDL cholesterol was lower among participants with undiagnosed diabetes (46.53 mg/dL) than among those without undiagnosed diabetes (54.75 mg/dL), while weighted mean non-HDL cholesterol was higher (164.85 mg/dL vs 135.56 mg/dL).

Lifestyle variables showed more cautious patterns. Weighted current smoking prevalence was 14.75% among participants with undiagnosed diabetes and 18.23% among those without. Weighted short sleep prevalence was 30.24% and 24.80%, respectively. Weighted prevalence of any reported physical activity was lower among participants with undiagnosed diabetes than among those without undiagnosed diabetes (56.10% vs 81.00%). These descriptive results suggest a potential activity-related pattern, but they do not establish temporal sequence or causality.

## Survey-weighted logistic regression

In the primary parsimonious survey-weighted logistic regression model, waist circumference and non-HDL cholesterol were associated with higher odds of HbA1c-defined undiagnosed diabetes. Each 1-cm increase in waist circumference was associated with 5.1% higher odds of undiagnosed diabetes (OR, 1.051; 95% CI, 1.030-1.073). Each 1-mg/dL increase in non-HDL cholesterol was associated with 1.6% higher odds (OR, 1.016; 95% CI, 1.008-1.023).

Compared with non-Hispanic White participants, non-Hispanic Asian participants had higher odds of HbA1c-defined undiagnosed diabetes (OR, 5.986; 95% CI, 1.859-19.276), as did non-Hispanic Black participants (OR, 4.099; 95% CI, 1.334-12.600). Mexican American participants (OR, 3.072; 95% CI, 0.608-15.538), other Hispanic participants (OR, 3.737; 95% CI, 0.665-20.989), and other or multiracial participants (OR, 1.774; 95% CI, 0.390-8.077) had point estimates above 1, but their intervals were wide and included the null.

Age, sex, and mean systolic blood pressure had estimates compatible with uncertainty in the parsimonious model. Age had an OR of 1.025 per year (95% CI, 0.983-1.068). Female sex compared with male sex had an OR of 1.861 (95% CI, 0.728-4.756). Mean systolic blood pressure had an OR of 1.012 per mmHg (95% CI, 0.985-1.040). Reporting any physical activity was associated with lower odds in direction (OR, 0.478; 95% CI, 0.211-1.078), but the interval crossed 1.

Sensitivity models supported the general adiposity pattern. In the categorical screening model, obesity was associated with higher odds of HbA1c-defined undiagnosed diabetes (OR, 5.064; 95% CI, 2.574-9.963). In the BMI alternative model, BMI was associated with higher odds (OR per kg/m2, 1.106; 95% CI, 1.064-1.150). Non-HDL cholesterol remained positively associated in both sensitivity models. These sensitivity analyses support the robustness of the anthropometric and lipid-related findings while preserving the primary model's focus on waist circumference.

# Discussion

## Principal findings

In this nationally representative cross-sectional analysis of self-reported non-diabetic U.S. adults in NHANES 2017-2018, HbA1c-defined undiagnosed diabetes was present in 2.17% of the weighted analytic population. HbA1c-defined prediabetes was substantially more common, affecting nearly one-quarter of the weighted analytic population. In the fasting subsample, adding fasting plasma glucose increased the fasting-weighted estimate to 4.06%. These estimates demonstrate that self-reported absence of diabetes does not eliminate the possibility of diabetes-range laboratory values.

The study also identified a cardiometabolic profile associated with HbA1c-defined undiagnosed diabetes. Participants with undiagnosed diabetes had higher weighted mean BMI, waist circumference, systolic blood pressure, total cholesterol, and non-HDL cholesterol, and lower HDL cholesterol than participants without undiagnosed diabetes. In survey-weighted logistic models, waist circumference and non-HDL cholesterol remained associated with higher odds of undiagnosed diabetes. Obesity and BMI were also associated with higher odds in sensitivity models. These findings indicate that routine anthropometric and lipid measures may help characterize screening gaps among adults who self-report no diabetes diagnosis.

Subgroup differences were notable. Weighted prevalence was higher among adults with obesity than among adults without obesity. Higher prevalence and higher adjusted odds were also observed among non-Hispanic Asian and non-Hispanic Black participants compared with non-Hispanic White participants. These patterns should be interpreted as population-level associations rather than biological determinism. Screening access, health care contact, social determinants of health, cardiometabolic risk distributions, and structural factors may all contribute to observed differences.

## Interpretation of undiagnosed diabetes prevalence

The prevalence estimate in this study is lower than recent national estimates of undiagnosed diabetes among all U.S. adults because the denominator and definition differ. NCHS Data Brief No. 516 reported undiagnosed diabetes prevalence among U.S. adults in August 2021-August 2023 using surveillance definitions that are not identical to this study's primary analytic denominator. The present study restricted the denominator to adults who self-reported no diabetes and had available HbA1c data, and the primary definition used HbA1c alone. When fasting plasma glucose was added, the prevalence estimate increased, demonstrating how laboratory definition affects the estimated burden.

This definitional issue is not a limitation unique to the current study; it is a central problem in diabetes surveillance. HbA1c reflects average glycemia over approximately two to three months and does not require fasting, making it convenient for population studies. Fasting plasma glucose captures a different aspect of glycemic physiology. Prior research has documented that HbA1c and glucose-based classifications can be discordant. Therefore, the primary HbA1c definition provides a clear, reproducible epidemiologic category, while the HbA1c/FPG sensitivity analysis illustrates how a broader laboratory definition can identify additional participants.

The practical implication is that undiagnosed diabetes estimates should always be read with attention to the denominator, laboratory criterion, and confirmation rules. For clinical diagnosis, a single test generally requires confirmation unless symptoms are present. For epidemiologic research, however, single-measure definitions are often used to estimate population burden and compare risk profiles. This study follows that epidemiologic convention while explicitly avoiding clinical diagnostic claims.

The lower primary prevalence estimate in this study should not be interpreted as evidence that undiagnosed diabetes is unimportant. A weighted prevalence near 2% among self-reported non-diabetic adults still represents a meaningful public health signal, especially because the same analytic population had a much larger burden of HbA1c-defined prediabetes. The prediabetes estimate is relevant because people in this range may not have symptoms and may not be aware of their glycemic status. Public health objectives such as Healthy People 2030 explicitly track undiagnosed prediabetes awareness [8], reflecting the view that earlier identification is part of chronic disease prevention. The current findings therefore fit within a broader prevention continuum rather than a narrow disease-detection frame.

The sensitivity analysis also illustrates why surveillance studies should report definitions transparently. HbA1c-only and HbA1c-or-fasting-glucose definitions do not identify identical populations. In the fasting subsample, incorporating fasting glucose increased the fasting-weighted estimate from 1.84% to 4.06%. That shift is large enough to matter for interpretation, but not so large that it undermines the primary analysis. Instead, it shows that HbA1c-defined undiagnosed diabetes is a conservative and reproducible main definition, while broader laboratory definitions may capture additional adults with dysglycemia.

## Anthropometric measures and screening relevance

Waist circumference was one of the clearest correlates of HbA1c-defined undiagnosed diabetes. The association persisted in a parsimonious model adjusted for demographic variables, systolic blood pressure, non-HDL cholesterol, and physical activity. The BMI alternative model showed a similar pattern, and the categorical model found that obesity was associated with substantially higher odds of undiagnosed diabetes. Together, these results support the role of adiposity, particularly central adiposity, in identifying people who may benefit from glycemic screening despite reporting no diabetes diagnosis.

The choice of waist circumference as the primary anthropometric variable has both biological and practical rationale. Central adiposity is closely linked with insulin resistance, hepatic fat accumulation, dyslipidemia, and cardiometabolic risk. Waist circumference is easy to measure, inexpensive, and more directly related to abdominal fat distribution than BMI. In clinical and public health settings, waist circumference may add information beyond general body size, particularly in populations where BMI does not fully reflect metabolic risk.

At the same time, waist circumference should not be framed as a diagnostic substitute. The OR per centimeter is statistically and clinically interpretable at a population level, but no single waist circumference value in this study was evaluated as a screening threshold. The results are best interpreted as evidence that central adiposity is part of the risk profile among self-reported non-diabetic adults with diabetes-range HbA1c.

The consistency between the waist circumference model, BMI alternative model, and categorical obesity model strengthens the adiposity finding. In the primary model, waist circumference was associated with higher odds of HbA1c-defined undiagnosed diabetes. In the BMI sensitivity model, BMI showed a similar positive association. In the categorical model, obesity was associated with approximately fivefold higher odds. These analyses do not prove that adiposity causes undiagnosed diabetes, but they reduce concern that the finding depends entirely on a single anthropometric specification. For a manuscript, this is useful because it allows the main text to emphasize waist circumference while using supplementary models to show that the general adiposity pattern is robust.

## Lipid profile and non-HDL cholesterol

Non-HDL cholesterol was associated with higher odds of HbA1c-defined undiagnosed diabetes in the primary model and remained associated in sensitivity models. This finding is consistent with the broader cardiometabolic clustering of dysglycemia, central adiposity, and atherogenic lipid profiles. Non-HDL cholesterol includes cholesterol carried by atherogenic lipoproteins and can be calculated from standard lipid panels. Its availability and interpretability make it attractive for population-level screening research.

The observed association should be interpreted as a marker of cardiometabolic risk rather than a causal claim. Cross-sectional data cannot determine whether adverse lipid profiles preceded diabetes-range HbA1c, developed concurrently, or reflect unmeasured metabolic processes. Furthermore, medication use, diet, physical activity, and access to health care were not comprehensively modeled in this analysis. Even so, the finding contributes to the study's core message: people who report no diabetes diagnosis but have diabetes-range HbA1c may have a broader adverse cardiometabolic profile that could be detectable through routine measurements.

Non-HDL cholesterol is also useful because it can be interpreted without requiring fasting status or specialized lipid fractions. In many real-world settings, non-HDL cholesterol can be calculated from total and HDL cholesterol, making it practical for population risk assessment. The present study does not claim that non-HDL cholesterol should be used alone to trigger diabetes testing. A more defensible interpretation is that non-HDL cholesterol may be one component of a broader cardiometabolic profile that includes central adiposity and demographic risk. This framing is aligned with the manuscript's screening-gap objective and avoids turning an association into a clinical rule.

## Race/ethnicity patterns and interpretation boundaries

The higher odds observed among non-Hispanic Asian and non-Hispanic Black participants require careful interpretation. Race and ethnicity in NHANES are social categories shaped by ancestry, culture, structural conditions, health care access, discrimination, environment, and measurement practices. They should not be interpreted as direct biological causes. In the context of undiagnosed diabetes, higher prevalence or odds may reflect differences in screening opportunities, health insurance, access to primary care, risk factor distributions, body composition, or thresholds at which glycemic abnormalities emerge.

The finding among non-Hispanic Asian participants is particularly important because prior NHANES analyses have reported a relatively high proportion of undiagnosed diabetes among Asian American adults [9,10]. However, this study did not test ethnicity-specific BMI or waist thresholds, nor did it disaggregate Asian subgroups. The broad non-Hispanic Asian category may mask substantial heterogeneity. Similarly, the higher odds among non-Hispanic Black participants may reflect a combination of cardiometabolic risk, access to care, structural inequities, and diagnostic opportunities. Prior studies have reported racial and ethnic differences in cardiometabolic risk among adults with undiagnosed diabetes and gaps between guideline-based screening eligibility and actual screening behavior [18,19]. Future studies with larger samples and more detailed social and health care access measures are needed to clarify these patterns.

In the manuscript, these findings should be presented as evidence that screening gaps are unevenly distributed. The discussion should connect them to public health screening equity rather than assigning inherent risk to racial or ethnic groups.

This distinction is not merely rhetorical. If race/ethnicity findings are written carelessly, they can imply that differences are inherent to groups rather than produced through complex interactions between biology, social context, environment, access, and clinical practice. A more appropriate interpretation is that these categories identify populations in which undiagnosed glycemic abnormality may be more common or more likely to be missed under current screening pathways. The manuscript should therefore use these findings to motivate equity-oriented screening research, not to assign individual risk on the basis of race or ethnicity alone.

The broad NHANES race/ethnicity categories also limit inference. Non-Hispanic Asian participants are reported as a single group, but Asian American populations are heterogeneous with respect to ancestry, migration history, socioeconomic position, diet, body composition, and health care access. The same caution applies to Hispanic categories and other multiracial groups. The current sample was not large enough to support fine-grained subgroup modeling. This limitation should be stated directly, especially because the odds ratios for some groups were large but imprecise.

## Lifestyle correlates

Physical activity showed a lower-odds direction in the primary model, but the confidence interval crossed the null. This result should be described cautiously. The descriptive data showed that any reported physical activity was less common among participants with HbA1c-defined undiagnosed diabetes than among those without it, but the adjusted association was imprecise. Because physical activity was self-reported and summarized broadly, measurement error is likely. Reverse causation is also possible if people with early symptoms, comorbidities, or functional limitations reduce activity before diabetes is identified.

Smoking and short sleep were not strong findings in this analysis and should not be foregrounded in the paper. They can remain in descriptive tables or be mentioned briefly as lifestyle variables considered in the broader profile. The study's stronger contribution lies in anthropometric and lipid correlates, subgroup prevalence, and the demonstration of a measurable screening gap.

The physical activity result is still worth retaining as a cautious secondary observation. In both the descriptive table and adjusted models, any reported physical activity pointed toward lower prevalence or lower odds of undiagnosed diabetes, although the adjusted confidence interval included the null. This pattern is compatible with broader diabetes prevention evidence, but the present analysis cannot establish whether activity protects against dysglycemia, whether healthier participants are more able to be active, or whether self-report misclassification attenuated the estimate. The manuscript should therefore present physical activity as a hypothesis-generating correlate rather than a decisive finding.

The decision not to foreground smoking and sleep is also important for manuscript coherence. Including every measured lifestyle factor in the narrative would dilute the central argument and increase the risk of selective interpretation. A disciplined Results and Discussion section should emphasize the findings with the strongest empirical support in this dataset: undiagnosed diabetes prevalence, adiposity measures, non-HDL cholesterol, and selected subgroup patterns.

## Strengths

This study has several strengths. First, it used NHANES, a nationally representative survey with standardized interview, examination, and laboratory protocols. Second, it focused on adults who self-reported no diabetes diagnosis, directly addressing the discrepancy between self-reported disease status and laboratory-defined glycemic abnormality. Third, the analysis incorporated NHANES weights, strata, and primary sampling units, improving population inference relative to unweighted analyses. Fourth, the study combined demographic, anthropometric, blood pressure, lipid, and lifestyle measures, allowing a screening-oriented profile rather than a single-exposure analysis. Fifth, sensitivity analyses examined a broader HbA1c/FPG definition and alternative anthropometric model specifications.

## Limitations

Several limitations should be considered. The study was cross-sectional, so temporal order cannot be established. Waist circumference, non-HDL cholesterol, physical activity, and undiagnosed diabetes were measured at the same survey cycle. Associations therefore cannot be interpreted as causal effects.

The primary outcome was based on a single HbA1c measurement. Although HbA1c >=6.5% is a diabetes-range threshold, clinical diagnosis generally requires confirmation unless symptoms are present. This study therefore describes HbA1c-defined undiagnosed diabetes, not clinically confirmed diabetes. The fasting glucose sensitivity analysis identified more cases, but fasting glucose was available for a smaller subsample.

Self-reported diabetes status may be misclassified. Some participants may have been diagnosed but did not report it, while others may have been unaware of prior results. Health care access and testing history were not comprehensively modeled. Medication use, diet, insulin, triglycerides, and longitudinal outcomes were not included in the current analysis. The single-cycle design limited sample size, subgroup precision, and model complexity. Some race/ethnicity subgroup estimates had wide confidence intervals, and the broad NHANES categories do not capture within-group heterogeneity.

Finally, the study did not evaluate clinical screening algorithms, prediction models, or diagnostic thresholds. The findings suggest correlates that may inform screening awareness and future research, but they should not be used as a clinical decision rule without external validation.

The manuscript should also acknowledge the limitations introduced by using a single NHANES cycle. A single cycle preserves temporal clarity and avoids complexities of combining weights across cycles, but it reduces sample size and limits model degrees of freedom. This constraint was visible during analysis: a fuller model including many covariates was less suitable for the survey design, leading to the selection of a parsimonious model. This modeling decision is a strength if described transparently. It shows that the analysis was adapted to the data structure rather than forcing an overparameterized model into a single-cycle survey sample.

Another limitation concerns unmeasured clinical context. Participants with diabetes-range HbA1c may have had prior abnormal tests, limited access to follow-up, or health care encounters not captured in the variables used here. Medication use, diet quality, triglycerides, insulin resistance markers, and family history were not included. These omissions mean that the models should be viewed as descriptive and screening-oriented, not mechanistic. Future analyses could extend this work by adding medication files, dietary recalls, triglycerides, insulin, or additional NHANES cycles.

## Public health and research implications

The findings support a screening-gap perspective. In self-reported non-diabetic adults, diabetes-range HbA1c was not rare, and prediabetes-range HbA1c was common. People with higher waist circumference, higher non-HDL cholesterol, obesity, and certain demographic profiles appeared more likely to have laboratory evidence of undiagnosed glycemic abnormality. These variables are routinely collected or relatively easy to measure, which makes them useful for describing population-level screening-oriented profiles.

Future research should extend this analysis by pooling multiple NHANES cycles, incorporating health care access and medication variables, and testing whether the identified profiles persist under alternative glycemic definitions. Longitudinal cohorts would be needed to evaluate whether waist circumference and non-HDL cholesterol predict incident diabetes among people without diagnosed disease. Studies focused on screening equity should examine whether differences in undiagnosed diabetes reflect differential testing, access to primary care, insurance coverage, or structural determinants of health.

The findings also have implications for how AI and data science should be positioned in this topic. It may be tempting to use NHANES variables to build a diabetes prediction model, but prediction would require separate training and validation samples, careful calibration, fairness evaluation, and external validation. The current work is better framed as an epidemiologic foundation for future model development. It identifies variables and subgroups that may be relevant to screening, but it does not claim deployable predictive performance. This conservative positioning is likely to be more credible for peer review than presenting an unvalidated machine learning model.

# Conclusion

Among self-reported non-diabetic U.S. adults in NHANES 2017-2018, HbA1c-defined undiagnosed diabetes affected 2.17% of the weighted analytic population, while HbA1c-defined prediabetes affected nearly one-quarter. A fasting-subsample HbA1c or fasting glucose definition yielded a higher undiagnosed diabetes estimate. Waist circumference and non-HDL cholesterol were associated with higher odds of HbA1c-defined undiagnosed diabetes, and higher prevalence was observed among adults with obesity and in several race/ethnicity subgroups. These results suggest that routine anthropometric and lipid measures may help characterize diabetes screening gaps among adults who report no prior diabetes diagnosis. The findings should be interpreted as cross-sectional associations and require confirmation in studies with repeated testing, richer clinical covariates, and longitudinal follow-up.

---

# Tables and Figures

## Figure 1

Study population selection. File: `results/S8b/figure1_flow.png`.

## Figure 2

Weighted prevalence of HbA1c-defined undiagnosed diabetes by subgroup. File: `results/S8b/figure2_subgroup_prevalence.png`.

## Table 1

Weighted characteristics of self-reported non-diabetic adults by HbA1c-defined undiagnosed diabetes status. Values are weighted mean (SE) or weighted percent (SE).

| Characteristic | No HbA1c-defined undiagnosed diabetes | HbA1c-defined undiagnosed diabetes | Missing, n |
| --- | --- | --- | --- |
| Age, years | 46.51 (0.57) | 54.71 (1.83) | 0 |
| Obesity, % | 38.8% (1.8) | 75.8% (3.4) | 57 |
| BMI, kg/m2 | 29.16 (0.22) | 35.07 (0.45) | 57 |
| Waist circumference, cm | 98.94 (0.66) | 112.89 (1.25) | 188 |
| Mean systolic BP, mmHg | 122.39 (0.52) | 135.90 (3.16) | 190 |
| Mean diastolic BP, mmHg | 72.89 (0.58) | 77.05 (1.83) | 196 |
| HbA1c, % | 5.42 (0.01) | 7.50 (0.22) | 0 |
| Total cholesterol, mg/dL | 190.32 (1.61) | 211.39 (4.87) | 72 |
| HDL cholesterol, mg/dL | 54.75 (0.54) | 46.53 (1.14) | 72 |
| Non-HDL cholesterol, mg/dL | 135.56 (1.66) | 164.85 (4.87) | 72 |
| Current smoker, % | 18.2% (1.2) | 14.8% (6.7) | 0 |
| Short sleep <7h, % | 24.8% (1.5) | 30.2% (6.4) | 31 |
| Any reported physical activity, % | 81.0% (0.9) | 56.1% (7.0) | 0 |

## Table 2

Survey-weighted logistic regression for HbA1c-defined undiagnosed diabetes. Main waist-circumference model.

| Variable | OR (95% CI) | Design df | Model n |
| --- | --- | --- | --- |
| Age, per year | 1.025 (0.983-1.068) | 15 | 3621 |
| Female vs male | 1.861 (0.728-4.756) | 15 | 3621 |
| Mexican American vs Non-Hispanic White | 3.072 (0.608-15.538) | 15 | 3621 |
| Non-Hispanic Asian vs Non-Hispanic White | 5.986 (1.859-19.276) | 15 | 3621 |
| Non-Hispanic Black vs Non-Hispanic White | 4.099 (1.334-12.600) | 15 | 3621 |
| Other Hispanic vs Non-Hispanic White | 3.737 (0.665-20.989) | 15 | 3621 |
| Other/Multiracial vs Non-Hispanic White | 1.774 (0.390-8.077) | 15 | 3621 |
| Waist circumference, per cm | 1.051 (1.030-1.073) | 15 | 3621 |
| Mean systolic BP, per mmHg | 1.012 (0.985-1.040) | 15 | 3621 |
| Non-HDL cholesterol, per mg/dL | 1.016 (1.008-1.023) | 15 | 3621 |
| Any reported physical activity vs none | 0.478 (0.211-1.078) | 15 | 3621 |

## Supplementary Tables

- Supplementary Table 1: BMI alternative model (`results/S8b/supplementary_table_bmi_model.md`).

- Supplementary Table 2: categorical screening model (`results/S8b/supplementary_table_categorical_model.md`).

- Supplementary Table 3: fasting-weighted HbA1c/FPG sensitivity prevalence (`results/S8b/supplementary_table_fasting_sensitivity.md`).

- Supplementary Table 4: covariate missingness (`results/S8b/covariate_missingness.md`).


---

# References

1. Centers for Disease Control and Prevention, National Center for Health Statistics. NHANES Survey Methods and Analytic Guidelines. Accessed June 10, 2026. https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx
2. Centers for Disease Control and Prevention, National Center for Health Statistics. NHANES Weighting Module. Accessed June 10, 2026. https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx
3. Centers for Disease Control and Prevention, National Center for Health Statistics. Glycohemoglobin, GHB_J, NHANES 2017-2018 Data Documentation, Codebook, and Frequencies. Accessed June 10, 2026. https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/GHB_J.htm
4. Centers for Disease Control and Prevention, National Center for Health Statistics. NHANES 2017-2018 Laboratory Data. Accessed June 10, 2026. https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Laboratory&Cycle=2017-2018
5. American Diabetes Association. Diabetes Diagnosis. Accessed June 10, 2026. https://diabetes.org/about-diabetes/diagnosis
6. National Institute of Diabetes and Digestive and Kidney Diseases. The A1C Test & Diabetes. Accessed June 10, 2026. https://www.niddk.nih.gov/health-information/diagnostic-tests/a1c-test
7. Centers for Disease Control and Prevention, National Center for Health Statistics. Prevalence of Total, Diagnosed, and Undiagnosed Diabetes in Adults: United States, August 2021-August 2023. NCHS Data Brief No. 516. Accessed June 10, 2026. https://www.cdc.gov/nchs/products/databriefs/db516.htm
8. Healthy People 2030. Reduce the proportion of adults who do not know they have prediabetes: D-02. Accessed June 10, 2026. https://odphp.health.gov/healthypeople/objectives-and-data/browse-objectives/diabetes/reduce-proportion-adults-who-dont-know-they-have-prediabetes-d-02/data-methodology
9. Menke A, Casagrande S, Geiss L, Cowie CC. Prevalence of and trends in diabetes among adults in the United States, 1988-2012. JAMA. 2015;314(10):1021-1029. doi:10.1001/jama.2015.10029
10. Fang M, Wang D, Coresh J, Selvin E. Undiagnosed diabetes in U.S. adults: prevalence and trends. Diabetes Care. 2022;45(9):1994-2002. doi:10.2337/dc22-0242
11. Gupta K, Obeidat L, Kakar TS, Fadel RA, Al Rifai M, Abushamat LA, Virani SS. Trends in undiagnosed diabetes mellitus among United States adults: cross-sectional analyses from NHANES 2011-2020. Am J Cardiol. 2022;175:184-185. doi:10.1016/j.amjcard.2022.04.032
12. Kiefer MM, Silverman JB, Young BA, Nelson KM. National patterns in diabetes screening: data from the National Health and Nutrition Examination Survey (NHANES) 2005-2012. J Gen Intern Med. 2015;30(5):612-618. doi:10.1007/s11606-014-3147-8
13. Staimez LR, Kipling LM, Nina Ham J, Legvold BT, Jackson SL, Wilson PWF, Rhee MK, Phillips LS. Potential misclassification of diabetes and prediabetes in the U.S.: mismatched HbA1c and glucose in NHANES 2005-2016. Diabetes Res Clin Pract. 2022;189:109935. doi:10.1016/j.diabres.2022.109935
14. Firouzi SA, Tucker LA, LeCheminant JD, Bailey BW. Sagittal abdominal diameter, waist circumference, and BMI as predictors of multiple measures of glucose metabolism: an NHANES investigation of US adults. J Diabetes Res. 2018;2018:3604108. doi:10.1155/2018/3604108
15. Tan MY, Weng L, Yang ZH, Zhu SX, Wu S, Su JH. The association between non-high-density lipoprotein cholesterol to high-density lipoprotein cholesterol ratio with type 2 diabetes mellitus: recent findings from NHANES 2007-2018. Lipids Health Dis. 2024;23(1):151. doi:10.1186/s12944-024-02143-8
16. Seo IH, Son DH, Lee HS, Lee YJ. Non-HDL cholesterol as a predictor for incident type 2 diabetes in community-dwelling adults: longitudinal findings over 12 years. Transl Res. 2022;243:52-59. doi:10.1016/j.trsl.2021.12.008
17. Ley SH, Harris SB, Connelly PW, Mamakeesick M, Gittelsohn J, Wolever TM, Hegele RA, Zinman B, Hanley AJ. Utility of non-high-density lipoprotein cholesterol in assessing incident type 2 diabetes risk. Diabetes Obes Metab. 2012;14(9):821-825. doi:10.1111/j.1463-1326.2012.01607.x
18. Hunt KJ, Gebregziabher M, Egede LE. Racial and ethnic differences in cardio-metabolic risk in individuals with undiagnosed diabetes: National Health and Nutrition Examination Survey 1999-2008. J Gen Intern Med. 2012;27(8):893-900. doi:10.1007/s11606-012-2023-7
19. Sheehy A, Pandhi N, Coursin DB, Flood GE, Kraft SA, Johnson HM, Smith MA. Minority status and diabetes screening in an ambulatory population. Diabetes Care. 2011;34(6):1289-1294. doi:10.2337/dc10-1785

---

# Draft Metadata

| Metric | Value |
|---|---:|
| Draft stage | S8b |
| Target word count | 6,500-8,500 |
| Approximate current word count | See `wc -w` after final formatting |
| Sections completed | Abstract, Introduction, Methods, Results, Discussion, Conclusion |
| Citation status | Verified Vancouver-style reference list; target-journal formatting still required |
| Tables/figures inserted | Table 1, Table 2, Figure 1, Figure 2, and supplementary tables generated |

## Word Count by Section

| Section | Target | Status |
|---|---:|---|
| Abstract | 250-300 | Complete |
| Introduction | 1,300-1,700 | Complete |
| Methods | 1,200-1,500 | Complete |
| Results | 1,100-1,400 | Complete |
| Discussion | 2,200-2,700 | Complete |
| Conclusion | 150-250 | Complete |


# Data Availability

NHANES 2017-2018 public-use files are available from CDC/NCHS. Analysis scripts and derived non-identifiable outputs for this project are stored in the local workflow directory under `artifacts/` and `results/`.

# Ethics Statement

This secondary analysis used publicly available, de-identified NHANES data. NHANES protocols are reviewed by the NCHS Research Ethics Review Board, and no additional participant contact occurred in this analysis.
