---
schema_version: "1.0"
poster:
  id: "imdis-marine-term-translations"
  title: "Marine Term Translations (MTT): A Self-Hosted Platform for Multilingual Marine Terminology Interoperability"
  subtitle: "IMDIS 2026 | MULTILINGUAL MARINE VOCABULARIES | FOR DOMAIN TRANSLATORS & ONTOLOGY MAINTAINERS"
  created_at: "2026-10-28T09:44:00+01:00"
  updated_at: "2026-10-28T10:21:00+01:00"
  status: "audited"

deliverables:
  formats:
    - "latex"
    - "pptx"
  canvas:
    preset: "A0_PORTRAIT"
    width_mm: 841
    height_mm: 1189
    width_in: 33.11
    height_in: 46.81
    orientation: "portrait"

audience:
  primary_archetype: "Domain Specialists & Infrastructure Stewards"
  specific_personas:
    - "Domain Experts / Marine Term Translators"
    - "Ontology & Controlled Vocabulary Owners / Maintainers"
  engagement_goal: "Dissemination of Published IMDIS Paper & Live Self-Hosted Platform Onboarding"

authors:
  - name: "Cedric Decruw"
    affiliation: "Flanders Marine Institute (VLIZ), InnovOcean Campus, Ostend, Belgium"
    email: "cedric.decruw@vliz.be"
    orcid: "0000-0001-6387-5988"
    corresponding: true

conference:
  name: "IMDIS 2026 (International Conference on Marine Data and Information Systems)"
  date: "2026"
  location: "IMDIS Conference"
  url: "https://imdis.seadatanet.org/"
  reserve_default_conference_logo_space: true
  conference_logo_path: null
  conference_logo_position: "title_header_right"

branding:
  theme_preset: "VLIZ Marine Institute (#91C8CD)"
  primary_institution_name: "Flanders Marine Institute (VLIZ)"
  primary_institution_url: "vliz.be"
  primary_institution_logo: "assets/vliz_logo.png"
  extra_logos:
    - name: "Partner / Funder Logo 1"
      path: null
      placeholder: true
      position: "footer_right"
    - name: "Partner / Funder Logo 2"
      path: null
      placeholder: true
      position: "footer_right"

inputs:
  source_documents:
    - path_or_url: "https://cedricdcc.github.io/papers/marine-term-translations/marine-term-translations.pdf"
      type: "manuscript"
      description: "Published IMDIS 2026 conference paper PDF"
    - path_or_url: "papers/marine-term-translations/marine-term-translations.md"
      type: "manuscript"
      description: "Local Markdown source of the IMDIS 2026 paper"
    - path_or_url: "https://github.com/marine-term-translations/mtt-self-host-platform"
      type: "repository"
      description: "Open-source self-hosted MTT platform source code (React, Node.js, PostgreSQL)"
    - path_or_url: "https://mtt.vliz.be/"
      type: "platform"
      description: "Live production deployment at Flanders Marine Institute (VLIZ)"
  provided_assets:
    - path: "assets/vliz_logo.png"
      role: "primary_institution_logo"
      description: "Official VLIZ wave logo"
  qr_codes:
    - label: "Live Platform (mtt.vliz.be)"
      url: "https://mtt.vliz.be/"
      asset_path: "assets/qr_mtt_platform.png"
    - label: "IMDIS Paper PDF"
      url: "https://cedricdcc.github.io/papers/marine-term-translations/marine-term-translations.pdf"
      asset_path: "assets/qr_imdis_paper.png"
  key_references:
    - "[1] Wilkinson et al. (2016). FAIR Guiding Principles. Sci. Data 3:160018."
    - "[2] BODC (2024). NERC P02 Parameter Discovery Vocabulary."
    - "[3] Colpaert, Van de Vyvere & Verborgh (2021). Linked Data Event Streams (LDES)."
    - "[4] Decruw (2024). MTT Self-Host Platform: github.com/marine-term-translations/mtt-self-host-platform."
  ai_disclosure: "Assisted with language polish and schematic layout; system design and evaluation by the author."

audit_summary:
  mar_score: "15 / 16 (93.8%) [pptx] | 14 / 16 (87.5%) [tex] — EXEMPLARY (Publication / Conference Award Tier)"
  pptx_score: "100 / 100"
  estimated_word_count: 408
---

# Poster Provenance & Requirements Log

## 1. Phase 1: Strategic Discovery & Requirements Intake

