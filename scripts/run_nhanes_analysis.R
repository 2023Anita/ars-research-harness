args_all <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args_all, value = TRUE)
script_path <- if (length(file_arg) > 0) normalizePath(sub("^--file=", "", file_arg[[1]])) else normalizePath("scripts/run_nhanes_analysis.R")
project_root <- normalizePath(file.path(dirname(script_path), ".."))
run_root <- file.path(project_root, "examples", "nhanes-undiagnosed-diabetes")
raw_dir <- file.path(project_root, "data", "nhanes_2017_2018", "raw")
out_dir <- file.path(run_root, "results", "S3")
local_lib <- file.path(run_root, "r-lib")

dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
if (dir.exists(local_lib)) {
  .libPaths(c(local_lib, .libPaths()))
}

library(haven)
library(dplyr)
library(readr)
library(survey)

options(survey.lonely.psu = "adjust")

read_xpt_local <- function(file) {
  read_xpt(file.path(raw_dir, file))
}

mean_nonzero <- function(data, vars) {
  x <- data[, vars]
  x[x == 0] <- NA
  rowMeans(x, na.rm = TRUE)
}

demo <- read_xpt_local("DEMO_J.xpt") %>%
  select(SEQN, RIDAGEYR, RIAGENDR, RIDRETH3, INDFMPIR, WTMEC2YR, SDMVPSU, SDMVSTRA, RIDEXPRG)

bmx <- read_xpt_local("BMX_J.xpt") %>%
  select(SEQN, BMXBMI, BMXWAIST)

bpx_raw <- read_xpt_local("BPX_J.xpt")
bpx <- bpx_raw %>%
  transmute(
    SEQN,
    sbp_mean = mean_nonzero(bpx_raw, c("BPXSY1", "BPXSY2", "BPXSY3", "BPXSY4")),
    dbp_mean = mean_nonzero(bpx_raw, c("BPXDI1", "BPXDI2", "BPXDI3", "BPXDI4"))
  )

diq <- read_xpt_local("DIQ_J.xpt") %>%
  select(SEQN, DIQ010)

ghb <- read_xpt_local("GHB_J.xpt") %>%
  select(SEQN, LBXGH)

glu <- read_xpt_local("GLU_J.xpt") %>%
  select(SEQN, LBXGLU)

tchol <- read_xpt_local("TCHOL_J.xpt") %>%
  select(SEQN, LBXTC)

hdl <- read_xpt_local("HDL_J.xpt") %>%
  select(SEQN, LBDHDD)

paq <- read_xpt_local("PAQ_J.xpt") %>%
  select(SEQN, PAQ605, PAQ620, PAQ635, PAQ650, PAQ665)

smq <- read_xpt_local("SMQ_J.xpt") %>%
  select(SEQN, SMQ020, SMQ040)

slq <- read_xpt_local("SLQ_J.xpt") %>%
  select(SEQN, SLD012)

