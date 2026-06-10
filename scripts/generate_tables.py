from __future__ import annotations

import textwrap
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUN_ROOT = PROJECT_ROOT / "examples" / "nhanes-undiagnosed-diabetes"
RESULTS_S3 = RUN_ROOT / "results" / "S3"
RESULTS_S3B = RUN_ROOT / "results" / "S3b"
RESULTS_S8B = RUN_ROOT / "results" / "S8b"
CHECKPOINTS = RUN_ROOT / "checkpoints"

RESULTS_S8B.mkdir(parents=True, exist_ok=True)


def fmt_est(row: pd.Series) -> str:
    if row["metric"] == "weighted_percent":
        return f"{row['estimate']:.1f}% ({row['se']:.1f})"
    return f"{row['estimate']:.2f} ({row['se']:.2f})"


def markdown_table(df: pd.DataFrame) -> str:
    values = df.fillna("").astype(str)
    headers = list(values.columns)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for _, row in values.iterrows():
        lines.append("| " + " | ".join(row[col].replace("\n", " ") for col in headers) + " |")
    return "\n".join(lines)


def make_table1() -> pd.DataFrame:
    table1 = pd.read_csv(RESULTS_S3 / "table1_weighted_by_outcome.csv")
    analysis = pd.read_csv(RESULTS_S3 / "analysis_sample.csv")
    variable_map = {
        "Age, years": "RIDAGEYR",
        "Obesity, %": "obesity",
        "BMI, kg/m2": "BMXBMI",
        "Waist circumference, cm": "BMXWAIST",
        "Mean systolic BP, mmHg": "sbp_mean",
        "Mean diastolic BP, mmHg": "dbp_mean",
        "HbA1c, %": "LBXGH",
        "Total cholesterol, mg/dL": "LBXTC",
        "HDL cholesterol, mg/dL": "LBDHDD",
        "Non-HDL cholesterol, mg/dL": "non_hdl",
        "Current smoker, %": "current_smoker",
        "Short sleep <7h, %": "short_sleep",
        "Any reported physical activity, %": "any_activity",
    }
    table1["formatted"] = table1.apply(fmt_est, axis=1)
    wide = table1.pivot(index="variable", columns="group", values="formatted").reset_index()
    wide.columns = ["Characteristic", "No HbA1c-defined undiagnosed diabetes", "HbA1c-defined undiagnosed diabetes"]
    missing_rows = []
    for label in wide["Characteristic"]:
        col = variable_map[label]
        missing_rows.append(int(analysis[col].isna().sum()))
    wide["Missing, n"] = missing_rows
    ordered = list(variable_map.keys())
    wide["order"] = wide["Characteristic"].map({name: i for i, name in enumerate(ordered)})
    wide = wide.sort_values("order").drop(columns=["order"])
    wide.to_csv(RESULTS_S8B / "table1_formatted.csv", index=False)
    (RESULTS_S8B / "table1_formatted.md").write_text(markdown_table(wide), encoding="utf-8")
    return wide


def make_table2() -> pd.DataFrame:
    table2 = pd.read_csv(RESULTS_S3B / "table2_final_main_waist_model.csv")
    out = table2.copy()
    out["OR (95% CI)"] = out.apply(
        lambda r: f"{r['odds_ratio']:.3f} ({r['ci_low']:.3f}-{r['ci_high']:.3f})",
        axis=1,
    )
    out = out[["variable", "OR (95% CI)", "design_df", "model_n"]]
    out.columns = ["Variable", "OR (95% CI)", "Design df", "Model n"]
    out.to_csv(RESULTS_S8B / "table2_formatted.csv", index=False)
    (RESULTS_S8B / "table2_formatted.md").write_text(markdown_table(out), encoding="utf-8")
    return out


def make_supplementary_tables() -> None:
    files = {
        "supplementary_table_bmi_model": RESULTS_S3B / "table2_sensitivity_bmi_model.csv",
        "supplementary_table_categorical_model": RESULTS_S3B / "table2_sensitivity_categorical_screening_model.csv",
        "supplementary_table_fasting_sensitivity": RESULTS_S8B / "fasting_weighted_sensitivity_prevalence.csv",
    }
    for stem, path in files.items():
        df = pd.read_csv(path)
        out_csv = RESULTS_S8B / f"{stem}.csv"
        out_md = RESULTS_S8B / f"{stem}.md"
        df.to_csv(out_csv, index=False)
        out_md.write_text(markdown_table(df), encoding="utf-8")


