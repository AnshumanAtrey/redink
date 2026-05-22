<!-- markdownlint-disable MD033 MD041 -->
<div align="center">

<img src="assets/red-ink.png" alt="redink — wax-sealed pentest report" width="900" />

# redink

**Compose pentest reports from 28 modular sections for 17+ compliance frameworks.**
An open-source Claude Code pipeline. Drop PoC screenshots, pick your sections, get a validated submission-ready report.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-2.1%2B-purple.svg)](https://code.claude.com)
[![Status](https://img.shields.io/badge/Status-Alpha-orange.svg)]()

[Quick start](#quick-start) · [Supported frameworks](#supported-frameworks) · [Sections](#section-library) · [User flow](#user-flow) · [Disclaimer](DISCLAIMER.md) · [Security](SECURITY.md)

</div>

---

## What `redink` does

Penetration tests produce findings. Every compliance framework demands those findings be wrapped in a report with specific sections, specific formatting, and validated CWE/CVE/CVSS/EPSS citations.

`redink` is a **modular pipeline** that lets you compose that report from 28 reusable section types — picking exactly the pages your framework requires (or your firm prefers). The validators (CWE at MITRE, CVE at NVD, CVSS per FIRST.org, EPSS live) run identically for every framework. Only the report wrapper differs.

## Why redink

### The time math

A 300-finding pentest report — typical for mid-size enterprise audits and most national-empanelment testbeds — has roughly this **manual workload per finding**:

| Per-finding task | Manual time |
|---|---|
| Look up CWE at MITRE; verify Usage = ALLOWED / ALLOWED-WITH-REVIEW | ~3 min |
| Look up CVE at NVD; pull exact-quote affected-version range | ~5 min |
| Compute CVSS v3.1 base score from vector (per FIRST.org spec) | ~3 min |
| Look up EPSS probability at `api.first.org/data/v1/epss` | ~1 min |
| Write description (≤ 80 words), recommendations, references | ~5–10 min |
| Format into framework template — fields, embedded screenshots, captions | ~3–5 min |
| **Per finding total** | **~20–30 min** |

For **300 findings, that's ~125 hours** of pure per-finding citation + formatting work. Add Part 1 narrative + manpower/standards/tools tables + aggregated-findings table + QA + cross-reference fix passes and you're at **~140–160 hours per engagement.**

Most firms throw 3–5 senior auditors at that load for the 5-day delivery window. Two days in, fatigue sets in. By day 4, citation typos and wrong version ranges start slipping through.

**`redink`'s expected workload — same 300-finding engagement:**

| Phase | Wall-clock time |
|---|---|
| One-time setup: fill `brand-guidelines.md` + `targets.yaml` + `engagement-summary.md` | ~1–2 h |
| `/redink-recipe` — 28 Y/N section questions | ~5–10 min |
| `/redink-build` — 20 concurrent sub-agents hitting MITRE / NVD / FIRST.org in parallel | **~1 h** for 300 findings |
| Adversarial QA pass (`report-reviewer` re-fetches every citation independently) | ~30–60 min |
| Human review of assembled output (senior auditor still signs off) | ~3–5 h |
| Final docx polish + firm template integration | ~1–2 h |
| **Total** | **~7–10 hours** |

> **~150 hours → ~8 hours per engagement. ~20× speedup. ~95% time reduction.**
>
> Numbers are *projected* from per-finding manual cost benchmarks, not measured at scale — but the per-task estimates are conservative (try timing your team's own next MITRE-Usage check + NVD version-range lookup + CVSS computation, then multiply by 300).

### The pentester psychology

Pentesters and security auditors have a specific kind of brain. The same creative, sideways-thinking, break-assumptions mindset that finds privilege escalation chains and unexpected IDORs is what makes them valuable in the first place.

**That brain is the worst possible tool for hours of MITRE lookups, NVD version-string copy-pasting, and Word table formatting.** It's like making a chef wash dishes for six hours. They *can* do it, but:

- Every minute spent on lookups is a minute their creative engine isn't running
- After 4-5 hours of repetitive citation work, fatigue starts eating accuracy
- The "I should pivot and try X" instinct goes quiet under manual-task overhead
- The deepest vulnerabilities — chained exploits, business-logic flaws, post-exploitation creativity — are exactly what dies first when the analyst is mentally burned out

`redink` takes the busywork. Pentesters get to spend their hours on the parts that actually need their brain:

- Exploitation chains
- Unexpected attack paths
- "What if I combine these two findings?" moments
- Real Business Impact Analysis (not boilerplate)
- The next engagement (because this one's report is done by lunch on day 2 instead of day 5)

Auditing firms have been making their best technical people do paperwork for as long as compliance reports have existed. `redink` lets you stop.

### The error problem (and why automation wins here)

Manual reports have measurable error categories — every senior auditor has seen each of these in their team's draft reports:

| Error category | What happens manually | What `redink` does |
|---|---|---|
| **CWE Usage mismatches** | Cites `CWE-287` as ALLOWED when MITRE flags it DISCOURAGED → coordinator rejects | `cwe-validator` fetches MITRE before acceptance; the known-bad list (CWE-200, CWE-269, CWE-284, CWE-285, CWE-287, CWE-693, CWE-1187) is rejected automatically |
| **CVE version-range errors** | Claims target version 1.0.2u is affected by a CVE patched in 1.0.2t → coordinator rejects | `cve-validator` fetches NVD's exact affected-range; stores the exact-quote excerpt for re-verification |
| **CVSS arithmetic mistakes** | Vector says `AC:H` but the math was done as `AC:L` | `cvss-calculator` shows ISC / Impact / Exploitability / Base math for every finding |
| **Stale EPSS** | Looked up two weeks ago; current probability is materially different | `epss-lookup` fetches live per finding, records lookup date; QA pass demands re-fetch if > 7 days old |
| **Blank fields** | Cells left empty under deadline pressure → automatic rejection by frameworks that enforce a "no-blanks" rule (CMMC C3PAO scorecards, PCI DSS ROC, CHECK reports, CERT-In) | Assembler refuses to render the docx if mandatory fields are empty; `/redink-build` won't start with `<...>` placeholders in input files |
| **Inconsistent severity** | Same vulnerability rated High by one team member, Medium by another | Single deterministic CVSS-derived severity rubric applied across all findings |
| **Citation fabrication** (LLM-era) | Plausible-looking but invented CVE numbers or MITRE descriptions | Every entry's `cwe_cve_audit` field stores exact-quote excerpts from MITRE / NVD / FIRST.org; `report-reviewer` independently re-fetches and string-compares before submission |

**Rule enforcement runs at three layers, not one:**

1. **Validator agents** — reject invalid citations at write time
2. **Assembler** — refuses to render the docx if mandatory fields are empty
3. **`report-reviewer`** — adversarial re-fetch pass; flags any drift between draft and submission

No single layer is the safety mechanism. The post-write re-validation is what catches LLM hallucinations the writer agents didn't notice. The audit-trail field on every finding lets the evaluator (or you, on review) re-fetch the canonical source and verify independently — the workflow CMMC C3PAOs, CHECK Team Leaders, PASSI auditeurs, PCI QSAs, IRAP assessors, BSI auditors, and CERT-In coordinators all run in parallel during their own re-checks.

The result: a report where **every cited reference is traceable, every score is showable, every required field is populated**, and no fatigue-driven typos sneak through to submission.

## Who redink is built for

`redink` is built for every team that produces pentest reports — whether the driver is a **regulatory mandate** (CMMC, SOC 2 attestation, ISO 27001, NIS2, DORA, RBI, MAS-TRMG, SAMA CSF, KISA ISMS-P, CERT-In, etc.) or **commercial trust** (customer due-diligence, M&A security DD, cyber-insurance underwriting, vendor-risk questionnaires, internal red-team exercises, bug-bounty programme rollups). The validator chain and section composition are identical; only the framework wrapper changes per engagement.

| Segment | Examples (regulated + private drivers, globally) | Reports / firm / year | Worldwide footprint |
|---|---|---|---|
| **Big 4 / global consultancies** | Deloitte, EY, KPMG, PwC — cyber + audit divisions running both regulated (CMMC C3PAO assessments, ISO 27001 audits, SOC 2 attestations, CHECK engagements, PCI ROC) AND private (customer DD, M&A, vendor-risk, internal-audit) work across 50+ country offices each | 500–2,000 | 4 firms × ~50 country offices = **~200 cyber business units** |
| **Pure-play cyber boutiques** | Mandiant (Google Cloud), Bishop Fox, NCC Group, NetSPI, Coalfire, IOActive, Trustwave, Synack, Synopsys SIG, F-Secure / WithSecure, Praetorian, Kudelski Security, Aon Cyber Solutions, GuidePoint Security; SISA, Aujas, Kratikal, Astra Security | 100–500 | **~1,000+ pure-play firms** globally |
| **IT-services cyber divisions** | Accenture Security, Capgemini, Atos, NTT Security, DXC, Cognizant Security, Fujitsu Cyber; TCS Cyber, Infosys, Wipro, HCL CyberSecurity, Tech Mahindra | 200–800 | **~50 major firms** with full cyber-services arms |
| **Government-accredited audit firms** (also do private work — accreditation is a credential, not a scope limit) | NCSC CHECK Green-Light (UK) · C3PAOs under Cyber AB (US) · CREST member firms (intl) · PASSI auditeurs (FR) · BSI auditors (DE) · IRAP assessors (AU) · KISA-registered (KR) · ISMAP-listed (JP) · CSA-approved (SG) · NESA-accredited (UAE) · NCA-licensed CSPs via Haseen (KSA) · FSTEC-licensed (RU); CERT-In empanelled (IN) | 50–300 | **~2,500+ firms** across the 17 schemes redink supports |
| **In-house red teams at regulated entities** | Banks (under FFIEC / FCA / BaFin / FINMA / MAS / OSFI / APRA / RBI / SAMA), insurers (NAIC / EIOPA / IRDAI), exchanges (SEC / FCA / FINMA / MAS / JFSA / NSE), critical-infrastructure operators under DORA / NIS2 / SOCI / KRITIS / CNI / CIKR / NCIIPC | 50–200 internal | **~5,000–10,000 regulated entities** with formal red-team functions |
| **In-house red teams at private enterprises** (customer-trust + internal drivers, no regulatory mandate) | Hyperscalers + SaaS (Google, Microsoft, AWS, Meta, Apple, Stripe, Cloudflare, Atlassian, Shopify, GitLab, Snowflake, Datadog, MongoDB) · fintech (Coinbase, Block, Klarna, Revolut, Wise, N26, Razorpay) · telcos (Vodafone, Orange, Deutsche Telekom, NTT, KDDI, Telstra, AT&T, Verizon) · defense primes (Lockheed Martin, Boeing, BAE Systems, Thales, Saab, Mitsubishi Heavy, Hanwha) · pharma (Pfizer, Roche, Novartis, AstraZeneca, GSK, J&J, Bayer) · retail (Walmart, Target, Carrefour, Tesco, IKEA, Ahold Delhaize) · energy (BP, Shell, TotalEnergies, Saudi Aramco, Equinor) — drives SOC 2 + ISO 27001 attestation, customer DD, M&A security, cyber-insurance, internal red-team exercises | 30–200 internal | **~3,000–5,000 private enterprises** with formal red-team functions |
| **Solo + small consultancies + bug-bounty practitioners** | Independent bug-bounty hunters (HackerOne / Bugcrowd / Synack / Intigriti / YesWeHack top-ranked), freelance pentesters, 2–5 person shops across every cyber hub (Tel Aviv, London, Berlin, Bengaluru, Seoul, Singapore, Sydney, São Paulo, Tokyo, Toronto, Amsterdam, Dubai, San Francisco, Boston) | 10–50 | **~100,000+ independent practitioners** worldwide |

**Global addressable market:** **~120,000+ organizations** producing compliance / customer-trust / internal pentest reports + the long tail of solo practitioners. Estimated **3–10 million pentest reports produced annually worldwide** across all segments combined.

The split between "regulated" and "private" rows above is descriptive, not architectural — most teams do both. A Big 4 cyber engagement might be a SOC 2 (private trust) one quarter and a CMMC C3PAO assessment (regulatory) the next. An in-house team at Stripe runs SOC 2 + PCI DSS + internal red-team continuously; a team at a German bank runs BaFin + NIS2 + customer-DD pentests in parallel. **redink serves every one of them** — same validator chain, same per-finding rigor, framework-appropriate skin per engagement.

## Supported frameworks

17 framework presets — each is a recipe under [`frameworks/<name>/manifest.yaml`](frameworks/). Pick one in [`framework.yaml`](framework.yaml).

Ordered roughly by the size of each market's empanelled / accredited tester pool — North America and Western Europe lead the global cyber consulting industry, and the table follows that gravity.

| # | Framework | Region | Audience |
|---|---|---|---|
| 1 | **CMMC Level 2/3 FAR** | 🇺🇸 USA | DoD contractors assessed by C3PAOs under the Cyber AB |
| 2 | **PCI DSS ROC v4.0** | 🌍 Global (card industry) | PCI SSC QSAs / ISAs |
| 3 | **NCSC CHECK** | 🇬🇧 UK | NCSC CHECK-accredited Green-Light testers (HMG, CNI) |
| 4 | **CREST CDPT** | 🇬🇧 UK / 🌍 Global | CREST-accredited member firms |
| 5 | **ANSSI PASSI** | 🇫🇷 France | ANSSI-qualified PASSI auditeurs (4 audit categories) |
| 6 | **BSI IT-Grundschutz** | 🇩🇪 Germany | BSI-certified auditors (BSIG / KRITIS operators) |
| 7 | **Switzerland NCSC / FINMA** | 🇨🇭 Switzerland | NCSC-aligned testers; FINMA for regulated banks |
| 8 | **Israel INCD ICDM 2.0** | 🇮🇱 Israel | INCD-listed assessors (banking, telecom, healthcare) |
| 9 | **UAE NESA / SIA IAS** | 🇦🇪 UAE | NESA-accredited assessors |
| 10 | **Saudi NCA ECC / CCC / OTCC** | 🇸🇦 Saudi Arabia | NCA-licensed Cybersecurity Service Providers |
| 11 | **IRAP** | 🇦🇺 Australia | ASD-registered IRAP assessors |
| 12 | **K-ISMS-P (KISA)** | 🇰🇷 South Korea | KISA-registered assessors (102 criteria) |
| 13 | **Japan ISMAP / NISC** | 🇯🇵 Japan | ISMAP-listed audit firms |
| 14 | **Singapore CSA CCoP 2.0** | 🇸🇬 Singapore | CSA-accredited CII assessors |
| 15 | **Russia FSTEC / FSB** | 🇷🇺 Russia | FSTEC-licensed assessors (КИИ / FZ-187) |
| 16 | **CERT-In** | 🇮🇳 India | CERT-In empanelled auditors |
| 17 | **OWASP OPTRS** (JSON) | 🌍 Open standard | Machine-readable consumers (CI/CD, SOAR) |

Every preset wires the **same** universal validators (CWE / CVE / CVSS / EPSS pinned to MITRE / NVD / FIRST.org). Frameworks differ only in the section list, per-finding field shape, severity rubric, and signing / submission requirements — all encoded in each `manifest.yaml`.

Don't see your framework? Compose your own recipe — see [§"Build your own recipe"](#build-your-own-recipe).

## Section library

The 28 universal sections live under [`sections/`](sections/). Each is a self-contained block the assembler can drop into any report.

| # | Section | Common in |
|---|---|---|
| 01 | Cover page | All frameworks |
| 02 | Document control / version history | CMMC, NCSC CHECK, PASSI, PCI DSS |
| 03 | Executive summary | All frameworks |
| 04 | Engagement scope statement | All frameworks |
| 05 | Out-of-scope statement | CHECK, CREST, PCI DSS, Singapore |
| 06 | Testing methodology | All frameworks |
| 07 | Standards & frameworks adopted | CERT-In, CHECK, PCI DSS, PASSI, BSI |
| 08 | Team roster / technical manpower | CERT-In, CHECK, PASSI, CMMC, PCI DSS |
| 09 | Tools, scripts & frameworks used | CERT-In, CHECK, CREST, PASSI |
| 10 | Risk-rating methodology | Most (excluded by IRAP) |
| 11 | Summary of findings (severity counts) | All frameworks |
| 12 | Key observations & critical risks | CERT-In, CHECK, PASSI, CREST |
| 13 | Aggregated findings table | CHECK §C-37e, CREST CDPT §10, PASSI, CERT-In |
| 14 | Per-finding details | All frameworks |
| 15 | Controls matrix | CMMC, IRAP, PCI DSS, ISO 27001, NESA, NCA ECC, K-ISMS-P, BSI |
| 16 | Compensating controls register | PCI DSS |
| 17 | POA&M (Plan of Action & Milestones) | CMMC |
| 18 | Threat landscape | BSI, INCD, NCA ECC, CMMC |
| 19 | Compliance status statement | PCI DSS, BSI, K-ISMS-P, NESA, NCA ECC |
| 20 | Remediation roadmap / priority matrix | CMMC, CHECK, CREST, PASSI, K-ISMS-P |
| 21 | Limitations & disclaimers | All frameworks |
| 22 | References / bibliography | All frameworks |
| 23 | Appendices (raw scan data) | CMMC, CHECK, CREST, PASSI, IRAP, PCI DSS |
| 24 | Glossary of terms | CMMC, PASSI, BSI |
| 25 | Acronyms & abbreviations | CMMC, PASSI, BSI |
| 26 | Signoff page | CHECK, PCI DSS, CMMC, PASSI, IRAP |
| 27 | Incident-reporting alignment | Switzerland 24h, Japan ACDA, EU NIS2 |
| 28 | Continuous monitoring evidence | K-ISMS-P (Q3 2026+), INCD ICDM 2.0 |

## Quick start

```bash
# 1. Clone
git clone https://github.com/AnshumanAtrey/redink.git
cd redink

# 2. Install as a Claude Code plugin
./install.sh

# 3. Pick your framework
$EDITOR framework.yaml          # 17 presets — pick one

# 4. Pick your sections interactively
claude
> /redink-recipe                # walks you through all 28 sections, asks Y/N
```

Then drop your PoCs, fill `brand-guidelines.md`, `targets.yaml`, and `engagement-summary.md`, and run `/redink-build`.

## User flow

### Step 1 — Drop PoC screenshots

Folder names become the vulnerability title verbatim. Typos, spaces, mixed case preserved.

```
poc/
├── web/
│   ├── 01_WordPress_Plugin_Unauth_RCE/
│   ├── 02_phpMyAdmin_Default_Credentials/
│   └── 03_Apache_Server_Status_Exposed/
└── server/
    ├── 01_Tomcat_HTTP_PUT_Method_RCE/
    ├── 02_FTP_Anonymous_Read_Enabled/
    └── 03_Outdated_OpenSSH_7.4/
```

See [`poc/EXAMPLE.md`](poc/EXAMPLE.md) for the naming conventions.

### Step 2 — Fill brand-guidelines.md

Firm name, team roster, methodology, tools, contact details. Framework-agnostic.

### Step 3 — Fill targets.yaml

The hosts you tested.

### Step 4 — Fill engagement-summary.md

Three short narrative sections: Overview · Summary of Findings · Key Observations & Critical Risks. Drives the executive-summary section of the assembled report.

### Step 5 — Pick a framework

```yaml
# framework.yaml
framework: owasp-optrs    # one of 17 presets — pick any
```

### Step 6 — Pick sections

```
/redink-recipe
```

Walks you through every section: "Section 01 — Cover Page. Default for certin: ENABLED. Include? [Y/n]". After 28 questions, saves your selection to [`report-recipe.yaml`](report-recipe.yaml).

You can hand-edit `report-recipe.yaml` instead if you prefer.

### Step 7 — Run

```
/redink-build
```

What happens:

1. Read `framework.yaml` + `report-recipe.yaml` + `brand-guidelines.md` + `targets.yaml` + `engagement-summary.md`
2. Walk `poc/web/` and `poc/server/`
3. Ask 3–5 clarifying questions
4. Spawn parallel sub-agents per finding:
   - `cwe-validator` → fetches MITRE, rejects PROHIBITED/DISCOURAGED CWEs
   - `cve-validator` → fetches NVD, confirms affected version range
   - `cvss-calculator` → applies FIRST.org v3.1 spec
   - `epss-lookup` → fetches `api.first.org/data/v1/epss`
   - `finding-writer` → composes the per-finding JSON
5. Adversarial QA pass — `report-reviewer` independently re-fetches every citation
6. Assemble — sections enabled in `report-recipe.yaml` render to `output/<framework>-report.docx`

### Step 8 — Review

- Open the output. Each finding has a source-audit footer with exact-quote MITRE/NVD/EPSS excerpts.
- Iterate one finding: `/redink-rebuild 015`
- Check status: `/redink-status`
- Switch framework: edit `framework.yaml` and re-run

## Performance & architecture

`redink` exists to exploit the fact that compliance-report citation work is **embarrassingly parallel** — every finding's CWE/CVE/CVSS/EPSS lookup is independent of every other finding's. Sequential lookup is the bottleneck a human team can't escape; parallel agent spawn can.

### Agent topology

```
                 /redink-build
                       │
        ┌──────────────┴───────────────────┐
        │                                  │
   finding-writer × 5 concurrent       report-reviewer (adversarial QA)
        │ (one per PoC folder)             │
        │                          (re-fetches every cited
        │                           CWE/CVE/EPSS independently)
   ┌────┼────────┬──────────┬─────────┐
   │    │        │          │         │
  cwe-  cve-   cvss-     epss-     finding-writer composes
  val.  val.   calc.     lookup    the final JSON entry
 (MITRE)(NVD) (FIRST.org)(FIRST.org)
```

At peak: **5 finding-writers × 4 validators = 20 concurrent sub-agents** simultaneously fetching MITRE, NVD, and FIRST.org. A 300-finding engagement runs in ~60 batches of parallel work instead of ~300 sequential lookups.

The 5-finding cap exists to avoid rate-limiting upstream sources. Higher caps are possible if you're OK with the API risk; lower caps if you want gentler load.

### Time complexity

| Mode | Complexity | n=300 findings |
|---|---|---|
| **Manual sequential** | `O(n × T_v)` where `T_v` ≈ 12 min/finding (CWE 3m + CVE 5m + CVSS 3m + EPSS 1m) | ~60 hours of pure citation work |
| **`redink` parallel** | `O(⌈n/5⌉ × T_v_parallel)` where `T_v_parallel` ≈ 45s (4 validators run concurrently) | ~60 batches × 45s ≈ **~45 minutes** |

The speedup compounds: the more findings you have, the bigger the per-finding parallelism win — because manual-team coordination overhead scales linearly while parallel agent spawn doesn't.

### What runs non-stop

Once you run `/redink-build`, the pipeline does not stop until every finding is written and every citation is re-verified. While you make coffee:

- Sub-agents fetch MITRE, parse Vulnerability Mapping Notes, store Usage values
- Sub-agents fetch NVD, parse affected-version strings, match against your target version
- Sub-agents compute CVSS v3.1 math per FIRST.org spec, show per-metric reasoning
- Sub-agents fetch live EPSS probabilities and store the lookup date
- `finding-writer` composes per-finding JSON conforming to the universal schema
- `report-reviewer` runs an adversarial second pass, independently re-fetching everything from a clean shell
- Assembler iterates enabled sections from `report-recipe.yaml`, renders cover → exec summary → tables → per-finding blocks → references

No coffee-break tradeoffs. No "I'll come back to this finding after lunch." The pipeline runs until done.

## Universal validation rules

These apply to **every** framework. They're enforced by the validator agents.

| Rule | Source |
|---|---|
| CWE must be `ALLOWED` or `ALLOWED-WITH-REVIEW` | [cwe.mitre.org](https://cwe.mitre.org) |
| CVE affected-version range must match the target | [nvd.nist.gov](https://nvd.nist.gov) |
| CVSS v3.1 metrics computed per spec, with math shown | [first.org/cvss/v3.1](https://www.first.org/cvss/v3.1/specification-document) |
| EPSS probability fetched per CVE on the lookup date | [api.first.org/data/v1/epss](https://api.first.org/data/v1/epss) |
| Folder names preserved exactly as the finding title | enforced by walker |

Known PROHIBITED / DISCOURAGED / Category CWE list (re-verify at MITRE before submission):

- **PROHIBITED — never cite:** `CWE-1187`
- **DISCOURAGED — replace with specific child:** `CWE-200`, `CWE-269`, `CWE-284`, `CWE-285`, `CWE-287`, `CWE-693`
- **Category pages — not for vuln mapping:** `CWE-254`, `CWE-264`, `CWE-388`

## Using redink with other AI coding agents

`redink` is built primarily as a Claude Code plugin (sub-agent spawning gives the biggest parallelism win). But the content layer — sections, framework manifests, schemas, Python assembler — is **agent-agnostic**.

To use redink with Codex, Cursor, Gemini CLI, Aider, Kimi, or any other AI coding agent that reads [`AGENTS.md`](AGENTS.md):

1. Clone the repo
2. The agent reads `AGENTS.md` automatically (most modern AI coding agents do)
3. Use the standalone Python tools instead of slash commands:
   - `python3 scripts/recipe.py` — interactive section picker (replaces `/redink-recipe`)
   - `python3 scripts/recipe.py --non-interactive` — accept all framework defaults
   - `python3 scripts/assemble_docx.py` — final assembly (same on every agent)
4. For the per-finding citation work (CWE / CVE / CVSS / EPSS lookups), the agent fetches MITRE / NVD / FIRST.org directly per the rules in `AGENTS.md` — same canonical sources every agent uses

| Capability | Claude Code | Codex / Cursor / Gemini / Aider / Kimi |
|---|---|---|
| Read CLAUDE.md / AGENTS.md | ✅ both | ✅ AGENTS.md |
| Slash commands (`/redink-build`, `/redink-recipe`, etc.) | ✅ native | ❌ N/A — use Python equivalents |
| Sub-agent fanout (20 concurrent validators) | ✅ native | 🟡 serial fetch (slower but works) |
| Python recipe picker (`scripts/recipe.py`) | ✅ also works here | ✅ |
| Python assembler (`scripts/assemble_docx.py`) | ✅ also works here | ✅ |
| 28 modular sections + 17 framework presets | ✅ | ✅ |

The fastest experience is on Claude Code (parallel sub-agent spawn), but every other agent can drive the same pipeline with the Python helpers and AGENTS.md.

## Build your own recipe

Don't see your framework? Or your firm has a custom report shape? Compose it:

1. Pick any framework as starting point in `framework.yaml`
2. Run `/redink-recipe` and select the sections you want
3. (Optional) Reorder by editing `report-recipe.yaml` directly
4. Run `/redink-build`

If you want to contribute your composition back as a new framework preset, drop a `frameworks/<your-framework>/manifest.yaml` + `README.md` and open a PR.

## Commands

| Command | What it does |
|---|---|
| `/redink-recipe` | Interactive section picker. Writes `report-recipe.yaml`. |
| `/redink-build` | Full pipeline. Reads recipe, validates findings, assembles output. |
| `/redink-rebuild <id>` | Re-run one finding by ID. |
| `/redink-status` | Show progress — recipe state, finding counts, QA report. |
| `/redink-frameworks` | List all supported frameworks + active one. |

### Python CLI equivalents (for non-Claude-Code agents)

| Python CLI | Replaces | Notes |
|---|---|---|
| `python3 scripts/recipe.py` | `/redink-recipe` | Interactive section picker; no LLM needed |
| `python3 scripts/recipe.py --non-interactive` | — | Accept framework defaults silently |
| `python3 scripts/assemble_docx.py` | `/redink-build` | Final assembly; per-finding citation work done by your agent first |
| `python3 scripts/assemble_docx.py --framework <name>` | — | Override `framework.yaml` per-run |
| `python3 scripts/assemble_docx.py --only <id>` | `/redink-rebuild` | Re-assemble with only one finding |

## Project layout

```
redink/
├── .claude-plugin/plugin.json
├── .claude/
│   ├── agents/         (cwe + cve + cvss + epss validators · finding-writer · report-reviewer)
│   └── commands/       (/redink-build · /redink-recipe · /redink-rebuild · /redink-status · /redink-frameworks)
├── sections/           (28 universal report sections, one per folder)
├── frameworks/         (17 framework presets, one per folder with manifest.yaml + README.md)
├── poc/{web,server}/   (← drop your PoC screenshots here)
├── scans/              (← optional: Nessus/Burp/nmap output)
├── jsons/              (generated per-finding entries)
├── output/             (final report .docx or .json)
├── templates/          (drop your firm's docx template here, named <framework>.docx)
├── assets/             (firm logo)
├── scripts/
│   ├── assemble_docx.py      (recipe-driven assembler, framework-aware)
│   └── recipe.py             (standalone interactive section picker, no-LLM)
├── brand-guidelines.md       ← firm details (framework-agnostic)
├── targets.yaml              ← engagement scope
├── engagement-summary.md     ← exec summary narrative
├── framework.yaml            ← active framework
├── report-recipe.yaml        ← active section selection
├── AGENTS.md                 ← instructions for Codex/Cursor/Gemini/Aider/Kimi
├── CLAUDE.md · README.md · DISCLAIMER.md · SECURITY.md · LICENSE
└── install.sh · .gitignore
```

## What `redink` does NOT do

- **It does not exploit anything.** Bring your own PoC screenshots; this is the reporting layer.
- **It does not guarantee compliance.** Evaluators grade PoC quality, technical depth, and writing craft — automation can validate references and structure, not insight.
- **It does not bypass your framework's rules.** Read your framework's official documentation before using.

For the exploitation phase, pair `redink` with [0xSteph/pentest-ai-agents](https://github.com/0xSteph/pentest-ai-agents) or your existing toolkit.

## Contributing

PRs especially welcome from active assessors / auditors / pentesters in any of the supported regions:

- Refining framework manifests with regional practitioner expertise — e.g., NCSC CHECK CTL signing nuances, PASSI two-axis severity quirks, PCI QSA Customized Approach edge cases, IRAP "weakness not risk" wording
- Full control catalogues for control-centric frameworks (NIST SP 800-171 / NIST SP 800-172 for CMMC, ISM for IRAP, the 12 PCI DSS requirements, BSI IT-Grundschutz catalogues, NCA ECC 5 domains × 29 subdomains, NESA 188 controls, K-ISMS-P 102 criteria) — drop a `frameworks/<name>/controls.yaml`
- Localised prompts (French for PASSI, German for BSI, Korean for K-ISMS-P, Japanese for ISMAP, Arabic for NCA ECC / NESA, Russian for FSTEC)
- Polished docx renderers per framework — sections currently fall through a generic renderer

For now, open an issue first to discuss the scope before submitting a PR.

## License

MIT — see [LICENSE](LICENSE).

## Acknowledgements

Influenced by [0xSteph/pentest-ai-agents](https://github.com/0xSteph/pentest-ai-agents) (safety model, scope guard), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) (multi-agent template → final deliverable), [Pimzino/claude-code-spec-workflow](https://github.com/Pimzino/claude-code-spec-workflow) (staged pipeline pattern), [OWASP OPTRS](https://owasp.org/www-project-penetration-test-reporting-standard/) (machine-readable standard).
