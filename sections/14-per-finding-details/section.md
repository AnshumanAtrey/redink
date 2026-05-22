---
id: 14-per-finding-details
title: Per-Finding Details
required_by: [all]
inputs:
  - from: jsons/*.json
    field: full-entry
output_type: per-finding-block
---

# Per-Finding Details

The heart of the report — one block per finding, conforming to the active framework's per-finding schema. This is what the `cwe-validator`, `cve-validator`, `cvss-calculator`, `epss-lookup`, `finding-writer`, and `report-reviewer` sub-agents produce.

## Universal per-finding schema

See [`schema.json`](schema.json) in this directory for the full JSON Schema. Required fields:

| Field | Notes |
|---|---|
| `s_no` / `id` / `finding_id` | Sequential identifier (format varies by framework) |
| `name_of_vulnerability` / `title` | Verbatim from PoC folder name |
| `severity` | Critical / High / Medium / Low / Informational (omitted for IRAP) |
| `vulnerable_location` / `affected_asset` | Host + service descriptor |
| `vulnerable_path_port_url` | Exact URL/port/path |
| `vulnerable_parameter` | HTTP param / form field / null |
| `cve_cwe` / `cwe` + `cve` | Validated values only |
| `cvss_epss_score` / `cvss_v3_1` + `epss` | Per FIRST.org spec |
| `description` | ≤ 80 words |
| `poc_steps` / `evidence` | Array with captions + image paths |
| `recommendations` / `remediation` | 2–4 actionable bullets |
| `references` | CWE link, NVD link, vendor advisory, EPSS link |
| `additional_observations` | Optional chain/related notes |
| `cwe_cve_audit` / `audit_trail` | Exact-quote excerpts for evaluator re-verification |
| `cvss_audit` | Per-metric reasoning + math |

## Template

For each finding in `jsons/`:

```
[Severity badge] [S.No] — [Name of Vulnerability]

| S.No.                | <id>                    |
| Name                 | <name>                  |
| Severity             | <severity>              |
| Vulnerable Location  | <location>              |
| Path / Port / URL    | <path_port_url>         |
| Parameter            | <parameter>             |
| CVE / CWE            | <cve_cwe>               |
| CVSS / EPSS          | <cvss_epss_score>       |

Description:
<description>

Proof of Concept:
<poc_intro>
1. <caption 1>     [embedded image 1]
2. <caption 2>     [embedded image 2]
3. <caption 3>     [embedded image 3]

Recommendations:
- <rec 1>
- <rec 2>
- <rec 3>

References:
<references>

Additional Observations:
<additional_observations>

Source-audit footer (small gray text):
<cwe_cve_audit>
```

## Notes

- Universal schema lives in `sections/14-per-finding-details/schema.json` — every framework reads this as the base.
- Frameworks with control-centric reporting (CMMC, PCI DSS, IRAP) wrap this with additional control-mapping fields per their own `frameworks/<name>/schema-overlay.json` (when present).
- The "Vulnerable Point / Error Location" parent grouping common to CERT-In Audit Guidelines reports is rendered as a nested cell structure by the assembler.
