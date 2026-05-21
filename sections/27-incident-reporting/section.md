---
id: 27-incident-reporting
title: Incident-Reporting Alignment
required_by: [switzerland-ncsc, japan-nco]
inputs:
  - ask_user:
      prompt: "If this engagement uncovered any incidents reportable under the framework's incident-reporting rules (e.g., Switzerland 24h rule, Japan ACDA), list them with reporting timelines."
      default: "No reportable incidents identified during this engagement."
output_type: structured
---

# Incident-Reporting Alignment

Notes any findings that trigger statutory incident-reporting obligations. Required by frameworks that combine audit + statutory incident-disclosure obligations.

## Template

**Statutory reporting framework:** <Switzerland NCSC 24-hour rule / Japan ACDA / EU NIS2 / sector-specific>

**Reportable incidents identified in this engagement:**

| Finding ID | Description | Statutory Trigger | Reporting Deadline | Reported Y/N |
|---|---|---|---|---|
| <id> | <description> | <which clause> | <within X hours of discovery> | <yes/no + date if yes> |

If none: "No reportable incidents identified during this engagement."

## Notes

- Switzerland NCSC requires 24-hour reporting for critical infrastructure operators from April 2025.
- Japan ACDA (Active Cyber Defense Act, effective ~November 2026) requires specified essential infrastructure providers to report incidents to competent authorities.
- EU NIS2 Directive: 24-hour early-warning + 72-hour incident notification + 1-month final report.
- This section does NOT replace the formal incident-reporting submission to the regulator. It only documents what was discovered and what reporting was triggered.
