---
id: 23-appendices
title: Appendices (Raw Data)
required_by: [cmmc-level-3, ncsc-check, crest-cdpt, passi, irap, pci-dss-roc, israel-incd, germany-bsi-grundschutz, singapore-ccop, uae-nesa, saudi-nca-ecc]
inputs:
  - scan: scans/*
  - ask_user:
      prompt: "Include raw scan data as appendices (Nessus / Burp / Nmap output)? [y/N]"
      default: "n"
output_type: attachment
---

# Appendices (Raw Data)

Optional attachments — raw scan output, sanitized payload logs, configuration dumps that support the findings. Sized appropriately (large dumps go in a separate ZIP).

## Template

Each appendix gets a labeled section:

- **Appendix A — Nessus Scan Output** (file: scans/nessus.html)
- **Appendix B — Burp Suite Pro Export** (file: scans/burp.xml)
- **Appendix C — Nmap Scan Results** (file: scans/nmap.txt)
- **Appendix D — Sanitized Payload Log** (file: scans/payloads.txt)
- **Appendix E — Network Topology Diagram** (file: assets/topology.png)

## Notes

- Appendices for files > 10 MB get a separate ZIP delivered alongside the main report.
- Some frameworks (IRAP, BSI) expect specific control-evidence file structures — those go here.
- PCI DSS QSAs typically include the cardholder-data-environment network diagram here.
- The assembler does NOT embed large files into the docx; it lists references and ships a companion ZIP if needed.
