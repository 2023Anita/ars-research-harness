args_all <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args_all, value = TRUE)
script_path <- if (length(file_arg) > 0) normalizePath(sub("^--file=", "", file_arg[[1]])) else normalizePath("scripts/generate_figures.R")
project_root <- normalizePath(file.path(dirname(script_path), ".."))
run_root <- file.path(project_root, "examples", "nhanes-undiagnosed-diabetes")
in_dir <- file.path(run_root, "results", "S3")
out_dir <- file.path(run_root, "results", "S8b")

dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

flow <- read.csv(file.path(in_dir, "flow_counts.csv"), stringsAsFactors = FALSE)
png(file.path(out_dir, "figure1_flow.png"), width = 2200, height = 1800, res = 300)
par(mar = c(1, 1, 3, 1))
plot.new()
plot.window(xlim = c(0, 1), ylim = c(0, nrow(flow) + 1))
title("Figure 1. Study population selection", cex.main = 1.1, font.main = 2)
ys <- rev(seq_len(nrow(flow)))
for (i in seq_len(nrow(flow))) {
  y <- ys[i]
  rect(0.12, y - 0.28, 0.88, y + 0.28, border = "#333333", col = "#f7f7f7", lwd = 1.5)
  label <- paste0(flow$step[i], ": n=", format(flow$n[i], big.mark = ","))
  text(0.5, y, label, cex = 0.78)
  if (i < nrow(flow)) {
    arrows(0.5, y - 0.32, 0.5, y - 0.72, length = 0.08, lwd = 1.2)
  }
}
dev.off()

subgroups <- read.csv(file.path(in_dir, "weighted_prevalence_subgroups.csv"), stringsAsFactors = FALSE)
subgroups <- subgroups[subgroups$group_var %in% c("sex", "age_group", "race_ethnicity", "obesity"), ]
subgroups$display_var <- subgroups$group_var
subgroups$display_var[subgroups$display_var == "race_ethnicity"] <- "race/ethnicity"
subgroups$label <- paste(subgroups$display_var, subgroups$group, sep = ": ")
subgroups$label[subgroups$label == "obesity: 0"] <- "obesity: no"
subgroups$label[subgroups$label == "obesity: 1"] <- "obesity: yes"
subgroups <- subgroups[nrow(subgroups):1, ]

png(file.path(out_dir, "figure2_subgroup_prevalence.png"), width = 3400, height = 2200, res = 300)
par(mar = c(4.5, 13.5, 3.5, 1.5))
y <- seq_len(nrow(subgroups))
x <- subgroups$weighted_proportion
plot(
  x,
  y,
  xlim = c(0, max(subgroups$ci_u, na.rm = TRUE) + 1),
  yaxt = "n",
  xlab = "Weighted prevalence, %",
  ylab = "",
  pch = 19,
  col = "#1f5a85",
  main = "Figure 2. HbA1c-defined undiagnosed diabetes by subgroup"
)
axis(2, at = y, labels = subgroups$label, las = 1, cex.axis = 0.72)
segments(subgroups$ci_l, y, subgroups$ci_u, y, col = "#6c8fad", lwd = 1.4)
arrows(subgroups$ci_l, y, subgroups$ci_u, y, angle = 90, code = 3, length = 0.035, col = "#6c8fad")
grid(nx = NA, ny = NULL, col = "#dddddd")
points(x, y, pch = 19, col = "#1f5a85")
dev.off()

cat("Figures written to", out_dir, "\n")
