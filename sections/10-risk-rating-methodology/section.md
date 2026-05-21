---
id: 10-risk-rating-methodology
title: Risk-Rating Methodology
required_by: [cmmc-level-3, ncsc-check, crest-cdpt, singapore-ccop, israel-incd, germany-bsi-grundschutz, uae-nesa, saudi-nca-ecc]
explicitly_excluded_by: [irap]
inputs:
  - from: brand-guidelines.md
    field: Severity rubric
  - ask_user:
      prompt: "Use CVSS v3.1 default mapping, or override with a custom rubric? [default/custom]"
      default: "default"
output_type: structured
---

# Risk-Rating Methodology

Describes the scoring/rating system applied to findings. **Explicitly excluded by IRAP** — IRAP assessors identify weaknesses without rating risk, leaving that to the consumer.

## Template

Findings in this report are rated per CVSS v3.1 base scores, mapped to severity as follows:

| CVSS v3.1 Base | Severity |
|---|---|
| 9.0 – 10.0 | Critical |
| 7.0 – 8.9 | High |
| 4.0 – 6.9 | Medium |
| 0.1 – 3.9 | Low |
| 0.0 | Informational |

EPSS (Exploit Prediction Scoring System) probabilities are fetched live from `api.first.org/data/v1/epss` per CVE and reported alongside CVSS where applicable.

## Notes

- IRAP: this section is REMOVED from IRAP reports. The framework manifest explicitly excludes it.
- Some frameworks (PCI DSS, K-ISMS-P) use their own pass/fail rubric instead of CVSS — the section renders the framework-appropriate language.
- ANSSI PASSI uses two-axis classification (impact + exploitation difficulty) rather than single-score CVSS; the section adapts accordingly.
