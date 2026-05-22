---
id: 01-cover-page
title: Cover Page
required_by: [all]
inputs:
  - from: brand-guidelines.md
    field: Firm name
  - from: brand-guidelines.md
    field: Logo path
  - from: brand-guidelines.md
    field: Engagement code
  - from: brand-guidelines.md
    field: Test duration (start)
  - from: brand-guidelines.md
    field: Test duration (end)
  - from: brand-guidelines.md
    field: Submitted on
  - ask_user:
      prompt: "Optional classification banner (e.g., 'CONFIDENTIAL — DO NOT DISTRIBUTE'). Leave blank for none."
      default: ""
output_type: cover
---

# Cover Page

The first page of the report. Combines firm branding, engagement identifiers, and optional classification language. Required by every supported framework.

## Template

```
[Optional classification banner — top of page]

                      <Firm Logo>

                      [Report title]
                  <framework display name>
                       VAPT Report

                    Submitted by
                    <Firm name>

           Engagement: <engagement code>
           Tested: <start date> → <end date>
           Submitted: <submitted on>

                   <primary contact name>
                   <email> · <phone>
```

## Notes

- The framework display name and report title vary by framework (e.g. "CERT-In VAPT Report", "CMMC L2 Final Assessment Report").
- If `assets/logo.png` is missing, the cover renders text-only.
- Classification banner sits at top of page in red, bold; only renders if the user provided a value.
