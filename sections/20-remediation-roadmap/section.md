---
id: 20-remediation-roadmap
title: Remediation Roadmap / Priority Matrix
required_by: [cmmc-level-3, ncsc-check, crest-cdpt, passi, singapore-ccop, k-isms-p, israel-incd, germany-bsi-grundschutz, uae-nesa, saudi-nca-ecc]
inputs:
  - computed_from: jsons/*.json
    fields: [severity, recommendations]
  - ask_user:
      prompt: "Suggested remediation horizons for each severity: Critical (default 30d), High (60d), Medium (90d), Low (180d)?"
      default: "30/60/90/180"
output_type: table
---

# Remediation Roadmap / Priority Matrix

A prioritized list of remediation actions with suggested timelines. Helps the client triage which findings to address first.

## Template

| Priority | Finding | Severity | Suggested Remediation Window | Owner Suggestion |
|---|---|---|---|---|
| 1 | <name> | Critical | 30 days | <CISO / Infra Lead> |
| 2 | <name> | Critical | 30 days | <Infra Lead> |
| ... | | | | |
| n | <name> | Low | 180 days | <Application Owner> |

Categorical summary:

- **Quick wins** (Critical/High + clear remediation path): N findings
- **Medium-term** (Medium severity): N findings
- **Defer / accept** (Low/Informational): N findings

## Notes

- "Owner Suggestion" is a default; the client adjusts based on their org chart.
- Some frameworks (CMMC) map this directly to the POA&M (§17); for those, the assembler avoids duplicating content.
- CREST CDPT emphasizes "Business Impact Analysis" within reporting — that lands here.
