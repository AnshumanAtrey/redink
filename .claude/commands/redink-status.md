---
description: Show pipeline progress — active framework, which findings exist, which are validated, which are pending.
---

# /redink-status — progress check

Read-only inspection. No writes, no validators spawned.

## Output

```
redink — status

Active framework: certin-annexure-a  (frameworks/certin-annexure-a/ — implemented)

Inputs:
  framework.yaml        ✓ certin-annexure-a
  brand-guidelines.md   ✓ filled         (or: ✗ contains <placeholders>)
  targets.yaml          ✓ valid
  poc/web/              12 folders
  poc/server/           17 folders
  scans/                nessus.html, nmap.txt

Findings:
  Total expected:      29  (12 web + 17 server)
  JSONs written:       23
  JSONs pending:        6  — list below
  QA report:           output/qa-report.md  (last run: YYYY-MM-DD HH:MM, 0 issues)

Pending folders (not yet in jsons/):
  - poc/web/13_Open_Redirect_Login/
  - poc/web/14_Session_Fixation/
  - poc/server/15_Outdated_OpenSSH/
  - poc/server/16_NTP_Amplification/
  - poc/server/17_SNMPv1_Community_String/

Severity distribution (written so far):
  Critical:  4
  High:      9
  Medium:    8
  Low:       2

Output:
  output/certin-annexure-a-report.docx  (last assembled: YYYY-MM-DD HH:MM)

Next:
  Run  /redink-build  to generate the 6 pending findings.
  Run  /redink-rebuild <id>  to refresh a specific finding.
```

## What to compute

- Read `framework.yaml`. Resolve active framework + its implementation status.
- Compare folders under `poc/web/` and `poc/server/` against files in `jsons/` (match by slug).
- Count `<...>` placeholders in `brand-guidelines.md` and report.
- If `output/qa-report.md` exists, parse the issue count from its first heading.
- If the framework's output file (`output/<framework>-report.docx` or `.json`) exists, show its mtime.

Do not run any validators. Do not write any files.
