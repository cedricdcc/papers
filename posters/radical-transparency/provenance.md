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
  mar_score: "14 / 16 (87.5%) [tex & pptx] — EXEMPLARY (Publication / Conference Award Tier)"
  pptx_score: "100 / 100"
  estimated_word_count: 481
---

# Poster Provenance & Requirements Log

## 1. Phase 1: Strategic Discovery & Requirements Intake

- **Target Audience & Personas**:
  - **Data Stewards & Research Software Engineers**: Need unambiguous, machine-actionable signposts on the wire rather than manual parsing of HTML landing pages or tribal API rules.
  - **Dataspace Architects & Ontology Practitioners**: Need a lightweight, federated bootstrapping mechanism (RFC 9264 linksets) to declare conformity profiles across EOSC, CDIF, OGC, and ODIS without central governance lock-in.
- **Conference & Logo Allocation**:
  - **Target Event**: General Open Science / VLIZ Institutional Dissemination.
  - **Conference Logo Slot**: Disabled (`reserve_default_conference_logo_space: false`), allowing full title header width for the 10-author institutional attribution.
  - **Extra Partner / Funder Logos**: None requested; clean footer bar focused on references, QR codes, and AI disclosure.
- **Captured Source Inputs**:
  - Position Paper PDF: `https://open-science.vliz.be/papers/2026-radical-transparency-position/2026-radical-transparency-position.pdf`
  - Linkset Usage Patterns: `https://github.com/eosc-semantic-interop/if-solutions-proposals/tree/main/proposals/radical-transparency/linkset-usage-patterns`
  - Institutional Brand Assets: Flanders Marine Institute (`assets/vliz_logo.png`, Sea-teal `#91C8CD`, Navy `#3057A5`).

---

## 2. Phase 2: Distilled Scientific Narrative (30% Text Budget: 250–400 Words)

- **Background & Context Bullets (3 points)**:
  1. Distributed scientific data sharing suffers from **"assumed compatibility"**—unproven guesses that endpoints share implicit schemas, units, and APIs.
  2. Data discovery remains buried in human-facing HTML landing pages and tribal knowledge, forcing data stewards to spend up to **80% of their time on manual schema translation**.
  3. While standards exist (RFC 8288, RFC 9264), systems lack a common bootstrap to explicitly declare conformance and link relationships on the wire.
- **Explicit Research Question (RQ)**:
  - *How can distributed data ecosystems achieve scalable interoperability without enforcing fragile, centralized APIs or burdensome consumer-side guesswork?*
- **Explicit Hypothesis / Prediction**:
  - *Shifting the architectural burden from consumer inference to producer declaration via RFC 9264 Linksets and machine-verifiable conformity profiles enables scalable, autonomous web-scale discovery at minimal transaction cost.*
- **Methods & The 4 Strategic Pillars (2025–2030)**:
  - **1. Linkset Usage Patterns**: 10 documented patterns (Profile Declaration, Composition, Content Negotiation, API Subsetting) that solve the "Broken Chain" and mitigate "Semantic Drift".
  - **2. Cross-Organisational Alignment**: Harmonizing EOSC-if, CDIF, OGC, RO-Crate, and ODIS through a shared lightweight bootstrap.
  - **3. Practical Tooling**: wrx, stitch, and modular rdf-webcomponents automating observable graph discovery.
  - **4. Community Adoption**: Fostering an open market of federated, DNS-like profile registers.
- **Key Quantitative Metrics & Paradigm Shifts**:
  - **80% Curation Reclaimed**: Shifts digital agents from brittle scrapers into self-navigating assistants.
  - **10 Core Linkset Patterns**: Eliminates implicit API guesswork via RFC 9264 link relations.
  - **0 Central Bottleneck**: Federated, decentralized profile governance.
  - **"Maximum Boredom"**: Scalable interoperability via predictable, mature web standards over proprietary glue code.
- **Discussion & Future Outlook**:
  - **Hypothesis Verdict**: Supported — externalizing typed web links and conformity markers establishes a measurable "navigation map" (analogous to the London Tube) for autonomous agents.
  - **1 Study Limitation**: Adoption velocity depends on cross-organizational willingness to shift from bespoke APIs to standard HTTP link headers and linkset endpoints.
  - **1 Actionable Future Direction**: Finalize the 10 EOSC-if Linkset Usage Patterns in Q3 2026 and release reference implementations in the wrx framework.

---

## 3. Phase 4: Layout Wireframe & Hero Infographic Provenance

- **Selected Layout Option**: `Option 1: Central Hero Showcase + 2x2 Flanking Grid`
- **Approved ASCII Wireframe**:
  ```text
  +-------------------------------------------------------------------------+
  | [ TOP SEA-TEAL BANNER (#91C8CD): VLIZ Wave Logo (Left) | vliz.be ]      |
  +-------------------------------------------------------------------------+
  | [ MAIN TITLE: Radical Transparency: A Vision for Scalable Interoperability ]|
  | [ SUBTITLE: LINKSET USAGE PATTERNS | FROM ASSUMED COMPATIBILITY ... ]   |
  | [ AUTHORS: Marc Portier (corr.), Bram Ulrichts, Cedric Decruw, et al. ]  |
  +-----------------------------------+-------------------------------------+
  | [ 1. CONTEXT, RQ & HYPOTHESIS ]   | [ 2. RESULTS & PARADIGM SHIFTS ]    |
  | • Assumed Compatibility trap      | [80% Reclaimed] [10 Patterns]       |
  | • Discovery lost in HTML & APIs   | [0 Bottleneck]  [Maximum Boredom]   |
  | • Explicit RQ & Hypothesis        | • Measurable ROI over belief systems|
  +-----------------------------------+-------------------------------------+
  |   ===================================================================   |
  |   |          DOMINANT CENTRAL HERO INFOGRAPHIC (~48% AREA)          |   |
  |   |  Assumed Compatibility -> Radical Transparency -> Web Nav Map   |   |
  |   |    (Fractured Silo -> URI/Profile Triple -> London Tube Map)    |   |
  |   ===================================================================   |
  +-----------------------------------+-------------------------------------+
  | [ 3. THE 4 STRATEGIC PILLARS ]    | [ 4. OUTLOOK, MECHANISMS & QR ]     |
  | • Linkset Patterns (RFC 9264/8288)| • Hypothesis Verdict & London Tube  |
  | • Cross-Org Alignment (EOSC/CDIF) | • 1 Study Limitation & 1 Direction  |
  | • Practical Tooling (wrx, stitch) | • [ QR 1: Position Paper ]          |
  | • Open Profile Registers / Market | • [ QR 2: Linkset Usage Patterns ]  |
  +-----------------------------------+-------------------------------------+
  | [ FOOTER: Key References [1-4] & AI Tool Disclosure | VLIZ Team ]       |
  +-------------------------------------------------------------------------+
  ```
