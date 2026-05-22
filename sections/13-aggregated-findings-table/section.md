---
id: 13-aggregated-findings-table
title: Aggregated Findings Table (Vulnerable Locations Overview)
required_by: [certin, ncsc-check, crest-cdpt, passi]
inputs:
  - computed_from: jsons/*.json
    fields: [s_no, vulnerable_location, vulnerable_path_port_url, name_of_vulnerability, cve_cwe]
output_type: table
---

# Aggregated Findings Table

A single table listing every finding with its location, name, and CVE/CWE reference. Maps to CERT-In audit reports — the "List of Vulnerable Parameter, Location discovered" summary.

## Template

| S.No. | Vulnerable Location / Parameter / Path | Name of Vulnerability | References (CVE-ID, CWE-ID) |
|---|---|---|---|
| 001 | <location> · <path> · <param> | <name> | <cve_cwe> |
| 002 | <location> · <path> · <param> | <name> | <cve_cwe> |
| ... | | | |

## Notes

- Auto-computed by walking `jsons/*.json`. The order matches the per-finding-details section (severity descending, then scope, then alphabetical).
- This is the "see at a glance" view for evaluators before they dive into the per-finding details.
- For frameworks where per-finding ID is not `001`/`002`/... but `FINDING-001`/`F-001`/etc., the table uses the framework-appropriate ID format.
