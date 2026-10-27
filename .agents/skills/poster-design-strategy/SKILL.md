---
name: poster-design-strategy
description: Visual layout, strategic content distillation, template selection, and oral presentation coaching for scientific research posters based on empirical research communication standards. Use when designing, restructuring, or auditing scientific posters to maximize attendee engagement and avoid cognitive overload.
---

# Poster Design Strategy & Best Practice Skill

This skill guides researchers through the end-to-end design, distillation, structural layout selection, and oral delivery of scientific conference posters. It implements the empirical findings of **Khadka & Peeters (2024)** and enforces the **"Illustrated Abstract"** paradigm to maximize conference engagement while eliminating cognitive overload.

---

## Workflow Overview

When invoked (or when pair programming with an author to build or refine a poster), execute the following **5-Phase Workflow**:

```
[ Phase 1: Format & Template Discovery ]
  - Two-step prompt: Format (LaTeX vs. PPTX) -> Template (VLIZ, tikzposter, baposter, beamerposter)
                    │
                    ▼
[ Phase 2: Paper Intake & Precision Distillation ]
  - Hybrid intake: Auto-distill manuscript (papers/*.md) or conduct structured questionnaire
  - Enforce Section 4 architecture: 2-4 context bullets, explicit RQ & Hypothesis, diagrammed methods,
    1-3 result figures without raw tables, 1 limitation, 1 future direction, QR code
                    │
                    ▼
[ Phase 3: Visual Layout Paradigm Selection ]
  - Data-driven recommendation based on visual assets:
    * Single dominant map/finding -> Large Central Box or Hybrid Central Highlight
    * Multi-figure empirical data  -> Traditional 3-Column
    * High-impact keynote finding -> Morrison Billboard or Persky Single-Message
                    │
                    ▼
[ Phase 4: Generation Coordination ]
  - Generate poster source using repository templates and sister skills (latex-posters, pptx-posters)
                    │
                    ▼
[ Phase 5: MAR Rubric Quality Audit & 10-Minute Oral Coach ]
  - Audit against the 4-tier Mixed-Approach Rubric (Cohen's kappa = 0.80)
  - Generate a synchronized 10-minute oral presentation cue sheet (10-minute hard cap)
```

---

## Phase 1: Format & Template Discovery

Begin by asking the author the two-step selection question:

1. **Target Output Format**:
   - **LaTeX (`tikzposter`, `baposter`, `beamerposter`)**: For vector precision, mathematical formulas, and Git-tracked workflows.
   - **PowerPoint (`.pptx`)**: For interactive manual editing, collaborator drag-and-drop, and standard conference templates.
2. **Template Selection**:
   - **VLIZ Institutional (`vliz_tikzposter.tex` / `vliz_poster_template.pptx`)**: Flanders Marine Institute corporate theme featuring the exact sea-teal (`#91C8CD`) banner, vector wave logo, and left-aligned title/author block.
   - **Modern `tikzposter` (`templates/posters/tikzposter.tex`)**: Flexible themes (`Rays`, `Wave`, `Board`, `Default`) with customizable card blocks.
   - **Classical `baposter` (`templates/posters/baposter.tex`)**: High-density multi-column layout with explicit coordinate anchoring.
   - **`beamerposter` (`templates/posters/beamerposter.tex`)**: Slide-style modular blocks.

---

## Phase 2: Paper Intake & Precision Distillation

Apply the **10-10 Rule**: Attendees scan from 10 feet for 10 seconds. The target word count for the entire board is **250 to 450 words** (never exceeding 600 words).

### Hybrid Ingestion
- **If a manuscript exists** (e.g., in `papers/*.md` or provided PDF): Parse the text, automatically draft the required sections according to the rules below, and present the distilled draft to the author for validation.
- **If starting from scratch**: Interview the author step-by-step to isolate the 6 core components below.

### The Section Architecture Rules (Mandatory)

1. **Title Block**:
   - Informative, descriptive title highlighting primary variables or core discovery.
   - Full author names, institutional affiliations, and corresponding email.
