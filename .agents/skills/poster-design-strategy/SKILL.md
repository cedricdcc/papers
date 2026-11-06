---
name: poster-design-strategy
description: Visual layout, strategic content distillation, provenance tracking, template selection (LaTeX and/or PowerPoint .pptx), and oral presentation coaching for scientific research posters based on empirical research communication standards. Use when designing, restructuring, or auditing scientific posters to maximize attendee engagement and avoid cognitive overload.
---

# Poster Design Strategy & Best Practice Skill

This skill guides researchers through end-to-end strategy, structured provenance capture (`provenance.md`), precision distillation, **4-Layer Visual Magnet Architecture**, human-in-the-loop (HITL) layout selection, AI-powered infographic generation via Nano Banana 2, multi-format rendering (**LaTeX `.tex/.pdf`**, **PowerPoint `.pptx`**, or **Both**), and oral presentation delivery for scientific conference posters.

It operationalizes the empirical findings of **Khadka & Peeters (2024)**, enforces the **70/30 Infographic Rule** (70% visual storytelling vs. 30% concise text), eliminates sterile "box-in-a-box" rigidity via a **10-Foot Visual Magnet Architecture**, tracks complete project requirements and decision provenance in `posters/<poster-name>/provenance.md`, and targets standard **A0 Portrait ($841 \times 1189\,\text{mm}$)** orientation to maximize engagement while eliminating cognitive overload.

---

## Workflow Overview

When designing, restructuring, or pair programming with an author to build a poster, execute this **6-Phase Workflow** with incremental provenance persistence at every gate:

```
[ Phase 1: Strategic Discovery, Deliverable Format, Branding/Motifs & Provenance Intake ]
  - 6-Pillar Interview (via ask_question): Deliverable Format (LaTeX | PPTX | Both) ->
    Audience & Personas -> Authors List -> Conference & Default Logo Space ->
    Branding, Extra Logos & Domain Background Motif (bathymetry, network_mesh, topography,
    molecular, or hybrid) -> Captured Source Inputs & QR Targets
  - Persist Gate 1: Create posters/<poster-name>/provenance.md from template
                                │
                                ▼
[ Phase 2: Paper Intake & Precision Distillation ]
  - Enforce the 30% Text Budget: Strictly 250–400 words total across the board
  - Enforce Section Architecture: 2–4 context bullets, explicit RQ & Hypothesis,
    visual methods, focal results (zero raw tables), 1 limitation, 1 future direction, QR code
  - Draft 5-to-7-word 10-Foot Billboard Hook Pill headline
  - Persist Gate 2: Update provenance.md (Section 2: Distilled Scientific Narrative)
                                │
                                ▼
[ Phase 3: 70/30 Infographic Architecture & 4-Layer Visual Magnet Planning ]
  - Layer 0: Atmospheric Canvas & Header Vector Motifs (12–15% header texture; 4–8% canvas watermark)
  - Layer 1: Borderless "Breakout" Hero Stage & 10-Foot Billboard Hook Pill
  - Layer 2: Cross-Board Visual Conduit (Title -> Hero Stage -> Central Column Spine -> QR Card)
  - Layer 3: Tactile UI Card Elevation (6pt left-accent bars, soft shadows, clean typographic hierarchy; zero AI icon spam)
                                │
                                ▼
[ Phase 4: Human-in-the-Loop (HITL) Layout & Infographic Creation ]
  - Step 4A: Present 2 tailored A0 Portrait ASCII wireframes with explicit 70/30 spatial allocations,
    Borderless Hero Stage + Billboard Hook Pill, Cross-Board Conduit, and Logo slots
  - Step 4B: Author selects or adjusts block positions before any code generation
  - Step 4C: Interactive Nano Banana Infographic Creator Loop (enforcing Seamless Stage Integration
    with #FFFFFF / #F4F9FA edge matching, zero outer boxes, and horizontal transit flow ribbon)
  - Persist Gate 3: Update provenance.md (Section 3: Wireframe & Infographic Prompt Log)
                                │
                                ▼
[ Phase 5: Template & Generation Coordination (LaTeX and/or Direct LLM PPTX) ]
  - Render in LaTeX (tikzposter, baposter, beamerposter), PowerPoint (.pptx), or Both targeting A0 Portrait
  - Programmatically render Z-Index 0 Vector Watermarks, Borderless Hero Stage + Hook Pill,
    Cross-Board Conduit Lines, and Tactile Left-Accent Sub-Cards
  - Enforce MAR Typography & Card-Fill Discipline (sans-serif >=22pt body copy, giant 44-54pt metric
    numbers, ragged-right anti-orphan text, content-fitted cards with zero hollow vertical voids)
  - For PPTX: LLM generates posters/<poster-name>/poster.pptx directly via ephemeral python-pptx
    execution in scratch/memory and cleans up (no per-poster .py build script committed in poster folder)
  - Render Conference Logo (or reserved placeholder box) and Extra Logos in configured zones
                                │
                                ▼
[ Phase 6: MAR 70/30 Quality Audit, Anti-Boxiness/Typography Gate & 10-Minute Oral Coach ]
  - Audit against the 4-tier, 4-dimension Mixed-Approach Rubric (16 points max) + provenance check
  - Verify Contrast, Anti-Boxiness, Typography Scale & Anti-AI Icon Restraint Gate (>= 7:1 WCAG AAA
    contrast; <= 8% canvas watermark opacity; zero \tiny/\scriptsize text; zero AI icon/glyph spam)
  - If PPTX generated: Run audit_existing_pptx.py (target 100/100 score, >=150-300 DPI, 0 sibling
    overlaps with Z-Order layer whitelisting for bg_motif_*, conduit_*, hero_stage_*, hook_pill_*, accent_bar_*)
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

5. **Institutional Branding, Domain Background Motif & Extra Logos List**:
   - **Theme & Primary Brand**: Curated color preset (e.g., Flanders Marine Institute VLIZ Sea-teal `#91C8CD`, corporate navy `#3057A5`), primary institutional logo (`assets/vliz_logo.png`), and primary domain URL (`vliz.be`).
   - **Domain Background Motif Selection (`visual_magnet.canvas_motif` & `header_motif`)**:
     - Select the programmatic Z-Index 0 vector motif that pairs with the domain or institutional brand (motifs can be decoupled from the color palette for interdisciplinary work, such as combining VLIZ marine colors with a hybrid wave + semantic node-mesh motif):
       - `bathymetry_waves`: Bathymetric depth contours, acoustic sonar arcs, and oceanic wave harmonics.
       - `network_mesh`: Isometric node-link constellation meshes and metro-circuit traces (ideal for Semantic Web, Linkset, AI, and Data Architecture posters).
       - `hybrid_wave_mesh`: VLIZ wave harmonics in the top banner paired with subtle node-link constellation meshes and bathymetric contours in the canvas margins.
       - `topography`: Topographic elevation isolines or botanical leaf venation vectors.
       - `molecular`: Abstract double-helix ribbons or cellular Voronoi tessellations.
   - **Extra Partner / Funder / Project Logos List (`extra_logos`)**:
     - Ask if any additional logos (e.g., Horizon Europe, EMODnet, partner universities, grant badges) must be included or have placeholder slots reserved.
     - Record each extra logo's `name`, `path` (or `placeholder: true`), and configurable placement zone (default: `footer_right` in the Footer Bar, or `top_banner_right` / `title_header_right`).