analytic_all <- demo %>%
  left_join(bmx, by = "SEQN") %>%
  left_join(bpx, by = "SEQN") %>%
  left_join(diq, by = "SEQN") %>%
  left_join(ghb, by = "SEQN") %>%
  left_join(glu, by = "SEQN") %>%
  left_join(tchol, by = "SEQN") %>%
  left_join(hdl, by = "SEQN") %>%
  left_join(paq, by = "SEQN") %>%
  left_join(smq, by = "SEQN") %>%
  left_join(slq, by = "SEQN") %>%
  mutate(
    adult = RIDAGEYR >= 20,
    self_report_no_diabetes = DIQ010 == 2,
    pregnant = !is.na(RIDEXPRG) & RIDEXPRG == 1,
    has_hba1c = !is.na(LBXGH),
    undiagnosed_diabetes = ifelse(self_report_no_diabetes & has_hba1c & LBXGH >= 6.5, 1,
                                  ifelse(self_report_no_diabetes & has_hba1c, 0, NA)),
    prediabetes = ifelse(self_report_no_diabetes & has_hba1c & LBXGH >= 5.7 & LBXGH < 6.5, 1,
                         ifelse(self_report_no_diabetes & has_hba1c, 0, NA)),
    sex = factor(ifelse(RIAGENDR == 1, "Male", "Female")),
    race_ethnicity = factor(case_when(
      RIDRETH3 == 1 ~ "Mexican American",
      RIDRETH3 == 2 ~ "Other Hispanic",
      RIDRETH3 == 3 ~ "Non-Hispanic White",
      RIDRETH3 == 4 ~ "Non-Hispanic Black",
      RIDRETH3 == 6 ~ "Non-Hispanic Asian",
      RIDRETH3 == 7 ~ "Other/Multiracial",
      TRUE ~ NA_character_
    )),
    age_group = factor(case_when(
      RIDAGEYR >= 20 & RIDAGEYR < 40 ~ "20-39",
      RIDAGEYR >= 40 & RIDAGEYR < 60 ~ "40-59",
      RIDAGEYR >= 60 ~ "60+",
      TRUE ~ NA_character_
    ), levels = c("20-39", "40-59", "60+")),
    pir_group = factor(case_when(
      INDFMPIR < 1.3 ~ "<1.3",
      INDFMPIR >= 1.3 & INDFMPIR < 3.5 ~ "1.3-<3.5",
      INDFMPIR >= 3.5 ~ ">=3.5",
      TRUE ~ NA_character_
    ), levels = c("<1.3", "1.3-<3.5", ">=3.5")),
    obesity = ifelse(!is.na(BMXBMI), as.integer(BMXBMI >= 30), NA),
    abdominal_obesity = ifelse(!is.na(BMXWAIST) & !is.na(RIAGENDR),
                               as.integer((RIAGENDR == 1 & BMXWAIST > 102) |
                                            (RIAGENDR == 2 & BMXWAIST > 88)), NA),
    measured_hypertension = ifelse(!is.na(sbp_mean) | !is.na(dbp_mean),
                                   as.integer((!is.na(sbp_mean) & sbp_mean >= 130) |
                                                (!is.na(dbp_mean) & dbp_mean >= 80)), NA),
    non_hdl = LBXTC - LBDHDD,
    non_hdl_hdl_ratio = non_hdl / LBDHDD,
    current_smoker = case_when(
      SMQ020 == 1 & SMQ040 %in% c(1, 2) ~ 1L,
      SMQ020 == 2 | (SMQ020 == 1 & SMQ040 == 3) ~ 0L,
      TRUE ~ NA_integer_
    ),
    short_sleep = ifelse(!is.na(SLD012), as.integer(SLD012 < 7), NA),
    any_activity = ifelse(
      PAQ605 == 1 | PAQ620 == 1 | PAQ635 == 1 | PAQ650 == 1 | PAQ665 == 1,
      1,
      ifelse(PAQ605 == 2 | PAQ620 == 2 | PAQ635 == 2 | PAQ650 == 2 | PAQ665 == 2, 0, NA)
    )
  )

flow_counts <- tibble(
  step = c(
    "NHANES 2017-2018 interview participants",
    "Adults aged >=20 years",
    "Adults with diabetes questionnaire",
    "Self-reported no diabetes",
    "Self-reported no diabetes and HbA1c available",
    "After excluding pregnant participants"
  ),
  n = c(
    nrow(analytic_all),
    sum(analytic_all$adult, na.rm = TRUE),
    sum(analytic_all$adult & !is.na(analytic_all$DIQ010), na.rm = TRUE),
    sum(analytic_all$adult & analytic_all$self_report_no_diabetes, na.rm = TRUE),
    sum(analytic_all$adult & analytic_all$self_report_no_diabetes & analytic_all$has_hba1c, na.rm = TRUE),
    sum(analytic_all$adult & analytic_all$self_report_no_diabetes & analytic_all$has_hba1c & !analytic_all$pregnant, na.rm = TRUE)
  )
)

analysis <- analytic_all %>%
  filter(adult, self_report_no_diabetes, has_hba1c, !pregnant) %>%
  mutate(
    undiagnosed_diabetes = as.numeric(undiagnosed_diabetes),
    prediabetes = as.numeric(prediabetes),
    sex = relevel(sex, ref = "Male"),
    age_group = relevel(age_group, ref = "20-39"),
    race_ethnicity = relevel(race_ethnicity, ref = "Non-Hispanic White"),
    pir_group = relevel(pir_group, ref = ">=3.5")
  )

