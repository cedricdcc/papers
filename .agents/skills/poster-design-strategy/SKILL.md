---
name: poster-design-strategy
description: Visual layout, strategic content distillation, provenance tracking, template selection (LaTeX and/or PowerPoint .pptx), and oral presentation coaching for scientific research posters based on empirical research communication standards. Use when designing, restructuring, or auditing scientific posters to maximize attendee engagement and avoid cognitive overload.
---

# Poster Design Strategy & Best Practice Skill

This skill guides researchers through end-to-end strategy, structured provenance capture (`provenance.md`), precision distillation, human-in-the-loop (HITL) layout selection, AI-powered infographic generation via Nano Banana 2, multi-format rendering (**LaTeX `.tex/.pdf`**, **PowerPoint `.pptx`**, or **Both**), and oral presentation delivery for scientific conference posters.

It operationalizes the empirical findings of **Khadka & Peeters (2024)**, enforces the **70/30 Infographic Rule** (70% visual storytelling vs. 30% concise text), tracks complete project requirements and decision provenance in `posters/<poster-name>/provenance.md`, and targets standard **A0 Portrait ($841 \times 1189\,\text{mm}$)** orientation to maximize engagement while eliminating cognitive overload.

---

## Workflow Overview

When designing, restructuring, or pair programming with an author to build a poster, execute this **6-Phase Workflow** with incremental provenance persistence at every gate:

```
[ Phase 1: Strategic Discovery, Deliverable Format, Branding/Logos & Provenance Intake ]
  - 6-Pillar Interview (via ask_question): Deliverable Format (LaTeX | PPTX | Both) ->
    Audience & Personas -> Authors List -> Conference & Default Logo Space ->
    Branding & Extra Logos List -> Captured Source Inputs & QR Targets
  - Persist Gate 1: Create posters/<poster-name>/provenance.md from template
                                │
                                ▼
[ Phase 2: Paper Intake & Precision Distillation ]
  - Enforce the 30% Text Budget: Strictly 250–400 words total across the board
  - Enforce Section Architecture: 2–4 context bullets, explicit RQ & Hypothesis,
    visual methods, focal results (zero raw tables), 1 limitation, 1 future direction, QR code
  - Persist Gate 2: Update provenance.md (Section 2: Distilled Scientific Narrative)
                                │
                                ▼
[ Phase 3: 70/30 Infographic Architecture & Visual Planning ]
  - Visual narrative decomposition: Translate the core research argument into a dominant visual representation
  - Style & theme selection (VLIZ Marine Institute #91C8CD, Ecology, Biomed, Tech)
                                │
                                ▼
[ Phase 4: Human-in-the-Loop (HITL) Layout & Infographic Creation ]
  - Step 4A: Present 2 tailored A0 Portrait ASCII wireframes with explicit 70/30 spatial allocations
    and configured Conference Logo / Placeholder & Extra Logo slots
  - Step 4B: Author selects or adjusts block positions before any code generation
  - Step 4C: Interactive Nano Banana Infographic Creator Loop (iterative visual refinement until approved)
  - Persist Gate 3: Update provenance.md (Section 3: Wireframe & Infographic Prompt Log)
                                │
                                ▼
[ Phase 5: Template & Generation Coordination (LaTeX and/or Direct LLM PPTX) ]
  - Render in LaTeX (tikzposter, baposter, beamerposter), PowerPoint (.pptx), or Both targeting A0 Portrait
  - For PPTX: LLM generates posters/<poster-name>/poster.pptx directly via ephemeral python-pptx
    execution in scratch/memory and cleans up (no per-poster .py build script committed in poster folder)
  - Render Conference Logo (or reserved placeholder box) and Extra Logos in configured zones
                                │
                                ▼
[ Phase 6: MAR 70/30 Quality Audit, PPTX Technical Audit & 10-Minute Oral Coach ]
  - Audit against the 4-tier, 4-dimension Mixed-Approach Rubric (16 points max) + provenance check
  - If PPTX generated: Run audit_existing_pptx.py (target 100/100 score, >=150-300 DPI, 0 overlaps)
  - Persist Gate 4: Record final audit scores in provenance.md (status: "audited")
  - Generate a synchronized 10-minute oral presentation cue sheet
```

