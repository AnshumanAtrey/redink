---
id: 09-tools-used
title: Tools, Scripts & Frameworks Used
required_by: [certin, ncsc-check, crest-cdpt, passi, japan-nco]
inputs:
  - from: brand-guidelines.md
    field: Tools used
output_type: table
---

# Tools, Scripts & Frameworks Used

Tools and tooling categories used during the engagement. Maps to CERT-In audit reports.

## Template

| S.No. | Category | Tools / Scripts / Frameworks Used | Purpose / Usage |
|---|---|---|---|
| 1 | Web app testing | <Burp Suite Pro, OWASP ZAP, ...> | Manual + automated testing of web applications |
| 2 | Network / infra | <Nessus Pro, Nmap, Metasploit Pro, ...> | Vulnerability scanning + manual exploitation |
| <... read from brand-guidelines.md §6 table> | | | |

## Notes

- Read from `brand-guidelines.md §6`. The category column is generated; the tools column is verbatim from the firm's list.
- NIST SP 800-115 expects each tool to be tied to a specific phase of the testing methodology — the Purpose/Usage column captures that.
