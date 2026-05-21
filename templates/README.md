# templates/

## Drop your firm's `.docx` template(s) here

The assembler (`scripts/assemble_docx.py`) will use `templates/<framework>.docx` as the base document if present. If absent, it falls back to a built-in skeleton.

Naming convention: one template per framework.

```
templates/
├── certin-annexure-a.docx
├── cmmc-level-3.docx
├── ncsc-check.docx
├── pci-dss-roc.docx
└── README.md
```

(`owasp-optrs` outputs JSON, no template needed.)

### Why bring your own

Each compliance framework leaves cover, fonts, and Part 1 styling to the firm. Your senior has probably already produced a template with:

- Firm cover page (logo, address, classification banner)
- Part 1 / Executive Summary tables pre-styled
- Heading and table styles matching the firm's house style
- Placeholder finding sections you can delete

Drop that file here. The assembler will:

1. Open it as the base document
2. Skip generating its own cover / Part 1 (yours is already there)
3. Append finding entries from `jsons/` after the existing content

### Without a template

If `templates/<framework>.docx` is missing, the assembler builds a minimal report:

- Generic cover page populated from `brand-guidelines.md`
- Engagement summary table
- Part 1 stub pointing to `brand-guidelines.md`
- Findings (the actual deliverable)

This works but is plain. For final submission, you almost certainly want your firm's template.

### How to create one

If you don't have a template:

1. Take any prior report from your firm in the same framework.
2. Strip the findings section to a single placeholder entry.
3. Save as `templates/<framework>.docx`.
4. The assembler will append generated entries below the placeholder — delete the placeholder manually after assembly.