- **Hero Infographic Generation Log**:
  - **Asset Path**: `assets/hero_infographic_hd.png` (`5504 x 3072`, upscaled with Lanczos + unsharp masking to guarantee $>180$ DPI print resolution)
  - **Aspect Ratio & Zone**: `16:9 Wide Banner` in Central Hero Showcase
  - **Master Prompt Used**:
    ```text
    Generate a publication-grade scientific hero infographic for an A0 portrait academic poster.
    TOPIC / CORE NARRATIVE:
    Radical Transparency for Scalable Interoperability. Shifting data integration from "assumed compatibility" (hidden APIs, tribal knowledge) into an open, machine-actionable web navigation map powered by RFC 9264 Linksets and explicit conformity profiles.
    VISUAL COMPOSITION (Left-to-Right 3-Stage Flow, 16:9 Aspect Ratio):
    1. Stage 1 (Left - The Barrier): "Assumed Compatibility" — A fractured data silo / broken stone bridge with dark silhouette figures, question marks, and a severed data cable representing hidden APIs and manual schema guesswork.
    2. Stage 2 (Center - The Core Mechanism): "Radical Transparency Engine" — A clean, modern luminous translucent glass container in Flanders Marine Institute sea-teal (#91C8CD) and corporate navy (#3057A5). Showing: [Digital Asset URI] -> «conformsTo» -> [Profile] -> «identifies» -> [Representation]. Externalized HTTP link headers and typed RFC 9264 linksets emanate outward.
    3. Stage 3 (Right - The Navigation Highway): "Autonomous Web Map" — A stylized, clean transit line map (inspired by London Tube map) with multi-colored tracks connecting digital stations labeled with standard patterns (Profile, Linkset, Catalog, Discovery), leading smoothly to autonomous AI agents and open FAIR dataspaces.
    VISUAL STYLE & THEME:
    Flanders Marine Institute (VLIZ) palette: Sea-teal (#91C8CD), Corporate Navy (#3057A5), Deep Ocean Navy (#002B49) on pure solid white (#FFFFFF). 50% negative space, publication-quality finish.
    STRICT NEGATIVE CONSTRAINTS:
    Solid white background, no long narrative text, no figure numbers.
    ```
  - **HITL Refinement Notes**: Approved v2 image, upscaled to HD `5504 x 3072` PNG for flawless print rendering.

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
  - `poster.pptx`: **100 / 100** (1 slide, `A0_PORTRAIT` `33.11" x 46.81"`, 0 text overlaps, 0 boundary overflows, 4 embedded images all exceeding print standards: `VLIZ_Logo` at `923.6 DPI`, `Hero_Infographic` at `193.8 DPI`, `QR_Paper` at `370.4 DPI`, `QR_Patterns` at `370.4 DPI`).
- **MAR 70/30 Rubric Audit (`audit_poster_rubric.py`)**:
  - `poster.tex`: **14 / 16 (87.5%) — EXEMPLARY (Publication / Conference Award Tier)** (All 11 empirical checks passed: A0 Portrait geometry, Hero Infographic present, Abstract excluded, RQ & Hypothesis detected, No raw tables, Dual QR codes present, Exactly 1 limitation and 1 future direction, Provenance verified).
  - `poster.pptx`: **14 / 16 (87.5%) — EXEMPLARY (Publication / Conference Award Tier)** (481 words, all 11 empirical checks passed, zero collisions).

---

## 5. The 10-Minute Oral Presentation Coach

```text
TOTAL PRESENTATION TIME: 10 MINUTES (HARD CAP)
├── 1. The Interoperability Crisis & RQ : 2 Minutes
│   └── Point to "Assumed Compatibility" & broken bridge on hero graphic; explain why 80% curation time is lost.
├── 2. Hero Infographic & Core Model   : 3 Minutes
│   └── Guide audience to the luminous Radical Transparency Engine: URI -> conformsTo -> Profile -> identifies -> Representation.
│       Explain the transfer of burden: servers declare machine-actionable typed linksets; clients contextualize.
├── 3. The 4 Pillars & London Tube Map : 3 Minutes
│   └── Walk along the subway transit highway: 10 Linkset Patterns (RFC 9264), cross-org alignment (EOSC, CDIF, OGC),
│       and the practical wrx toolchain. Point to the "Maximum Boredom" metric badge.
└── 4. Outlook, Limitations & Dual QR  : 2 Minutes
│   └── Disclose community alignment limitation, announce Q3 2026 EOSC-if pattern formalization,
│       and invite listeners to scan the paper and GitHub proposal QR codes.
```