---

## Phase 1: Strategic Discovery, Deliverable Format, Branding/Logos & Provenance Intake

Whenever making a new poster or invoking this skill on a project without an existing `posters/<poster-name>/provenance.md`, you **MUST interview the author** (using `ask_question`) across the **6 Discovery & Provenance Pillars** before proposing layouts or generating files:

1. **Deliverable Format(s)**:
   - Ask whether the target deliverable is:
     - **LaTeX (`poster.tex` $\rightarrow$ `poster.pdf`)**
     - **PowerPoint (`poster.pptx`)**
     - **Both (`poster.tex` + `poster.pdf` + `poster.pptx`)**

2. **Audience Archetype, Personas & Engagement Goal**:
   - **Primary Archetype**:
     - *Domain Specialists*: High-density scientific terminology allowed; emphasize novel methodology, nuanced statistical distributions, and fine-grained mechanisms.
     - *Interdisciplinary Researchers*: Avoid niche jargon; clearly define acronyms; emphasize broad cross-disciplinary implications and conceptual frameworks.
     - *Stakeholders / Policy / Industry / Public*: Focus on practical utility, macro-level impact, economic/environmental consequences, and bold visual takeaways.
   - **Specific Personas List**: Concrete sub-groups (e.g., `["Term Translators", "Ontology Stewards"]`).
   - **Engagement Goal**: *Conference Award / Competition*, *Academic Networking / Early Feedback*, or *Dissemination of Published Paper / Live Platform*.

3. **Authors & Affiliations List**:
   - Capture the ordered list of all authors, including for each author:
     - Full name
     - Institutional affiliation(s) and location
     - Contact email (and `corresponding: true/false`)
     - ORCID identifier (if applicable)

4. **Target Conference, Physical Constraints & Conference Logo Space**:
   - **Conference Details**: Event name (e.g., *VLIZ Marine Science Day 2026*), date, location, and URL.
   - **Standard Canvas**: Default is **A0 Portrait ($841 \times 1189\,\text{mm}$ / $33.11 \times 46.81\,\text{in}$)** unless the conference specifies custom board dimensions.
   - **Conference Logo / Reserved Placeholder Toggle**:
     - Explicitly ask whether the poster should include a **specific conference logo file** (`conference_logo_path`) OR **reserve space for a default conference logo** (`reserve_default_conference_logo_space: true/false`) so a conference badge can be dropped in later.
     - Default placement zone for the conference logo / placeholder is the **Top Header / Title Zone right** (`title_header_right`), configurable to `top_banner_right` or `footer_right`.

5. **Institutional Branding & Extra Logos List**:
   - **Theme & Primary Brand**: Curated color preset (e.g., Flanders Marine Institute VLIZ Sea-teal `#91C8CD`, corporate navy `#3057A5`), primary institutional logo (`assets/vliz_logo.png`), and primary domain URL (`vliz.be`).
   - **Extra Partner / Funder / Project Logos List (`extra_logos`)**:
     - Ask if any additional logos (e.g., Horizon Europe, EMODnet, partner universities, grant badges) must be included or have placeholder slots reserved.
     - Record each extra logo's `name`, `path` (or `placeholder: true`), and configurable placement zone (default: `footer_right` in the Footer Bar, or `top_banner_right` / `title_header_right`).

6. **Captured Source Inputs & Digital Destinations**:
   - **Source Material**: Local manuscript paths (`papers/<name>/<name>.md`), PDFs, GitHub repositories, datasets, or interview notes used to derive the poster content.
   - **Available Visuals**: Existing vector plots, photos, GIS maps, or need for Nano Banana 2 schematic synthesis.
   - **QR Code Targets**: Companion URLs and labels for scannable QR codes (live platform, GitHub repo, DOI/pre-print, dataset).
   - **References & Disclosures**: 2–5 key literature citations and mandatory AI tool disclosure text.

### Mandatory Gate 1: Initialize `posters/<poster-name>/provenance.md`
Immediately upon collecting the Phase 1 answers, create `posters/<poster-name>/provenance.md` by copying [templates/provenance_template.md](templates/provenance_template.md) and populating the YAML frontmatter (`poster`, `deliverables`, `audience`, `authors`, `conference`, `branding`, `inputs`) and Section 1 notes. Never leave `REPLACE_ME_*` tokens in completed fields.

