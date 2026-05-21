---
id: 18-threat-landscape
title: Threat Landscape / Threat Actors Considered
required_by: [germany-bsi-grundschutz, israel-incd, saudi-nca-ecc, cmmc-level-3, japan-nco]
inputs:
  - ask_user:
      prompt: "Describe the threat actors / threat scenarios considered during testing (e.g., external attacker, insider, supply-chain compromise). Brief — 1-3 paragraphs."
      default: "External unauthenticated attacker; assumed-compromise internal user with standard privileges."
output_type: narrative
---

# Threat Landscape / Threat Actors Considered

Describes the threat actors and scenarios the engagement assumed. Required by frameworks that emphasize threat-informed defense (BSI IT-Grundschutz threat catalog, INCD ICDM 2.0, NCA ECC threat-context governance).

## Template

The following threat actors and scenarios were considered during this engagement:

<from user prompt — typically 1-3 paragraphs>

Standard threat actor categories the assessment covered:

- **External unauthenticated attacker** — internet-facing reconnaissance and exploitation
- **External authenticated attacker** — credentialed user attempting privilege escalation
- **Insider — standard user** — assumed-compromise scenario
- **Insider — privileged** — abuse of legitimate access
- **Supply-chain / third-party compromise** — vendor-introduced risk
- **Physical access** — only if engagement included physical pen-test

## Notes

- BSI IT-Grundschutz "Bausteine" (modules) explicitly reference its threat catalog (Gefährdungskatalog) — the section ties findings to elemental threats.
- ICDM 2.0 + NIST CSF 1.1 require Threat-Informed Defense as a baseline.
- Saudi NCA ECC has Cybersecurity Defense as one of 5 core domains; this section feeds the Threat-Informed evidence.