- **Target Audience & Personas**:
  - **Domain Experts (Marine Term Translators)**: Need a frictionless, browser-based side-by-side translation interface with AI-assisted drafting, human review gates, and citable ORCID attribution—without touching raw RDF/SKOS or unstructured spreadsheets.
  - **Ontology / Vocabulary Owners & Maintainers**: Need sovereign self-hostable infrastructure (React, Node.js, PostgreSQL), zero concept URI churn, standards-compliant exports (CSV, SKOS, JSON-LD), and continuous Linked Data Event Streams (LDES) synchronization.
- **Conference & Logo Allocation**:
  - **Target Event**: `IMDIS 2026 (International Conference on Marine Data and Information Systems)`
  - **Conference Logo Slot**: Reserved placeholder box (`[ IMDIS 2026 Logo ]`) in the right side of the Title Header zone (`title_header_right`).
  - **Extra Partner / Funder Logos**: Reserved placeholder slots in the right side of the Footer Bar (`footer_right`).
- **Captured Source Inputs**:
  - IMDIS Paper PDF: `https://cedricdcc.github.io/papers/marine-term-translations/marine-term-translations.pdf` (local source: `papers/marine-term-translations/marine-term-translations.md`)
  - Source Code Repository: `https://github.com/marine-term-translations/mtt-self-host-platform`
  - Live Platform: `https://mtt.vliz.be/`

---

## 2. Phase 2: Distilled Scientific Narrative (30% Text Budget: 250–400 Words)

- **Background & Context Bullets (2–4 points)**:
  1. Marine data infrastructures (SeaDataNet, EMODnet, BODC NVS) depend on English-first controlled vocabularies, while multilingual maintenance relies on fragmented spreadsheets and ad hoc scripts.
  2. Static snapshot harvesting causes synchronization lag, duplicated effort, and concept URI drift across distributed marine catalogs.
- **Explicit Research Question (RQ)**:
  - *How can marine institutions run a sovereign, end-to-end multilingual terminology workflow that engages domain translators while publishing machine-actionable, standards-compliant updates?*
- **Explicit Hypothesis / Prediction**:
  - *Decoupling persistent concept identity from mutable language labels within an ORCID-governed, LDES-enabled web platform accelerates translation without URI churn or full-dump overhead.*
- **Methods & Architecture Overview**:
  - Self-hosted open-source stack (`mtt-self-host-platform`: React UI, Node.js REST API, PostgreSQL) with ORCID authentication, AI-assisted candidate drafting, human-in-the-loop review gates, and dual exports (CSV, SKOS, JSON-LD + continuous LDES RDF streams).
- **Key Quantitative / Empirical Results (BODC P02 Beta)**:
  - **25% BODC P02 Translated**: Validated Dutch & French translations published as live LDES streams.
  - **2× Drafting Velocity**: AI-assisted suggestions accelerated first-pass batch curation while keeping human reviewers in control.
  - **0 URI Churn**: Persistent NERC concept URIs remained immutable across iterative multilingual updates.
- **Discussion & Future Outlook**:
  - **Hypothesis Verdict**: Supported — end-to-end continuity from expert translation to live LDES stream synchronization proven in beta operation.
  - **1 Study Limitation**: Translation throughput remains bounded by domain-expert reviewer capacity.
  - **1 Actionable Future Direction**: Add automated confidence analytics and configurable policy triage to prioritize expert review queues.

---

## 3. Phase 4: Layout Wireframe & Hero Infographic Provenance

- **Selected Layout Option**: `Option 2: Central Hero Showcase + 2x2 Flanking Persona Grid`
- **Approved ASCII Wireframe**:
  ```text
  +-------------------------------------------------------------------------+
  | [ TOP SEA-TEAL BANNER (#91C8CD): VLIZ Wave Logo (Left) | vliz.be ]      |
  +-------------------------------------------------------------------------+
  | [ SUBTITLE, MAIN TITLE & AUTHOR (Cedric Decruw) ]   [ IMDIS 2026 LOGO ] |
  +-----------------------------------+-------------------------------------+
  | [ 1. CONTEXT, RQ & HYPOTHESIS ]   | [ 2. BODC P02 BETA RESULTS ]        |
  | • English-only vocab bottleneck   | [ 25% P02 NL/FR ] [2x] [0 Churn]    |
  | • Explicit RQ & Hypothesis        | • Verdict, 1 Limitation, 1 Outlook  |
  +-----------------------------------+-------------------------------------+
  |   ===================================================================   |
  |   |          DOMINANT CENTRAL HERO INFOGRAPHIC (~48% AREA)          |   |
  |   |     1. Ingest RDF LDES -> 2. Curated Translation (mtt.vliz.be)  |   |
  |   |     -> 3. Publish Enriched LDES -> 4. vocab.vliz.be Web Widget  |   |
  |   ===================================================================   |
  +-----------------------------------+-------------------------------------+
  | [ 3. FOR MAINTAINERS & TRANSLATORS| [ 4. WIDGET REUSE & DUAL QR CODES ] |
  | • Self-Host Stack & LDES Sync     | • vocab.vliz.be Same-URI Widget     |
  | • Side-by-Side UI, AI + ORCID     | • [ QR 1: mtt.vliz.be ] [ QR 2: PDF]|
  +-----------------------------------+-------------------------------------+
  | [ FOOTER: References [1-4] & AI Disclosure ]  [ PARTNER LOGO SLOTS 1&2 ]|
  +-------------------------------------------------------------------------+
  ```
