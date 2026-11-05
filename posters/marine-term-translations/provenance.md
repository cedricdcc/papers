---
schema_version: "1.0"
poster:
  id: "imdis-marine-term-translations"
  title: "Marine Term Translations (MTT): A Self-Hosted Platform for Multilingual Marine Terminology Interoperability"
  subtitle: "IMDIS 2026 | MULTILINGUAL MARINE VOCABULARIES | FOR DOMAIN TRANSLATORS & ONTOLOGY MAINTAINERS"
  created_at: "2026-10-28T09:44:00+01:00"
  updated_at: "2026-11-04T08:15:00+01:00"
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
    - name: "SeaDataNet"
      role: "partner_standard"
      zone: "footer_right"
    - name: "EMODnet"
      role: "partner_standard"
      zone: "footer_right"
    - name: "BODC NVS"
      role: "partner_standard"
      zone: "footer_right"

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
    - path: "assets/imdis-mtt-ldes-hero.png"
      role: "hero_infographic"
      description: "4-stage continuous LDES semantic pipeline diagram (HD 200 DPI)"
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
  mar_score: "16 / 16 (100.0%) [tex & pptx] — EXEMPLARY (Publication / Conference Award Tier)"
  pptx_score: "100 / 100"
  estimated_word_count: 365
---

# Poster Provenance & Requirements Log

## 1. Phase 1: Strategic Discovery & Requirements Intake

- **Target Audience & Personas**:
  - **Domain Experts (Marine Term Translators)**: Need a frictionless, browser-based side-by-side translation interface with AI-assisted drafting, human review gates, and citable ORCID attribution—without touching raw RDF/SKOS or unstructured spreadsheets.
  - **Ontology / Vocabulary Owners & Maintainers**: Need sovereign self-hostable infrastructure (React, Node.js, PostgreSQL), zero concept URI churn, standards-compliant exports (CSV, SKOS, JSON-LD), and continuous Linked Data Event Streams (LDES) synchronization.
- **Conference & Logo Allocation**:
  - **Target Event**: `IMDIS 2026 (International Conference on Marine Data and Information Systems)`
  - **Conference Logo Slot**: Reserved placeholder box (`[ IMDIS 2026 Logo ]`) in the right side of the Title Header zone (`title_header_right`).
  - **Extra Partner / Funder Logos**: Reserved partner badges (SeaDataNet, EMODnet, BODC NVS) in the right side of the Footer Bar (`footer_right`).
- **Captured Source Inputs**:
  - IMDIS Paper PDF: `https://cedricdcc.github.io/papers/marine-term-translations/marine-term-translations.pdf`
  - Source Code Repository: `https://github.com/marine-term-translations/mtt-self-host-platform`
  - Live Platform: `https://mtt.vliz.be/`
  - Primary Institutional Brand Assets: Flanders Marine Institute (`assets/vliz_logo.png`, Sea-teal `#91C8CD`, Navy `#3057A5`).

---

## 2. Phase 2: Distilled Scientific Narrative (30% Text Budget: 250–400 Words)

- **Background & Context (3 Styled Mini-Cards)**:
  1. **Operational Gap**: Marine data infrastructures (SeaDataNet, EMODnet, BODC NVS) depend on English-first vocabularies, while multilingual maintenance relies on fragmented spreadsheets.
  2. **Sync Lag & Drift**: Periodic static snapshot harvesting causes synchronization lag, duplicated translation effort, and concept URI drift.
  3. **Curator Burnout**: Domain specialists lack dedicated tooling with contextual AI assistance and citable ORCID provenance attribution.
- **Explicit Research Question (RQ)**:
  - *How can marine institutions run a sovereign, end-to-end multilingual terminology workflow that engages domain translators while publishing machine-actionable, standards-compliant updates?*
- **Explicit Hypothesis / Prediction**:
  - *Decoupling persistent concept identity from mutable language labels within an ORCID-governed, LDES-enabled web platform accelerates translation without URI churn or full-dump overhead.*
