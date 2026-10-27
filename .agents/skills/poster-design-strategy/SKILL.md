---
name: poster-design-strategy
description: Visual layout, strategic content distillation, template selection, and oral presentation coaching for scientific research posters based on empirical research communication standards. Use when designing, restructuring, or auditing scientific posters to maximize attendee engagement and avoid cognitive overload.
---

# Poster Design Strategy & Best Practice Skill

This skill guides researchers through end-to-end strategy, precision distillation, human-in-the-loop (HITL) layout selection, AI-powered infographic generation via Nano Banana 2, and oral presentation delivery for scientific conference posters.

It operationalizes the empirical findings of **Khadka & Peeters (2024)**, enforces the **70/30 Infographic Rule** (70% visual storytelling vs. 30% concise text), and targets standard **A0 Portrait ($841 \times 1189\,\text{mm}$)** orientation to maximize engagement while eliminating cognitive overload.

---

## Workflow Overview

When designing, restructuring, or pair programming with an author to build a poster, execute this **6-Phase Workflow**:

```
[ Phase 1: Strategic Discovery: Audience, Venue & Asset Intake ]
  - 4-Pillar Intake: Audience Archetype -> Engagement Goal -> Physical A0 Constraints -> Asset Inventory
                                │
                                ▼
[ Phase 2: Paper Intake & Precision Distillation ]
  - Enforce the 30% Text Budget: Strictly 250–400 words total across the board
  - Enforce Section Architecture: 2–4 context bullets, explicit RQ & Hypothesis,
    visual methods, focal results (zero raw tables), 1 limitation, 1 future direction, QR code
                                │
                                ▼
[ Phase 3: 70/30 Infographic Architecture & Visual Planning ]
  - Visual narrative decomposition: Translate the core research argument into a dominant visual representation
  - Style & theme selection (VLIZ Marine Institute #91C8CD, Ecology, Biomed, Tech)
                                │
                                ▼
[ Phase 4: Human-in-the-Loop (HITL) Layout & Infographic Creation ]
  - Step 4A: Present 2 tailored A0 Portrait ASCII wireframes with explicit 70/30 spatial allocations
  - Step 4B: Author selects or adjusts block positions before any code generation
  - Step 4C: Interactive Nano Banana Infographic Creator Loop (iterative visual refinement until approved)
                                │
                                ▼
[ Phase 5: Template & Generation Coordination ]
  - Render in LaTeX (tikzposter, baposter, beamerposter) or PPTX targeting A0 Portrait
  - Enforce typographic hierarchy (dual-font rule) and color accessibility
                                │
                                ▼
[ Phase 6: MAR 70/30 Quality Audit & 10-Minute Oral Coach ]
  - Audit against the 4-tier, 4-dimension Mixed-Approach Rubric (16 points max)
  - Generate a synchronized 10-minute oral presentation cue sheet
```

---

## Phase 1: Strategic Discovery: Audience, Venue & Asset Intake

Before proposing layouts or writing code, interview the author across the **4 Discovery Pillars**:

1. **Audience Archetype**:
   - **Domain Specialists**: High-density scientific terminology allowed; emphasize novel methodology, nuanced statistical distributions, and fine-grained mechanisms.
   - **Interdisciplinary Researchers**: Avoid niche jargon; clearly define acronyms; emphasize broad cross-disciplinary implications and conceptual frameworks.
   - **Stakeholders / Policy / Industry / Public**: Focus on practical utility, macro-level impact, economic/environmental consequences, and bold visual takeaways.

2. **Engagement Goal**:
   - **Conference Award / Competition**: High-polish visual execution, full adherence to empirical rubric, seamless oral pitch.
   - **Academic Networking / Early Feedback**: Prominent research question, explicit limitation, designated "Feedback Wanted" discussion prompts.
   - **Dissemination of Published Paper**: Central hero infographic summarizing paper conclusions, scannable QR code directly to DOI/pre-print.

3. **Physical Venue Constraints**:
   - **Standard Canvas**: Fixed default is **A0 Portrait ($841 \times 1189\,\text{mm}$ / $33.1 \times 46.8\,\text{in}$)**.
   - **Viewing Geometry**: Eye-level focal band is 130–170 cm from the floor. Hero graphics and key findings must occupy this central band; secondary references and acknowledgments remain at the lower perimeter.

4. **Asset & Brand Inventory**:
   - **Available Visuals**: Existing vector plots, raw photos, GIS maps, or need for generative schematic synthesis.
   - **Institutional Branding**: Color schemes (e.g., Flanders Marine Institute VLIZ Sea-teal `#91C8CD`, university colors), logos, and grant acknowledgment badges.
   - **Digital Destinations**: Companion URLs for QR codes (GitHub repository, interactive dataset, pre-print PDF).

