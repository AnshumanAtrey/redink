---
id: 15-controls-matrix
title: Controls Matrix
required_by: [cmmc-level-3, irap, pci-dss-roc, k-isms-p, israel-incd, germany-bsi-grundschutz, uae-nesa, saudi-nca-ecc, singapore-ccop]
inputs:
  - from: framework_controls.yaml
    field: full
  - computed_from: jsons/*.json
    fields: [controls_failed, control_status, compliance_status]
output_type: table
---

# Controls Matrix

Per-control table showing implementation status for the framework's prescribed controls. Required by every control-centric framework.

Per-framework control sets:

| Framework | Control set | Status enum |
|---|---|---|
| CMMC L2/L3 | NIST 800-171 (110 controls) + L3 additions | Met / Not Met / N/A |
| IRAP | Australian ISM controls | Implemented / Partially / Not Implemented / N/A |
| PCI DSS | 12 PCI DSS requirements + sub-reqs | In Place / Not In Place / N/A / Compensating Control |
| K-ISMS-P | 102 controls (80 infosec + 22 PII) | Compliant / Non-Compliant / N/A |
| Israel ICDM 2.0 | NIST CSF + 800-53 R5 mapping | Mature / Developing / Initial / N/A |
| BSI IT-Grundschutz | ~100 modules across 10 layers | Erfüllt / Teilweise / Nicht erfüllt / Entbehrlich |
| UAE NESA | 188 controls | Compliant / Partial / Non-Compliant / N/A |
| Saudi NCA ECC | 5 domains, 114 controls | Yes / Partial / No / N/A |
| Singapore CCoP 2.0 | Per CCoP v2 control list | Compliant / Non-Compliant / N/A |

## Template

| S.No. | Control ID | Control Description | Implementation Status | Evidence Reference | Notes |
|---|---|---|---|---|---|
| 1 | <id> | <description> | <status> | <jsons/NNN_*.json if relevant> | <notes> |
| ... | | | | | |

## Notes

- Each framework's preset specifies its control set via `frameworks/<name>/controls.yaml` (loaded at assembly time).
- Controls that have failures point to the per-finding JSONs that demonstrate them (cross-link to section 14).
- For frameworks where redink doesn't ship the full control catalog (most), the user supplies their own `controls.yaml` or PRs one in.
