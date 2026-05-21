---
id: 17-poam
title: Plan of Action & Milestones (POA&M)
required_by: [cmmc-level-3]
inputs:
  - computed_from: jsons/*.json
    filter: severity in [Critical, High] OR control_status == "Not Met"
  - ask_user:
      prompt: "For each unresolved finding/control, what is the target remediation date and assigned owner?"
      default: "<60 days, <CISO>>"
output_type: table
---

# Plan of Action & Milestones (POA&M)

CMMC-specific. A POA&M tracks unresolved findings with milestones, target dates, and assigned owners. Required for a Conditional CMMC Level 2 Certificate (some failures present, but all in POA&M-eligible categories).

## Template

| S.No. | Finding / Control ID | Description | Severity / Status | Target Remediation Date | Owner | Milestones |
|---|---|---|---|---|---|---|
| 1 | <id> | <description> | <Not Met> | <YYYY-MM-DD> | <name> | <bulleted milestones> |
| ... | | | | | | |

## Notes

- Auto-populated for any finding with severity Critical/High or any control marked Not Met.
- Some CMMC requirements are NOT POA&M-eligible (high-value requirements) — failures in those trigger a Determination Letter instead of a Conditional Certificate.
- POA&M format aligns with the OSCAL POA&M model where possible for interop with FedRAMP/eMASS.
