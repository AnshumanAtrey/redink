# Disclaimer

**Read this before using `redink`.**

## What this is

A Claude Code plugin that helps penetration testers structure their findings into the report format their compliance framework expects. It validates CWE/CVE/CVSS/EPSS citations against canonical sources (MITRE, NVD, FIRST.org) and assembles findings into the framework's report wrapper.

Currently supports: CERT-In · OWASP OPTRS · CMMC Level 2/3 · NCSC CHECK · PCI DSS ROC. IRAP and ANSSI PASSI are on the roadmap.

## What this is not

- **Not exploitation tooling.** This is the *reporting* layer. It assumes you have already completed the exploitation phase and have PoC screenshots.
- **Not a guarantee of compliance.** Evaluators grade on PoC quality, technical depth, and writing craft — not just structure. A perfectly-formatted report with weak PoCs will not pass.
- **Not a substitute for your framework's official rules.** Read your framework's official documentation. If it restricts AI-assisted reporting, do not use this plugin.

## Framework compliance

Cybersecurity audit frameworks are **regulated processes**. Before using AI assistance to draft any portion of an audit report:

1. Read your framework's official rules of engagement / assessment guide / scheme standard for the current cycle.
2. Confirm with the auditor or coordinator that AI-assisted drafting is permitted.
3. Disclose use of AI tooling in your submission cover letter if required.

The authors of this plugin are not liable for audit outcomes, evaluator findings, or any rejection arising from use of the tool.

## What you must still do yourself

| Task | Why |
|---|---|
| Manual PoC verification | Screenshots prove the finding. AI cannot fabricate evidence you do not have. |
| Reading every generated entry | LLMs hallucinate. The `report-reviewer` agent does a re-validation pass, but **the human auditor signs off, not Claude.** |
| Independent re-fetch of cited sources | Every entry's `cwe_cve_audit` field shows the exact-quote source excerpt. Cross-check at least a sample before submission. |
| Senior review | A junior tester + Claude is not a substitute for senior auditor sign-off. |

## Scope of use — authorized testing only

This plugin documents findings from **authorized** penetration tests on systems you have written permission to test (scope-of-work documents, signed contracts, official lab testbeds).

**Do not use this plugin to:**
- Document or distribute findings from unauthorized testing
- Aggregate vulnerability data on production systems without consent
- Bypass disclosure timelines or vendor coordination

If you are unsure whether your testing is authorized, stop and confirm with the system owner.

## Data handling

- All PoC screenshots, scan data, and target details stay on your local filesystem.
- The plugin does not phone home, exfiltrate evidence, or upload findings anywhere.
- Web fetches are limited to public canonical sources: `cwe.mitre.org`, `nvd.nist.gov`, `first.org`.
- The user (you) is responsible for the security of the local workspace — credentials, screenshots, and scan output are sensitive.

## No warranty

This software is provided "as is" under the MIT license, without warranty of any kind. See [LICENSE](LICENSE).

## Reporting concerns

- Security issues with the plugin itself: see [SECURITY.md](SECURITY.md).
- Misuse of the plugin: open a GitHub issue or contact the maintainer.
