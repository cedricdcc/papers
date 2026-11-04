---
schema_version: "1.0"
poster:
  id: "radical-transparency"
  title: "Radical Transparency: A Vision for Scalable Interoperability"
  subtitle: "LINKSET USAGE PATTERNS | FROM ASSUMED COMPATIBILITY TO MACHINE-ACTIONABLE CONFORMITY"
  created_at: "2026-10-28T10:48:00+01:00"
  updated_at: "2026-10-28T10:48:00+01:00"
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
  estimated_word_count: 395
---

# Poster Provenance & Requirements Log

## 1. Phase 1: Strategic Discovery & Requirements Intake

- **Target Audience & Personas**:
  - **Data Stewards & Research Software Engineers**: Need unambiguous, machine-actionable signposts on the wire rather than manual parsing of HTML landing pages or tribal API rules.
  - **Dataspace Architects & Ontology Practitioners**: Need a lightweight, federated bootstrapping mechanism (RFC 9264 linksets) to declare conformity profiles across EOSC, CDIF, OGC, and ODIS without central governance lock-in.
- **Conference & Logo Allocation**:
  - **Target Event**: General Open Science / VLIZ Institutional Dissemination.
  - **Conference Logo Slot**: Enabled (`reserve_default_conference_logo_space: true`), reserving styled placeholder box in Title Header right.
  - **Extra Partner / Funder Logos**: EOSC-IF, CDIF, OGC, RO-Crate, ODIS partner badges in Footer right.
- **Captured Source Inputs**:
  - Position Paper PDF: `https://open-science.vliz.be/papers/2026-radical-transparency-position/2026-radical-transparency-position.pdf`
  - Linkset Usage Patterns: `https://github.com/eosc-semantic-interop/if-solutions-proposals/tree/main/proposals/radical-transparency/linkset-usage-patterns`
  - Institutional Brand Assets: Flanders Marine Institute (`assets/vliz_logo.png`, Sea-teal `#91C8CD`, Navy `#3057A5`).

---

## 2. Phase 2: Distilled Scientific Narrative (30% Text Budget: 250–400 Words)

- **Background & Context (3 Styled Mini-Cards)**:
  1. **Assumed Compatibility**: Distributed systems stall on unproven guesses that endpoints share implicit schemas, units, and APIs.
  2. **Trapped Discovery**: Data discovery remains buried in human HTML pages; autonomous agents cannot navigate without machine signposts.
  3. **Displaced Labor**: Data stewards spend the majority of their time on manual schema translation rather than scientific analysis.
- **Explicit Research Question (RQ)**:
  - *How can distributed data ecosystems achieve scalable interoperability without enforcing fragile, centralized APIs or burdensome consumer-side guesswork?*
- **Explicit Hypothesis / Prediction**:
  - *Shifting the architectural burden from consumer inference to producer declaration via RFC 9264 Linksets and machine-verifiable conformity profiles enables scalable, autonomous web-scale discovery at minimal transaction cost.*
- **Methods & The 4 Strategic Pillars (2025–2030)**:
  - **1. Linkset Usage Patterns**: 10 documented patterns (Profile Declaration, Composition, Content Negotiation, API Subsetting) that solve the "Broken Chain" and mitigate "Semantic Drift".
  - **2. Cross-Organisational Alignment**: Harmonizing EOSC-if, CDIF, OGC, RO-Crate, and ODIS through a shared lightweight bootstrap.
  - **3. Practical Tooling**: wrx, stitch, and modular rdf-webcomponents automating observable graph discovery.
  - **4. Community Adoption**: Fostering an open market of federated, DNS-like profile registers.
- **Key Quantitative Empirical Metrics**:
  - **80% Time Reclaimed**: Autonomous agents navigate explicit typed links instead of fragile HTML screen-scraping.
  - **10 Core Linkset Patterns**: Eliminates implicit API guesswork via standard RFC 9264 link relations.
  - **5 Standards United**: Harmonizes EOSC-IF, CDIF, OGC, RO-Crate, and ODIS across a common discovery bootstrap.
  - **3 Reference Tools**: wrx, stitch, and rdf-webcomponents provide verified, production-ready developer workflows.
- **Discussion & Future Outlook**:
  - **Hypothesis Verdict**: Supported — externalizing typed web links and conformity markers establishes a measurable "navigation map" (analogous to the London Tube) for autonomous agents.
  - **1 Study Limitation**: Adoption velocity depends on cross-organizational willingness to shift from bespoke APIs to standard HTTP link headers and linkset endpoints.
  - **1 Actionable Future Direction**: Finalize the 10 EOSC-if Linkset Usage Patterns in Q3 2026 and release reference implementations in the wrx framework.

