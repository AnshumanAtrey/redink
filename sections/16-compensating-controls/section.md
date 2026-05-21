---
id: 16-compensating-controls
title: Compensating Controls Register
required_by: [pci-dss-roc]
inputs:
  - ask_user:
      prompt: "Any compensating controls used in lieu of standard control implementations? Provide for each: original requirement, business reason, compensating control, validation, maintenance, and risk analysis."
      default: "None"
output_type: structured
---

# Compensating Controls Register

PCI DSS-specific. When a standard control is not implemented as written, the QSA documents an equivalent compensating control with all required justification fields.

## Template (PCI DSS Compensating Control Worksheet format)

For each compensating control:

| Field | Value |
|---|---|
| Original PCI DSS Requirement | <e.g. Requirement 8.2.4 — Change passwords every 90 days> |
| Business Justification for Non-Standard | <why the standard cannot be met> |
| Compensating Control Description | <what the equivalent control does> |
| Validation of Compensating Control | <how it provides similar/greater protection> |
| Maintenance Procedures | <how the control is kept current> |
| Risk Analysis Performed By | <QSA + date> |

## Notes

- PCI SSC mandates this format. Compensating controls must be reviewed annually + after material changes to the CDE.
- Other frameworks (CMMC, ISO 27001) may also use compensating controls but with less formalised structures.