---

## Phase 2: Paper Intake & Precision Distillation

Apply the **10-10 Rule**: Attendees scan from 10 feet for 10 seconds. The target word count for the entire board is strictly **250 to 400 words** (never exceeding 500 words) to protect the 70/30 visual balance.

### Hybrid Intake
- **If a manuscript exists** (`papers/*.md` or provided PDF): Auto-extract and distill the 6 mandatory sections according to the rules below, presenting the distilled draft to the author for approval.
- **If starting from scratch**: Conduct a focused interview to populate each block.

### Mandatory Section Architecture Rules

1. **Title Block**:
   - Informative, descriptive headline highlighting primary discovery or key variables.
   - Full author names, institutional affiliations, ORCIDs, and corresponding email (from `provenance.md`).
   - Conference logo or reserved `[ Conference Logo ]` placeholder box on the right side of the Title Header zone if enabled in `provenance.md`.
2. **Background & Context (Condensed Introduction)**:
   - **Strictly 2 to 4 concise bullet points** citing seminal literature.
   - What is known $\rightarrow$ The specific scientific gap.
   - **Explicit Statement of Research Question (RQ)**.
   - **Explicit Statement of Hypothesis or Prediction**.
   - **PROHIBITION**: Never paste an abstract text block ($\beta = -0.10$ negative impression driver).
3. **Methods Overview**:
   - State study system, experimental approach, independent/dependent variables, sample size ($n$).
   - **Visual Anchor**: Anchored by a visual experimental setup diagram or flowchart ($\beta = +0.15$).
4. **Results Visualization (The Focal Point)**:
   - **1 to 3 high-value figures** or **bold metric callout badges** showcasing primary data trends.
   - Brief standalone descriptive caption below every figure.
   - Bullet points highlighting statistical findings ($p$-values, effect sizes).
   - **PROHIBITIONS**: Zero raw data tables; zero narrative literature interpretation.
5. **Discussion & Mechanisms**:
   - Clear statement: Was the hypothesis supported or refuted?
   - Explanatory mechanism (chemical, physical, biological, or computational).
   - Broad domain-level implications.
   - **Exactly ONE major study limitation**.
   - **Exactly ONE actionable future direction** directly addressing that limitation.
6. **Supplemental, Extra Logos & Digital Integration**:
   - **2 to 5 key references** cited in-text.
   - Mandatory AI / super-intelligence tool disclosures.
   - **Scannable QR code** ($\beta = +0.12$) linking to the full paper, dataset, or live platform.
   - **Extra Partner / Funder Logos** rendered in the Footer Bar (or their configured placement zone from `provenance.md`).

### Mandatory Gate 2: Update `provenance.md` (Distilled Narrative)
Once the author approves the distilled content, write the finalized bullets, RQ, Hypothesis, Methods summary, Results metrics, Limitation, and Future Direction into Section 2 of `posters/<poster-name>/provenance.md` and set `poster.status: "distilled"`.

---

## Phase 3: 70/30 Infographic Architecture & Visual Planning

Under the **70/30 Rule**, 70% of the poster's physical surface area is dedicated to visual storytelling, while 30% is allocated to concise descriptive text.

### Visual Narrative Decomposition
Help the author deconstruct their study into three visual layers:
1. **The Hero Infographic**: A dominant, high-impact visual representation of the project (e.g. system architecture, experimental workflow, spatial transect, or biological pathway) occupying 40–50% of the total board area.
2. **Supporting Empirical Figures**: 1–2 focused data plots, maps, or metric callout badges occupying 20–30% of the board area.
3. **Generous Whitespace**: 40–50% negative space inside and around the visual graphics to ensure comfortable visual parsing from 3–10 feet.

### Selecting Domain Style Presets
Consult [templates/infographic_prompt_templates.md](templates/infographic_prompt_templates.md) to select a curated theme:
- **VLIZ Marine Institute**: Sea-teal (`#91C8CD`), Deep Ocean Navy (`#002B49`), Corporate Navy (`#3057A5`), clean marine vector accents.
- **Ecology & Environment**: Forest green (`#2D5A27`), Earth ochre (`#C29B38`), River teal (`#2B7A78`).
- **Biomedical & Genomics**: Okabe-Ito colorblind-accessible palette (`#2A4D69`, `#D55E00`, `#56B4E9`).
- **Modern Tech / AI / Systems**: Electric Indigo (`#4361EE`), Tech Cyan (`#4CC9F0`), Slate Grey (`#334155`).