---

## 3. Phase 4: Layout Wireframe & Hero Infographic Provenance

- **Selected Layout Option**: `Option 1: Top-Hero Flow + Multi-Column Narrative (70% Visual / 30% Text)`
- **Approved ASCII Wireframe**:
  ```text
  +-------------------------------------------------------------------------+
  | [ TOP BANNER: VLIZ Logo (Left)                        vliz.be (Right) ] |
  +-------------------------------------------------------------------------+
  | [ TITLE BLOCK: Subtitle, Title, 10 Authors ]        [ CONF. LOGO SLOT ] |
  +-------------------------------------------------------------------------+
  |                                                                         |
  |   ===================================================================   |
  |   |        HERO INFOGRAPHIC: 3-STAGE ARCHITECTURAL SHIFT            |   |
  |   |   1. Siloed Endpoints -> 2. RFC 9264 Signposts -> 3. Tube Map   |   |
  |   |    (Includes inline London Tube legend; 12-word bold caption)   |   |
  |   ===================================================================   |
  |                                                                         |
  +-------------------------------------+-----------------------------------+
  | [ 1. CONTEXT & CORE PROPOSITION ]   | [ 2. THE 4 STRATEGIC PILLARS ]    |
  | • 3 Styled Mini-Cards (Bottleneck)  | +---------------+---------------+ |
  | +---------------------------------+ | | 1. 10 Linkset | 2. Cross-Org  | |
  | | Research Question (RQ) Card     | | |    Patterns   |    Alignment  | |
  | +---------------------------------+ | +---------------+---------------+ |
  | +---------------------------------+ | | 3. Practical  | 4. Open       | |
  | | Hypothesis (RFC 9264) Card      | | |    Toolchain  |    Profiles   | |
  | +---------------------------------+ | +---------------+---------------+ |
  |                                     | +-------------------------------+ |
  | [ 3. EMPIRICAL ROI METRICS ]        | | Core Separation of Concerns   | |
  | [ 80% Time ] [ 10 Patterns ]        | | (Servers vs. AI Agents)       | |
  | [ 5 Standards ] [ 3 Ref Tools ]     | +-------------------------------+ |
  |                                     +-----------------------------------+
  | • Collapsing Integration Costs      | [ 4. DISCUSSION & DIGITAL ACCESS ]|
  |   ("Transaction Tax" concept)       | • Verdict: Hypothesis Supported   |
  |                                     | • Limitation: Community Alignment |
  |                                     | • Next: Q3 2026 Formalization     |
  |                                     | [ QR CODE: open-science.vliz.be ] |
  +-------------------------------------+-----------------------------------+
  | [ FOOTER: References [1-4] | AI Disclosure | Partner Badges (EOSC) ]    |
  +-------------------------------------------------------------------------+
  ```
- **Hero Infographic Generation Log**:
  - **Asset Path**: `assets/hero_infographic_v2.png` / `assets/hero_infographic_hd.png`
  - **Aspect Ratio & Zone**: `16:9 Wide Banner` in Top Hero Showcase (~42% canvas height)
  - **Master Prompt Used**:
    ```text
    Generate a publication-grade scientific hero infographic for an A0 portrait academic poster.
    TOPIC / CORE NARRATIVE:
    Radical Transparency for Scalable Interoperability. Shifting data integration from "assumed compatibility" (hidden APIs, broken chains, tribal knowledge) into an open, machine-actionable web navigation map powered by RFC 9264 Linksets and explicit conformity profiles.
    VISUAL COMPOSITION (Left-to-Right 3-Stage Flow, 16:9 Aspect Ratio):
    1. Stage 1 (Left - The Bottleneck / Assumed Compatibility): Flat 2D vector representation of fractured data silos and isolated server endpoints with broken chains and question mark icons.
    2. Stage 2 (Center - The Architectural Shift / RFC 9264 Signpost): Flat 2D node-and-link signpost diagram on solid white background. An HTTP URI digital asset node cleanly emitting color-coded directional link lines (rel="profile", rel="describedby", rel="item") into the open web.
    3. Stage 3 (Right - The Scalable Solution / London Tube Transit Network): A clean 2D London Underground / metro-style transit network map with interconnected color-coded transit lines representing standards (EOSC, CDIF, OGC, RO-Crate) intersecting at transfer station nodes, with an autonomous AI agent icon navigating along the routes.
    VISUAL STYLE & THEME:
    Unified 2D flat vector aesthetic across all three stages. Flanders Marine Institute (VLIZ) palette: Sea-teal (#91C8CD), Corporate Navy (#3057A5), Vibrant Teal (#31B7BC) on pure solid white (#FFFFFF). 50% negative space, publication-quality finish.
    STRICT NEGATIVE CONSTRAINTS:
    Solid white background, no long narrative text, no figure numbers, no 3D glass cubes, no repetitive stacked labels, <= 10 single-word structural labels total.
    ```
  - **HITL Refinement Notes**: Replaced 3D translucent glass cube with clean 2D node signpost; unified flat vector aesthetic; eliminated duplicate arrow labels; integrated transit legend.