6. **Captured Source Inputs & Digital Destinations**:
   - **Source Material**: Local manuscript paths (`papers/<name>/<name>.md`), PDFs, GitHub repositories, datasets, or interview notes used to derive the poster content.
   - **Available Visuals**: Existing vector plots, photos, GIS maps, or need for Nano Banana 2 schematic synthesis.
   - **QR Code Targets**: Companion URLs and labels for scannable QR codes (live platform, GitHub repo, DOI/pre-print, dataset).
   - **References & Disclosures**: 2–5 key literature citations and mandatory AI tool disclosure text.

### Mandatory Gate 1: Initialize `posters/<poster-name>/provenance.md`
Immediately upon collecting the Phase 1 answers, create `posters/<poster-name>/provenance.md` by copying [templates/provenance_template.md](templates/provenance_template.md) and populating the YAML frontmatter (`poster`, `deliverables`, `audience`, `authors`, `conference`, `branding`, `visual_magnet`, `inputs`) and Section 1 notes. Never leave `REPLACE_ME_*` tokens in completed fields.

---

## Phase 2: Paper Intake & Precision Distillation

Apply the **10-10 Rule**: Attendees scan from 10 feet for 10 seconds. The target word count for the entire board is strictly **250 to 400 words** (never exceeding 500 words) to protect the 70/30 visual balance.

### Hybrid Intake
- **If a manuscript exists** (`papers/*.md` or provided PDF): Auto-extract and distill the 6 mandatory sections plus the **5-to-7-word Billboard Hook Pill** according to the rules below, presenting the distilled draft to the author for approval.
- **If starting from scratch**: Conduct a focused interview to populate each block.

### Mandatory Section Architecture Rules

1. **Title Block & 10-Foot Billboard Hook Pill**:
   - Informative, descriptive headline highlighting primary discovery or key variables.
   - **10-Foot Billboard Hook Pill**: A high-contrast, 5-to-7-word uppercase callout badge (e.g., `"FROM SILOED GUESSWORK TO AUTONOMOUS WEB MAPS"`) that crowns the top center of the Borderless Hero Stage.
   - Author attribution: Bold or underline the presenting/corresponding author; group co-authors in a clean, slightly lighter typographical weight to maintain clear visual dominance for the title.
   - Conference logo or reserved `[ Conference Logo ]` placeholder box on the right side of the Title Header zone if enabled in `provenance.md`.
2. **Background & Context (Condensed Introduction)**:
   - **Strictly 2 to 4 concise points** citing seminal literature.
   - **Tactile Left-Accent Mini-Cards (Zero AI Icon Spam)**: Prohibit plain unstyled bullet walls; format points as tactile mini-cards with 6pt colored left-accent borders, soft drop shadows, and bold sans-serif headers. **Never prepend artificial icon badges, emojis, or decorative Unicode symbols (`◈`, `⬡`, `⚡`, `🔗`, `▸`, `[!]`, `[?]`, `\vicon`) to card headers.**
   - What is known $\rightarrow$ The specific scientific gap.
   - **Explicit Statement of Research Question (RQ)**.
   - **Explicit Statement of Hypothesis or Prediction**.
   - **PROHIBITIONS**:
     - Never paste an abstract text block ($\beta = -0.10$ negative impression driver).
     - Never insert redundant italic section sub-headers directly beneath a numbered section banner (e.g., `1. Context...` followed immediately by `The Interoperability Bottleneck in Open Science:`). Let the section header and mini-cards carry the structure.
     - Never print floating, raw duplicate URLs in body text that mirror the QR code destination.
3. **Methods & Architectural Pillars**:
   - State study system, experimental approach, independent/dependent variables, sample size ($n$), or strategic framework pillars.
   - **Visual Anchor**: Anchored by a visual experimental setup diagram, pipeline flowchart ($\beta = +0.15$), or an even **$2 \times 2$ grid of tactile mini-cards** for 4-element structures (e.g., 4 Strategic Pillars), avoiding monotonous stacked text bars. Use clean typographic numerals (`01`–`04` or `1.`–`4.`) for sequential pillars rather than cartoon/Unicode icons.
4. **Results Visualization & Empirical Metrics (The Focal Point)**:
   - **1 to 3 high-value figures** or **bold metric callout badges** showcasing primary data trends.
   - **Giant Metric Callout Scale**: In metric callout badges, render the primary quantitative number in **giant bold sans-serif ($42\text{--}54\,\text{pt}$, e.g. `\fontsize{44}{48}\selectfont\bfseries`)** paired with a concise bold label ($20\text{--}22\,\text{pt}$) so the numbers command attention from 10 feet without artificial icon clutter.
   - Standalone figure captions strictly limited to **$\le 12\text{--}15$ words** stating the single core takeaway (zero duplication of hypothesis or discussion prose).
   - **Empirical Metric Credibility Rule**:
     - Metric badges must represent **verifiable, empirical quantities** (e.g., `80% Time Reclaimed`, `10 Patterns`, `5 Standards United`, `3 Reference Tools`, sample size $n$, effect sizes, $p$-values, or runtime speedups).
     - **PROHIBITION**: Never use humorous, subjective, or ironic metrics (e.g., `0 Bottlenecks`, `Max Boredom`, `100% Happiness`) in empirical metric slots; they undermine scientific credibility and peer review rigor.
     - **Deduplication Rule**: Never duplicate statistics between metric badges and adjacent body bullets (e.g., stating "80% of their time" in a bullet next to an "80% Time Reclaimed" badge).
   - **PROHIBITIONS**: Zero raw data tables; zero narrative literature interpretation.
