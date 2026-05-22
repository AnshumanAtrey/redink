---
id: 08-team-roster
title: Team Roster / Technical Manpower
required_by: [certin, ncsc-check, passi, cmmc-level-3, pci-dss-roc, crest-cdpt, singapore-ccop]
inputs:
  - from: brand-guidelines.md
    field: Technical manpower
output_type: table
---

# Team Roster / Technical Manpower

The team that conducted the engagement. Maps to CERT-In audit reports.

## Template

| S.No. | Name | Designation / Role | Email | Phone | Certifications |
|---|---|---|---|---|---|
| 1 | <name> | <role> | <email> | <phone> | <certs> |
| <... read from brand-guidelines.md §4 table> | | | | | |

## Notes

- Different framework templates expect different column counts (e.g. Name / Designation / Contact for minimal templates; Name / Designation / Email / Certifications / Years of Experience for richer templates). The assembler renders all columns from brand-guidelines.md and the framework template trims to required.
- CHECK reports require ≥1 team member to be a "CHECK Team Leader" with the appropriate UK CSC Security Testing title.
- CMMC requires the Lead Assessor to be a Certified CMMC Assessor; this table also includes the C3PAO firm name.
