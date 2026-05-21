---
description: Re-run validation and re-write one finding by ID.
argument-hint: "<id>"
---

# /redink-rebuild — re-generate one finding

Re-run the pipeline for a single finding. Useful when:

- A PoC screenshot was updated and the entry needs refreshing
- `report-reviewer` flagged drift on a single entry
- A CVE published a new advisory and the citation needs updating
- The active framework was switched and one finding needs re-conversion

## Steps

1. **Parse argument.** Expect `$ARGUMENTS` to be the finding ID (format depends on active framework — `001` for CERT-In, `FINDING-001` for OWASP, `F-001` for CMMC, etc.). If missing or malformed, error.

2. **Resolve active framework.** Read `framework.yaml`.

3. **Locate the existing JSON.** Glob `jsons/<id>*` or `jsons/*<id>*.json`. If zero or multiple match, error and list candidates.

4. **Locate the source folder.** From the existing JSON's first evidence/PoC step's `image_path`, derive the folder. Confirm it still exists.

5. **Spawn `finding-writer`** with the same inputs as `/redink-build` would have passed: `folder_path`, `id`, `scope`, `framework`, and any `scans/*` excerpt that mentions the host/service.

6. **Diff.** After the new JSON is written, show a unified diff vs. the previous version. Highlight changes to severity, CWE, CVE, CVSS, or EPSS.

7. **Re-validate.** Spawn `report-reviewer` for **just this entry** (`--single-entry <id>`). If clean, exit. If issues, report them and do not silently retry.

8. **Re-assemble.** Run `python3 scripts/assemble_docx.py --only <id>` to splice the updated entry into the output document without regenerating the whole report.

Print:

```
Re-built finding 014.

  Framework: certin-annexure-a
  Folder: poc/server/14_Outdated_OpenSSL/
  Severity: High → Critical (changed)
  CVE: CVE-2023-XXXX (unchanged)
  EPSS: 12.3% → 18.7% (re-fetched YYYY-MM-DD)

  Diff: jsons/014_Outdated_OpenSSL.json
  Output: output/certin-annexure-a-report.docx (spliced)
```
