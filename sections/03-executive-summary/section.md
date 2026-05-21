---
id: 03-executive-summary
title: Executive Summary
required_by: [all]
inputs:
  - from: engagement-summary.md
    field: Overview
  - from: engagement-summary.md
    field: Summary of Findings
  - from: engagement-summary.md
    field: Key Observations & Critical Risks
output_type: narrative
---

# Executive Summary

A 1–2 page non-technical narrative describing what was tested, what was found, and what matters most. Required by every framework.

## Template

### Overview
<from engagement-summary.md — 2-3 sentences: org, test setup, scope at-a-glance>

### Summary of Findings
<from engagement-summary.md — 1 paragraph: counts by severity, headline categories>

### Key Observations & Critical Risks
<from engagement-summary.md — 2-4 paragraphs: the most important things the evaluator should walk away knowing>

## Notes

- This section is read first and often only by senior management / evaluation committees. Keep it accessible.
- ANSSI PASSI explicitly requires "a summary understandable by non-experts" at the top — this section satisfies that.
- The narrative content is captured in `engagement-summary.md` (a separate input file). If unfilled, `/redink-build` refuses to run.