- **Methods & Dual-Persona Architecture (4 Pillars)**:
  - **1. Sovereign Self-Host Stack**: Open-source React UI, Node.js REST API, and PostgreSQL (`mtt-self-host-platform`).
  - **2. LDES + SKOS/JSON-LD**: Incremental RDF event stream synchronization plus deterministic CSV, SKOS, and JSON-LD exports.
  - **3. Side-by-Side UI + AI**: Distraction-free web interface with contextual AI candidate drafting for human expert validation.
  - **4. ORCID Governance & Triage**: Two-step validation gates and citable ORCID attribution for translation contributions.
  - **Downstream Integration**: `vocab.vliz.be` search widgets where any multilingual label resolves to the exact same persistent Concept URI.
- **Key Quantitative Empirical Results (BODC P02 Beta)**:
  - **25% BODC P02 Translated**: Validated Dutch & French translations published as live incremental LDES streams.
  - **2× Drafting Velocity**: AI suggestions accelerated first-pass curation while maintaining strict human-in-the-loop control.
  - **0 URI Churn**: Persistent NERC concept URIs remained completely immutable across iterative multilingual enrichments.
  - **100% LDES Continuity**: Continuous live stream ingestion and re-publication without periodic snapshot lag.
- **Discussion & Future Outlook**:
  - **Hypothesis Verdict**: Supported — end-to-end continuity from expert translation to live LDES stream synchronization proven in beta operation.
  - **1 Study Limitation**: Translation throughput remains bounded by domain-expert reviewer availability.
  - **1 Actionable Future Direction**: Add automated confidence analytics and configurable policy triage to prioritize expert review queues.

---

## 3. Phase 4: Layout Wireframe & Hero Infographic Provenance

- **Selected Layout Option**: `Option 1: Top-Hero Flow + Multi-Column Narrative (70% Visual / 30% Text)`
- **Approved ASCII Wireframe**:
  ```text
  +-------------------------------------------------------------------------+
  | [ TOP BANNER: VLIZ Logo (Left)                        vliz.be (Right) ] |
  +-------------------------------------------------------------------------+
  | [ TITLE BLOCK: Subtitle, Title, Cedric Decruw ]     [ IMDIS 2026 LOGO ] |
  +-------------------------------------------------------------------------+
  |                                                                         |
  |   ===================================================================   |
  |   |        HERO INFOGRAPHIC: CONTINUOUS LDES SEMANTIC PIPELINE      |   |
  |   |   1. Ingest LDES -> 2. Curation (mtt.vliz.be) -> 3. LDES Stream |   |
  |   |        -> 4. vocab.vliz.be Widget (12-word bold caption)        |   |
  |   ===================================================================   |
  |                                                                         |
  +-------------------------------------+-----------------------------------+
  | [ 1. CONTEXT & CORE PROPOSITION ]   | [ 2. DUAL-PERSONA ARCHITECTURE ]  |
  | • 3 Styled Mini-Cards (Bottleneck)  | +---------------+---------------+ |
  | +---------------------------------+ | | 1. Self-Host  | 2. LDES Sync  | |
  | | Research Question (RQ) Card     | | |    Stack      |    + SKOS     | |
  | +---------------------------------+ | +---------------+---------------+ |
  | +---------------------------------+ | | 3. Side-by-   | 4. ORCID      | |
  | | Hypothesis Statement Card       | | |    Side + AI  |    Governance | |
  | +---------------------------------+ | +---------------+---------------+ |
  |                                     | +-------------------------------+ |
  | [ 3. EMPIRICAL EVALUATION (BODC) ]  | | Downstream Widget Integration | |
  | [ 25% P02 ]   [ 2x Speed ]          | | (Same Persistent Concept URI) | |
  | [ 0 URI Churn][ 100% LDES ]         | +-------------------------------+ |
  |                                     +-----------------------------------+
  | • Live RDF Stream Continuity        | [ 4. DISCUSSION & DIGITAL ACCESS ]|
  |   (Incremental Synchronization)     | • Verdict: Hypothesis Supported   |
  |                                     | • Limitation: Expert Bandwidth    |
  |                                     | • Next: Automated Policy Triage   |
  |                                     | [ DUAL QR: mtt.vliz.be & Paper ]  |
  +-------------------------------------+-----------------------------------+
  | [ FOOTER: References [1-4] | AI Disclosure | Partner Badges ]           |
  +-------------------------------------------------------------------------+
  ```