2. **Background & Context (Condensed Introduction)**:
   - **Strictly 2 to 4 concise bullet points** with key literature citations.
   - What is known $\rightarrow$ The specific scientific gap.
   - **Explicit Statement of Research Question (RQ)**.
   - **Explicit Statement of Hypothesis or Prediction**.
   - **PROHIBITION**: Never paste a submission abstract ($\beta = -0.10$ negative impression driver).
3. **Methods Overview**:
   - Present study organism/system, experimental approach, independent/dependent variables, and sample size ($n$).
   - **Best Practice**: Replace narrative prose with a visual experimental setup diagram or flowchart ($\beta = +0.15$).
4. **Results Visualization (The Focal Point)**:
   - **1 to 3 high-value figures** showcasing major trends and statistical differences.
   - A concise, standalone descriptive caption below every figure.
   - Brief bullet points highlighting statistical findings ($p$-values, effect sizes).
   - **PROHIBITIONS**: Zero raw data tables; zero narrative literature interpretation.
5. **Discussion & Mechanisms**:
   - Clear statement: Was the hypothesis supported or refuted?
   - Explanatory chemical, physical, or biological mechanism.
   - Broad domain-level implications.
   - **Exactly ONE major study limitation**.
   - **Exactly ONE actionable future direction** directly addressing that limitation.
6. **Supplemental & Digital Integration**:
   - **2 to 5 key references** cited in-text.
   - Mandatory AI / super-intelligence tool disclosures.
   - **Scannable QR code** ($\beta = +0.12$) linking to the full paper, supplementary dataset, or video.

---

## Phase 3: Visual Layout Paradigm Determination

Evaluate the author's visual assets and narrative type against the **6 Structural Layout Paradigms**:

```
1. Traditional Multi-Column       2. Large Central Box              3. Hybrid Central Highlight
+-------------------------------+  +-------------------------------+  +-------------------------------+
| [ Title Block & Authors ]     |  | [ Title Block & Authors ]     |  | [ Title Block & Authors ]     |
+-------+-------+-------+-------+  +-------+---------------+-------+  +-------------------------------+
| Col 1 | Col 2 | Col 3 | Col 4 |  | Col 1 | PRIMARY DATA | Col 3 |  | [ FULL-WIDTH HERO CALLOUT &   |
| Intro | Meth. | Res.  | Disc. |  | Intro | & FIGURES     | Disc. |  |   KEY TAKEAWAY / MAP SECTION ] |
| (IMRaD flow, 2-4 columns)     |  | Meth. | (Focal Box)   | Concl.|  +-------+-------+---------------+
| Familiar, but text risk       |  |       |               | QR    |  | Col 1 | Col 2 | Col 3 (Grids) |
+-------+-------+-------+-------+  +-------+---------------+-------+  +-------+-------+---------------+

4. Morrison's "Better Poster"      5. Persky's Single-Message        6. Portrait Row Arrangement
+-------+---------------+-------+  +-------------------------------+  +-------------------------------+
| Col 1 |               | QR    |  | [ Title Block & Authors ]     |  | [ Title Block & Authors ]     |
| Intro | MASSIVE CORE  | Code  |  +-------------------------------+  +-------------------------------+
| Meth. | TAKEAWAY      | &     |  | [ SINGLE CORE TAKEAWAY PANEL] |  | Row 1: Context & Hypotheses   |
|       | HEADLINE      | Mini  |  +-------------------------------+  +-------------------------------+
|       |               | Res.  |  | Visual Data   | Visual Data   |  | Row 2: Methods Diagram        |
|       |               |       |  | Panel A       | Panel B       |  +-------------------------------+
+-------+---------------+-------+  +-------------------------------+  | Row 3: Results & Discussion   |
```

