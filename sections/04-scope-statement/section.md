---
id: 04-scope-statement
title: Engagement Scope Statement
required_by: [all]
inputs:
  - from: targets.yaml
    field: scopes
  - from: targets.yaml
    field: testing_window
output_type: structured
---

# Engagement Scope Statement

Defines what was in scope for the engagement. Every framework requires this — without an explicit scope statement, findings have no boundary.

## Template

The following systems were assessed during this engagement:

<for each scope in targets.yaml>
- **<scope.name>** — `<scope.host>` @ `<scope.ip>`
  - Services tested: <comma-separated services>
  - Notes: <scope.notes>
</for each>

**Testing window:** <start> to <end> (<timezone>)

**Source of testing:** <connection.vpn or "Direct">

## Notes

- For frameworks with explicit cardholder-data-environment (CDE) scoping (PCI DSS), the scope statement also enumerates network segments and explicitly marks each scope as in-scope/out-of-scope.
- IRAP requires explicit boundary diagrams — the user may include a `scope-diagram.png` under `assets/` that the assembler embeds here.
