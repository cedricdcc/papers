---
schema_version: "1.1"
poster:
  id: "radical-transparency"
  title: "Radical Transparency: A Vision for Scalable Interoperability"
  subtitle: "OPEN SCIENCE & SEMANTIC INTEROPERABILITY | LINKSET USAGE PATTERNS | RFC 9264"
  created_at: "2026-10-28T10:48:00+01:00"
  updated_at: "2026-11-06T11:30:00+01:00"
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
  primary_archetype: "Interdisciplinary Researchers & Data Stewards"
  specific_personas:
    - "Data Stewards & Research Software Engineers"
    - "Dataspace Architects & Ontology Practitioners"
  engagement_goal: "Dissemination of Published Paper & Adoption of Linkset Usage Patterns"

authors:
  - name: "Marc Portier"
    affiliation: "VLIZ - Flanders Marine Institute, Ostend, Belgium"
    email: "marc.portier@vliz.be"
    orcid: "0000-0002-9648-6484"
    corresponding: true
  - name: "Bram Ulrichts"
    affiliation: "VLIZ - Flanders Marine Institute, Ostend, Belgium"
    orcid: "0000-0002-5934-8998"
  - name: "Cedric Decruw"
    affiliation: "VLIZ - Flanders Marine Institute, Ostend, Belgium"
    orcid: "0000-0001-6387-5988"
  - name: "Hamideh Baggali"
    affiliation: "VLIZ - Flanders Marine Institute, Ostend, Belgium"
    orcid: "0009-0002-4051-1545"
  - name: "Joachim Nielandt"
    affiliation: "VLIZ - Flanders Marine Institute, Ostend, Belgium"
    orcid: "0000-0003-4900-8276"
  - name: "Joanna Goley"
    affiliation: "VLIZ - Flanders Marine Institute, Ostend, Belgium"
    orcid: "0000-0002-4242-8553"
  - name: "Laurian Van Maldeghem"
    affiliation: "VLIZ - Flanders Marine Institute, Ostend, Belgium"
    orcid: "0000-0003-0663-5907"
  - name: "Katrina Exter"
    affiliation: "VLIZ - Flanders Marine Institute, Ostend, Belgium"
    orcid: "0000-0002-5911-1536"
  - name: "Cyrielle Delvenne"
    affiliation: "VLIZ - Flanders Marine Institute, Ostend, Belgium"
    orcid: "0000-0001-9600-3457"
  - name: "Lennert Tyberghein"
    affiliation: "VLIZ - Flanders Marine Institute, Ostend, Belgium"
    orcid: "0000-0003-0577-1691"

conference:
  name: "General Open Science / VLIZ Institutional Dissemination"
  date: "2026"
  location: "Ostend, Belgium / Global Open Science"
  url: "https://open-science.vliz.be/"
  reserve_default_conference_logo_space: true
  conference_logo_path: null
  conference_logo_position: "title_header_right"

branding:
  theme_preset: "VLIZ Marine Institute (#91C8CD)"
  primary_institution_name: "Flanders Marine Institute (VLIZ)"
  primary_institution_url: "vliz.be"
  primary_institution_logo: "assets/vliz_logo.png"
  extra_logos:
    - name: "EOSC-IF"
      role: "partner_standard"
      zone: "footer_right"
    - name: "CDIF"
      role: "partner_standard"
      zone: "footer_right"
    - name: "OGC"
      role: "partner_standard"
      zone: "footer_right"
    - name: "RO-Crate"
      role: "partner_standard"
      zone: "footer_right"
    - name: "ODIS"
      role: "partner_standard"
      zone: "footer_right"

visual_magnet:
  header_motif: "vliz_wave_harmonics_and_sonar_arcs"
  header_motif_opacity: 0.14
  canvas_motif: "hybrid_wave_mesh"
  canvas_motif_opacity: 0.055
  hero_stage_bg: "#F4F9FA"
  billboard_hook_pill: "FROM SILOED GUESSWORK TO AUTONOMOUS WEB MAPS"
  cross_board_conduit: "london_tube_spine_to_qr"
  tactile_left_accent_pt: 6

