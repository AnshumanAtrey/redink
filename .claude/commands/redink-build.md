---
description: Generate a full compliance report from poc/ folders, brand-guidelines.md, targets.yaml, and framework.yaml.
argument-hint: "[--skip-validation] [--no-docx] [--framework <name>]"
---

# /redink-build — generate the active framework's report

You are running the full pipeline. Follow these steps **in order**. Do not skip steps. Do not improvise.

## Step 1 — Resolve the active framework

Read `framework.yaml`. Resolve the active framework name. If `--framework <name>` was passed as an argument, that overrides the file.

Confirm `frameworks/<active>/` exists and contains:

- `schema.json`
- `prompt.md`
- (optionally) `EXAMPLE.json` and `README.md`

If the active framework is in the "skeleton" or "roadmap" status, **warn the user explicitly**: the schema may be incomplete and PRs are welcome. Continue if the user accepts.

## Step 2 — Read inputs

Read every file:

1. `frameworks/<active>/README.md` — framework status, official sources
2. `frameworks/<active>/schema.json` — the per-entry schema
3. `frameworks/<active>/prompt.md` — framework-specific instructions
4. `frameworks/<active>/EXAMPLE.json` (if present) — sample populated entry
5. `brand-guidelines.md` — firm details, team, methodology
6. `targets.yaml` — engagement scopes
7. `CLAUDE.md` — house rules (universal)

Walk `poc/web/` and `poc/server/`. List every folder. For each, list every image file inside.

Read any scan data present:

- `scans/nessus.html`, `scans/burp.xml`, `scans/nmap.txt`

## Step 3 — Refuse to run if inputs are incomplete

Stop and tell the user what to fix if ANY of these are true:

- `framework.yaml` resolves to a value not present under `frameworks/`
- `brand-guidelines.md` still contains `<...>` placeholders in required fields
- `targets.yaml` still contains `<...>` placeholders
- `poc/web/` AND `poc/server/` are both empty
- Any PoC folder has no image files
- Folder names contain control characters or characters that will break docx

When refusing, list every issue. Do not generate a partial report.

## Step 4 — Ask 3–5 clarifying questions

Only the questions a senior pentester would actually ask. Be specific. Quote folder names exactly as they appear. Examples:

- "I see `poc/server/02_LDAP_Anonymous_Bind` and `poc/server/04_LDAP_Anon`. Same finding or two distinct ones?"
- "`poc/web/05_SQLi_login/` has 8 screenshots but no DB-extract evidence. Did SQLi succeed (Critical) or was it only confirmed via error-based detection (High)?"
- "`scans/nessus.html` flags CVE-2024-1086 on the host, but I see no matching folder under `poc/server/`. Skip it, or draft a finding from the Nessus data alone?"

Do not ask questions you can answer by reading `brand-guidelines.md`, `targets.yaml`, or the active framework's prompt.

Wait for answers before proceeding.

## Step 5 — Assign serial numbers / finding IDs

The ID format depends on the active framework's schema:

- CERT-In Annexure-A → `s_no` as `001`, `002`, ...
- OWASP OPTRS → `id` as `FINDING-001`, `FINDING-002`, ...
- CMMC → `finding_id` as `F-001`, `F-002`, ...
- NCSC CHECK → `finding_ref` as `CHK-001`, ...
- PCI DSS ROC → `finding_ref` as `PCI-001`, ...

Order findings by severity (Critical → Informational), then scope (Network → Web), then alphabetical by folder name.

## Step 6 — Generate findings in parallel

For each folder under `poc/web/` and `poc/server/`, spawn a `finding-writer` subagent. Pass it:

- `folder_path`: relative path
- `id`: the assigned identifier (format depends on framework)
- `scope`: matching entry from `targets.yaml`
- `framework`: the active framework name
- `scan_excerpt`: any relevant section from `scans/*` (optional)

`finding-writer` reads `frameworks/<active>/prompt.md` to shape the output, then delegates to `cwe-validator`, `cve-validator`, `cvss-calculator`, `epss-lookup` in parallel.

Cap parallelism at 5 findings at a time.

## Step 7 — Adversarial QA pass

After all JSONs are written, spawn `report-reviewer` once. It:

- Independently re-fetches every cited CWE/CVE/EPSS
- Compares against each entry's audit-trail excerpt
- Flags any drift in `output/qa-report.md`

If `qa-report.md` lists any hard issues, fix each and re-run until clean.

## Step 8 — Assemble the output

Run:

```bash
python3 scripts/assemble_docx.py
```

The assembler reads `framework.yaml` to determine the output format:

- Most frameworks → `output/<framework>-report.docx`
- OWASP OPTRS → `output/owasp-optrs-report.json`

If `python-docx` is not installed (and the framework needs docx), instruct the user:

```bash
pip install python-docx pyyaml
```

## Step 9 — Summary

Print a one-screen summary:

```
redink report built.

  Framework: certin-annexure-a
  Findings written: 23
    Critical: 4
    High: 9
    Medium: 8
    Low: 2
  Validation: CWE 23/23 · CVE 18/18 · CVSS 23/23 · EPSS 18/18
  Output: output/certin-annexure-a-report.docx
  QA report: output/qa-report.md (clean)

Next:
  - Open the output and review
  - Re-run one finding:  /redink-rebuild 014
  - Check status:        /redink-status
  - Switch framework:    edit framework.yaml + re-run
```

## Flags

- `--skip-validation`: skip the adversarial QA pass (for fast iteration; **never use for final submission**)
- `--no-docx`: stop after writing JSONs; skip assembly
- `--framework <name>`: override `framework.yaml` for this run
