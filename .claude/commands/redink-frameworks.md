---
description: List all frameworks supported by redink and show the active one.
---

# /redink-frameworks — framework directory

Read-only. No writes.

## Output

```
redink — supported frameworks

Active: certin-annexure-a   (from framework.yaml)

Available frameworks:

  ✅ certin-annexure-a   — India · CERT-In empaneled auditors
  ✅ owasp-optrs         — Global · OWASP Penetration Test Reporting Standard (JSON)
  🚧 cmmc-level-3        — USA · DoD contractors via C3PAOs (skeleton)
  🚧 ncsc-check          — UK · CHECK-accredited testers (skeleton)
  🚧 pci-dss-roc         — Global · PCI QSAs / ISAs (skeleton)
  📋 irap                — Australia · ASD-registered IRAP assessors (roadmap)
  📋 passi               — France · ANSSI PASSI-qualified providers (roadmap)

Legend:
  ✅ implemented — fully populated schema, prompt, and example
  🚧 skeleton    — schema and prompt scaffolded; needs practitioner validation
  📋 roadmap     — README only; PRs welcome

To switch framework: edit framework.yaml and re-run /redink-build.
To override per-run:  /redink-build --framework <name>
```

## What to compute

- Read `framework.yaml` to identify active framework.
- List subdirectories of `frameworks/`.
- For each, parse `README.md` to extract the status (✅ / 🚧 / 📋) and region/audience line.

Do not run any validators. Do not write any files.