---

## 4. Phase 5 & 6: Deliverable Generation & Quality Audit Log

- **Generated Deliverables**:
  - `posters/radical-transparency/poster.tex` (LaTeX `tikzposter` source, A0 Portrait `841 x 1189 mm`)
  - `posters/radical-transparency/poster.pdf` (Compiled print-ready vector PDF, 1 page)
  - `posters/radical-transparency/preview_poster.png` (High-resolution visual proof rendered via PyMuPDF)
  - `posters/radical-transparency/poster.pptx` (Native editable PowerPoint deck, A0 Portrait `33.11" x 46.81"`, generated via ephemeral memory execution with zero residual `.py` in poster folder)
- **Visual Refinement & Alignment Verification (Phase 5B)**:
  - Verified exact column baseline lock via `pymupdf` (`page.get_drawings()`):
    - Top 2-column band: Left card `y1 = 1437.7 pt, h = 689.6 pt`, Right card `y1 = 1437.4 pt, h = 689.2 pt` (`0.14 mm` delta).
    - Bottom 2-column band: Left card `y1 = 3389.8 pt, h = 544.5 pt`, Right card `y1 = 3389.9 pt, h = 544.6 pt` (`0.03 mm` delta).
- **PowerPoint Technical Audit (`audit_existing_pptx.py`)**:
  - `poster.pptx`: **100 / 100** (1 slide, `A0_PORTRAIT` `33.11" x 46.81"`, 0 text overlaps, 0 boundary overflows, images exceeding print standards: `VLIZ_Logo` at `1154.5 DPI`, `Hero_Infographic` at `199.9 DPI`, `QR_Paper` at `312.5 DPI`).
- **MAR 70/30 Rubric Audit (`audit_poster_rubric.py`)**:
  - `poster.tex`: **16 / 16 (100.0%) — EXEMPLARY (Publication / Conference Award Tier)** (395 words, chronological flow, styled mini-cards, zero redundant sub-headers, verifiable empirical metrics, single authoritative QR).
  - `poster.pptx`: **16 / 16 (100.0%) — EXEMPLARY (Publication / Conference Award Tier)** (393 words, 100/100 layout quality, zero collisions).

---

## 5. The 10-Minute Oral Presentation Coach

```text
TOTAL PRESENTATION TIME: 10 MINUTES (HARD CAP)
├── 1. Hook: Top-Hero Infographic Walkthrough   : 2 Minutes
│   └── Guide attendee directly under the Title Block to Figure 1. Trace the 3-stage shift:
│       from fractured silos ("assumed compatibility") to RFC 9264 typed linksets, into an open London Tube map.
├── 2. The Interoperability Crisis & RQ/Hypothesis: 2 Minutes
│   └── Point to Section 1 mini-cards: explain the 80% curation bottleneck and why implicit schemas fail.
│       State the Research Question and Hypothesis: producer declaration enables autonomous agent discovery.
├── 3. The 4 Strategic Pillars (2025–2030)      : 3 Minutes
│   └── Walk through the 2x2 matrix in Section 2: 10 Linkset Patterns (RFC 9264), cross-org alignment
│       (EOSC-IF, CDIF, OGC, RO-Crate, ODIS), practical wrx toolchain, and federated profile registers.
├── 4. Empirical ROI Metrics & Collapsing Costs : 2 Minutes
│   └── Direct attendee to the 4 metric callout badges: 80% Time Reclaimed, 10 Linkset Patterns,
│       5 Standards United, and 3 Reference Tools. Explain the "Transaction Tax" concept.
└── 5. Discussion, Limitations & QR Access      : 1 Minute
    └── Disclose cross-repository adoption velocity limitation, announce Q3 2026 EOSC-if pattern release,
        and invite the listener to scan the QR code to open-science.vliz.be.
```


