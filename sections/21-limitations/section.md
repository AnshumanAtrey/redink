---
id: 21-limitations
title: Limitations & Disclaimers
required_by: [all]
inputs:
  - ask_user:
      prompt: "List any limitations on testing — time-boxing, access constraints, scope exclusions that affected findings. Defaults included."
      default: "Testing was conducted within the timebox stated in §4 (Engagement Scope). Findings reflect the system state during the testing window only. Subsequent changes may have introduced new vulnerabilities or remediated reported ones. The report is point-in-time and not a continuous-monitoring product."
output_type: narrative
---

# Limitations & Disclaimers

Standard report limitations. Critical for legal defensibility — defines what the report does and does not represent.

## Template

The following limitations apply to this report:

<from user prompt + defaults>

**Standard caveats:**

1. Testing was conducted within the timebox in §4 (Engagement Scope). Findings reflect system state during the testing window only.
2. Subsequent changes to the systems may have introduced new vulnerabilities or remediated those reported.
3. The report represents the auditor's professional opinion based on evidence collected; it is not a guarantee of system security.
4. No testing was performed outside the scope defined in §4 — including no testing of upstream/downstream dependencies unless explicitly named.
5. Findings have been validated against MITRE (CWE), NVD (CVE), and FIRST.org (CVSS, EPSS) as of the report submission date. Source data may have changed since.

## Notes

- This is standard "audit firm liability shield" language. Some clients require this section to be more prominent (e.g., before the executive summary).
- Frameworks like IRAP also explicitly state that the assessor does not provide risk ratings — that disclaimer goes here.