---

## Phase 2: Paper Intake & Precision Distillation

Apply the **10-10 Rule**: Attendees scan from 10 feet for 10 seconds. The target word count for the entire board is strictly **250 to 400 words** (never exceeding 500 words) to protect the 70/30 visual balance.

### Hybrid Intake
- **If a manuscript exists** (`papers/*.md` or provided PDF): Auto-extract and distill the 6 mandatory sections according to the rules below, presenting the distilled draft to the author for approval.
- **If starting from scratch**: Conduct a focused interview to populate each block.

### Mandatory Section Architecture Rules

1. **Title Block**:
   - Informative, descriptive headline highlighting primary discovery or key variables.
   - Full author names, institutional affiliations, and corresponding email.
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
   - **1 to 3 high-value figures** showcasing primary data trends.
   - Brief standalone descriptive caption below every figure.
   - Bullet points highlighting statistical findings ($p$-values, effect sizes).
   - **PROHIBITIONS**: Zero raw data tables; zero narrative literature interpretation.
5. **Discussion & Mechanisms**:
   - Clear statement: Was the hypothesis supported or refuted?
   - Explanatory mechanism (chemical, physical, biological, or computational).
   - Broad domain-level implications.
   - **Exactly ONE major study limitation**.
   - **Exactly ONE actionable future direction** directly addressing that limitation.
6. **Supplemental & Digital Integration**:
   - **2 to 5 key references** cited in-text.
   - Mandatory AI / super-intelligence tool disclosures.
   - **Scannable QR code** ($\beta = +0.12$) linking to the full paper, dataset, or video.

---

## Phase 3: 70/30 Infographic Architecture & Visual Planning

Under the **70/30 Rule**, 70% of the poster's physical surface area is dedicated to visual storytelling, while 30% is allocated to concise descriptive text.

### Visual Narrative Decomposition
Help the author deconstruct their study into three visual layers:
1. **The Hero Infographic**: A dominant, high-impact visual representation of the project (e.g. system architecture, experimental workflow, spatial transect, or biological pathway) occupying 40–50% of the total board area.
2. **Supporting Empirical Figures**: 1–2 focused data plots, maps, or charts occupying 20–30% of the board area.
3. **Generous Whitespace**: 40–50% negative space inside and around the visual graphics to ensure comfortable visual parsing from 3–10 feet.

### Selecting Domain Style Presets
Consult [templates/infographic_prompt_templates.md](templates/infographic_prompt_templates.md) to select a curated theme:
- **VLIZ Marine Institute**: Sea-teal (`#91C8CD`), Deep Ocean Navy (`#002B49`), clean marine vector accents.
- **Ecology & Environment**: Forest green (`#2D5A27`), Earth ochre (`#C29B38`), River teal (`#2B7A78`).
- **Biomedical & Genomics**: Okabe-Ito colorblind-accessible palette (`#2A4D69`, `#D55E00`, `#56B4E9`).
- **Modern Tech / AI / Systems**: Electric Indigo (`#4361EE`), Tech Cyan (`#4CC9F0`), Slate Grey (`#334155`).

---

## Phase 4: Human-in-the-Loop (HITL) Layout & Infographic Creation

### Step 4A: Present 2 Tailored A0 Portrait ASCII Wireframes
Always present **two tailored ASCII options** explicitly annotated with 70/30 spatial allocations:

#### Option 1: Top Hero Banner + Dual-Column Flow (70% Visual / 30% Text)
```
+-------------------------------------------------------------+
| [ TITLE BLOCK: Project Title, Authors, VLIZ / Affiliations ]|
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
| • Explicit Hypothesis        | | Map Visual               | |
|                              | +--------------------------+ |
| [ METHODS SUMMARY: 10% AREA ]| • Statistical Key Findings   |
| • System, Variables, n       | • p-values & Effect Sizes    |
| • Setup Micro-Diagram        +------------------------------+
+------------------------------+ [ DISCUSSION & TAKEAWAY: 5% ]|
| [ REFERENCES & DISCLOSURES ] | • Hypothesis Supported?      |
| • 2-3 Citations              | • 1 Limitation & 1 Outlook   |
| • AI Disclosure              | [ QR CODE ]                  |
+------------------------------+------------------------------+
  Spatial Budget: ~70% Visual Assets & Negative Space | ~30% Text
```