### Selection Guide
- **Use Large Central Box or Hybrid Central Highlight**: When the study is anchored by an expansive bathymetric map, spatial GIS distribution, or single primary mechanism diagram.
- **Use Traditional 3-Column**: When presenting 2–3 distinct empirical experimental figures that follow a sequential narrative.
- **Use Morrison's Billboard Style**: For fast-paced conference halls where the goal is rapid headline dissemination from 10 feet away.
- **Use Persky's Single-Message**: For focused single-finding papers where auxiliary text must be strictly curtailed.
- **Avoid Shape-Based / Complex Circles**: Poor spatial packing efficiency for rectangular scientific charts.

---

## Phase 4: Generation Coordination

Once content is distilled and the layout paradigm is chosen:
1. Populate the selected template in `posters/<poster-name>/poster.tex` or generate via `create_vliz_poster.py`.
2. Ensure strict typographic hierarchy:
   - **Dual-font rule**: Distinct bold header font paired with clean, readable body font.
   - **Font sizes**: Titles $\ge 50\,\text{pt}$, Headings $\ge 32\,\text{pt}$, Body text $\ge 22\,\text{pt}$ (readable from 3–6 feet).
   - **Color accessibility**: Dark text on light neutral background; zero red-green pairings.
3. Compile using repository automation:
   ```bash
   make posters
   ```

---

## Phase 5: MAR Quality Audit & 10-Minute Oral Presentation Coach

### Automated Mixed-Approach Rubric (MAR) Audit
Run the automated MAR assessment script:
```bash
python .agents/skills/poster-design-strategy/scripts/audit_poster_rubric.py posters/<poster-name>/poster.tex
```

The script evaluates the poster across the 3 core criteria (Cohen's kappa $\kappa = 0.80$):

| Visual Criteria | Poor [1] | Sub-par [2] | Acceptable [3] | Exemplary [4] |
| :--- | :--- | :--- | :--- | :--- |
| **Organization** | Confusing, unstructured flow; abstract included. | Awkward section progression; missing RQ/Hypothesis. | Generally organized IMRaD sequence. | Exceptionally clean, logical visual hierarchy. |
| **Poster Design & Visuals** | Visually unpleasant; lacks diagrams; raw tables present. | Weak visuals; raw data tables clutter results. | Functional graphics; pleasant layout. | High figure-to-text ratio; visual diagrams replace prose; QR offloads details. |
| **Wordiness / Text Density** | $>800$ words (severe cognitive overload). | $600–800$ words (excessive dwell time). | $450–600$ words (acceptable). | $250–450$ words (optimal illustrated abstract). |

### The 10-Minute Oral Presentation Coach
Conference poster sessions enforce a **hard 10-minute cap**. Session moderators strictly stop presentations at 10 minutes. Provide the author with the following synchronized speech plan:

```
TOTAL PRESENTATION TIME: 10 MINUTES (HARD CAP)
├── 1. Background & Research Question : 1 to 2 Minutes
│   └── Point to context bullets; state the scientific gap; articulate RQ & Prediction.
├── 2. Methods Overview               : 2 Minutes
│   └── Direct audience to the setup diagram; summarize variables & sample size (n).
├── 3. Results & Figure Walkthrough   : 4 to 5 Minutes
│   └── The core presentation; walk through Figures 1-3 sequentially; highlight p-values.
└── 4. Discussion & Limitations       : 1 to 2 Minutes
    └── State if hypothesis was supported; explain biological/physical mechanism;
        disclose exactly 1 limitation; propose exactly 1 future direction; invite questions.
```

#### Board Interaction & Engagement Mechanics (The Heather Winslow Method)
- Never read bullets verbatim; treat bullet points as anchors while expanding conversationally.
- Physically interact with the board by pointing directly to chart axes, data trends, and setup diagrams as they are spoken.
- Connect specific micro-datasets to overarching, field-level domain questions (as demonstrated by AGU OSPA awardee Heather Winslow) to maintain multi-hour audience engagement.

---

## References

For full empirical regression models, standardized $\beta$ coefficients, and research literature details, consult:
- [.agents/skills/poster-design-strategy/references/best_practice_guide.md](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/references/best_practice_guide.md)