---

## Phase 4: Human-in-the-Loop (HITL) Layout & Infographic Creation

### Step 4A: Present 2 Tailored A0 Portrait ASCII Wireframes
Always present **two tailored ASCII options** explicitly annotated with 70/30 spatial allocations AND showing the configured **Conference Logo / Placeholder slot** and **Extra Logos slots** from `provenance.md`:

#### Option 1: Top Hero Banner + Multi-Column Flow (70% Visual / 30% Text)
```
+-------------------------------------------------------------+
| [ TOP BANNER: Primary Institution Logo (Left) | URL (Right) ]|
+-------------------------------------------------------------+
| [ TITLE BLOCK: Subtitle, Title, Authors ]   [ CONF. LOGO /  |
|                                               PLACEHOLDER ] |
+-------------------------------------------------------------+
|                                                             |
|   =======================================================   |
|   |         CENTRAL HERO INFOGRAPHIC / PIPELINE         |   |
|   |             (~45% TOTAL POSTER AREA)                |   |
|   |   High-impact visual representation generated via   |   |
|   |     Nano Banana 2 in A0 Portrait aspect ratio       |   |
|   =======================================================   |
|                                                             |
+------------------------------+------------------------------+
| [ CONTEXT & HYPOTHESIS: 15% ]| [ RESULTS VISUAL: 25% AREA ] |
| • 2-3 Context Bullets        | +--------------------------+ |
| • Explicit Research Question | | Empirical Data Plot /    | |
| • Explicit Hypothesis        | | Metric Callout Badges    | |
|                              | +--------------------------+ |
| [ METHODS SUMMARY: 10% AREA ]| • Statistical Key Findings   |
| • System, Variables, n       +------------------------------+
| • Rounded Feature Sub-Cards  | [ DISCUSSION & TAKEAWAY: 5% ]|
+------------------------------+ • Hypothesis Supported?      |
| [ FOOTER: References & AI ]  | • 1 Limitation & 1 Outlook   |
| [ EXTRA LOGOS / PARTNERS ]   | [ QR CODE CARD ]             |
+------------------------------+------------------------------+
  Spatial Budget: ~70% Visual Assets & Negative Space | ~30% Text
```

#### Option 2: Central Hero Box + Flanking Context (70% Visual / 30% Text)
```
+-------------------------------------------------------------+
| [ TOP BANNER: Primary Institution Logo (Left) | URL (Right) ]|
+-------------------------------------------------------------+
| [ TITLE BLOCK: Subtitle, Title, Authors ]   [ CONF. LOGO /  |
|                                               PLACEHOLDER ] |
+------------------------------+------------------------------+
| [ CONTEXT & HYPOTHESIS: 15% ]| [ RESULTS HIGHLIGHT: 20% ]   |
| • 2-3 Literature Bullets     | +--------------------------+ |
| • Research Question (RQ)     | | Key Finding Chart /      | |
| • Explicit Prediction        | | Metric Callout Badges    | |
| • Study Variables & n        | +--------------------------+ |
+------------------------------+------------------------------+
|                                                             |
|   =======================================================   |
|   |          DOMINANT PROJECT HERO INFOGRAPHIC          |   |
|   |               (~50% TOTAL CANVAS AREA)              |   |
|   |      Comprehensive visual representation of the     |   |
|   |     entire mechanism, dataset, or spatial model     |   |
|   =======================================================   |
|                                                             |
+------------------------------+------------------------------+
| [ METHODS & MECHANISMS: 10% ]| [ DISCUSSION & FUTURE: 5% ]  |
| • Experimental Workflow      | • Primary Mechanism Summary  |
| • Rounded Feature Sub-Cards  | • 1 Constraint | 1 Next Step |
|                              | • [ QR CODE TO DATA / PAPER ]|
+------------------------------+------------------------------+
| [ FOOTER: References & AI Disclosure | EXTRA LOGOS BAR ]    |
+-------------------------------------------------------------+
  Spatial Budget: ~70% Visual Assets & Negative Space | ~30% Text
```