5. **Discussion, Mechanisms & Takeaways**:
   - Clear statement: Was the hypothesis supported or refuted?
   - Explanatory mechanism (chemical, physical, biological, or computational).
   - Broad domain-level implications.
   - **Analogy & Legend Integration**: Merge explanatory analogies (e.g., transit map navigation metaphors) and visual legends directly into the hero figure rather than consuming dedicated text cards.
   - **Exactly ONE major study limitation**.
   - **Exactly ONE actionable future direction** directly addressing that limitation.
6. **Supplemental, Extra Logos & Digital Integration**:
   - **2 to 5 key references** cited in-text.
   - Mandatory AI / super-intelligence tool disclosures.
   - **Scannable QR code** ($\beta = +0.12$) linking to the full paper, dataset, or live platform, anchored in a dedicated bottom card where the Cross-Board Visual Conduit terminates. **Size the QR code generously ($\ge 55\%\text{--}65\%$ of the QR card height, e.g. $6.0\text{--}6.6\,\text{cm}$ on A0)** with $\ge 20\,\text{pt}$ (`\small`) domain/repository labels—never leave a tiny QR code floating inside an empty card with micro-text.
   - **Extra Partner / Funder Logos** rendered as clean monochrome/themed badges in the Footer Bar (or configured zone).
   - **Baseline Alignment & Card-Fill Rule**: Ensure all columns terminate at the exact same horizontal baseline without dead vertical voids, and size sub-cards to fit their typography naturally ($65\%\text{--}85\%$ internal fill) rather than forcing tall hollow white boxes around small text.

### Mandatory Gate 2: Update `provenance.md` (Distilled Narrative)
Once the author approves the distilled content, write the finalized bullets, Billboard Hook Pill text, RQ, Hypothesis, Methods summary, Results metrics, Limitation, and Future Direction into Section 2 of `posters/<poster-name>/provenance.md` and set `poster.status: "distilled"`.

---

## Phase 3: 70/30 Infographic Architecture & 4-Layer Visual Magnet Planning

Under the **70/30 Rule**, 70% of the poster's physical surface area is dedicated to visual storytelling, while 30% is allocated to concise descriptive text.

### Visual Narrative Decomposition
Help the author deconstruct their study into three spatial components:
1. **The Hero Infographic**: A dominant, high-impact visual representation of the project (e.g. system architecture, experimental workflow, spatial transect, or biological pathway) occupying 40–50% of the total board area.
2. **Supporting Empirical Figures & Metric Badges**: 1–2 focused data plots, maps, or tactile metric callout badges occupying 20–30% of the board area.
3. **Generous Whitespace**: 40–50% negative space inside and around the visual graphics to ensure comfortable visual parsing from 3–10 feet.

### Visual Magnet & Atmospheric Architecture (The "10-Foot X-Factor")
To prevent sterile "box-on-white-paper" layouts ("dashboard screenshot syndrome"), every poster must incorporate **four layered visual hooks** across Z-Indices 0 through 3:

1. **Layer 0 (Z-Index 0): Atmospheric Canvas & Header Vector Motif**:
   - **Header Banner Texture**: Overlay a subtle programmatic domain vector pattern at **$12\%\text{--}15\%$ opacity** across the top institutional/title banner zone (e.g., harmonic wave isolines or geometric circuit traces).
   - **Canvas Watermark**: Render a large, ultra-faint vector motif at **$4\%\text{--}8\%$ opacity** in the background canvas corners/margins (strictly behind container cards; never reducing text contrast below $7:1$ WCAG AAA).
   - **Preset Motif Mapping (Decouplable from Color Palette)**:
     - *VLIZ Marine Institute*: Bathymetric depth contours, acoustic sonar arcs, or oceanic wave isolines in Sea-teal (`#91C8CD`) / Navy (`#3057A5`).
     - *Ecology & Environment*: Topographic elevation lines or botanical leaf venation vectors.
     - *Biomedical & Genomics*: Abstract double-helix ribbons or cellular Voronoi tessellations.
     - *Modern Tech / AI / Systems*: Isometric node-link constellation meshes or metro-circuit traces (ideal for Linkset / Web Architecture posters; can be combined with VLIZ wave headers as `hybrid_wave_mesh`).
2. **Layer 1 (Z-Index 1): Borderless "Breakout" Hero Stage & 10-Foot Billboard Hook Pill**:
   - **Anti-Box Hero Stage**: Never trap the Hero Infographic inside a heavy rectangular border box. Match or alpha-blend its outer background (`#FFFFFF` or soft sea-tint `#F4F9FA`) into a full-bleed or borderless stage band so the visual floats seamlessly across the A0 canvas.
   - **Billboard Hook Pill**: Crown the top center of the Hero Stage with a high-contrast pill badge (`#002B49` Deep Navy fill, white $26\text{--}28\,\text{pt}$ bold uppercase typography, teal accent border) delivering a 5-to-7-word walk-by hook (e.g., `"FROM SILOED GUESSWORK TO AUTONOMOUS WEB MAPS"`).
3. **Layer 2 (Z-Index 2): Cross-Board Visual Conduit**:
   - Draw a continuous programmatic vector path (e.g., an extension of a London Tube transit line or ocean current streamline) that originates at the **Title Block**, flows into the **Hero Infographic**, travels down the **central column spine** (with station nodes branching into Sections 1–4 so it never crosses behind body text), and terminates directly at the bottom-right **Digital Companion QR Code Card**.
