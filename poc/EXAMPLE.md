# PoC folder conventions

Every finding gets its own folder under `poc/web/` or `poc/server/`. The folder name **becomes the vulnerability title** in the report, verbatim — typos, spaces, mixed case all preserved.

## Folder name format

Recommended pattern:

```
NN_<Short_Descriptive_Name>/
```

- `NN` — 2-digit ordinal for ordering within scope (`01`, `02`, ...). Stripped from the final report name.
- `Short_Descriptive_Name` — what the finding actually is. Underscores for spaces. Specific enough that a senior auditor can name the weakness from the folder alone.

### Good names

```
poc/web/01_WordPress_Plugin_Unauth_RCE/
poc/web/02_phpMyAdmin_Default_Credentials/
poc/web/03_Apache_Server_Status_Exposed/
poc/web/04_Insecure_Direct_Object_Reference_Profile_API/

poc/server/01_Tomcat_HTTP_PUT_Method_RCE/
poc/server/02_FTP_Anonymous_Read_Enabled/
poc/server/03_SMB_Null_Session_Enabled/
poc/server/04_Outdated_OpenSSH_7.4/
```

### Bad names — and why

```
poc/web/01_bug/                          ← too vague — name the weakness
poc/web/02_vuln_in_login/                ← which weakness? SQLi, XSS, IDOR?
poc/web/03_login_page_has_issue/         ← prose; senior auditor cannot map this to a CWE
poc/server/04_NESSUS_PLUGIN_12345/       ← evaluator cares about the weakness, not the scanner ID
```

## Image files inside each folder

One screenshot per PoC step. Sequence matters — `redink` orders by filename, so:

```
poc/server/01_Tomcat_HTTP_PUT_Method_RCE/
├── 1_options_response_put_enabled.png    # the vuln (PUT method allowed)
├── 2_jsp_uploaded_via_put.png            # the exploit (webshell deployed)
├── 3_command_execution.png               # the impact (commands run as Tomcat user)
└── notes.txt                             # optional — your own notes (ignored by redink)
```

### What each screenshot should prove

A senior auditor reads a PoC sequence and asks three questions:

1. **The vulnerability exists.** Screenshot showing the misconfiguration / weak code / exposed endpoint.
2. **It can be exploited.** Screenshot showing the exploit step succeeding — request + response, payload + output.
3. **The impact is real.** Screenshot showing what an attacker can actually do with it — extracted data, command execution, privilege escalation.

Three screenshots per finding is the floor, not the ceiling. Add more if exploitation has multiple stages, but don't pad — each image must prove something distinct.

## Capturing good screenshots

- **Full window, not zoomed crops** — evaluators want context (URL bar, terminal prompt, hostname).
- **Black-out credentials, not findings** — your VPN source IP can be visible; your client's plaintext passwords cannot.
- **Use a consistent OS / theme** — Kali default theme, Burp Pro, etc. The evaluator should not be distracted by visual chaos.
- **PNG, not JPEG** — text in screenshots stays crisp.

## What `redink` does with these folders

When you run `/redink-build`:

1. Walks `poc/web/` and `poc/server/`
2. Reads each folder name (verbatim) → vulnerability title
3. Reads up to ~4 screenshots per folder to understand what the finding is
4. Maps the finding to a CWE + CVE
5. Asks you 3–5 questions if anything is ambiguous
6. Writes `jsons/<id>_<slug>.json` per folder (id format depends on the active framework)
7. Assembles `output/<framework>-report.docx` (or `.json` for OWASP OPTRS)

Filename, sequence, and exact content of the folder are all load-bearing. Spend the time to name folders well — every minute saved here pays back fivefold in fewer clarifying questions.