### Step 4B: Author Approval & Layout Adjustment
Prompt the author:
> *"Here are two tailored 70/30 layout architectures for your A0 portrait poster (including your configured logo slots). Which option best fits your narrative flow, or would you like to adjust the block arrangement before we generate the infographic and poster?"*

### Step 4C: Interactive Infographic Creator & Multi-Modal Self-Critique Loop
Once the layout is approved, launch the iterative visual creator loop using [templates/infographic_prompt_templates.md](templates/infographic_prompt_templates.md):

1. **Assemble Master Prompt (Eliminating Text Hallucinations)**:
   - Target zone geometry (`16:9` wide banner, `1:1` square, or `3:4` vertical).
   - Apply domain theme preset (e.g. VLIZ Marine Sea-teal `#91C8CD`, Deep Navy `#002B49`).
   - Strict negative constraint: Zero AI prose, no figure numbers, maximum 10 single-word structural labels total. Detailed explanations are delegated strictly to LaTeX/PPTX markup.
2. **Execute Generation**:
   Generate publication-grade visual asset using Nano Banana 2 / `generate_image`.
3. **Multi-Modal AI Self-Critique**:
   Before presenting to the author, inspect the image to verify:
   - Ample whitespace ($50\text{--}60\%$ negative space).
   - Clear left-to-right or top-to-bottom directional conduit.
   - Absence of distorted synthetic pseudo-fonts or unwanted palette legends.
4. **Interactive HITL Feedback Step (Mandatory Modal Gate)**:
   - Present the image preview to the author using an interactive modal (`ask_question`).
   - Prompt the author for direct feedback:
     - *"Does this visual representation accurately reflect your project?"*
     - *"Are the theme colors, containers, and element weights balanced?"*
   - **Iterative Refinement Rule**: If the author comments or requests adjustments, regenerate the infographic and present again. Only advance to the next step once the author explicitly approves the visual asset.

### Mandatory Gate 3: Update `provenance.md` (Layout & Infographic Log)
Record the approved ASCII wireframe, the final Nano Banana 2 master prompt, asset path, and iteration history in Section 3 of `posters/<poster-name>/provenance.md`, and set `poster.status: "layout_approved"`.

---

## Phase 5: Template & Generation Coordination (LaTeX and/or Direct LLM PPTX)

Check `deliverables.formats` in `posters/<poster-name>/provenance.md` and execute the corresponding generation pathway(s):

### Pathway A: LaTeX Poster Generation (`"latex"` in `deliverables.formats`)
1. **Render Template**:
   - Create `posters/<poster-name>/poster.tex` using `tikzposter`, `baposter`, or `beamerposter` targeting A0 Portrait ($841 \times 1189\,\text{mm}$).
2. **Typographic Hierarchy & Hybrid Visual Blocks**:
   - Replace plain bullet point lists with **Hybrid Visual Blocks**:
     - Key metrics and statistics transformed into bold metric callout badges (`tcolorbox` minipages, e.g. `25% Translated`, `2× Curation Speed`).
     - Procedural and feature lists formatted into soft-colored rounded mini-cards (`tcolorbox`) with bold titles rather than monotonous dot bullets.
3. **Logo & Placeholder Integration**:
   - Render `primary_institution_logo` in the top banner.
   - If `conference.conference_logo_path` is set, include the image in the configured `conference_logo_position` (default: right side of Title Header). If `conference.reserve_default_conference_logo_space: true` and no image path is provided, render a clean dashed/bordered TikZ node (`[ Conference Logo ]`) reserving that exact space.
   - Render any `branding.extra_logos` (images or reserved placeholders) in their configured zones (default: right side of the Footer Block).
4. **Compile & Inspect PDF**:
   - Compile `poster.pdf` (`pdflatex -interaction=nonstopmode -output-directory=posters/<poster-name> posters/<poster-name>/poster.tex`) and generate `preview_poster.png`.