4. **Layer 3 (Z-Index 3): Tactile UI Card Elevation, MAR Typography Scale & Anti-AI Icon Restraint**:
   - **Tactile Left-Accent Cards**: Upgrade plain rounded rectangles (`tcolorbox` / `MSO_SHAPE.ROUNDED_RECTANGLE`) with **6pt (`0.18 in`) solid colored left-accent borders**, soft elevation drop shadows, and solid 100% opaque white interiors (`#FFFFFF`) to shield body text.
   - **Anti-AI Icon Restraint Rule**: **Never decorate sub-card titles or metric cards with synthetic Unicode symbols (`◈`, `⬡`, `⚡`, `🔗`, `▸`, `◀`, `▶`), emojis, or artificial mini-icon boxes (`[!]`, `[?]`, `[#]`, `\vicon`).** Overusing decorative icons makes scientific posters look "AI-generated" and cluttered. Rely on the 6pt colored left-accent bar, clean sans-serif hierarchy, giant `42–54pt` metric numerals, and simple typographic numbers (`01`–`04` or `1.`–`4.`) only where sequence matters.
   - **MAR Typography Scale, Ragged-Right Alignment & Card-Fill Rule**:
     - **Clean Sans-Serif Mandatory**: Enforce a modern sans-serif typeface (`\renewcommand{\familydefault}{\sfdefault}` with `helvet`/`lmodern` in LaTeX; `Calibri`/`Arial` in PPTX) across the entire poster. Never allow LaTeX to fall back to default Computer Modern Roman serif inside sub-cards.
     - **Minimum Font Scale**: At A0 scale (`25pt` base in `tikzposter`), set sub-card titles to `\normalsize\bfseries` (`24–25pt`) and sub-card body text to `\small` (`20.5–22pt`). **Strictly prohibit `\footnotesize` (`17pt`), `\scriptsize` (`14pt`), and `\tiny` (`12pt`) inside narrative cards, 4-Pillar cards, or QR cards** ($\le 18\,\text{pt}$ reserved strictly for footer references/disclosures).
     - **Ragged-Right Anti-Orphan Alignment**: Format narrow sub-card prose with `\raggedright` (`\hyphenpenalty=10000 \exhyphenpenalty=10000`) to prevent awkward hyphenated word breaks (`end-points`, `monop-olies`) and single-word orphan lines (`Drift.`). Reserve horizontal centering strictly for the Billboard Hook Pill, giant Metric Callout numbers, and the QR Code stack.
     - **Natural Card-Fill Balance ($65\%\text{--}85\%$)**: Never force a short 2-line sentence into a tall fixed-height container (`height=6.2cm` or `height=13cm`) that leaves $50\%+$ empty white void inside the card. Size card heights dynamically to their content (`equal height group` per row in `tcolorbox`) and distribute vertical spacing evenly between cards.

### Selecting Domain Style Presets
Consult [templates/infographic_prompt_templates.md](templates/infographic_prompt_templates.md) to select a curated theme:
- **VLIZ Marine Institute**: Sea-teal (`#91C8CD`), Deep Ocean Navy (`#002B49`), Corporate Navy (`#3057A5`), Vibrant Teal (`#31B7BC`), Soft Sea Stage (`#F4F9FA`).
- **Ecology & Environment**: Forest green (`#2D5A27`), Earth ochre (`#C29B38`), River teal (`#2B7A78`).
- **Biomedical & Genomics**: Okabe-Ito colorblind-accessible palette (`#2A4D69`, `#D55E00`, `#56B4E9`).
- **Modern Tech / AI / Systems**: Electric Indigo (`#4361EE`), Tech Cyan (`#4CC9F0`), Slate Grey (`#334155`).

---

## Phase 4: Human-in-the-Loop (HITL) Layout & Infographic Creation

### Step 4A: Present 2 Tailored A0 Portrait ASCII Wireframes
Always present **two tailored ASCII options** explicitly annotated with 70/30 spatial allocations, the **4-Layer Visual Magnet elements** (`Layer 0 Motif`, `Billboard Hook Pill`, `Borderless Hero Stage`, `Cross-Board Conduit`), AND the configured **Conference Logo / Placeholder slot** and **Extra Logos slots** from `provenance.md`:

#### Option 1: Top Borderless Hero Stage + Central Conduit Spine (70% Visual / 30% Text)
```
+-------------------------------------------------------------+
| [ TOP BANNER (Layer 0 Wave Texture 14%): Logo | URL ]       |
+-------------------------------------------------------------+
| [ TITLE BLOCK: Subtitle, Title, Authors ]   [ CONF. LOGO /  |
| (Bold Presenting Author; Lighter Co-Authors)  PLACEHOLDER ] |
+-----------------------------o-------------------------------+
|        [ BILLBOARD HOOK PILL: 5-7 WORD WALK-BY HOOK ]       |
|   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   |
|     BORDERLESS HERO INFOGRAPHIC STAGE (#F4F9FA / #FFFFFF)   |
|       (~42-45% TOTAL POSTER AREA - ZERO OUTER BOX)          |
|     High-impact visual with horizontal flow stream          |
|       [ Pill Caption: <=12-word core visual takeaway ]      |
|   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   |
+-----------------------------|-------------------------------+
| [ 1. CONTEXT & RQ / HYP. ]  o--[ 2. METHODS & 4 PILLARS ]   |
| • Left-Accent Tactile Cards |  +------------+-------------+ |
| |▌ Research Question (RQ)   |  |▌ 01 Pillar |▌ 02 Pillar  | |
| |▌ Hypothesis Statement     |  +------------+-------------+ |
|                             |  |▌ 03 Pillar |▌ 04 Pillar  | |
| [ 3. EMPIRICAL ROI METRICS] o  +------------+-------------+ |
| [▌Metric 1] [▌Metric 2]     |  |▌ Separation of Concerns  | |
| [▌Metric 3] [▌Metric 4]     |  +--------------------------+ |
| |▌ Verifiable Outcome Card  |  [ 4. DISCUSSION & ACCESS ]   |
|  (Layer 0 Faint Corner      |  |▌ Verdict, 1 Limit, 1 Next  |
|   Watermark 4-6% Opacity)   +--o-> [ QR CODE COMPANION ]    |
+-------------------------------------------------------------+
| [ FOOTER: References [1-4] | AI Disclosure | Partner Badges ]|
+-------------------------------------------------------------+
  Spatial Budget: ~70% Visual Assets & Negative Space | ~30% Text
  4-Layer Visual Magnet: Layer 0 Motif + Layer 1 Borderless Hero + Layer 2 Spine Conduit + Layer 3 Tactile Cards
```

