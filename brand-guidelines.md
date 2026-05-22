# Brand Guidelines

**Fill every field below.** Used to populate the cover page, Part 1 / Executive Summary sections, and the methodology narrative of the final report. Replace the `<...>` placeholders with your firm's real details.

The `/redink-build` command will refuse to run if any required field is still a placeholder.

These fields are framework-agnostic — the same `brand-guidelines.md` works whether the active framework is CERT-In, CMMC, NCSC CHECK, IRAP, PASSI, PCI DSS ROC, or OWASP OPTRS. The assembler picks the relevant fields per framework.

---

## 1. Firm details

| Field | Value |
|---|---|
| Firm name | `<your firm's registered name>` |
| Registration / CIN / corporate identifier | `<corporate identification number>` |
| Registered address | `<street, city, postcode>` |
| Website | `<https://...>` |
| Logo path | `assets/logo.png` *(drop your firm's logo here)* |

## 2. Engagement details

| Field | Value |
|---|---|
| Engagement code | `<your engagement reference code>` |
| Test duration (start) | `<DD/MM/YYYY>` |
| Test duration (end) | `<DD/MM/YYYY>` |
| Report version | `1.0` |
| Submitted on | `<DD/MM/YYYY>` |

## 3. Primary contact (Auditor / Coordinator / QSA / Team Leader)

The role title here varies by framework:

- CERT-In → Auditor / Coordinator
- CMMC → Lead Assessor (C3PAO)
- NCSC CHECK → CHECK Team Leader
- IRAP → IRAP Assessor
- PASSI → Auditeur Principal
- PCI DSS → QSA (Qualified Security Assessor)
- OWASP OPTRS → Lead Pentester

| Field | Value |
|---|---|
| Name | `<full name>` |
| Designation | `<role title — see options above>` |
| Email | `<name@firm.tld>` |
| Phone | `<+CC-XXXXXXXXXX>` |
| Certification(s) held | `<e.g. CHECK Team Leader (Infrastructure), QSA, IRAP Assessor>` |

## 4. Technical manpower (the team that did the engagement)

List 3–7 people. Order matters — the senior-most (typically CISO / Technical Lead) goes first.

| # | Name | Role | Email | Phone | Certifications |
|---|------|------|-------|-------|----------------|
| 1 | `<CISO full name>` | `<CISO / Technical Lead>` | `<email>` | `<phone>` | `<CISSP, OSCP, ...>` |
| 2 | `<team lead full name>` | `<Team Lead / Auditor>` | `<email>` | `<phone>` | `<...>` |
| 3 | `<senior pentester full name>` | `<Senior Pentester>` | `<email>` | `<phone>` | `<...>` |
| 4 | `<pentester full name>` | `<Pentester>` | `<email>` | `<phone>` | `<...>` |
| 5 | `<pentester full name>` | `<Pentester>` | `<email>` | `<phone>` | `<...>` |

## 5. Standards adopted

Tick the ones your engagement follows. Default selection covers the most common compliance expectations.

- [x] OWASP Top 10 (Web)
- [x] OWASP API Security Top 10
- [x] OSSTMM v3
- [x] SANS Top 25
- [x] CIS Benchmarks
- [x] CVSS v3.1
- [x] EPSS (FIRST.org)
- [ ] NIST SP 800-115
- [ ] NIST SP 800-171 (CMMC L2/L3 prerequisite)
- [ ] PTES (Penetration Testing Execution Standard)
- [ ] ISO/IEC 27001:2022
- [ ] PCI DSS v4.0
- [ ] PASSI Référentiel (FR)
- [ ] IRAP Common Assessment Framework (AU)

## 6. Tools used

| Category | Tools |
|---|---|
| Web app testing | `<Burp Suite Pro, OWASP ZAP, ...>` |
| Network / infra | `<Nessus Pro, Nmap, Metasploit Pro, ...>` |
| Password / cred | `<Hashcat, John the Ripper, CrackMapExec, ...>` |
| Enumeration | `<Enum4linux, smbmap, ldapsearch, ...>` |
| Post-exploitation | `<Linpeas, BloodHound, ...>` |
| OS / distro | `<Kali Linux 2026.x>` |
| Benchmarking | `<CIS-CAT Pro>` |

## 7. Attack methodology narrative

3–6 paragraph description of how your firm approached this engagement. Goes into the Methodology / Approach section of the report.

Suggested structure:

1. **Reconnaissance** — passive + active discovery
2. **Vulnerability assessment** — scans run, tools used, baseline
3. **Exploitation** — chains attempted, what worked, what was deliberately not exploited (and why)
4. **Post-exploitation** — privilege escalation, lateral movement, data access
5. **Reporting** — how findings were prioritized, severity scoring approach

`<Write your methodology here. Replace this placeholder before running /redink-build.>`

## 8. Severity rubric (used by validators)

Default mapping from CVSS v3.1 base score. Most frameworks default to this; some (IRAP) don't use severity at all. Override only if your client or framework demands.

| CVSS Base | Severity |
|---|---|
| 9.0 – 10.0 | Critical |
| 7.0 – 8.9 | High |
| 4.0 – 6.9 | Medium |
| 0.1 – 3.9 | Low |
| 0.0 | Informational |

## 9. Report cover language (optional)

Anything specific the cover page should say — confidentiality notice, classification banner, distribution restrictions. Leave blank to use the framework's default language.

`<Optional: paste cover banner here. Leave as-is if the default is fine.>`
