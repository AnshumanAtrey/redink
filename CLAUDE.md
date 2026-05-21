# redink — house rules (Claude Code)

> Agent-agnostic equivalent for Codex / Cursor / Gemini / Aider / Kimi: see [AGENTS.md](AGENTS.md).

You are writing vulnerability entries that will be read by a compliance evaluator. The specific evaluator depends on the active framework (CERT-In coordinator, C3PAO assessor, CHECK Team Leader, PCI QSA, IRAP assessor, PASSI auditeur, ANSSI evaluator, KISA assessor, BSI auditor, NCA ECC reviewer, etc.).

Write like a senior penetration tester documenting findings for an external auditor — terse, present-tense, third-person, factual. No process narration. No hedge fluff. No internal coordination language.

## Architecture

redink is **modular**. Three layers compose every report:

1. **Sections** (`sections/<id>/section.md`) — 28 universal report blocks (cover page, exec summary, controls matrix, signoff, etc.). Each is a self-contained template.
2. **Frameworks** (`frameworks/<name>/manifest.yaml`) — 17 presets bundling sections in framework-appropriate order. Each preset is just a list of section IDs.
3. **Recipe** (`report-recipe.yaml`) — per-engagement override. Built by `/redink-recipe`. Lists which sections to actually render for THIS report.

The universal validators (CWE / CVE / CVSS / EPSS) run identically for every framework. Only the section composition + per-finding field shape differs.

## Inputs you read

| File | Purpose |
|---|---|
| `framework.yaml` | Active framework |
| `report-recipe.yaml` | Active section selection (override of framework default) |
| `frameworks/<active>/manifest.yaml` | Section defaults + metadata + official sources |
| `sections/<id>/section.md` | Section template + frontmatter (inputs, frameworks using) |
| `sections/14-per-finding-details/schema.json` | Universal per-finding schema |
| `brand-guidelines.md` | Firm name, team, contact, methodology, tools, standards |
| `targets.yaml` | Engagement scopes (hosts, IPs, services) |
| `engagement-summary.md` | Three exec-summary narratives (Overview · Findings · Key Observations) |
| `poc/web/<NN_FolderName>/` | Web-scope evidence — folder name is the vulnerability title |
| `poc/server/<NN_FolderName>/` | Network-scope evidence — same convention |
| `scans/*` | (Optional) Nessus/Burp/nmap output for cross-reference |

## Outputs you write

| Path | Format |
|---|---|
| `jsons/NNN_<slug>.json` | One per-finding entry conforming to universal schema |
| `output/<framework>-report.docx` | Final assembled report (docx framework) |
| `output/owasp-optrs-report.json` | OWASP OPTRS machine-readable bundle |
| `output/qa-report.md` | Adversarial QA pass results |

## Universal hard rules (apply to every framework)

These apply regardless of which framework is selected — every supported framework defers to MITRE/NVD/FIRST.org as the source of truth.

1. **Preserve folder names exactly.** Typos, trailing spaces, mixed case kept as-is. The folder name becomes the vulnerability-title field (whatever the framework calls it).

2. **CWE verified at MITRE.** Fetch `https://cwe.mitre.org/data/definitions/<n>.html`. Read the **Vulnerability Mapping Notes → Usage** value. Only `ALLOWED` and `ALLOWED-WITH-REVIEW` may be cited.

   As of this plugin's last update, the following CWEs WILL be rejected during evaluator re-checks. **Re-verify at MITRE before submission** — this list can change.
   - **PROHIBITED — never cite:** `CWE-1187`
   - **DISCOURAGED — replace with a more specific child:** `CWE-200`, `CWE-269`, `CWE-284`, `CWE-285`, `CWE-287`, `CWE-693`
   - **Category pages — not for vulnerability mapping:** `CWE-254`, `CWE-264`, `CWE-388`

   In the audit-trail field, include the exact-quote Usage value.

3. **CVE verified at NVD.** Fetch `https://nvd.nist.gov/vuln/detail/CVE-YYYY-NNNNN`. Confirm the affected version range matches the target. Record the exact-quote version-range string.

4. **CVSS computed per FIRST.org spec.** Use the metric values at `https://www.first.org/cvss/v3.1/specification-document`. Show per-metric reasoning + ISC/Impact/Exploitability/Base math.

5. **EPSS looked up per CVE.** Any entry with a CVE must include EPSS from `https://api.first.org/data/v1/epss?cve=CVE-YYYY-NNNNN`. Format: `EPSS X.YY% (lookup YYYY-MM-DD)`.

6. **Image paths preserved.** Copy the exact path string. Never normalize.

7. **CVE required for outdated-component class.** Outdated-library/version findings MUST carry ≥ 1 verified CVE.

**Verification enforcement:** Every CWE/CVE/EPSS will be independently re-fetched by `report-reviewer` (and by the human evaluator) from a clean shell and compared against audit-trail excerpts.

## Framework-specific rules

Each framework's `manifest.yaml` includes `hard_rules` and (optionally) `explicitly_excluded_sections` arrays. Read the manifest before generating entries.

A few examples of framework-specific exclusions:

- **IRAP** explicitly excludes section 10 (risk-rating) — assessors identify weaknesses, consumer assesses risk
- **CMMC** uses Met/Not Met/N-A status per 32 CFR §170.24 (not Critical/High/Medium/Low)
- **PCI DSS** uses In Place/Not In Place/N-A/Not Tested/Compensating Control
- **PASSI** uses two-axis classification (impact × exploitation difficulty)

## Workflow

When the user runs `/redink-build`:

1. Read `framework.yaml` → active framework name
2. Load `frameworks/<active>/manifest.yaml` → section defaults + metadata
3. Read `report-recipe.yaml` → user's per-engagement selection (overrides framework default)
4. Read `brand-guidelines.md`, `targets.yaml`, `engagement-summary.md`. If any contain `<...>` placeholders, stop and tell the user what to fill.
5. Walk `poc/web/` and `poc/server/`. Cross-check with `scans/*` if present.
6. Ask 3–5 clarifying questions — only what a senior pentester would ask (suspected duplicates, severity disagreements, missing CVE mappings).
7. Spawn `finding-writer` per folder in parallel (cap at 5 concurrent). Each writer delegates to `cwe-validator`, `cve-validator`, `cvss-calculator`, `epss-lookup` in parallel.
8. After every JSON written, spawn `report-reviewer` for adversarial pass.
9. Run `scripts/assemble_docx.py`. It reads the recipe, iterates enabled sections in order, renders each.

## What to never write in an entry

- Process meta — caps, rules, internal categories, "Claude", "the AI", "the agent"
- Hedging — "might", "could potentially", "may possibly"
- LLM tells — "I'll analyze...", "Let me walk through...", "Here is a comprehensive..."
- Marketing — "robust", "comprehensive", "cutting-edge", "leverage", "synergy"
- Vendor blame — stick to the weakness, not who's at fault

## Tone reference

**Bad:** "It appears that the application might be vulnerable to a potential SQL injection issue which could possibly allow attackers to leverage the database in malicious ways."

**Good:** "The login form's `username` parameter is concatenated into a SQL query without parameterization. Authenticated database read is possible via UNION-based extraction (see PoC step 3)."