write_csv(analytic_all, file.path(out_dir, "analytic_all.csv"))
write_csv(analysis, file.path(out_dir, "analysis_sample.csv"))
write_csv(flow_counts, file.path(out_dir, "flow_counts.csv"))

design <- svydesign(
  id = ~SDMVPSU,
  strata = ~SDMVSTRA,
  weights = ~WTMEC2YR,
  nest = TRUE,
  data = analysis
)

prop_ci <- function(var, design_obj, label) {
  f <- as.formula(paste0("~", var))
  est <- svyciprop(f, design_obj, method = "logit", na.rm = TRUE)
  tibble(
    outcome = label,
    unweighted_n = sum(!is.na(model.frame(f, design_obj$variables)[[1]])),
    unweighted_cases = sum(model.frame(f, design_obj$variables)[[1]] == 1, na.rm = TRUE),
    weighted_percent = as.numeric(coef(est)) * 100,
    ci_low = as.numeric(confint(est)[1]) * 100,
    ci_high = as.numeric(confint(est)[2]) * 100
  )
}

overall_prevalence <- bind_rows(
  prop_ci("undiagnosed_diabetes", design, "HbA1c-defined undiagnosed diabetes"),
  prop_ci("prediabetes", design, "HbA1c-defined prediabetes")
)
write_csv(overall_prevalence, file.path(out_dir, "weighted_prevalence_overall.csv"))

subgroup_prop <- function(group_var) {
  f <- as.formula(paste0("~undiagnosed_diabetes"))
  byf <- as.formula(paste0("~", group_var))
  res <- svyby(f, byf, design, svymean, na.rm = TRUE, vartype = c("se", "ci"))
  as_tibble(res) %>%
    mutate(group_var = group_var) %>%
    rename(group = all_of(group_var), weighted_proportion = undiagnosed_diabetes) %>%
    mutate(group = as.character(group)) %>%
    select(group_var, group, weighted_proportion, se, ci_l, ci_u) %>%
    mutate(across(c(weighted_proportion, se, ci_l, ci_u), ~ .x * 100))
}

subgroup_prevalence <- bind_rows(
  subgroup_prop("sex"),
  subgroup_prop("age_group"),
  subgroup_prop("race_ethnicity"),
  subgroup_prop("obesity")
)
write_csv(subgroup_prevalence, file.path(out_dir, "weighted_prevalence_subgroups.csv"))

weighted_mean_by_outcome <- function(var, label) {
  f <- as.formula(paste0("~", var))
  res <- svyby(f, ~undiagnosed_diabetes, design, svymean, na.rm = TRUE, vartype = c("se"))
  tbl <- as_tibble(res)
  se_col <- if (paste0("se.", var) %in% names(tbl)) paste0("se.", var) else "se"
  tbl %>%
    transmute(
      variable = label,
      group = undiagnosed_diabetes,
      estimate = .data[[var]],
      se = .data[[se_col]],
      metric = "weighted_mean"
    )
}

weighted_prop_by_outcome <- function(var, label) {
  f <- as.formula(paste0("~", var))
  res <- svyby(f, ~undiagnosed_diabetes, design, svymean, na.rm = TRUE, vartype = c("se"))
  tbl <- as_tibble(res)
  se_col <- if (paste0("se.", var) %in% names(tbl)) paste0("se.", var) else "se"
  tbl %>%
    transmute(
      variable = label,
      group = undiagnosed_diabetes,
      estimate = .data[[var]] * 100,
      se = .data[[se_col]] * 100,
      metric = "weighted_percent"
    )
}

table1 <- bind_rows(
  weighted_mean_by_outcome("RIDAGEYR", "Age, years"),
  weighted_prop_by_outcome("obesity", "Obesity, %"),
  weighted_mean_by_outcome("BMXBMI", "BMI, kg/m2"),
  weighted_mean_by_outcome("BMXWAIST", "Waist circumference, cm"),
  weighted_mean_by_outcome("sbp_mean", "Mean systolic BP, mmHg"),
  weighted_mean_by_outcome("dbp_mean", "Mean diastolic BP, mmHg"),
  weighted_mean_by_outcome("LBXGH", "HbA1c, %"),
  weighted_mean_by_outcome("LBXTC", "Total cholesterol, mg/dL"),
  weighted_mean_by_outcome("LBDHDD", "HDL cholesterol, mg/dL"),
  weighted_mean_by_outcome("non_hdl", "Non-HDL cholesterol, mg/dL"),
  weighted_prop_by_outcome("current_smoker", "Current smoker, %"),
  weighted_prop_by_outcome("short_sleep", "Short sleep <7h, %"),
  weighted_prop_by_outcome("any_activity", "Any reported physical activity, %")
)
write_csv(table1, file.path(out_dir, "table1_weighted_by_outcome.csv"))

