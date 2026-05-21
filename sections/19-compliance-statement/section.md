---
id: 19-compliance-statement
title: Compliance Status Statement
required_by: [pci-dss-roc, k-isms-p, israel-incd, germany-bsi-grundschutz, uae-nesa, saudi-nca-ecc, singapore-ccop, russia-fstec]
inputs:
  - computed_from: section 15 (controls matrix)
    field: aggregate-status
  - ask_user:
      prompt: "Overall compliance opinion (Compliant / Substantially Compliant / Non-Compliant / Conditional)?"
      default: "<computed from controls matrix>"
output_type: structured
---

# Compliance Status Statement

The headline assurance opinion. Read by audit committees and executive management. Maps to the "opinion" section of audit reports across most enterprise frameworks.

## Template

**Engagement opinion:** <Compliant / Substantially Compliant / Non-Compliant / Conditional>

**Overall control implementation rate:** <X> of <Y> controls met (<percentage>%).

**By domain / requirement:**

| Domain / Requirement | Met | Not Met | N/A | Compliance % |
|---|---|---|---|---|
| <domain 1> | <#> | <#> | <#> | <%> |
| <domain 2> | <#> | <#> | <#> | <%> |
| ... | | | | |

**Trend versus prior audit (if applicable):** <Improved / Stable / Regressed>

**Open findings register reference:** See §14 (Per-Finding Details) and §17 (POA&M) for outstanding items.

## Notes

- PCI DSS QSAs use language like "In Place" / "Not In Place" — adapted per framework manifest.
- Some frameworks (K-ISMS-P) require an annual surveillance audit + a 3-year recertification — the opinion section may also reference cycle status.
- Saudi NCA ECC: this section feeds the Cybersecurity Compliance & Audit domain.
