---
description: List all frameworks supported by redink and show the active one.
---

# /redink-frameworks — framework directory

Read-only. No writes.

## Output

```
redink — supported frameworks

Active: owasp-optrs   (from framework.yaml)

Available frameworks:

  ✅ cmmc-level-3            — USA · DoD contractors assessed by C3PAOs (L2) or DCMA DIBCAC (L3)
  ✅ pci-dss-roc             — Global card industry · PCI SSC QSAs / ISAs (v4.0.1)
  ✅ ncsc-check              — UK · NCSC CHECK Green-Light providers (HMG, CNI)
  ✅ crest-cdpt              — Global · CREST-Accredited Member Companies
  ✅ passi                   — France · ANSSI-qualified PASSI auditeurs (substantiel / élevé)
  ✅ germany-bsi-grundschutz — Germany · BSI-licensed IT-Grundschutz auditors
  ✅ switzerland-ncsc        — Switzerland · BACS/NCSC + FINMA-supervised institutions
  ✅ israel-incd             — Israel · INCD-recognized assessors (ICDM 2.0)
  ✅ uae-nesa                — UAE · SIA-accredited assessors (IA Standard v1.1)
  ✅ saudi-nca-ecc           — Saudi Arabia · NCA-licensed CSPs (Haseen)
  ✅ irap                    — Australia · ASD-registered IRAP assessors
  ✅ k-isms-p                — South Korea · KISA-registered ISMS-P certification bodies
  ✅ japan-nco               — Japan · ISMAP-registered audit institutions (NCO / NISC)
  ✅ singapore-ccop          — Singapore · CSA-approved CII auditors
  ✅ russia-fstec            — Russia · FSTEC-licensed attestation organisations
  ✅ certin-annexure-a       — India · CERT-In empanelled auditors
  ✅ owasp-optrs             — Global open standard · JSON for CI/CD + SOAR

Legend:
  ✅ production-ready — manifest fully populated; section list, hard_rules, and
                       severity scheme validated against official sources

To switch framework: edit framework.yaml and re-run /redink-build.
To override per-run:  /redink-build --framework <name>
```

## What to compute

- Read `framework.yaml` to identify active framework.
- List subdirectories of `frameworks/`.
- For each, parse `manifest.yaml` `name` + `region` + `audience` fields.

Do not run any validators. Do not write any files.