- **Hero Infographic Generation Log**:
  - **Asset Path**: `assets/imdis-mtt-ldes-hero.png` (`1322 x 652` after tight top-margin auto-crop)
  - **Aspect Ratio & Zone**: `16:9 Wide Banner` in Central Hero Showcase
  - **Master Prompt Used**:
    ```text
    4-stage left-to-right data pipeline diagram on a pure solid white (#FFFFFF) background using the Flanders Marine Institute (VLIZ) color palette (#91C8CD, #31B7BC, #3057A5, #002B49):
    Stage 1: "1. Ingest RDF LDES Feed" (BODC P02 / RDF LDES Stream — Consumes upstream RDF LDES feeds)
    Stage 2: "2. Curated Translation (mtt.vliz.be)" (MTT Self-Host Platform: Ontology Maintainers + Domain Translators + AI Suggestions -> ORCID Expert Review Gate -> EN/NL/FR tags)
    Stage 3: "3. Publish Enriched LDES" (Enriched RDF LDES & SKOS / JSON-LD — Publishes curated translations as LDES feed)
    Stage 4: "4. vocab.vliz.be Web Widget" (Multilingual dropdown EN/NL/FR converging to "Same Persistent Concept URI" — Any language label resolves to the same URI)
    ```
  - **HITL Refinement Notes**: Approved on `v1` with tight top-margin auto-crop applied.

---

## 4. Phase 5 & 6: Deliverable Generation & Quality Audit Log

- **Generated Deliverables**:
  - `posters/imdis-marine-term-translations/poster.tex` (LaTeX `tikzposter` source, A0 Portrait `841 x 1189 mm`)
  - `posters/imdis-marine-term-translations/poster.pdf` (Compiled print-ready vector PDF)
  - `posters/imdis-marine-term-translations/preview_poster.png` (300 DPI PNG visual proof)
  - `posters/imdis-marine-term-translations/poster.pptx` (Native editable PowerPoint deck, A0 Portrait `33.11" x 46.81"`, generated via ephemeral memory/scratch execution with no residual `.py` builder script)
- **Visual Refinement & Alignment Verification (Phase 5B / 5C)**:
  - Verified exact column baseline lock via `pymupdf` (`page.get_drawings()`):
    - Top 2-column band: Left card `h = 202.14 mm`, Right card `h = 202.14 mm` (`0.00 mm` delta).
    - Bottom 2-column band: Left card `h = 188.49 mm`, Right card `h = 188.50 mm` (`0.01 mm` delta).
- **MAR 70/30 Rubric Audit (`audit_poster_rubric.py`)**:
  - `poster.pptx`: **15 / 16 (93.8%) — EXEMPLARY (Publication / Conference Award Tier)** (`408 words`, 4 visual graphic assets, Hero Infographic present, Abstract excluded, RQ & Hypothesis detected, Dual QR codes present, 1 Limitation, 1 Future Direction, Provenance verified).
  - `poster.tex`: **14 / 16 (87.5%) — EXEMPLARY (Publication / Conference Award Tier)** (`453 words` including LaTeX/TikZ markup tokens, all 11 empirical checklist gates `[OK]`, Provenance verified).
- **PowerPoint Technical Audit (`audit_existing_pptx.py`)**:
  - `poster.pptx`: **100 / 100** (1 slide, `A0_PORTRAIT` `33.11" x 46.81"`, 0 text overlaps, 0 boundary overflows, 4 embedded images at `769.7`, `232.9`, `400.0`, and `400.0 DPI`).


