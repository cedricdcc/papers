---
schema_version: "1.0"
poster:
  id: "REPLACE_ME_POSTER_SLUG"
  title: "REPLACE_ME_POSTER_TITLE"
  subtitle: "REPLACE_ME_SUBTITLE_OR_TOPIC"
  created_at: "REPLACE_ME_ISO_DATE"
  updated_at: "REPLACE_ME_ISO_DATE"
  status: "intake" # intake | distilled | layout_approved | generated | audited

deliverables:
  formats:
    - "latex" # Options: "latex", "pptx" (include one or both)
  canvas:
    preset: "A0_PORTRAIT"
    width_mm: 841
    height_mm: 1189
    width_in: 33.11
    height_in: 46.81
    orientation: "portrait"

audience:
  primary_archetype: "REPLACE_ME_ARCHETYPE" # Domain Specialists | Interdisciplinary Researchers | Stakeholders / Policy / Public
  specific_personas:
    - "REPLACE_ME_PERSONA_1"
    - "REPLACE_ME_PERSONA_2"
  engagement_goal: "REPLACE_ME_GOAL" # Conference Award | Academic Networking & Feedback | Dissemination of Published Paper/Platform

authors:
  - name: "REPLACE_ME_AUTHOR_NAME"
    affiliation: "REPLACE_ME_INSTITUTION_AND_ADDRESS"
    email: "REPLACE_ME_EMAIL"
    orcid: "REPLACE_ME_ORCID"
    corresponding: true

conference:
  name: "REPLACE_ME_CONFERENCE_NAME"
  date: "REPLACE_ME_CONFERENCE_DATE"
  location: "REPLACE_ME_CONFERENCE_LOCATION"
  url: "REPLACE_ME_CONFERENCE_URL"
  reserve_default_conference_logo_space: false # true to reserve a placeholder box for a conference logo
  conference_logo_path: null # Relative path (e.g. "assets/conf_logo.png") or null
  conference_logo_position: "title_header_right" # title_header_right | top_banner_right | footer_right

branding:
  theme_preset: "VLIZ Marine Institute (#91C8CD)" # VLIZ Marine Institute | Ecology & Environment | Biomedical & Genomics | Modern Tech / AI
  primary_institution_name: "Flanders Marine Institute (VLIZ)"
  primary_institution_url: "vliz.be"
  primary_institution_logo: "assets/vliz_logo.png"
  extra_logos: []
  # Example extra_logos items:
  # - name: "European Union / Horizon Europe"
  #   path: "assets/eu_logo.png" # or null if placeholder
  #   placeholder: false
  #   position: "footer_right" # footer_right | top_banner_right | title_header_right

inputs:
  source_documents:
    - path_or_url: "REPLACE_ME_SOURCE_PAPER_OR_DOC"
      type: "manuscript" # manuscript | repository | dataset | slides | interview_notes
      description: "Primary scientific source material"
  provided_assets:
    - path: "assets/vliz_logo.png"
      role: "primary_institution_logo"
      description: "Official institutional vector/high-res logo"
  qr_codes:
    - label: "REPLACE_ME_QR_LABEL"
      url: "REPLACE_ME_QR_TARGET_URL"
      asset_path: "assets/qr_code.png"
  key_references:
    - "[1] REPLACE_ME_REFERENCE_1"
    - "[2] REPLACE_ME_REFERENCE_2"
  ai_disclosure: "Assisted with language polish and schematic layout; system design and evaluation by the author."

audit_summary:
  mar_score: null # e.g. "15 / 16 (93.8%) - EXEMPLARY"
  pptx_score: null # e.g. "100 / 100" (when pptx is generated)
  estimated_word_count: null
---

# Poster Provenance & Requirements Log

## 1. Phase 1: Strategic Discovery & Requirements Intake

- **Target Audience & Personas**: Describe how terminology density and visual framing are calibrated for the target audience.
- **Conference & Logo Allocation**:
  - **Target Event**: `REPLACE_ME_CONFERENCE_NAME`
  - **Conference Logo Slot**: Specify whether a dedicated conference logo or reserved placeholder box is included in the header/title zone.
  - **Extra Partner / Funder Logos**: List any additional project, partner, or grant logos and their assigned layout zones.
- **Captured Source Inputs**: Summarize the manuscripts, repositories, datasets, or user answers used as ground truth.

---

## 2. Phase 2: Distilled Scientific Narrative (30% Text Budget: 250–400 Words)

- **Background & Context Bullets (2–4 points)**:
  1. `REPLACE_ME_CONTEXT_1`
  2. `REPLACE_ME_CONTEXT_2`
- **Explicit Research Question (RQ)**:
  - *`REPLACE_ME_RESEARCH_QUESTION`*
- **Explicit Hypothesis / Prediction**:
  - *`REPLACE_ME_HYPOTHESIS`*
- **Methods & Architecture Overview**:
  - `REPLACE_ME_METHODS_SUMMARY`
- **Key Quantitative / Empirical Results**:
  - `REPLACE_ME_KEY_METRICS_AND_FINDINGS`
- **Discussion & Future Outlook**:
  - **Hypothesis Verdict**: `REPLACE_ME_VERDICT`
  - **1 Study Limitation**: `REPLACE_ME_LIMITATION`
  - **1 Actionable Future Direction**: `REPLACE_ME_FUTURE_DIRECTION`

---

## 3. Phase 4: Layout Wireframe & Hero Infographic Provenance

- **Selected Layout Option**: `Option 1 (Top Hero Banner + Columns)` or `Option 2 (Central Hero Box + Flanking Context)`
- **Approved ASCII Wireframe**:
  ```text
  [Paste approved ASCII wireframe with 70/30 spatial allocation and logo slots]
  ```
- **Hero Infographic Generation Log**:
  - **Asset Path**: `assets/hero_infographic.png`
  - **Aspect Ratio & Zone**: `16:9 Wide Banner` / `1:1 Central Box` / `3:4 Vertical`
  - **Master Prompt Used**:
    ```text
    [Record exact Nano Banana 2 prompt used]
    ```
  - **HITL Refinement Notes**: Record author feedback and iterations (`v1 -> v2`).

---

## 4. Phase 5 & 6: Deliverable Generation & Quality Audit Log

- **Generated Deliverables**:
  - LaTeX: `poster.tex` / `poster.pdf` (if selected)
  - PowerPoint: `poster.pptx` (if selected — generated directly via ephemeral `python-pptx` execution without leaving a build script in the poster folder)
- **MAR 70/30 Rubric Audit**:
  - Organization: `X / 4`
  - Poster Design & Visuals: `X / 4`
  - Wordiness / Text Density: `X / 4`
  - Visual-to-Text Ratio (70/30 Rule): `X / 4`
  - **Composite MAR Score**: `XX / 16`
- **PowerPoint Technical Audit** (if `.pptx` generated):
  - **PPTX Compliance Score**: `100 / 100`
  - **Effective Image DPIs**: Record audited DPIs (`>= 150-300 DPI`)

