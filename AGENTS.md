# AGENTS.md — instructions for any AI coding agent

This file is the agent-agnostic counterpart to [CLAUDE.md](CLAUDE.md). It tells any AI coding agent (Codex, Cursor, Gemini CLI, Aider, Kimi, Claude Code, etc.) how to drive `redink`'s report-generation pipeline.

> **Claude Code users**: you can ignore this file — Claude Code reads `CLAUDE.md` + `.claude/agents/` + `.claude/commands/` directly and dispatches sub-agents. AGENTS.md exists so the same workflow runs on agents that don't have sub-agent spawning.

---

## What you're doing

A penetration tester has finished the exploitation phase of an engagement. They've left you a folder of PoC screenshots and configuration files. Your job is to turn that into a compliance-grade report.

You'll do this by:

1. Reading the engagement context (framework, scope, firm details, narrative summary)
2. For each PoC folder, composing one validated finding entry (with verified CWE / CVE / CVSS / EPSS)
3. Running the Python assembler to render everything into a docx (or JSON for OWASP OPTRS)

You are an external auditor. Write terse, present-tense, third-person, factual prose. No hedge fluff, no LLM tells, no marketing copy.

---

## Inputs you read (in this order)

| File | What it gives you |
|---|---|
| [`framework.yaml`](framework.yaml) | The active compliance framework (one of 17 presets) |
| [`frameworks/<active>/manifest.yaml`](frameworks/) | Section defaults, metadata, hard rules, official sources |
| [`report-recipe.yaml`](report-recipe.yaml) | Which of the 28 sections to include this engagement (overrides the framework default) |
| [`sections/<id>/section.md`](sections/) | Per-section template + frontmatter for the enabled sections |
| [`sections/14-per-finding-details/schema.json`](sections/14-per-finding-details/schema.json) | Universal per-finding schema |
| [`sections/14-per-finding-details/EXAMPLE.json`](sections/14-per-finding-details/EXAMPLE.json) | A sample populated finding |
| [`brand-guidelines.md`](brand-guidelines.md) | Firm name, team, contact, methodology, tools, standards |
| [`targets.yaml`](targets.yaml) | Engagement scopes — hosts, IPs, services |
| [`engagement-summary.md`](engagement-summary.md) | Three narrative sections (Overview · Findings · Key Observations) |
| `poc/web/<NN_FolderName>/` | Web-scope evidence — folder name becomes the vulnerability title |
| `poc/server/<NN_FolderName>/` | Network/server-scope evidence |
| `scans/*` (optional) | Nessus / Burp / nmap output for cross-reference |

If `brand-guidelines.md`, `targets.yaml`, or `engagement-summary.md` still contain `<...>` placeholders, stop and tell the user what to fill — do not generate a partial report.

## Outputs you write

| Path | What |
|---|---|
| `jsons/NNN_<slug>.json` | One per-finding entry per PoC folder, conforming to the universal schema |
| `output/<framework>-report.docx` | Final assembled report (or `.json` for OWASP OPTRS) |
| `output/qa-report.md` | Self-audit log of citation re-validations |

---

## Universal hard rules — apply for every framework

These are non-negotiable. The recipient (a compliance evaluator) verifies them independently after submission. Get any of these wrong and the entry is rejected.

### Rule 1 — Preserve folder names exactly

The PoC folder name (minus the `NN_` prefix) is the vulnerability title. Preserve typos, trailing spaces, mixed case. Do not rewrite or clean up.

### Rule 2 — CWE verified at MITRE

For every CWE you cite, fetch `https://cwe.mitre.org/data/definitions/<n>.html`. Read the **Vulnerability Mapping Notes → Usage** value verbatim. Only `ALLOWED` or `ALLOWED-WITH-REVIEW` are acceptable.

**Known-bad CWE list (re-verify at MITRE before submission — list can change):**

- **PROHIBITED — never cite:** `CWE-1187`
- **DISCOURAGED — replace with a more specific child:** `CWE-200`, `CWE-269`, `CWE-284`, `CWE-285`, `CWE-287`, `CWE-693`
- **Category pages — not for vulnerability mapping:** `CWE-254`, `CWE-264`, `CWE-388`

If your candidate CWE is in any of these lists, walk MITRE's Children / CanFollow relationships and pick a more specific child. Read each candidate's Description + Vulnerability Mapping Notes before settling.

In the entry's `cwe_cve_audit` field, include the exact-quote Usage value (e.g., `"Usage: ALLOWED"`).

### Rule 3 — CVE verified at NVD

