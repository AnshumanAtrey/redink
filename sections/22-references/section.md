---
id: 22-references
title: References / Bibliography
required_by: [all]
inputs:
  - from: framework manifest
    field: official_sources
  - computed_from: jsons/*.json
    field: references
output_type: list
---

# References / Bibliography

Consolidated list of references — framework standards, advisories, CWE/CVE/EPSS sources. Required for traceability.

## Template

**Framework standards:**
<auto-populated from frameworks/<active>/manifest.yaml official_sources field>

**Vulnerability databases:**
- MITRE CWE: https://cwe.mitre.org/
- NIST NVD: https://nvd.nist.gov/
- FIRST.org CVSS: https://www.first.org/cvss/v3.1/specification-document
- FIRST.org EPSS: https://api.first.org/data/v1/epss

**Per-finding references:**
<auto-populated from each entry's `references` field, deduplicated>

## Notes

- Auto-deduplicated to avoid the same MITRE link appearing 50 times.
- Vendor advisories are linked verbatim from per-finding entries.
