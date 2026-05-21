---
id: 02-document-control
title: Document Control / Version History
required_by: [cmmc-level-3, ncsc-check, irap, passi, pci-dss-roc, crest-cdpt, japan-nco, singapore-ccop, k-isms-p, israel-incd, germany-bsi-grundschutz, uae-nesa, saudi-nca-ecc]
inputs:
  - from: brand-guidelines.md
    field: Report version
  - from: brand-guidelines.md
    field: Submitted on
  - ask_user:
      prompt: "Document author(s) for the version-history first row?"
      default: "<primary contact from brand-guidelines.md §3>"
  - ask_user:
      prompt: "Brief change-log entry for version 1.0 (e.g., 'Initial draft')?"
      default: "Initial submission"
output_type: table
---

# Document Control / Version History

Records the report version, date, author, and change history. Standard in any formal audit report; explicitly required by CMMC, PASSI, ISO-27001-derived frameworks, and most enterprise QSAs.

## Template

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | <submitted on> | <author> | <change log entry> |

## Notes

- This table grows as the report goes through internal review cycles. v0.1 ships only the first row; later runs can be hand-edited.
- Some frameworks (CMMC, PASSI) require this immediately after the cover page; others place it in an appendix.
