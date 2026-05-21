---
id: 28-continuous-monitoring
title: Continuous Monitoring Evidence
required_by: [k-isms-p, israel-incd]
inputs:
  - ask_user:
      prompt: "If the framework requires continuous-monitoring evidence (K-ISMS-P Q3 2026+, INCD continuous posture), describe the monitoring tools / cadence / live red-team artifacts."
      default: "Monitoring evidence to be supplied separately by the client."
output_type: narrative
---

# Continuous Monitoring Evidence

Required by frameworks shifting from annual-snapshot audits to continuous-posture models.

## Template

**Continuous monitoring posture:**

<narrative — typically 2-4 paragraphs describing>:

- Monitoring tools deployed (SIEM, EDR, ASM tools, vulnerability scanners)
- Monitoring cadence (real-time / hourly / daily)
- Coverage by environment (prod / staging / endpoints)
- Live red-team artifacts (for K-ISMS-P from Q3 2026+, this is mandatory)
- Incident response runbook references

**Last 30 days of monitoring evidence:**

| Date | Event Type | Severity | Resolution Time | Status |
|---|---|---|---|---|
| <date> | <type> | <sev> | <minutes/hours> | <closed/open> |

## Notes

- South Korea's K-ISMS-P moves to mandatory live red-teaming + continuous posture from Q3 2026.
- Israel INCD ICDM 2.0 emphasizes Zero-Trust + continuous posture assessment over annual snapshots.
- The redink pipeline doesn't run continuous monitoring — this section is for documenting what the client has in place; the auditor describes what they verified.