def make_missingness() -> pd.DataFrame:
    analysis = pd.read_csv(RESULTS_S3 / "analysis_sample.csv")
    variables = [
        "RIDAGEYR",
        "sex",
        "race_ethnicity",
        "BMXWAIST",
        "BMXBMI",
        "sbp_mean",
        "non_hdl",
        "any_activity",
        "obesity",
        "measured_hypertension",
        "LBXGLU",
    ]
    rows = []
    for var in variables:
        missing = int(analysis[var].isna().sum())
        rows.append(
            {
                "variable": var,
                "nonmissing_n": int(analysis[var].notna().sum()),
                "missing_n": missing,
                "missing_percent": round(missing / len(analysis) * 100, 2),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(RESULTS_S8B / "covariate_missingness.csv", index=False)
    (RESULTS_S8B / "covariate_missingness.md").write_text(markdown_table(df), encoding="utf-8")
    return df


def replace_section(text: str, start: str, end: str, replacement: str) -> str:
    start_idx = text.index(start)
    end_idx = text.index(end, start_idx)
    return text[:start_idx] + replacement + text[end_idx:]


def make_revised_manuscript(table1: pd.DataFrame, table2: pd.DataFrame, missingness: pd.DataFrame) -> None:
    src = CHECKPOINTS / "stage-S7b-citation-clean-draft.md"
    text = src.read_text(encoding="utf-8")
    text = text.replace("# S7b Draft: Citation-Clean English SCI Manuscript Draft", "# S8b Revised Manuscript Draft")
    text = text.replace(
        "This is a Stage S7b manuscript draft. The core numerical claims passed S7 data integrity review, and provisional references have been replaced with a verified Vancouver-style reference list. This draft is suitable for S8 reviewer-style critique, but it still requires target-journal formatting and table/figure insertion before submission.",
        "This is a Stage S8b revised manuscript draft. It implements the S8 major-revision roadmap by inserting manuscript tables and figures, clarifying missingness and model degrees of freedom, updating the fasting-glucose sensitivity analysis with fasting subsample weights, and tightening selected contribution and interpretation language. It still requires final target-journal formatting before S9 finalization.",
    )
    text = text.replace(
        "A sensitivity definition used HbA1c >=6.5% or fasting plasma glucose >=126 mg/dL.",
        "A fasting-subsample sensitivity definition used HbA1c >=6.5% or fasting plasma glucose >=126 mg/dL.",
    )
    text = text.replace(
        "When fasting plasma glucose was added to the outcome definition, the estimated prevalence of undiagnosed diabetes increased to 3.26% (95% CI, 2.66%-3.98%).",
        "In the fasting subsample, the fasting-weighted prevalence increased from 1.84% (95% CI, 1.29%-2.62%) using HbA1c alone to 4.06% (95% CI, 3.12%-5.28%) using HbA1c or fasting plasma glucose.",
    )
    text = text.replace(
        "The study further evaluated HbA1c-defined prediabetes and a sensitivity definition that incorporated fasting plasma glucose.",
        "The study further evaluated HbA1c-defined prediabetes and a fasting-subsample sensitivity definition that incorporated fasting plasma glucose.",
    )
    text = text.replace(
        "Because fasting glucose data were available for a smaller subsample, this definition was treated as a sensitivity analysis rather than the primary outcome.",
        "Because fasting glucose data were available only for the fasting subsample, this definition was treated as a sensitivity analysis using fasting subsample weights (`WTSAF2YR`) rather than the primary outcome.",
    )
    text = text.replace(
        "All analyses accounted for the NHANES complex sampling design. MEC examination weights (`WTMEC2YR`) were used because the primary outcome relied on examination and laboratory measures.",
        "All analyses accounted for the NHANES complex sampling design. MEC examination weights (`WTMEC2YR`) were used because the primary outcome relied on examination and laboratory measures.",
    )
    text = text.replace(
        "The `survey.lonely.psu` option was set to adjust lonely primary sampling units.",
        "The `survey.lonely.psu` option was set to adjust lonely primary sampling units. The final survey design had 15 design degrees of freedom; model parsimony was therefore prioritized over a broad covariate set.",
    )
    text = text.replace(
        "Two sensitivity models were generated: a BMI alternative model and a categorical screening model including obesity, measured hypertension, non-HDL cholesterol, and any reported physical activity.",
        "Two sensitivity models were generated: a BMI alternative model and a categorical screening model including obesity, measured hypertension, non-HDL cholesterol, and any reported physical activity. A fasting-weighted sensitivity prevalence analysis used `WTSAF2YR` among participants with fasting glucose data.",
    )
    text = text.replace(
        "The study also contributes by separating three related but distinct concepts: undiagnosed diabetes burden, cardiometabolic profile, and screening implications.",
        "The incremental contribution of this study is its deliberately parsimonious screening-gap profile for a recent pre-pandemic NHANES cycle: it separates undiagnosed diabetes burden, cardiometabolic profile, and screening implications in adults who self-report no diabetes diagnosis.",
    )
    text = text.replace(
        "In this study, incorporating fasting glucose increased the estimated weighted prevalence from 2.17% to 3.26%.",
        "In the fasting subsample, incorporating fasting glucose increased the fasting-weighted estimate from 1.84% to 4.06%.",
    )
    text = text.replace(
        "A broader HbA1c or fasting glucose definition yielded a higher undiagnosed diabetes estimate.",
        "A fasting-subsample HbA1c or fasting glucose definition yielded a higher undiagnosed diabetes estimate.",
    )
    text = text.replace(
        "| Approximate current word count | 7,174 words by `wc -w` |",
        "| Approximate current word count | See `wc -w` after final formatting |",
    )
    missing_summary = (
        "The primary analytic sample included 4,004 participants. The final waist-circumference "
        "model included 3,621 participants after excluding observations with missing model covariates; "
        "the BMI and categorical sensitivity models included 3,707 participants. Key covariate missingness "
        f"included waist circumference n={int(missingness.loc[missingness.variable == 'BMXWAIST', 'missing_n'].iloc[0])}, "
        f"non-HDL cholesterol n={int(missingness.loc[missingness.variable == 'non_hdl', 'missing_n'].iloc[0])}, "
        f"mean systolic blood pressure n={int(missingness.loc[missingness.variable == 'sbp_mean', 'missing_n'].iloc[0])}, "
        f"and physical activity n={int(missingness.loc[missingness.variable == 'any_activity', 'missing_n'].iloc[0])}."
    )
    text = text.replace(
        "Pregnant participants were excluded where pregnancy status was available because pregnancy can alter glycemic interpretation and because gestational diabetes is conceptually distinct from the nonpregnant adult diabetes screening question. The sample selection proceeded as follows:",
        "Pregnant participants were excluded where pregnancy status was available because pregnancy can alter glycemic interpretation and because gestational diabetes is conceptually distinct from the nonpregnant adult diabetes screening question. " + missing_summary + " The sample selection proceeded as follows:",
    )
    tables = "\n\n".join(
        [
            "# Tables and Figures",
            "## Figure 1",
            "Study population selection. File: `results/S8b/figure1_flow.png`.",
            "## Figure 2",
            "Weighted prevalence of HbA1c-defined undiagnosed diabetes by subgroup. File: `results/S8b/figure2_subgroup_prevalence.png`.",
            "## Table 1",
            "Weighted characteristics of self-reported non-diabetic adults by HbA1c-defined undiagnosed diabetes status. Values are weighted mean (SE) or weighted percent (SE).",
            markdown_table(table1),
            "## Table 2",
            "Survey-weighted logistic regression for HbA1c-defined undiagnosed diabetes. Main waist-circumference model.",
            markdown_table(table2),
            "## Supplementary Tables",
            "- Supplementary Table 1: BMI alternative model (`results/S8b/supplementary_table_bmi_model.md`).",
            "- Supplementary Table 2: categorical screening model (`results/S8b/supplementary_table_categorical_model.md`).",
            "- Supplementary Table 3: fasting-weighted HbA1c/FPG sensitivity prevalence (`results/S8b/supplementary_table_fasting_sensitivity.md`).",
            "- Supplementary Table 4: covariate missingness (`results/S8b/covariate_missingness.md`).",
            "\n---\n\n",
        ]
    )
    text = replace_section(text, "# Tables and Figures To Be Inserted", "# References", tables)
    text += "\n\n# Data Availability\n\nNHANES 2017-2018 public-use files are available from CDC/NCHS. Analysis scripts and derived non-identifiable outputs for this project are stored in the local workflow directory under `artifacts/` and `results/`.\n"
    text += "\n# Ethics Statement\n\nThis secondary analysis used publicly available, de-identified NHANES data. NHANES protocols are reviewed by the NCHS Research Ethics Review Board, and no additional participant contact occurred in this analysis.\n"
    out = CHECKPOINTS / "stage-S8b-revised-manuscript.md"
    out.write_text(text, encoding="utf-8")


def main() -> None:
    table1 = make_table1()
    table2 = make_table2()
    make_supplementary_tables()
    missingness = make_missingness()
    make_revised_manuscript(table1, table2, missingness)


if __name__ == "__main__":
    main()
