---
id: 11-summary-of-findings
title: Summary of Findings (Severity Counts)
required_by: [all]
inputs:
  - computed_from: jsons/*.json
    field: severity
output_type: table
---

# Summary of Findings (Severity Counts)

An aggregated count of findings by severity. Computed automatically from the per-finding JSONs in `jsons/`.

## Template

| Severity | Count |
|---|---|
| Critical | <count> |
| High | <count> |
| Medium | <count> |
| Low | <count> |
| Informational | <count> |
| **Total** | **<sum>** |

## Notes

- Auto-computed by walking `jsons/*.json` (one entry per finding) and grouping by the severity field.
- IRAP-style reports omit the Critical/High/Medium/Low columns (no risk rating) — instead this section just shows total observations.
- For CMMC, the table becomes Met / Not Met / Not Applicable counts instead of severity.