#### Option 2: Central Hero Box + Flanking Context (70% Visual / 30% Text)
```
+-------------------------------------------------------------+
| [ TITLE BLOCK: Project Title, Authors, VLIZ / Affiliations ]|
+------------------------------+------------------------------+
| [ CONTEXT & HYPOTHESIS: 15% ]| [ RESULTS HIGHLIGHT: 20% ]   |
| • 2-3 Literature Bullets     | +--------------------------+ |
| • Research Question (RQ)     | | Key Finding Chart        | |
| • Explicit Prediction        | +--------------------------+ |
| • Study Variables & n        | • Effect size & trend summary|
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
| • Specimen / Model Specs     | • 1 Constraint | 1 Next Step |
| • Key Reference Citations    | • [ QR CODE TO DATA / PAPER ]|
+------------------------------+------------------------------+
  Spatial Budget: ~70% Visual Assets & Negative Space | ~30% Text
```

### Step 4B: Author Approval & Layout Adjustment
Prompt the author:
> *"Here are two tailored 70/30 layout architectures for your A0 portrait poster. Which option best fits your narrative flow, or would you like to adjust the block arrangement before we generate the infographic and code?"*

### Step 4C: Interactive Nano Banana Infographic Creator Loop
Once the layout is approved, launch the iterative visual creator loop using [templates/infographic_prompt_templates.md](templates/infographic_prompt_templates.md):

1. **Assemble Master Prompt**:
   - Incorporate the approved layout zone geometry (`16:9` wide banner, `1:1` square, or `3:4` vertical).
   - Apply the selected domain theme preset (e.g. VLIZ Marine `#91C8CD`).
   - Enforce negative constraints (zero prose, no figure numbers, 50% white space).
2. **Execute Generation**:
   ```bash
   python .agents/skills/scientific-schematics/scripts/generate_schematic.py \
     "<assembled_prompt>" \
     -o posters/<poster-name>/figures/hero_infographic.png \
     --doc-type poster \
     --iterations 2
   ```
3. **Interactive HITL Feedback Step**:
   - Present the generated image path and visual summary to the author.
   - Ask for direct critique:
     - *"Does this visual representation accurately reflect your project?"*
     - *"Are the theme colors and element weights balanced?"*
   - Iteratively refine prompt and regenerate until the author confirms they are completely satisfied with the result.

---

## Phase 5: Template & Generation Coordination

Once the infographic is approved and the layout locked in:

1. **Select & Configure Template**:
   - **LaTeX (`tikzposter`, `baposter`, `beamerposter`)**: For vector precision and publication typography. Set document options to `a0paper, portrait`.
   - **PowerPoint (`.pptx`)**: Set slide dimensions strictly to $84.1\,\text{cm} \times 118.9\,\text{cm}$ (A0 Portrait).
2. **Enforce Strict Typographic Hierarchy**:
   - **Dual-Font Rule**: Bold sans-serif header font paired with clean body font.
   - **Font Sizes (A0 scale)**:
     - Poster Title: $\ge 50\,\text{pt}$ (readable from 15 feet).
     - Section Headings: $\ge 32\,\text{pt}$ (readable from 8–10 feet).
     - Body Text: $\ge 22\,\text{pt}$ (readable from 3–6 feet).
     - Infographic Labels: $\ge 80\,\text{pt}$ (readable from 3–6 feet).
     - Infographic Key Metrics: $\ge 120\,\text{pt}$.
3. **Color Accessibility & Contrast**:
   - Dark text on light background; zero red-green pairings.
4. **Compile & Build**:
   ```bash
   make posters
   ```

---

## Phase 6: MAR 70/30 Quality Audit & 10-Minute Oral Coach

### Automated 4-Dimension MAR Quality Audit
Run the automated compliance script:
```bash
python .agents/skills/poster-design-strategy/scripts/audit_poster_rubric.py posters/<poster-name>/poster.tex
```

The script audits the poster against the **4-Tier Mixed-Approach Rubric (16 points max)**:

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

---

### The 10-Minute Oral Presentation Coach

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
│   └── State hypothesis verdict; explain mechanism; disclose exactly 1 limitation;
│       propose exactly 1 future direction; invite attendee questions.
```

#### Board Interaction Mechanics (The Heather Winslow Method)
- Never read bullet points verbatim; use them as visual anchors while speaking conversationally.
- Point directly to infographic components, data curves, and axis labels as they are introduced.
- Connect specific empirical findings to overarching domain questions to sustain multi-hour audience engagement.

---

## References & Companion Guides

- Detailed prompt recipes & style presets: [templates/infographic_prompt_templates.md](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/templates/infographic_prompt_templates.md)
- Empirical regression models & cognitive standards: [references/best_practice_guide.md](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/references/best_practice_guide.md)
- Automated audit script: [scripts/audit_poster_rubric.py](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/scripts/audit_poster_rubric.py)