### Pathway B: Direct LLM PowerPoint (`.pptx`) Generation (`"pptx"` in `deliverables.formats`)
When PowerPoint output is requested (either standalone or alongside LaTeX):
1. **Direct Ephemeral Generation (No Committed Python Script in Poster Folder)**:
   - The LLM directly generates `posters/<poster-name>/poster.pptx` by running `python-pptx` ephemerally (via a temporary script in `<appDataDir>/brain/<conversation-id>/scratch/` or inline `python -c`) and **removes any temporary script afterward**, leaving only the clean `poster.pptx` deliverable inside `posters/<poster-name>/`.
2. **A0 Portrait Canvas & Native Shapes**:
   - Set exact 1-slide A0 Portrait dimensions (`33.11" × 46.81"` / `84.1 × 118.9 cm`).
   - Build all cards, rounded sub-cards (`MSO_SHAPE.ROUNDED_RECTANGLE`), metric callout badges, headers, and footers as native editable PowerPoint shapes.
   - Maintain explicit font sizing on runs: Title $\ge 54\,\text{pt}$, Section Headers $26\text{--}30\,\text{pt}$, Sub-card headings $22\,\text{pt}$, Body text $18.5\text{--}22\,\text{pt}$.
3. **High-DPI Image & QR Code Assurance**:
   - Ensure every placed raster graphic (logo, hero infographic, QR code) achieves $\ge 150\text{--}300$ effective print DPI ($\text{pixel width} / \text{placed inches}$). If an infographic raster is below threshold at full-banner width, upscale cleanly with Lanczos resampling + unsharp mask in memory before inserting into the slide.
   - Render a crisp, high-resolution QR code PNG (`assets/qr_<slug>.png`, $\ge 300\,\text{DPI}$) for the target URL in `provenance.md`.
4. **Logo & Placeholder Rendering**:
   - Place `primary_institution_logo` in the top banner.
   - If `conference.conference_logo_path` or `conference.reserve_default_conference_logo_space: true` is declared in `provenance.md`, narrow the Title/Subtitle width on the right and add either the conference logo picture or a styled rounded placeholder card (`[ Conference Logo ]`) in the configured `conference_logo_position`.
   - Place any `branding.extra_logos` (pictures or placeholder badges) in their configured zones (default: Footer Bar right).
5. **Zero-Overlap & Aligned Bottom Baseline Guarantee**:
   - Ensure all column cards start and end at the exact same vertical coordinates ($y_{\text{top}}$ and $y_{\text{bottom}}$), and all lowest inner sub-cards across columns terminate at the same horizontal baseline.
   - Ensure sibling shapes inside a container card never overlap each other.

### Step 5B: Automated Visual Inspection & 4-Point Visual QA
Inspect the rendered visual output (`preview_poster.png` and/or `.pptx` shape geometry):
1. **Bottom Baseline Alignment**: Verify that all columns terminate at the exact same horizontal baseline. No column should leave an empty bottom void.
2. **Dead Whitespace Minimization**: Eliminate dead vertical gaps between the title block, hero infographic, columns, and footer.
3. **Bullet Point Transformation Check**: Ensure no walls of plain dot-bullet items remain unstyled.
4. **Collision & Clipping Verification**: Verify clear separation between title text, conference/extra logo slots, block headers, and QR codes.

### Step 5C: Human Check-in Before Layout Changes (Mandatory HITL Gate)
When visual defects or alignment improvements are detected during inspection:
- **Ping the Author First**: Present a concise summary of the proposed visual modifications via an interactive modal (`ask_question`).
- **Proceed Upon Approval**: Apply the edits and regenerate only after the author confirms the proposed adjustments.

---

## Phase 6: MAR 70/30 Quality Audit, PPTX Technical Audit & 10-Minute Oral Coach

### 1. Automated 4-Dimension MAR & Provenance Quality Audit
Run the automated compliance script on the generated poster (`.tex` or `.pptx`):
```bash
python .agents/skills/poster-design-strategy/scripts/audit_poster_rubric.py posters/<poster-name>/poster.tex
# And/or when PPTX is generated:
python .agents/skills/poster-design-strategy/scripts/audit_poster_rubric.py posters/<poster-name>/poster.pptx
```

The script verifies `posters/<poster-name>/provenance.md` completeness and audits the poster against the **4-Tier Mixed-Approach Rubric (16 points max)**:

