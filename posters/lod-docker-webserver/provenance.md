---
schema_version: "1.0"
poster:
  id: "lod-docker-webserver"
  title: "LOD Docker Webserver: A Multi-Channel Testbed for Linked Data Discovery and Web-Scale Metadata Signposting"
  subtitle: "REPRODUCIBLE NGINX & TYPESCRIPT TESTBED | 30 DISCOVERY CHANNELS | FOR DATA STEWARDS & OPEN SCIENCE"
  created_at: "2026-11-04T13:54:00+01:00"
  updated_at: "2026-11-04T13:54:00+01:00"
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
  primary_archetype: "Interdisciplinary Data Stewards & Open Science Practitioners"
  specific_personas:
    - "Interdisciplinary Data Stewards & Repository Managers"
    - "Open Science Engineers & Web Architects"
    - "Metadata Curators & Crawler Authors"
  engagement_goal: "Dissemination of Published Research & Practical Testbed Deployment"

authors:
  - name: "Cedric Decruw"
    affiliation: "Flanders Marine Institute (VLIZ), InnovOcean Campus, Ostend, Belgium"
    email: "cedric.decruw@vliz.be"
    orcid: "0000-0001-6387-5988"
    corresponding: true

conference:
  name: "Research Presentation / Technical Showcase"
  date: "2026"
  location: "Ostend, Belgium"
  url: "https://vliz.be"
  reserve_default_conference_logo_space: false
  conference_logo_path: null
  conference_logo_position: "title_header_right"

branding:
  theme_preset: "VLIZ Marine Institute (#91C8CD)"
  primary_institution_name: "Flanders Marine Institute (VLIZ)"
  primary_institution_url: "vliz.be"
  primary_institution_logo: "assets/vliz_logo.png"
  extra_logos: []

inputs:
  source_documents:
    - path_or_url: "papers/lod_docker_webserver/lod_docker_webserver.md"
      type: "manuscript"
      description: "Full research manuscript detailing generator pipeline, Nginx serving architecture, and 30-channel taxonomy"
    - path_or_url: "https://github.com/vliz-be-opsci/lod_docker_webserver"
      type: "repository"
      description: "Open-source LOD Docker Webserver repository (TypeScript generator + Nginx Docker compose)"
  provided_assets:
    - path: "assets/vliz_logo.png"
      role: "primary_institution_logo"
      description: "Official VLIZ wave logo"
    - path: "assets/hero_infographic.png"
      role: "hero_infographic"
      description: "Multi-channel LOD discovery testbed architecture & 2x2 taxonomy diagram"
  qr_codes:
    - label: "GitHub Repository"
      url: "https://github.com/vliz-be-opsci/lod_docker_webserver"
      asset_path: "assets/qr_lod_repo.png"
  key_references:
    - "[1] Berners-Lee (2009). Linked Data Design Issues. W3C."
    - "[2] Nottingham (2017). Web Linking. RFC 8288, IETF."
    - "[3] VLIZ Open Science Team (2026). LOD Discovery Testbed: github.com/vliz-be-opsci/lod_docker_webserver."
  ai_disclosure: "Assisted with language polish and schematic layout; system design and evaluation by the author."

audit_summary:
  mar_score: "16 / 16 (100.0%) [tex & pptx] - EXEMPLARY (Publication / Conference Award Tier)"
  pptx_score: "100 / 100"
  estimated_word_count: 396
---

# Poster Provenance & Requirements Log

## 1. Phase 1: Strategic Discovery & Requirements Intake

- **Target Audience & Personas**:
  - **Interdisciplinary Data Stewards & Repository Managers**: Need reliable, standards-based discovery signals (Link headers, HTML metadata, sitemaps) that work across heterogeneous client ecosystems without brittle heuristics.
  - **Open Science Engineers & Web Architects**: Need reproducible containerized infrastructure (Docker, Nginx) demonstrating exact HTTP header delivery, MIME typing, and content negotiation.
  - **Metadata Curators & Crawler Authors**: Require a benchmark environment isolating direct RDF harvesting from expensive inferenced metadata extraction.
- **Conference & Logo Allocation**:
  - **Target Event**: `Research Presentation / Technical Showcase (VLIZ Open Science)`
  - **Conference Logo Slot**: Not required (`reserve_default_conference_logo_space: false`).
  - **Extra Partner / Funder Logos**: None requested.
