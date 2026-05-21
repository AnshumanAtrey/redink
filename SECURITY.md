# Security Policy

## Supported versions

`redink` is in **alpha**. Only the latest `main` branch is supported. Pin to a tagged release once one is published.

## Reporting a vulnerability

If you discover a security issue in `redink` itself (not in the systems it documents), report it privately:

- Open a [GitHub security advisory](https://github.com/AnshumanAtrey/redink/security/advisories/new) (preferred), or
- Email the maintainer (see the GitHub profile of [@AnshumanAtrey](https://github.com/AnshumanAtrey))

Please do not file a public issue for security reports.

## Scope

In scope for security reports:

- Prompt-injection vectors via `brand-guidelines.md`, `targets.yaml`, framework prompts, folder names, or scan data that cause the plugin to write malicious content into report JSON
- Path-traversal in the `image_path` field that could exfiltrate files outside the repo
- Validator bypass — ways to make `cwe-validator`, `cve-validator`, etc., accept a citation that fails official validation
- Insecure defaults in `install.sh`, hooks, or any shipped script
- Framework adapter flaws that cause invalid output to be marked as valid

Out of scope:

- Bugs in Claude Code itself — report to [Anthropic](https://github.com/anthropics/claude-code/issues)
- Vulnerabilities you find in **your** testbed using this plugin — those go in your report, not here
- The official compliance frameworks themselves (CERT-In RoE, CMMC AG, NCSC CHECK Standard, IRAP CAF, PASSI référentiel, PCI DSS, OWASP OPTRS)

## Responsible use

`redink` is intended for **authorized** penetration testing engagements where the auditor has written permission to test. Misuse — documenting findings from unauthorized testing, aggregating data on production systems without consent, helping evade disclosure timelines — is not supported.

See [DISCLAIMER.md](DISCLAIMER.md) for the full responsible-use position.

## Threat model

The plugin assumes:

- The user (auditor) is authorized to test the targets in `targets.yaml`
- The local workspace (PoC screenshots, scan data, credentials) is treated as sensitive
- Web fetches go only to canonical security sources (MITRE, NVD, FIRST.org)
- No data is exfiltrated to third-party services

If your workflow violates any of these assumptions, audit your setup before using.