| Rubric Dimension | Poor [1] | Sub-par [2] | Acceptable [3] | Exemplary [4] |
| :--- | :--- | :--- | :--- | :--- |
| **1. Organization** | Unstructured flow; abstract included. | Awkward progression; missing RQ/Hypothesis. | Generally organized IMRaD sequence. | Exceptionally clean visual hierarchy; explicit RQ/Hypothesis; no abstract. |
| **2. Poster Design & Visuals** | Visually unengaging; raw tables present. | Weak visuals; raw data tables clutter results. | Functional graphics; pleasant layout. | High figure-to-text ratio; visual schemas replace prose; QR offloads details. |
| **3. Wordiness / Text Density** | $>800$ words (severe overload). | $600\text{--}800$ words (excessive dwell time). | $400\text{--}600$ words (manageable). | **$250\text{--}400$ words** (optimal 30% text budget). |
| **4. Visual Ratio (70/30 Rule)** | Severe violation; wall of text; no hero graphic. | $<50\%$ visual area; text heavy; lacks hero visual. | $\sim 60\%$ visual balance; multiple graphics present. | **$\ge 70\%$ visual dominance**; prominent hero infographic; clean focal figures. |

**Scoring Tiers**:
- **14–16 pts**: Exemplary (Publication / Conference Award Tier)
- **11–13 pts**: Acceptable (Ready for presentation with minor polish)
- **$<11$ pts**: Needs Revision (High risk of attendee disengagement)

### 2. Automated PowerPoint Layout & DPI Audit (When `.pptx` is Generated)
Run the PPTX technical auditor:
```bash
python posters/pptx-workflow/audit_existing_pptx.py posters/<poster-name>/poster.pptx
```
Verify that `POSTER QUALITY SCORE: 100 / 100` is achieved (1 slide, `A0_PORTRAIT` match, 3-column grid detected, 0 overlapping sibling bounding boxes, all embedded images $\ge 150\,\text{DPI}$).

### Mandatory Gate 4: Finalize `provenance.md` Audit Summary
Record the final MAR score (`/ 16`), PPTX quality score (`/ 100`), and word count in `posters/<poster-name>/provenance.md` (`audit_summary` in YAML frontmatter + Section 4 log), and update `poster.status: "audited"`.

---

### 3. The 10-Minute Oral Presentation Coach

Conference poster sessions enforce a **hard 10-minute cap**. Provide the presenter with this synchronized cue sheet:

```
TOTAL PRESENTATION TIME: 10 MINUTES (HARD CAP)
├── 1. Background & Research Question : 1 to 2 Minutes
│   └── Point to context bullets; state the scientific gap; articulate RQ & Prediction.
├── 2. Hero Infographic & Methods     : 2 to 3 Minutes
│   └── Direct attendee to the central hero visual; walk through the core system/pipeline.
├── 3. Results Walkthrough            : 3 to 4 Minutes
│   └── Highlight primary empirical charts; point to effect sizes and p-values.
└── 4. Discussion & Limitations       : 1 to 2 Minutes
    └── State hypothesis verdict; explain mechanism; disclose exactly 1 limitation;
        propose exactly 1 future direction; invite attendee questions.
```

#### Board Interaction Mechanics (The Heather Winslow Method)
- Never read bullet points verbatim; use them as visual anchors while speaking conversationally.
- Point directly to infographic components, data curves, and axis labels as they are introduced.
- Connect specific empirical findings to overarching domain questions to sustain multi-hour audience engagement.

---

## References & Companion Guides

- Provenance & requirements template: [templates/provenance_template.md](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/templates/provenance_template.md)
- Detailed prompt recipes & style presets: [templates/infographic_prompt_templates.md](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/templates/infographic_prompt_templates.md)
- Empirical regression models & cognitive standards: [references/best_practice_guide.md](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/references/best_practice_guide.md)
- Automated MAR & provenance audit script: [scripts/audit_poster_rubric.py](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/scripts/audit_poster_rubric.py)
- Automated PPTX technical audit script: [posters/pptx-workflow/audit_existing_pptx.py](file:///c:/Users/cedricd/Documents/Github/papers/posters/pptx-workflow/audit_existing_pptx.py)