- **Captured Source Inputs**:
  - Research Manuscript: `papers/lod_docker_webserver/lod_docker_webserver.md`
  - GitHub Repository: `https://github.com/vliz-be-opsci/lod_docker_webserver`
  - Primary Institutional Brand Assets: Flanders Marine Institute (`assets/vliz_logo.png`, Sea-teal `#91C8CD`, Navy `#3057A5`).

---

## 2. Phase 2: Distilled Scientific Narrative (30% Text Budget: 250–400 Words)

- **Background & Context (3 Styled Mini-Cards)**:
  1. **Discovery Fragmentation**: Linked Data adoption is hampered because machine-readable RDF remains buried across disparate HTTP headers, HTML tags, feeds, and catalogs [1].
  2. **Crawler Fragility**: Automated harvesters rely on ad-hoc heuristics and endpoint guessing rather than formal RFC web signposting standards [2].
  3. **Absence of Benchmarks**: No unified testbed previously allowed researchers to isolate and cross-evaluate discovery channels under controlled server semantics [3].
- **Explicit Research Question (RQ)**:
  - *How can containerized server semantics and multi-channel signposting be unified into an inspectable testbed to systematically evaluate Linked Data discovery across resource and domain tiers?*
- **Explicit Hypothesis / Prediction**:
  - *A dual-axis matrix (Location: Resource vs. Domain; Extraction: Direct vs. Inferenced RDF) implemented in an Nginx Docker testbed provides deterministic evaluation across all 30 standard discovery channels.*
- **Methods & Testbed Architecture (4 Strategic Pillars)**:
  - **1. Generator Pipeline**: Staged TypeScript pipeline (`generator/index.ts`) synthesizing 150 pages with multi-format RDF serializations.
  - **2. Containerized Delivery**: Minimal Dockerized Nginx stack on port 8080 exposing explicit CORS, MIME types, and RFC 8288 link headers.
  - **3. Dual-Axis Taxonomy**: 2x2 classification of 30 channels across Location (Resource vs. Domain) and Extraction (Direct vs. Inferenced RDF).
  - **4. Topology Validation**: Complex graph simulation including collections, pagination, circular loops, and reciprocal backlinks.
- **Key Quantitative Empirical Results**:
  - **30 Discovery Channels**: 12 Resource-Direct, 10 Resource-Inferenced, 2 Domain-Direct, and 8 Domain-Inferenced channels formalized.
  - **4 Distinct Quadrants**: Clear confidence gradient enabling clients to prioritize direct RDF before inferenced fallback.
  - **150 Synthetic Pages**: Controlled graph topology validating crawler loop detection, pagination, and traversal integrity.
  - **100% Deterministic Stack**: Single-command Docker runtime (`docker compose up`) guaranteeing zero framework middleware opacity.
- **Discussion & Future Outlook**:
  - **Hypothesis Verdict**: Supported — the 30-channel matrix establishes an authoritative testbed for crawler benchmarking and FAIR compliance validation.
  - **1 Study Limitation**: Automated client crawler scoring logic is not yet fully executed across every synthesized channel.
  - **1 Actionable Future Direction**: Build automated compliance test suites that benchmark real-world harvesters against the 30 testbed channels.

---

## 3. Phase 4: Layout Wireframe & Hero Infographic Provenance

- **Selected Layout Option**: `Option 1: Top-Hero Flow + Multi-Column Narrative (70% Visual / 30% Text)`
- **Approved ASCII Wireframe**:
  ```text
  +-------------------------------------------------------------------------+
  | [ TOP BANNER: VLIZ Logo (Left)                        vliz.be (Right) ] |
  +-------------------------------------------------------------------------+
  | [ TITLE BLOCK: Subtitle, Title, Cedric Decruw ]                         |
  +-------------------------------------------------------------------------+
  |                                                                         |
  |   ===================================================================   |
  |   |           DOMINANT HERO INFOGRAPHIC / ARCHITECTURE BANNER       |   |
  |   |                     (~42% TOTAL POSTER AREA)                    |   |
  |   |   TypeScript Generator -> Dockerized Nginx -> 2x2 Discovery     |   |
  |   |   Caption <= 15 words; clean 2D vector style; 50% whitespace    |   |
  |   ===================================================================   |
  |                                                                         |
  +-------------------------------------+-----------------------------------+
  | [ 1. CONTEXT & RQ / HYPOTHESIS ]    | [ 2. METHODS & 4 PILLARS ]        |
  | • 3 Styled Mini-Cards               | +----------------+--------------+ |
  |   (Fragmentation, Fragility, Test)  | | 1. Generator   | 2. Container | |
  | +---------------------------------+ | +----------------+--------------+ |
  | | Research Question (RQ) Card     | | | 3. Taxonomy    | 4. Topology  | |
  | +---------------------------------+ | +----------------+--------------+ |
  | +---------------------------------+ | • HTTP Semantics Principle Card   |
  | | Hypothesis / Prediction Card    | |                                   |
  | +---------------------------------+ +-----------------------------------+
  |                                     | [ 4. DISCUSSION & DIGITAL ACCESS] |
  | [ 3. EMPIRICAL RESULTS MATRIX ]     | • Hypothesis Verdict: Supported   |
  | [ 30 Channels ] [ 4 Quadrants ]     | • 1 Study Limitation              |
  | [ 150 Pages   ] [ 100% Stack  ]     | • 1 Actionable Next Direction     |
  | • Verifiable Multi-Channel Findings | [ QR CODE CARD: GitHub Repo ]     |
  +-------------------------------------+-----------------------------------+
  | [ FOOTER: References [1-3] | AI Disclosure | Partner Badges ]           |
  +-------------------------------------------------------------------------+
  ```