For every CVE you cite, fetch `https://nvd.nist.gov/vuln/detail/CVE-YYYY-NNNNN`. Confirm the affected version range matches the target version. Record the exact-quote version-range string in `cwe_cve_audit`.

If the target version is explicitly patched/unaffected in the NVD record, do not cite that CVE — find the right one.

### Rule 4 — CVSS v3.1 per FIRST.org

Use the metric values at `https://www.first.org/cvss/v3.1/specification-document`. Show per-metric reasoning + ISC / Impact / Exploitability / Base math in `cvss_audit`.

Don't copy NVD's score blindly — re-derive. If you disagree with NVD, document why.

### Rule 5 — EPSS lookup per CVE

For every CVE, fetch `https://api.first.org/data/v1/epss?cve=CVE-YYYY-NNNNN`. Format: `EPSS X.YY% (lookup YYYY-MM-DD)`. CWE-only entries: `EPSS N/A`. If multiple CVEs, report the highest EPSS.

### Rule 6 — Preserve image paths

Copy paths character-for-character from disk. Never normalise spaces, never re-encode.

### Rule 7 — CVE required for outdated-component findings

If the finding is "outdated library / component / version with known vulnerabilities," at least one verified CVE must be cited.

**Enforcement** — after writing the entry, do a self-audit pass: re-fetch each cited source (CWE, CVE, EPSS) from a clean shell and string-compare against the audit-trail excerpts you wrote. Mismatches mean you fabricated or drifted; fix the entry before submission.

---

## Step-by-step workflow

### Step 1 — Resolve the active framework + recipe

