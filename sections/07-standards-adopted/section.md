---
id: 07-standards-adopted
title: Standards & Frameworks Adopted
required_by: [certin, ncsc-check, pci-dss-roc, crest-cdpt, passi, germany-bsi-grundschutz, japan-nco, israel-incd]
inputs:
  - from: brand-guidelines.md
    field: Standards adopted
output_type: table
---

# Standards & Frameworks Adopted

Lists the testing standards and severity-scoring systems the engagement followed. Maps to CERT-In audit reports.

## Template

| S.No. | Standard / Framework | Severity Scoring System | Other References |
|---|---|---|---|
| 1 | OWASP Top 10 (Web) | CVSS v3.1 | — |
| 2 | OWASP API Security Top 10 | CVSS v3.1 | — |
| 3 | OSSTMM v3 | CVSS v3.1 | — |
| 4 | SANS Top 25 | CVSS v3.1 | — |
| 5 | CIS Benchmarks | CVSS v3.1 | — |
| <... read from brand-guidelines.md §5 ticked items> | | | |

## Notes

- The table is generated from the checked items in `brand-guidelines.md §5`.
- CMMC frameworks add NIST SP 800-171 + 800-53 references.
- BSI IT-Grundschutz reports add BSI Standard 200-1/200-2/200-3 references.
- Israel INCD adds NIST CSF 1.1 + Zero-Trust reference.