fit_model <- function(formula, model_name) {
  fit <- svyglm(formula, design = design, family = quasibinomial())
  s <- summary(fit)$coefficients
  terms <- rownames(s)
  tibble(
    model = model_name,
    term = terms,
    beta = s[, "Estimate"],
    se = s[, "Std. Error"],
    p_value = s[, "Pr(>|t|)"],
    odds_ratio = exp(beta),
    ci_low = exp(beta - 1.96 * se),
    ci_high = exp(beta + 1.96 * se)
  )
}

model1 <- fit_model(
  undiagnosed_diabetes ~ RIDAGEYR + sex + race_ethnicity,
  "Model 1: demographics"
)

model2 <- fit_model(
  undiagnosed_diabetes ~ RIDAGEYR + sex + race_ethnicity + INDFMPIR + BMXBMI + BMXWAIST,
  "Model 2: + socioeconomic and anthropometric"
)

model3 <- fit_model(
  undiagnosed_diabetes ~ RIDAGEYR + sex + race_ethnicity + INDFMPIR + BMXBMI + BMXWAIST +
    sbp_mean + non_hdl + LBDHDD + current_smoker + short_sleep + any_activity,
  "Model 3: full model"
)

models <- bind_rows(model1, model2, model3)
write_csv(models, file.path(out_dir, "weighted_logistic_models.csv"))

fpg_analysis <- analysis %>%
  mutate(
    undiagnosed_diabetes_fpg_or_a1c = ifelse(!is.na(LBXGLU) | !is.na(LBXGH),
                                             as.integer((!is.na(LBXGH) & LBXGH >= 6.5) |
                                                          (!is.na(LBXGLU) & LBXGLU >= 126)),
                                             NA)
  )

fpg_design <- svydesign(
  id = ~SDMVPSU,
  strata = ~SDMVSTRA,
  weights = ~WTMEC2YR,
  nest = TRUE,
  data = fpg_analysis
)

sensitivity_prevalence <- prop_ci(
  "undiagnosed_diabetes_fpg_or_a1c",
  fpg_design,
  "HbA1c or fasting glucose-defined undiagnosed diabetes"
)
write_csv(sensitivity_prevalence, file.path(out_dir, "sensitivity_fpg_or_a1c_prevalence.csv"))

analysis_summary <- tibble(
  metric = c(
    "analysis_sample_n",
    "undiagnosed_diabetes_cases",
    "weighted_undiagnosed_diabetes_percent",
    "prediabetes_cases",
    "weighted_prediabetes_percent"
  ),
  value = c(
    nrow(analysis),
    sum(analysis$undiagnosed_diabetes == 1, na.rm = TRUE),
    overall_prevalence$weighted_percent[overall_prevalence$outcome == "HbA1c-defined undiagnosed diabetes"],
    sum(analysis$prediabetes == 1, na.rm = TRUE),
    overall_prevalence$weighted_percent[overall_prevalence$outcome == "HbA1c-defined prediabetes"]
  )
)
write_csv(analysis_summary, file.path(out_dir, "analysis_summary.csv"))

sink(file.path(out_dir, "analysis_log.txt"))
cat("S3 NHANES undiagnosed diabetes analysis\n")
cat("R version:", R.version.string, "\n")
cat("survey version:", as.character(packageVersion("survey")), "\n")
cat("Output directory:", out_dir, "\n\n")
print(flow_counts)
cat("\nOverall prevalence:\n")
print(overall_prevalence)
cat("\nModel terms written to weighted_logistic_models.csv\n")
sink()

cat("S3 analysis complete. Outputs written to:\n")
cat(out_dir, "\n")
print(analysis_summary)