- **Hero Infographic Generation Log**:
  - **Asset Path**: `assets/hero_infographic.png` and HD print asset `assets/hero_infographic_hd.png` (5504 x 3072, 183.5 DPI at 30" width)
  - **Aspect Ratio & Zone**: `16:9 Wide Banner` in Top Hero Showcase (~42% canvas height)
  - **Caption**: `Figure 1: Multi-channel LOD testbed architecture uniting TypeScript generator, containerized Nginx, and 30-channel taxonomy.`
  - **Master Prompt Used**:
    ```text
    A publication-grade scientific hero infographic diagram for an academic poster, horizontal 16:9 widescreen layout, clean crisp pure white background (#FFFFFF). Left-to-right architectural data pipeline with three main sections: Left container 'TypeScript Generator' (RDF Graphs, Page Matrix, Server Headers), Center container 'Dockerized Nginx Server :8080' (RFC 8288 Headers, Turtle & JSON-LD, CORS), and Right 2x2 matrix '30 Discovery Channels' ('Resource-Direct (12)', 'Resource-Inferenced (10)', 'Domain-Direct (2)', 'Domain-Inferenced (8)'). Maintain crisp sans-serif typography, clean rounded rectangular cards, and minimalist academic poster aesthetic.
    ```
  - **HITL Refinement Notes**: Iteration v1 contained top color swatch legend; self-critiqued and refined in v2 to pure white background and seamless vector cards. Approved by author on 2026-11-04.

---

## 4. Phase 5 & 6: Deliverable Generation & Quality Audit Log

- **Generated Deliverables**:
  - LaTeX: `posters/lod-docker-webserver/poster.tex` -> `posters/lod-docker-webserver/poster.pdf`
  - PowerPoint: `posters/lod-docker-webserver/poster.pptx` (Generated directly via ephemeral `python-pptx` execution; zero per-poster scripts committed)
  - Preview Image: `posters/lod-docker-webserver/preview_poster.png` (4967 x 7022 px)
- **MAR 70/30 Rubric Audit (`audit_poster_rubric.py`)**:
  - `poster.tex`: **16 / 16 (100.0%) - EXEMPLARY (Publication / Conference Award Tier)**
    * Organization: 4 / 4
    * Poster Design & Visuals: 4 / 4
    * Wordiness / Text Density: 4 / 4 (396 words, optimal 30% budget)
    * Visual-to-Text Ratio: 4 / 4 (70/30 Rule with dominant Hero Infographic)
  - `poster.pptx`: **16 / 16 (100.0%) - EXEMPLARY (Publication / Conference Award Tier)**
    * Organization: 4 / 4
    * Poster Design & Visuals: 4 / 4
    * Wordiness / Text Density: 4 / 4 (385 words)
    * Visual-to-Text Ratio: 4 / 4
- **PowerPoint Technical Audit (`audit_existing_pptx.py`)**:
  - **PPTX Compliance Score**: **100 / 100**
  - **Slide Count**: 1 slide (A0 Portrait: 33.11" x 46.81")
  - **Grid & Alignment**: 3-column grid detected, 0 overlapping shapes
  - **Font Inventory**: Arial, min 22.0pt to max 54.0pt
  - **Effective Image DPIs**:
    * VLIZ Logo: 1154.5 DPI
    * Hero Infographic: 186.5 DPI (exceeds 150 print threshold)
    * QR Code: 289.1 DPI (target >= 150-300 DPI)
