---
id: 24-glossary
title: Glossary of Terms
required_by: [cmmc-level-3, passi, israel-incd, germany-bsi-grundschutz, japan-nco]
inputs:
  - static: built-in dictionary
output_type: list
---

# Glossary of Terms

Defines technical terms used in the report. Helps non-technical readers (audit committees, executive management) follow per-finding details.

## Template

Standard glossary entries (auto-included):

| Term | Definition |
|---|---|
| CWE | Common Weakness Enumeration — MITRE's catalog of software weakness types |
| CVE | Common Vulnerabilities and Exposures — public catalog of specific known vulnerabilities |
| CVSS | Common Vulnerability Scoring System — standardized severity score |
| EPSS | Exploit Prediction Scoring System — daily-updated likelihood of exploitation |
| PoC | Proof of Concept — demonstrative evidence that a vulnerability is exploitable |
| RCE | Remote Code Execution |
| LFI / RFI | Local File Inclusion / Remote File Inclusion |
| SQLi | SQL Injection |
| XSS | Cross-Site Scripting |
| CSRF | Cross-Site Request Forgery |
| IDOR | Insecure Direct Object Reference |
| LDAP | Lightweight Directory Access Protocol |
| SSRF | Server-Side Request Forgery |
| MFA / 2FA | Multi-Factor Authentication / Two-Factor Authentication |
| WAF | Web Application Firewall |
| ISMS | Information Security Management System |
| <plus framework-specific terms from frameworks/<active>/glossary.yaml> | |

## Notes

- Framework-specific terms (e.g., "C3PAO" for CMMC, "SC clearance" for CHECK, "ISM" for IRAP, "CDE" for PCI DSS) are added from the active framework's optional `glossary.yaml`.
