# Scientific Poster Creation & Audit Guide

This repository supports creating, compiling, and auditing scientific conference posters in both **LaTeX** and **PowerPoint (.pptx)**, based on standards from [Claude Scientific Writer](https://github.com/K-Dense-AI/claude-scientific-writer).

---

## Quick Start: LaTeX Posters

LaTeX posters provide crisp vector typography, automated block positioning, and native mathematical typesetting.

### Supported Templates (in `templates/posters/`)
1. **`tikzposter.tex`** (Recommended): Modern, colorful, highly customizable 3-column layout based on TikZ.
2. **`beamerposter.tex`**: Inherits standard Beamer themes and institutional branding.
3. **`baposter.tex`**: Box-based multi-column layout with flexible anchors.

### Creating a New LaTeX Poster
1. Create a folder under `posters/`:
   ```bash
   mkdir posters/my-poster
   ```
2. Copy a template:
   ```bash
   cp templates/posters/tikzposter.tex posters/my-poster/poster.tex
   ```
3. Customize content in `posters/my-poster/poster.tex`.
4. Compile with `make`:
   ```bash
   make posters
   ```
   Or directly with `pdflatex`:
   ```bash
   pdflatex -output-directory=posters/my-poster posters/my-poster/poster.tex
   ```

---

## Quick Start: PowerPoint (.pptx) Poster Workflow

For editable PowerPoint posters or existing `.pptx` presentations you already have:

### 1. Audit an Existing PPTX Poster
To check slide dimensions, detect column layout, flag small fonts (< 22pt), check effective image DPI (>= 150-300 DPI), and find shape overlaps:
```bash
python posters/pptx-workflow/audit_existing_pptx.py path/to/your_poster.pptx
```
Or with `make`:
```bash
make audit-pptx file=posters/pptx-workflow/sample_poster.pptx
```

You can also output a JSON report:
```bash
python posters/pptx-workflow/audit_existing_pptx.py my_poster.pptx --json-out report.json
```

### 2. Generate a New Structured PPTX Poster
Run the 3-column scientific poster generator:
```bash
python posters/pptx-workflow/create_sample_pptx_poster.py --output posters/my-poster.pptx --width 48 --height 36
```

---

## Design Constraints & Hard Quality Limits

| Parameter | Recommended Limit | Why |
|---|---|---|
| **Canvas Size** | 48" x 36" (US) or 33.1" x 46.8" (A0) | Standard conference board dimensions |
| **Body Font** | >= 22-26 pt | Legible from 4 to 6 feet away |
| **Section Titles** | >= 32-36 pt | Visible from 10 feet |
| **Main Title** | >= 72-100 pt | Clear from 15 to 20 feet |
| **Total Word Count** | 300 to 800 words | Avoid walls of text; prioritize figures |
| **Whitespace** | >= 50% | Essential for visual hierarchy and readability |
| **Raster Image DPI** | >= 150-300 effective DPI | Eliminates pixelation on large-format plotters |

---

## Antigravity AI Skills

This workspace is equipped with native AI agent skills in `.agents/skills/`:
- **`latex-posters`**: Interactive poster layout design, TikZ styling, and quality gate enforcement.
- **`pptx-posters`**: Strict one-slide PowerPoint poster verification, manifest auditing, and package security.
- **`scientific-schematics`**: Generating publication-quality flowcharts, process diagrams, and pathways.
- **`scientific-writing` & `citation-management`**: Verifiable academic citations and IMRaD structuring.

Simply ask Antigravity:
> *"Create a 3-column conference poster on my CRISPR results using tikzposter"*
> *"Audit my existing PowerPoint poster at posters/my-poster.pptx and suggest layout improvements"*