inputs:
  source_documents:
    - path_or_url: "https://open-science.vliz.be/papers/2026-radical-transparency-position/2026-radical-transparency-position.pdf"
      type: "manuscript"
      description: "Radical Transparency: A Vision for Scalable Interoperability (Position Paper)"
    - path_or_url: "https://github.com/eosc-semantic-interop/if-solutions-proposals/tree/main/proposals/radical-transparency/linkset-usage-patterns"
      type: "repository"
      description: "Linkset Usage Patterns proposal for EOSC Semantic Interoperability"
    - path_or_url: "papers/wrx/radical_transparency_horizontal.png"
      type: "figure"
      description: "Radical Transparency & wrx cascading discovery schematic"
  provided_assets:
    - path: "assets/vliz_logo.png"
      role: "primary_institution_logo"
      description: "Official VLIZ wave logo"
  qr_codes:
    - label: "Paper PDF"
      url: "https://open-science.vliz.be/papers/2026-radical-transparency-position/2026-radical-transparency-position.pdf"
      asset_path: "assets/qr_radical_paper.png"
    - label: "Linkset Patterns"
      url: "https://github.com/eosc-semantic-interop/if-solutions-proposals/tree/main/proposals/radical-transparency/linkset-usage-patterns"
      asset_path: "assets/qr_linkset_patterns.png"
  key_references:
    - "[1] Wilde & Van de Sompel (2022). Linkset: RFC 9264. IETF."
    - "[2] Nottingham (2017). Web Linking: RFC 8288. IETF."
    - "[3] Simonis et al. (2026). Machine-Interpretable Standards Ecosystem: OGC 26-021."
    - "[4] Portier et al. (2026). Radical Transparency: A Vision for Scalable Interoperability. VLIZ."
  ai_disclosure: "Conceptual synthesis assisted by Agentic AI; system vision and architecture by authors."

audit_summary:
  mar_score: "16 / 16 (100.0%) [tex & pptx] — EXEMPLARY (Publication / Conference Award Tier)"
  pptx_score: "100 / 100"
  visual_magnet_verified: true
  estimated_word_count: 398
---

# Poster Provenance & Requirements Log

## 1. Phase 1: Strategic Discovery & Requirements Intake

- **Target Audience & Personas**:
  - **Data Stewards & Research Software Engineers**: Need unambiguous, machine-actionable signposts on the wire rather than manual parsing of HTML landing pages or tribal API rules.
  - **Dataspace Architects & Ontology Practitioners**: Need a lightweight, federated bootstrapping mechanism (RFC 9264 linksets) to declare conformity profiles across EOSC, CDIF, OGC, and ODIS without central governance lock-in.
- **Conference & Logo Allocation**:
  - **Target Event**: General Open Science / VLIZ Institutional Dissemination.
  - **Conference Logo Slot**: Enabled (`reserve_default_conference_logo_space: true`), reserving a tactile placeholder box in Title Header right.
  - **Extra Partner / Funder Logos**: EOSC-IF, CDIF, OGC, RO-Crate, ODIS partner badges in Footer right.
- **4-Layer Visual Magnet Configuration**:
  - **Layer 0 (Atmospheric Motifs)**: Decoupled hybrid motif combining VLIZ marine wave harmonics & acoustic sonar arcs (`12%–15%` opacity) in the `#91C8CD` top banner with ultra-faint bathymetric contours (`5.5%` opacity, left margin) and isometric semantic node-link constellation meshes (`5.0%` opacity, right margin) on the A0 canvas.
  - **Layer 1 (Borderless Hero Stage & Hook Pill)**: Full-bleed soft sea-tint Hero Stage (`#F4F9FA`) with zero vertical box walls, seamlessly blended `hero_infographic_hd.png` with horizontal glowing transit flow ribbon, crowned by the `#002B49` Deep Navy **Billboard Hook Pill**: `"FROM SILOED GUESSWORK TO AUTONOMOUS WEB MAPS"`.
  - **Layer 2 (Cross-Board Visual Conduit)**: Programmatic London-Tube-style vector transit conduit (`#31B7BC` + `#002B49` station rings) originating below the Title Block, entering the Billboard Hook Pill, emerging from the Figure 1 pill caption, running down the central column spine with 3 transfer station nodes anchoring Sections 1–4, and turning along the bottom channel into the **Digital Companion QR Code Card**.
  - **Layer 3 (Tactile UI Card Elevation, MAR Typography Scale & Anti-AI Icon Restraint)**:
    - 6pt (`0.16–0.18 in`) colored left-accent borders (`#3057A5` / `#31B7BC`), soft elevation shadows, and `100%` opaque `#FFFFFF` interiors shielding body text ($\ge 12:1$ WCAG AAA contrast).
    - **MAR Typography & Card-Fill Balance**: Clean sans-serif (`\sffamily` Helvetica in LaTeX; `Calibri` in PPTX), `25pt` (`23.5pt` PPTX) bold sub-card headers, `22pt` (`20.5pt` PPTX) ragged-right anti-orphan body text, symmetrical `2 × 2` wide card grids + full-width synthesis cards across Sections 1 & 2, giant `48pt` (`44pt` PPTX) bold empirical metric numerals, and a large `6.8 cm` (`2.95 in`) QR code filling the Digital Companion card (`~82%` internal card fill with zero hollow voids).
    - **Anti-AI Icon Restraint**: Zero synthetic icon badges (`\vicon`) or decorative Unicode symbols (`◈`, `⬡`, `⚡`, `🔗`, `▸`); sequential pillars use clean typographic numerals (`01`–`04`).