#### Option 2: Central Breakout Hero Stage + Chronological Conduit Flow (70% Visual / 30% Text)
```
+-------------------------------------------------------------+
| [ TOP BANNER (Layer 0 Wave Texture 14%): Logo | URL ]       |
+-------------------------------------------------------------+
| [ TITLE BLOCK: Subtitle, Title, Authors ]   [ CONF. LOGO /  |
| (Bold Presenting Author; Lighter Co-Authors)  PLACEHOLDER ] |
+-----------------------------o-------------------------------+
| [ 1. CONTEXT & RQ: 15% ]    |  [ 2. HYPOTHESIS & SETUP:15% ]|
| |▌ 2-3 Tactile Mini-Cards   o--|▌ Explicit Hypothesis Card  |
| |▌ Research Question Card   |  |▌ Conceptual Setup Card     |
+-----------------------------|-------------------------------+
|        [ BILLBOARD HOOK PILL: 5-7 WORD WALK-BY HOOK ]       |
|   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   |
|     BORDERLESS PROJECT HERO INFOGRAPHIC STAGE (~45% AREA)   |
|     Seamless edge-blended canvas with horizontal conduit    |
|       [ Pill Caption: <=12-word core visual takeaway ]      |
|   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   |
+-----------------------------|-------------------------------+
| [ 3. METHODS & PILLARS:15% ]o--[ 4. RESULTS & ACCESS: 20% ] |
| |▌ 2x2 Tactile Pillar Grid  |  • Verifiable Metric Badges   |
| |▌ Implementation Toolchain |  |▌ Verdict, 1 Limit, 1 Next  |
|                             +--o-> [ QR CODE COMPANION ]    |
+-------------------------------------------------------------+
| [ FOOTER: References & AI Disclosure | Partner Badges ]      |
+-------------------------------------------------------------+
  Spatial Budget: ~70% Visual Assets & Negative Space | ~30% Text
  *Chronology Rule*: Top quadrants setup the study; bottom quadrants deliver results and discussion.
  Never place Results or Discussion above the Hero Infographic.
```

### Step 4B: Author Approval & Layout Adjustment
Prompt the author:
> *"Here are two tailored 70/30 layout architectures incorporating the 4-Layer Visual Magnet Architecture and your configured logo slots. Which option best fits your narrative flow, or would you like to adjust the block arrangement before we generate the infographic and poster?"*

### Step 4C: Interactive Infographic Creator & Multi-Modal Self-Critique Loop
Once the layout is approved, launch the iterative visual creator loop using [templates/infographic_prompt_templates.md](templates/infographic_prompt_templates.md):

1. **Assemble Master Prompt (Eliminating Style Clash, Boxiness & Text Hallucinations)**:
   - Target zone geometry (`16:9` wide banner, `1:1` square, or `3:4` vertical).
   - Apply domain theme preset (e.g. VLIZ Marine Sea-teal `#91C8CD`, Deep Navy `#002B49`, Corporate Navy `#3057A5`).
   - **Seamless Stage Integration (Anti-Box Rule)**:
     - Specify a pure, uniform outer background (`#FFFFFF` or soft sea-tint `#F4F9FA`) with **zero outer border frames, drop-shadow boxes, or cropped edges** so the graphic blends invisibly into the A0 canvas stage.
     - Include a subtle background flow ribbon (e.g., glowing teal-to-navy horizontal transit stream) spanning from left to right to act as the poster's central visual magnet.
     - Post-process or alpha-blend outer margins if needed so there is zero visible rectangular bounding seam against the Hero Stage band.
   - **Unified Vector Aesthetic**: Enforce a coherent 2D flat vector aesthetic across all stages/panels. Prohibit mixing disparate illustration styles (e.g., cartoon sketches on one side and 3D renders on the other).
   - **Prohibit 3D Glass / Cramped Containers**: Prohibit pseudo-3D glass cubes, translucent volumetric blocks, or nested flowchart boxes with micro-text labels inside. Replace with crisp 2D node-and-link signposts.
   - **Eliminate Label Redundancy**: Prohibit repeating the exact same label across parallel stacked arrows or lines.
   - **Strict Negative Constraints**: Zero AI prose, no figure numbers, maximum 10 single-word structural labels total. Figure caption strictly $\le 12\text{--}15$ words. Detailed explanations are delegated strictly to LaTeX/PPTX markup.
2. **Execute Generation**:
   Generate publication-grade visual asset using Nano Banana 2 / `generate_image` or `scientific-schematics`.
3. **Multi-Modal AI Self-Critique**:
   Before presenting to the author, inspect the image to verify:
   - Ample whitespace ($50\text{--}60\%$ negative space) and seamless edge blending (zero outer frame box).
   - Unified visual style across all stages (zero stylistic clash).
   - Clear left-to-right or top-to-bottom directional conduit.
   - Absence of distorted synthetic pseudo-fonts, repetitive arrow text, or unwanted palette legends.
4. **Interactive HITL Feedback Step (Mandatory Modal Gate)**:
   - Present the image preview to the author using an interactive modal (`ask_question`).
   - Prompt the author for direct feedback:
     - *"Does this visual representation accurately reflect your project?"*
     - *"Are the theme colors, borderless stage blending, element weights, and illustration style balanced and unified?"*
   - **Iterative Refinement Rule**: If the author comments or requests adjustments, regenerate the infographic and present again. Only advance to the next step once the author explicitly approves the visual asset.

### Mandatory Gate 3: Update `provenance.md` (Layout & Infographic Log)
Record the approved ASCII wireframe, the 4-Layer Visual Magnet settings, the final Nano Banana 2 master prompt, asset path, and iteration history in Section 3 of `posters/<poster-name>/provenance.md`, and set `poster.status: "layout_approved"`.

---

## Phase 5: Template & Generation Coordination (LaTeX and/or Direct LLM PPTX)

Check `deliverables.formats` in `posters/<poster-name>/provenance.md` and execute the corresponding generation pathway(s), programmatically encoding all **4 Visual Magnet Layers** without relying on low-res external background rasters:

