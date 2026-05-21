---
id: 05-out-of-scope
title: Out-of-Scope Statement
required_by: [ncsc-check, crest-cdpt, pci-dss-roc, singapore-ccop, israel-incd, germany-bsi-grundschutz, saudi-nca-ecc]
inputs:
  - ask_user:
      prompt: "List systems / components / activities explicitly EXCLUDED from this engagement, one per line. Leave blank if none."
      default: ""
output_type: bullet-list
---

# Out-of-Scope Statement

Items that were deliberately NOT tested. Critical for legal defensibility — protects both the auditor and the client by making absence-of-coverage explicit.

## Template

The following items were explicitly out of scope for this engagement:

- <item 1>
- <item 2>
- ...

If no exclusions apply, this section may state: "All systems within the testbed defined in §4 (Engagement Scope) were assessed. No exclusions."

## Notes

- CREST CDPT specifically calls out "scope" and "out-of-scope" as distinct critical elements during the scoping phase.
- PCI DSS QSAs use this to call out systems segmented OUT of the cardholder data environment.
