---
id: 06-testing-methodology
title: Testing Methodology
required_by: [all]
inputs:
  - from: brand-guidelines.md
    field: Attack methodology narrative
output_type: narrative
---

# Testing Methodology

3-6 paragraph description of how the firm approached this engagement. Required by every framework.

## Template

<from brand-guidelines.md §7 — the firm's narrative>

Common structure:

1. **Reconnaissance** — passive + active discovery
2. **Vulnerability assessment** — scans run, tools used, baseline
3. **Exploitation** — chains attempted, what worked, what was deliberately not exploited (and why)
4. **Post-exploitation** — privilege escalation, lateral movement, data access
5. **Reporting** — how findings were prioritized, severity scoring approach

## Notes

- IRAP describes assessor approach as collecting + reviewing evidence; this section maps to the same narrative.
- PASSI requires this section to describe "the linear progress of the intrusion tests and the methodology used to detect vulnerabilities."
- CMMC ties methodology to the four phases of C3PAO assessment (Plan/Prepare → Pre-Assessment → Assess Conformity → Complete/Report).
