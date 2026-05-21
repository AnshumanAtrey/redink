---
id: 26-signoff
title: Signoff Page
required_by: [ncsc-check, pci-dss-roc, cmmc-level-3, passi, irap, crest-cdpt, israel-incd, germany-bsi-grundschutz, singapore-ccop, uae-nesa, saudi-nca-ecc]
inputs:
  - from: brand-guidelines.md
    field: Primary contact
  - ask_user:
      prompt: "Signoff role title (e.g., 'CHECK Team Leader', 'PCI QSA', 'C3PAO Lead Assessor', 'IRAP Assessor')?"
      default: "Lead Assessor"
output_type: signature-block
---

# Signoff Page

A formal signature page closing the report. Required by frameworks where the auditor's signature is part of the legal record (CHECK, PCI QSA, CMMC C3PAO, PASSI, IRAP).

## Template

```
                       SIGNOFF

This report has been reviewed and approved for submission.

  Lead Assessor:    <primary contact name>
  Role:             <e.g. CHECK Team Leader (Infrastructure)>
  Firm:             <firm name>
  Certifications:   <CISSP, OSCP, C3PAO, etc.>
  Signature:        ____________________________
  Date:             <YYYY-MM-DD>

  Quality Reviewer (where required):
  Name:             ____________________________
  Role:             ____________________________
  Signature:        ____________________________
  Date:             ____________________________
```

## Notes

- Frameworks differ in who must sign:
  - **CHECK**: CHECK Team Leader holding the UK CSC Security Testing title (Infrastructure or Web App)
  - **PCI DSS ROC**: QSA + QSA Company representative
  - **CMMC**: C3PAO Lead Assessor + QA Reviewer (independent, not on assessment team)
  - **PASSI**: Auditeur Principal qualifié
  - **IRAP**: ASD-registered IRAP Assessor
- The Quality Reviewer block is conditional — included for CMMC (mandatory) and CHECK (recommended).