1. Read `framework.yaml`. Note the active framework name.
2. Load `frameworks/<active>/manifest.yaml`. Note `sections`, `finding_id_format`, `hard_rules`, `explicitly_excluded_sections` (if present).
3. Read `report-recipe.yaml`. The enabled sections (in this file's order) are what gets rendered.
4. If `report-recipe.yaml` is missing, copy the framework's `sections` array as the default recipe and ask the user if they want to customise (otherwise proceed).

### Step 2 — Read everything else

- `brand-guidelines.md` — firm details
- `targets.yaml` — engagement scope
- `engagement-summary.md` — exec-summary narratives
- `sections/<id>/section.md` for each enabled section — frontmatter tells you what inputs each needs
- `sections/14-per-finding-details/schema.json` + `EXAMPLE.json` — finding shape + tone calibration
- `poc/web/*/` and `poc/server/*/` — list every folder, list every image inside
- `scans/*` if present — optional cross-reference

If any `<...>` placeholders remain in `brand-guidelines.md`, `targets.yaml`, or `engagement-summary.md`, stop and tell the user.

### Step 3 — Ask 3–5 clarifying questions

Only the questions a senior pentester would actually ask. Be specific. Quote folder names exactly as they appear. Examples:

- "I see `poc/server/02_LDAP_Anonymous_Bind` and `poc/server/04_LDAP_Anon`. Same finding or two distinct ones?"
- "`poc/web/05_SQLi_login/` has 8 screenshots but no DB-extract evidence. Did SQLi succeed (Critical) or only confirmed via error-based detection (High)?"
- "`scans/nessus.html` flags CVE-2024-1086 on the host, but I see no matching folder. Skip it, or draft a finding from the Nessus data alone?"

Do NOT ask things you can answer by reading the input files yourself. Wait for answers before proceeding.

### Step 4 — Assign finding IDs

Order findings by severity (Critical → Informational), then scope (Network → Web), then alphabetical by folder name. Assign IDs using the format from `frameworks/<active>/manifest.yaml#finding_id_format` (e.g. `001`, `FINDING-001`, `F-001`, `CHK-001`, `PCI-001`).

### Step 5 — Write each finding

For each PoC folder, produce one `jsons/<id>_<slug>.json` file conforming to the universal schema. Per-field guidance:

- `s_no` / `id` / `finding_id` — assigned in step 4
- `name_of_vulnerability` / `title` — verbatim folder name (strip the `NN_` prefix only)
- `severity` — from CVSS-derived rubric in `brand-guidelines.md §8` (or framework override; IRAP omits this entirely)
- `vulnerable_location` — `"<host> @ <ip> — <service description>"` (pull host/IP from `targets.yaml`)
- `vulnerable_path_port_url` — exact URL/port/path
- `vulnerable_parameter` — HTTP param / form field / CLI arg / config key / `null`
- `cve_cwe` — comma-separated `CWE-N, CVE-YYYY-NNNNN`, validated values only
- `cvss_epss_score` — `"CVSS v3.1 Base X.Y (vector) — Severity; EPSS X.YY% (lookup YYYY-MM-DD)"`
- `description` — ≤ 80 words. What weakness, where, worst-case impact.
- `poc_intro` — optional, ≤ 40 words; `null` if step 1 is self-explanatory
- `poc_steps` — array of `{step_number, caption, image_path}`; caption ≤ 30 words
- `recommendations` — 2–4 actionable bullets ≤ 25 words each
- `references` — CWE link + NVD link + vendor advisory + EPSS link, newline-separated
- `additional_observations` — optional chain notes, or `null`
- `cwe_cve_audit` — one sentence per cited source with the exact-quote excerpt from your fetch
- `cvss_audit` — per-metric reasoning + ISC/Impact/Exploitability/Base math

Validate against the schema before writing. No empty strings — use `null` (where the schema allows) or `"N/A"` / `"None"` for required-but-inapplicable text.

### Step 6 — Self-audit pass (adversarial)

After every JSON is written, do another pass: for each entry, re-fetch CWE / CVE / EPSS from clean URLs and string-compare against `cwe_cve_audit`. If anything drifted (you wrote `ALLOWED` but MITRE actually says `DISCOURAGED`; you wrote `EPSS 12.3%` but the API now returns `94.5%`), fix the entry.

Write a self-audit log to `output/qa-report.md` listing every re-validation + any hard issues + any advisory issues.

### Step 7 — Run the assembler

```bash
python3 scripts/assemble_docx.py
```

The Python assembler (no LLM needed for this step):

- Reads `framework.yaml` + `report-recipe.yaml`
- Iterates the enabled sections in recipe order
- Reads each `sections/<id>/section.md` template
- Pulls data from `brand-guidelines.md`, `targets.yaml`, `engagement-summary.md`, `jsons/*.json`
- Renders to `output/<framework>-report.docx` (or `.json` for OWASP OPTRS)
- Embeds screenshots from PoC folders

Requires `python-docx` + `pyyaml`:

```bash
pip install python-docx pyyaml
```

### Step 8 — Final report check

Open `output/<framework>-report.docx`. Verify:

- Every enabled section is present and populated
- Every finding has its screenshots embedded
- The source-audit footer is visible on every finding (small grey italic text)
- No `<...>` placeholders survived

If any blank fields or `<...>` placeholders appear in the rendered docx, the human auditor signs off — not you.

---

## What to never write

- **Process meta** — caps, rules, internal categories, "I'll analyze", "Let me walk through"
- **Hedging** — "might", "could potentially", "may possibly". State what is.
- **LLM tells** — "Here is a comprehensive...", "In summary, the vulnerability..."
- **Marketing language** — "robust", "comprehensive", "cutting-edge", "leverage", "synergy"
- **Vendor blame** — stick to the weakness, not who's at fault

## Tone reference

**Bad:** "It appears that the application might be vulnerable to a potential SQL injection issue which could possibly allow attackers to leverage the database in malicious ways."

**Good:** "The login form's `username` parameter is concatenated into a SQL query without parameterization. Authenticated database read is possible via UNION-based extraction (see PoC step 3)."

---

## Interactive section picker (no LLM needed)

If the user wants to customise which sections to include, run:

```bash
python3 scripts/recipe.py
```

This is a pure Python interactive picker — walks every section, asks Y/N, writes `report-recipe.yaml`. No LLM involvement needed.

Claude Code users can also use the `/redink-recipe` slash command, which is the LLM-mediated equivalent.

---

## Repository layout (quick reference)

```
sections/<id>/section.md     — 28 modular section templates
frameworks/<name>/manifest.yaml — 17 framework presets (section recipes)
.claude/                     — Claude Code-specific orchestration (ignore on other agents)
scripts/assemble_docx.py     — Python assembler (cross-agent)
scripts/recipe.py            — Python interactive picker (cross-agent)
brand-guidelines.md          — firm details
targets.yaml                 — engagement scope
engagement-summary.md        — exec summary narrative
framework.yaml               — active framework
report-recipe.yaml           — active section selection
poc/{web,server}/            — drop PoC folders here
jsons/                       — generated per-finding entries
output/                      — final report + qa-report.md
```

See [README.md](README.md) for the human-readable user flow, [CLAUDE.md](CLAUDE.md) for the Claude-Code-specific version of these instructions, and [DISCLAIMER.md](DISCLAIMER.md) for responsible-use framing.