- **Hero Infographic Generation Log**:
  - **Asset Path**: `assets/imdis-mtt-ldes-hero.png` (HD print scale `5288 x 2608`, Lanczos + unsharp mask, ~180 DPI print resolution)
  - **Aspect Ratio & Zone**: `16:9 Wide Banner` in Top Hero Showcase (~42% canvas height)
  - **Caption**: `Figure 1: Continuous semantic pipeline uniting upstream LDES ingestion, human-AI translation curation, and downstream multilingual widgets.`

---

## 4. Phase 5 & 6: Deliverable Generation & Quality Audit Log

- **Generated Deliverables**:
  - `posters/imdis-marine-term-translations/poster.tex` (LaTeX `tikzposter` source, A0 Portrait `841 x 1189 mm`)
  - `posters/imdis-marine-term-translations/poster.pdf` (Compiled print-ready vector PDF)
  - `posters/imdis-marine-term-translations/preview_poster.png` (Visual proof rendered via PyMuPDF)
  - `posters/imdis-marine-term-translations/poster.pptx` (Native editable PowerPoint deck, A0 Portrait `33.11" x 46.81"`, generated via ephemeral memory execution)
- **PowerPoint Technical Audit (`audit_existing_pptx.py`)**:
  - `poster.pptx`: **100 / 100** (1 slide, `A0_PORTRAIT` `33.11" x 46.81"`, 0 text overlaps, 0 boundary overflows, images $\ge 180\text{--}1154$ DPI).
- **MAR 70/30 Rubric Audit (`audit_poster_rubric.py`)**:
  - `poster.tex`: **16 / 16 (100.0%) — EXEMPLARY (Publication / Conference Award Tier)** (365 words, chronological flow, styled mini-cards, zero redundant sub-headers, verifiable metrics, dual QR codes).
  - `poster.pptx`: **16 / 16 (100.0%) — EXEMPLARY (Publication / Conference Award Tier)** (365 words, 100/100 layout quality, zero collisions).

---

## 5. The 10-Minute Oral Presentation Coach

```text
TOTAL PRESENTATION TIME: 10 MINUTES (HARD CAP)
├── 1. Hook: Central Pipeline Infographic        : 2 Minutes
│   └── Guide attendee directly under the Title Block to Figure 1. Trace the continuous pipeline:
│       from upstream BODC P02 LDES stream, through the mtt.vliz.be workbench, into re-published LDES feeds
│       and live vocab.vliz.be widgets where any language label resolves to the same Concept URI.
├── 2. The Operational Vocabulary Problem & RQ   : 2 Minutes
│   └── Point to Section 1 mini-cards: explain the English-only vocabulary bottleneck, spreadsheet fragmentation,
│       and synchronization lag. Articulate the Research Question and Hypothesis.
├── 3. Dual-Persona Architecture (The 4 Pillars) : 3 Minutes
│   └── Walk through the 2x2 matrix in Section 2:
│       - For Maintainers: Sovereign self-hosted stack and automated LDES + SKOS streaming.
│       - For Translators: Side-by-side UI with AI drafting suggestions and citable ORCID attribution.
│       Highlight the downstream widget integration card.
├── 4. Empirical Evaluation on BODC P02 Beta    : 2 Minutes
│   └── Point to the 4 metric callout badges: 25% P02 in Dutch & French, 2x drafting speedup,
│       0 URI churn, and 100% LDES continuity.
└── 5. Discussion, Limitations & Live QR Access  : 1 Minute
    └── Disclose domain-expert bandwidth limitation, propose automated confidence triage next step,
        and invite listeners to scan the live platform QR (mtt.vliz.be) and paper PDF.
```
