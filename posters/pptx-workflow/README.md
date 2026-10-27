# PowerPoint (.pptx) Poster Workflow

This directory provides specialized tools for auditing, structuring, and generating scientific conference posters in Microsoft PowerPoint.

---

## 1. Auditing an Existing `.pptx` Poster

If you already have a poster created in PowerPoint, run the layout analyzer:

```bash
python posters/pptx-workflow/audit_existing_pptx.py your_poster.pptx
```

### What the Audit Checks:
- **Slide Count:** Enforces exactly 1 slide for conference poster presentation.
- **Physical Canvas & Scaling:** Analyzes width x height (e.g. 48" x 36" or A0), detects orientation, and calculates scale factor for commercial printing.
- **Multi-Column Alignment:** Clusters content shapes to verify balanced 2, 3, or 4 column grids.
- **Typography & Readability:**
  - Flags text smaller than 20pt (which is unreadable from 4-6 feet away).
  - Checks if headers (>= 32pt) and titles (>= 72pt) establish clear hierarchy.
- **Effective Image DPI:**
  - Inspects pixel resolution of all embedded pictures against placed dimensions:
    $$\text{Effective DPI} = \frac{\text{Pixel Width}}{\text{Placed Width in Inches}}$$
  - Flags any figure under 150 DPI that will print blurry.
- **Bounding Box Overlaps:** Identifies overlapping text frames or figures that compromise whitespace.
- **Word Count Density:** Warns if total words exceed 800 (posters should be visual, not papers on a board).

---

## 2. Generating a Standard 3-Column PPTX Poster

To generate a clean, pre-structured 3-column academic poster in PowerPoint:

```bash
python posters/pptx-workflow/create_sample_pptx_poster.py --output posters/pptx-workflow/my_new_poster.pptx --width 48 --height 36
```

### Layout Specs:
- **Canvas Size:** 48 inches wide by 36 inches high (standard US conference board)
- **Grid:** 3 columns with 0.75" gutter and 1.0" outer margins
- **Header:** Full-width rounded card for Title, Authors, and Institutional Affiliation
- **Cards:** 6 modular rounded blocks with high-contrast text and clean borders

---

## 3. Strict Manifest-Driven Poster Generation (Claude Scientific Writer)

The `.agents/skills/pptx-posters/` skill also includes a deterministic generator from JSON manifests:

```bash
# Validate manifest
python .agents/skills/pptx-posters/scripts/validate_manifest.py poster.json

# Check layout & contrast
python .agents/skills/pptx-posters/scripts/check_layout.py poster.pptx --manifest poster.json
python .agents/skills/pptx-posters/scripts/check_palette.py poster.json
```