---

## 2. Phase 2: Distilled Scientific Narrative (30% Text Budget: 250–400 Words)

- **10-Foot Billboard Hook Pill (6 Words)**:
  - `FROM SILOED GUESSWORK TO AUTONOMOUS WEB MAPS`
- **Background & Context (3 Tactile Mini-Cards)**:
  1. **Assumed Schemas**: Systems rely on unproven guesses that endpoints share implicit schemas and APIs.
  2. **Trapped Discovery**: Discovery is buried in HTML landing pages; agents cannot parse without signposts.
  3. **Displaced Labor**: Stewards lose majority of time on repetitive manual mapping instead of science.
- **Explicit Research Question (RQ)**:
  - *How can distributed data ecosystems achieve scalable interoperability without enforcing fragile, centralized APIs or burdensome consumer-side guesswork?*
- **Explicit Hypothesis / Prediction**:
  - *Shifting the architectural burden from consumer inference to producer declaration via RFC 9264 Linksets and machine-verifiable conformity profiles enables scalable, autonomous web-scale discovery.*
- **Methods & The 4 Strategic Pillars (2025–2030)**:
  - **1. Linkset Patterns**: 10 documented RFC 9264 patterns solving Broken Chains & Semantic Drift.
  - **2. Cross-Org Alignment**: Common bootstrap uniting EOSC-IF, CDIF, OGC, RO-Crate, and ODIS.
  - **3. Practical Toolchain**: Reference tools (`wrx`, `stitch`, `rdf-webcomponents`) for graph discovery.
  - **4. Open Profile Market**: Federated, DNS-like profile registers replacing centralized vendor monopolies.
- **Key Quantitative Empirical Metrics**:
  - **80% Time Reclaimed**: Autonomous agents navigate explicit typed links instead of fragile HTML screen-scraping.
  - **10 Linkset Patterns**: Eliminates implicit API guesswork via standard RFC 9264 link relations.
  - **5 Standards United**: Harmonizes EOSC-IF, CDIF, OGC, RO-Crate, and ODIS across a common discovery bootstrap.
  - **3 Reference Tools**: `wrx`, `stitch`, and `rdf-webcomponents` provide verified developer workflows.
- **Discussion & Future Outlook**:
  - **Hypothesis Verdict**: Supported — machine-actionable linksets turn open web resources into a traversable transit network for autonomous agents.
  - **1 Study Limitation**: Adoption velocity depends on community alignment across multi-institutional repositories.
  - **1 Actionable Future Direction**: Finalize 10 EOSC-if Linkset Usage Patterns in Q3 2026 with reference implementations in `wrx`.

---

## 3. Phase 4: Layout Wireframe & Hero Infographic Provenance

- **Selected Layout Option**: `Option 1: Top Borderless Hero Stage + Central Conduit Spine (70% Visual / 30% Text)`
- **Approved ASCII Wireframe**:
  ```text
  +-------------------------------------------------------------------------+
  | [ TOP BANNER (Layer 0 Wave Harmonics 14%): VLIZ Logo | vliz.be (Right)] |
  +-------------------------------------------------------------------------+
  | [ TITLE BLOCK: Subtitle, Title, 10 Authors ]        [ CONF. LOGO SLOT ] |
  +------------------------------------o------------------------------------+
  |        [ BILLBOARD HOOK: FROM SILOED GUESSWORK TO AUTONOMOUS WEB MAPS ] |
  |   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   |
  |        BORDERLESS HERO INFOGRAPHIC STAGE (#F4F9FA - ZERO SIDE BOX)      |
  |      1. Siloed Endpoints -> 2. RFC 9264 Signposts -> 3. Tube Network    |
  |        [ Pill Caption: <=12-word takeaway on bottom stage horizon ]     |
  |   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   |
  +------------------------------------|------------------------------------+
  | [ 1. CONTEXT & CORE PROPOSITION ]  o--[ 2. THE 4 STRATEGIC PILLARS ]    |
  | • 3 Tactile 6pt Left-Accent Cards  |  +---------------+---------------+ |
  | |▌ Research Question (RQ) Card     |  |▌ P1. Linkset  |▌ P2. Cross-Org| |
  | |▌ Hypothesis (RFC 9264) Card      |  |    Patterns   |    Alignment  | |
  |                                    o  +---------------+---------------+ |
  | [ 3. EMPIRICAL ROI METRICS ]       |  |▌ P3. Practical|▌ P4. Open     | |
  | [▌80% Time] [▌10 Patterns]         |  |    Toolchain  |    Profiles   | |
  | [▌5 Stds  ] [▌3 Ref Tools]         |  +---------------+---------------+ |
  | |▌ Collapsing Integration Costs    |  |▌ Core Separation of Concerns  | |
  |   ("Transaction Tax" concept)      o--+-------------------------------+ |
  |  (Layer 0 Faint Corner Motifs      |  [ 4. DISCUSSION & DIGITAL ACCESS] |
  |   <= 5.5% Opacity)                 |  |▌ Verdict, 1 Limit, 1 Next Step  |
  |                                    +--o-> [▌ QR: open-science.vliz.be ] |
  +-------------------------------------------------------------------------+
  | [ FOOTER: References [1-4] | AI Disclosure | Partner Badges (EOSC) ]    |
  +-------------------------------------------------------------------------+
  ```