### Pathway A: LaTeX Poster Generation (`"latex"` in `deliverables.formats`)
1. **Render Template, Sans-Serif Typography & Packages**:
   - Create `posters/<poster-name>/poster.tex` using `tikzposter`, `baposter`, or `beamerposter` targeting A0 Portrait ($841 \times 1189\,\text{mm}$).
   - Load `\usepackage{helvet}` and `\renewcommand{\familydefault}{\sfdefault}` so all headers, sub-cards, and metric badges render in crisp modern sans-serif (never Computer Modern Roman serif).
   - Load `\usetikzlibrary{positioning,calc,arrows.meta,shadows.blur,decorations.pathmorphing}` and `\usepackage[skins]{tcolorbox}`.
2. **Programmatic 4-Layer Visual Magnet & MAR Typography Rules in LaTeX**:
   - **Layer 0 (Canvas & Header Vector Watermarks)**:
     - At the start of `\begin{document}` (on `tikzposter`'s background canvas layer), draw programmatic TikZ domain vectors:
       - Across the top header banner: `\draw[color=white, opacity=0.14, line width=2.2pt]` harmonic bezier wave curves or sonar arcs.
       - In the A0 canvas corners/margins: `\draw[color=vlizTeal, opacity=0.055, line width=1.8pt]` bathymetric depth contours and/or isometric constellation node-link graphs. Keep canvas watermark opacity strictly $\le 0.08$ ($4\%\text{--}6\%$ ideal).
   - **Layer 1 (Borderless Hero Stage & 10-Foot Billboard Hook Pill)**:
     - Never wrap the Hero Infographic in a bordered `\block`. Instead, draw a full-width or soft-edged stage band (`\fill[vlizHeroStage]` using `#F4F9FA` with subtle top/bottom hairline accents and zero vertical box walls), place the seamlessly blended hero graphic, and anchor a centered high-contrast **Billboard Hook Pill** (`\node[fill=vlizDeepNavy, draw=vlizTeal, line width=2pt, rounded corners=14pt, inner xsep=14mm, inner ysep=4.5mm]`) across the top border of the Hero Stage with $26\text{--}28\,\text{pt}$ bold uppercase white text (zero decorative triangles/icons).
   - **Layer 2 (Cross-Board Visual Conduit)**:
     - Draw a continuous programmatic TikZ transit path (`\draw[color=vlizTeal, line width=3.5pt]` paired with `\draw[color=vlizNavy, line width=1.8pt, dashed]` and circular station nodes `\filldraw[fill=white, draw=vlizNavy, line width=2.5pt] ... circle (4.5mm)`) that originates beneath the Title Block, enters the Hero Stage, runs vertically down the **central inter-column spine** with horizontal branch ticks into Sections 1–4, and terminates with an arrowhead at the **Digital Companion QR Code Card**.
   - **Layer 3 (Tactile Left-Accent Sub-Cards, Typography Scale & Anti-AI Icon Restraint)**:
     - Configure all inner `tcolorbox` mini-cards, RQ/Hypothesis cards, 4-Pillar cards, and metric callouts with:
       `enhanced, colback=white, colframe=vlizBorder, boxrule=1pt, borderline west={6pt}{0pt}{vlizNavy}, arc=3.5mm, drop fuzzy shadow={opacity=0.10, shadow xshift=1.2mm, shadow yshift=-1.2mm}` (alternating `vlizNavy` and `vlizTeal` left accent bars) and `fontupper=\small\sffamily\raggedright`.
     - **Typography Scale & Anti-Orphan Rule**: Set sub-card titles to `\normalsize\bfseries` (`25pt`) and body text to `\small\raggedright` (`21pt`, `\hyphenpenalty=10000 \exhyphenpenalty=10000`). **Never use `\footnotesize`, `\scriptsize`, or `\tiny` inside narrative cards or the QR code card.**
     - **Giant Metric Numbers**: In Metric Callout Badges, render the primary statistic in `\fontsize{44}{48}\selectfont\bfseries` (`44pt`) with a `\small\bfseries` (`21pt`) label.
     - **Anti-AI Icon Restraint**: Never define or invoke artificial icon badge macros (`\vicon`) or prepend synthetic symbols to sub-card headers. Use clean typographic numerals (`01`–`04`) only for sequential 4-Pillar cards.
     - **Natural Card-Fill Balance**: Use `equal height group` for side-by-side cards in the same row rather than hardcoded oversized `height=6.2cm` or `height=13cm` parameters that leave hollow white voids inside cards.
3. **Logo, Large QR Companion & Placeholder Integration**:
   - Render `primary_institution_logo` in the top banner.
   - If `conference.conference_logo_path` is set, include the image in the configured `conference_logo_position` (default: right side of Title Header). If `conference.reserve_default_conference_logo_space: true` and no image path is provided, render a clean dashed/bordered TikZ node (`[ Conference Logo ]`) reserving that exact space.
   - Render the **Digital Companion QR Code** at large, scannable dimensions ($\ge 6.0\text{--}6.6\,\text{cm}$ wide, occupying $\ge 55\%\text{--}65\%$ of its card height) with `\small\bfseries` (`21pt`) domain labels.
   - Render any `branding.extra_logos` (images or reserved placeholders) in their configured zones (default: right side of the Footer Block).
4. **Compile & Inspect PDF**:
   - Compile `poster.pdf` (`pdflatex -interaction=nonstopmode -output-directory=posters/<poster-name> posters/<poster-name>/poster.tex`) and generate `preview_poster.png`.

### Pathway B: Direct LLM PowerPoint (`.pptx`) Generation (`"pptx"` in `deliverables.formats`)
When PowerPoint output is requested (either standalone or alongside LaTeX):
1. **Direct Ephemeral Generation (No Committed Python Script in Poster Folder)**:
   - The LLM directly generates `posters/<poster-name>/poster.pptx` by running `python-pptx` ephemerally (via a temporary script in `<appDataDir>/brain/<conversation-id>/scratch/` or inline `python -c`) and **removes any temporary script afterward**, leaving only the clean `poster.pptx` deliverable inside `posters/<poster-name>/`.
2. **A0 Portrait Canvas & MAR Font Scale**:
   - Set exact 1-slide A0 Portrait dimensions (`33.11" × 46.81"` / `84.1 × 118.9 cm`).
   - Maintain explicit sans-serif font sizing (`Calibri` / `Arial`) on runs: Title $\ge 54\,\text{pt}$, Section Headers $26\text{--}30\,\text{pt}$, Billboard Hook Pill $26\text{--}28\,\text{pt}$, Giant Metric Numbers $42\text{--}48\,\text{pt}$, Sub-card headings $22\text{--}24\,\text{pt}$, Sub-card body & QR labels **$20\text{--}22\,\text{pt}$** (never $<20\,\text{pt}$ in narrative or QR cards; footer references $\ge 18\,\text{pt}$).
3. **Programmatic 4-Layer Visual Magnet Rules in `python-pptx`**:
   - **Z-Index 0 Background Shapes (`bg_motif_*`)**:
     - Before drawing foreground column cards, generate native decorative vector shapes (`MSO_SHAPE.WAVE`, concentric `MSO_SHAPE.OVAL` sonar/bathymetric rings, and node-connector lines) named with the prefix `bg_motif_` at ultra-low opacity ($\le 7\%$ opacity on canvas; $12\text{--}15\%$ in header banner) in the header banner and canvas margins.
   - **Z-Index 1 Borderless Hero Stage & Billboard Hook Pill (`hero_stage_*` & `hook_pill_*`)**:
     - Place a full-width soft accent band (`#F4F9FA` with zero outer border, named `hero_stage_band`) behind the seamlessly blended Hero Infographic, and overlay a pill-shaped `MSO_SHAPE.ROUNDED_RECTANGLE` (`#002B49` Deep Navy fill, `#31B7BC` border, white $26\text{--}28\,\text{pt}$ bold uppercase text, named `hook_pill_badge`) centered across the top border of the Hero Stage.
   - **Z-Index 2 Cross-Board Visual Conduit (`conduit_*`)**:
     - Draw native transit conduit lines and circular station nodes (named with prefix `conduit_`) originating from the Title zone, passing through the Hero Stage, running down the central column spine with branch ticks to each section, and terminating at the bottom-right QR Code Card.
   - **Z-Index 3 Tactile Left-Accent Strips & Anti-AI Icon Restraint (`accent_bar_*`)**:
     - Give every sub-card (`MSO_SHAPE.ROUNDED_RECTANGLE`) a solid 100% opaque white fill (`#FFFFFF`) to shield text legibility and pair it with a narrow `0.18"` (`~13pt`) vertical left-accent bar (`#3057A5` or `#31B7BC`, named `accent_bar_*`) flush against its left edge.
     - **Zero Decorative Unicode Glyphs**: Never prepend decorative Unicode symbols (`◈`, `⬡`, `⚡`, `🔗`, `▸`, `◀`, `▶`) to card titles. Use clean bold sans-serif headers, `01`–`04` numerals for sequential pillars, and giant `42–48pt` numbers inside Metric Callout Badges.
4. **High-DPI Image & Large QR Code Assurance**:
   - Ensure every placed raster graphic (logo, hero infographic, QR code) achieves $\ge 150\text{--}300$ effective print DPI ($\text{pixel width} / \text{placed inches}$).
   - Render a crisp, high-resolution QR code PNG (`assets/qr_<slug>.png`, $\ge 300\,\text{DPI}$) sized generously ($\ge 3.5\text{--}4.0\,\text{in}$ wide) so it fills the Digital Companion card cleanly alongside $20\text{--}22\,\text{pt}$ labels.
5. **Logo, Placeholder, Zero-Overlap & Baseline Guarantee**:
   - Place `primary_institution_logo`, conference logo/placeholder, and `branding.extra_logos` in their configured zones.
   - Ensure all column cards start and end at the exact same vertical coordinates ($y_{\text{top}}$ and $y_{\text{bottom}}$), and all lowest inner sub-cards across columns terminate at the same horizontal baseline with balanced internal card fill ($65\%\text{--}85\%$).

### Step 5B: Automated Visual Inspection & 8-Point MAR Visual QA
Inspect the rendered visual output (`preview_poster.png` and/or `.pptx` shape geometry):
1. **Bottom Baseline Alignment**: Verify that all columns terminate at the exact same horizontal baseline ($\le 0.5\,\text{mm}$ delta). No column should leave an empty bottom void.
2. **Card-Fill Balance & Whitespace Discipline**: Verify that no sub-card is an oversized hollow white box with tiny text floating in the middle. Every card must be filled $65\%\text{--}85\%$ by well-proportioned `20.5–25pt` sans-serif typography, and the QR code must fill $\ge 55\%\text{--}65\%$ of the Digital Companion card height.
3. **Typography Scale, Ragged-Right & Zero-Orphan Check**: Confirm clean sans-serif (`\sffamily`) throughout, giant `42–54pt` metric callout numbers, zero `\footnotesize`/`\scriptsize`/`\tiny` in narrative or QR cards, and ragged-right alignment with zero hyphenated line breaks (`end-points`, `monop-olies`) or single-word orphan lines (`Drift.`).
4. **Anti-AI Icon Restraint & Tactile Card Check**: Ensure every mini-card features its 6pt solid left-accent bar and soft shadow, and verify **zero decorative AI-like icon spam** (no `\vicon` badges, `[!]`, `[?]`, `[#]`, or Unicode symbols `◈`, `⬡`, `⚡`, `🔗`, `▸`).
5. **Redundant Sub-Header Check**: Verify that no numbered section banner is followed by an immediate italic subtitle or secondary header line.
6. **Empirical Metric Credibility Check**: Ensure all metric callout badges display verifiable project metrics (prohibit "Max Boredom", "0 Bottlenecks", etc.).
7. **Collision & Clipping Verification**: Verify clear separation between title text, Billboard Hook Pill, conference/extra logo slots, block headers, and QR codes.
8. **Contrast & Anti-Boxiness Safety Gate**:
   - Verify that the Hero Infographic sits on a borderless stage without a dark rectangular frame trapping it.
   - Verify that all Layer 0 canvas background vector motifs remain strictly $\le 8\%$ opacity under light areas and never cross directly behind small body text without a solid white (`100%` opaque `#FFFFFF`) card container shielding the text ($\ge 7:1$ WCAG AAA contrast).

### Step 5C: Human Check-in Before Layout Changes (Mandatory HITL Gate)
When visual defects or alignment improvements are detected during inspection:
- **Ping the Author First**: Present a concise summary of the proposed visual modifications via an interactive modal (`ask_question`).
- **Proceed Upon Approval**: Apply the edits and regenerate only after the author confirms the proposed adjustments.

---

## Phase 6: MAR 70/30 Quality Audit, PPTX Technical Audit & 10-Minute Oral Coach

### 1. Automated 4-Dimension MAR, Provenance & 4-Layer Visual Magnet Audit
Run the automated compliance script on the generated poster (`.tex` or `.pptx`):
```bash
python .agents/skills/poster-design-strategy/scripts/audit_poster_rubric.py posters/<poster-name>/poster.tex
# And/or when PPTX is generated:
python .agents/skills/poster-design-strategy/scripts/audit_poster_rubric.py posters/<poster-name>/poster.pptx
```

The script verifies `posters/<poster-name>/provenance.md` completeness, checks the **4-Layer Visual Magnet Architecture** (Layer 0 motifs, Layer 1 borderless hero + hook pill, Layer 2 cross-board conduit, Layer 3 tactile left-accent cards), and audits the poster against the **4-Tier Mixed-Approach Rubric (16 points max)**:

| Rubric Dimension | Poor [1] | Sub-par [2] | Acceptable [3] | Exemplary [4] |
| :--- | :--- | :--- | :--- | :--- |
| **1. Organization** | Unstructured flow; abstract included. | Inverted sequence (e.g. Discussion before Hero); missing RQ/Hypothesis. | Generally organized IMRaD sequence. | Exceptionally clean hierarchy; chronological narrative flow; explicit RQ/Hypothesis; no abstract. |
| **2. Poster Design & Visuals** | Visually unengaging; raw tables present. | Plain bullet walls; raw tables; clashing styles or subjective metrics. | Functional graphics; pleasant layout. | High figure-to-text ratio; 4-Layer Visual Magnet (borderless hero, hook pill, conduit, tactile left-accent cards); verifiable metrics; QR offloads details. |
| **3. Wordiness / Text Density** | $>800$ words (severe overload). | $600\text{--}800$ words (excessive dwell time). | $400\text{--}600$ words (manageable). | **$250\text{--}400$ words** (optimal 30% text budget). |
| **4. Visual Ratio (70/30 Rule)** | Severe violation; wall of text; no hero graphic. | $<50\%$ visual area; text heavy; lacks hero visual. | $\sim 60\%$ visual balance; multiple graphics present. | **$\ge 70\%$ visual dominance**; prominent borderless hero infographic; clean focal figures. |

**Scoring Tiers**:
- **14–16 pts**: Exemplary (Publication / Conference Award Tier)
- **11–13 pts**: Acceptable (Ready for presentation with minor polish)
- **$<11$ pts**: Needs Revision (High risk of attendee disengagement)

### 2. Automated PowerPoint Layout, Z-Order Layer Whitelisting & DPI Audit (When `.pptx` is Generated)
Run the PPTX technical auditor:
```bash
python posters/pptx-workflow/audit_existing_pptx.py posters/<poster-name>/poster.pptx
```
- **Z-Order Layer Whitelisting**: `audit_existing_pptx.py` recognizes shapes prefixed with `bg_motif_`, `conduit_`, `hero_stage_`, `hook_pill_`, and `accent_bar_` as deliberate Z-Index 0–3 architectural layers rather than accidental sibling card collisions.
- **Target Verification**: Verify that `POSTER QUALITY SCORE: 100 / 100` is achieved (1 slide, `A0_PORTRAIT` match, multi-column grid detected, 0 overlapping sibling bounding boxes, all 4 Visual Magnet layers verified, all embedded images $\ge 150\,\text{DPI}$).

### Mandatory Gate 4: Finalize `provenance.md` Audit Summary
Record the final MAR score (`/ 16`), PPTX quality score (`/ 100`), 4-Layer Visual Magnet verification status, and word count in `posters/<poster-name>/provenance.md` (`audit_summary` in YAML frontmatter + Section 4 log), and update `poster.status: "audited"`.

---

### 3. The 10-Minute Oral Presentation Coach

Conference poster sessions enforce a **hard 10-minute cap**. Provide the presenter with this synchronized cue sheet:

```
TOTAL PRESENTATION TIME: 10 MINUTES (HARD CAP)
├── 1. Walk-By Hook & Borderless Hero Stage : 2 Minutes
│   └── Point to the 10-Foot Billboard Hook Pill and trace the horizontal flow across
│       the Borderless Hero Infographic.
├── 2. Background & Research Question       : 2 Minutes
│   └── Follow the Cross-Board Visual Conduit to Section 1 tactile mini-cards;
│       state the scientific gap; articulate RQ & Prediction.
├── 3. Methods, Pillars & Empirical Metrics : 4 Minutes
│   └── Trace the conduit station nodes across the 2x2 Pillar Matrix and the
│       verifiable Empirical Metric Callout Badges.
└── 4. Discussion, Limitations & QR Hand-off: 2 Minutes
    └── State hypothesis verdict; disclose 1 limitation & 1 future direction;
        follow the conduit terminus to the Digital Companion QR Card.
```

#### Board Interaction Mechanics (The Heather Winslow Method)
- Never read bullet points verbatim; use them as visual anchors while speaking conversationally.
- Use the **Cross-Board Visual Conduit** as a physical pointer path to guide the attendee's eye from the top Billboard Hook Pill down to the QR code hand-off.
- Connect specific empirical findings to overarching domain questions to sustain multi-hour audience engagement.

---

## References & Companion Guides

- Provenance & requirements template: [templates/provenance_template.md](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/templates/provenance_template.md)
- Detailed prompt recipes & style presets: [templates/infographic_prompt_templates.md](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/templates/infographic_prompt_templates.md)
- Empirical regression models & cognitive standards: [references/best_practice_guide.md](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/references/best_practice_guide.md)
- Automated MAR & provenance audit script: [scripts/audit_poster_rubric.py](file:///c:/Users/cedricd/Documents/Github/papers/.agents/skills/poster-design-strategy/scripts/audit_poster_rubric.py)
- Automated PPTX technical audit script: [posters/pptx-workflow/audit_existing_pptx.py](file:///c:/Users/cedricd/Documents/Github/papers/posters/pptx-workflow/audit_existing_pptx.py)
