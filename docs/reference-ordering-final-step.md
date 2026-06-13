# Reference Ordering Final Step

## Background

The submission DOCX builder previously rendered the manuscript Markdown in the order it was written. If the working reference list was not already sorted by first citation appearance, the final DOCX could preserve a mismatched reference order. That is risky for journal submission because numbered citation styles expect in-text citation numbers and the References section to follow the same sequence.

## Optimization

`scripts/build_submission_docx.py` now runs a deterministic reference-ordering pass before writing the DOCX:

- Scans manuscript body text before `# References` for numeric citations such as `[7]`, `[1,2]`, and `[9-13]`.
- Builds an old-to-new mapping based on first citation appearance.
- Rewrites in-text citation groups with sorted, compact final numbers.
- Rewrites the References section in the same final order.
- Preserves manuscript sections that appear after the numbered References list, such as data availability or ethics statements.
- Raises an error if the body cites a reference number that is absent from the References section.
- Writes `reference_order_check.csv` beside the generated DOCX as an audit trail.

## Harness Principle

The optimization keeps reference cleanup inside the reproducible build harness. Authors edit the manuscript Markdown and working reference list, then the final build step produces a consistent DOCX plus an auditable mapping file. This avoids manual Word edits and makes the submission package easier to verify.

## Validation

Run:

```bash
python -m unittest discover -s tests
python scripts/build_submission_docx.py
```

The generated `examples/nhanes-undiagnosed-diabetes/submission_package/reference_order_check.csv` records every cited working-reference number and its final DOCX number.