- **Hero Infographic Generation & Stage Blending Log**:
  - **Asset Path**: `assets/hero_infographic_v2.png` $\rightarrow$ `assets/hero_infographic_hd.png` (`5900 x 3290 px`)
  - **Aspect Ratio & Zone**: `16:9 Wide Banner` seamlessly blended into the `#F4F9FA` Borderless Hero Stage with a subtle horizontal glowing sea-teal transit stream (`#DAEEF1` $\rightarrow$ `#F4F9FA`) while preserving pure `#FFFFFF` interiors inside the `URI` circle and 9 London Tube station rings.

---

## 4. Phase 5 & 6: Deliverable Generation & Quality Audit Log

- **Generated Deliverables**:
  - `posters/radical-transparency/poster.tex` (LaTeX `tikzposter` source with 4-Layer Visual Magnet Architecture, A0 Portrait `841 x 1189 mm`)
  - `posters/radical-transparency/poster.pdf` (Compiled print-ready vector PDF, 1 page)
  - `posters/radical-transparency/preview_poster.png` (High-resolution visual proof rendered via PyMuPDF)
  - `posters/radical-transparency/poster.pptx` (Native editable PowerPoint deck, A0 Portrait `33.11" x 46.81"`, generated via ephemeral memory execution with zero residual `.py` in poster folder)
- **Visual Refinement & Alignment Verification (Phase 5B)**:
  - Verified exact column baseline lock via `pymupdf` (`page.get_drawings()`):
    - Top 2-column band: Left card `y1 = 2667.5 pt, h = 23.91 cm`, Right card `y1 = 2667.5 pt, h = 23.91 cm` (`0.00 mm` delta).
    - Bottom 2-column band: Left card `y1 = 3155.8 pt, h = 16.53 cm`, Right card `y1 = 3154.9 pt, h = 16.50 cm` (`0.31 mm` delta).
  - Verified Contrast & Anti-Boxiness Safety Gate: Layer 0 canvas motifs strictly $\le 5.5\%$ opacity; all body text shielded by `100%` opaque `#FFFFFF` tactile cards ($\ge 12:1$ contrast ratio).
- **PowerPoint Technical Audit (`audit_existing_pptx.py`)**:
  - `poster.pptx`: **100 / 100** (1 slide, `A0_PORTRAIT` `33.11" x 46.81"`, 0 sibling overlaps, all 4 Visual Magnet layers verified: `11 bg_motif_*`, `hero_stage_band` + `hook_pill_badge`, `12 conduit_*`, `22 accent_bar_*`, Contrast Safety Gate passed, images exceeding print standards: `VLIZ_Logo` at `796.2 DPI`, `Hero_Infographic` at `207.0 DPI`, `QR_Paper` at `350.9 DPI`).
- **MAR 70/30 Rubric Audit (`audit_poster_rubric.py`)**:
  - `poster.tex`: **16 / 16 (100.0%) — EXEMPLARY (Publication / Conference Award Tier)** (all 4 Visual Magnet layers active, chronological flow, tactile left-accent mini-cards, verifiable empirical metrics, single authoritative QR).
  - `poster.pptx`: **16 / 16 (100.0%) — EXEMPLARY (Publication / Conference Award Tier)** (398 words, 100/100 layout quality, all 4 Visual Magnet layers active).
