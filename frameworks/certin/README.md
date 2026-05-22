# CERT-In

**Status:** ✅ Production-ready · **Region:** 🇮🇳 India · **Audience:** CERT-In empanelled auditors + RVDP submitters

CERT-In (Indian Computer Emergency Response Team) operates two public frameworks redink supports:

1. **Comprehensive Cyber Security Audit Policy Guidelines** — the baseline audit framework for empanelled auditors
2. **Responsible Vulnerability Disclosure and Coordination Policy (RVDP)** — coordinated vulnerability disclosure for researchers + vendors

This preset bundles the 13 sections that align with both: cover page, executive summary, scope, methodology, standards, team roster, tools, summary of findings, key observations, aggregated findings table, per-finding details, limitations, references.

See [`manifest.yaml`](manifest.yaml) for the exact section list and metadata.

## Official sources (all public)

- [Responsible Vulnerability Disclosure & Coordination Policy + Vulnerability Reporting Form](https://www.cert-in.org.in/PDF/certinvulnform.pdf)
- [Comprehensive Cyber Security Audit Policy Guidelines](https://www.cert-in.org.in/PDF/Comprehensive_Cyber_Security_Audit_Policy_Guidelines.pdf)
- [Empanelled Information Security Auditing Organisations list](https://www.cert-in.org.in/PDF/Empanel_org.pdf)

## Vulnerability disclosure submission

Per CERT-In RVDP §2:
- Email: `vdisclose@cert-in.org.in` (PGP key `0x3B4E082C` accepted, fingerprint `6927 2217 D8D4 0208 6B1C 23E9 CE29 EA67 3B4E 082C`)
- Helpdesk: `+91-1800-11-4949` (toll-free)
- Acknowledgement within 72 working hours

Per CERT-In RVDP §3, every report must include: affected product(s), exact software version/model, vendor details, description with reproducible steps, supporting evidence (PoC, code sample, crash report, screenshots, or video), and impact analysis. Vulnerability must be reproducible on a supported version and not previously known.
