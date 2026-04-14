# Requirements for the SEMANTICS 2026 RDF Web Components Paper

## Conference Information

| Field | Details |
|---|---|
| **Conference** | SEMANTiCS 2026 |
| **Track** | Research and Innovation Track |
| **Abstract Submission** | April 23, 2026, 23:59 AoE |
| **Full Paper Submission** | April 30, 2026, 23:59 AoE |
| **Reviewing Format** | Double-Anonymous |
| **Submission Link** | [EasyChair](https://easychair.org/conferences?conf=semantics2026) |
| **Page Length** | Maximum 15 pages (excluding references) |
| **Proceedings** | IOS Press (Open Access) |
| **Presentation** | In-person |
| **Contact** | semantics2026-research@easychair.org |

---

## Submission Checklist

- [ ] Abstract submitted by April 23, 2026 (structured abstract strongly encouraged)
- [ ] Full paper submitted by April 30, 2026
- [ ] Paper is maximum 15 pages (excluding references)
- [ ] Formatted using IOS Press Word or LaTeX template (or Overleaf copy)
- [ ] Paper is written in English
- [ ] Submission is **anonymous** (double-anonymous review)
- [ ] Includes **Declaration on Generative AI** at the end
- [ ] Addresses relevant **ethical issues**
- [ ] Provides estimates of the **environmental footprint** of the work
- [ ] Links to code/materials anonymised (e.g., via Anonymous GitHub)
- [ ] Optional: ORKG comparison included via EasyChair field
- [ ] Paper is **not under review elsewhere** and has **not been previously published**
- [ ] At least one author prepared to attend **in person**
- [ ] Fast-track to Posters and Demos opt-in box checked (optional)

---

## Relevant Conference Topics

The paper primarily addresses the following SEMANTiCS 2026 topics of interest:

- **Web Semantics & Linked (Open) Data** — the paper presents components for browsing and rendering Linked Data resources directly in the browser.
- **User Interfaces and Usability of Semantic Technologies** — declarative, framework-agnostic HTML components lower the barrier to consuming RDF in web applications.
- **Semantic Interoperability** — RDF discovery via FAIR Signposting, content negotiation, and linkset resolution enables cross-domain data access.
- **Knowledge Engineering and Management** — SHACL-based shape extraction (`rdf-lens`) supports structured knowledge access patterns.
- **Linked Data storage, triple stores, graph databases** — the `source-rdf` component supports multiple RDF loading strategies including SPARQL endpoints.
- **Decentralised and Federated Knowledge Graphs** — `wrx` enables automated discovery of RDF resources without centralised registries.
- **Provenance and Data Change Tracking** — caching strategies and cache-TTL configuration support reproducible, versioned data access.

---

## Paper Goal and Motivation

This paper presents **RDF Web Components** and **wrx**, two open-source projects that together enable declarative consumption and rendering of RDF Linked Data directly in web browsers, without requiring any JavaScript framework or back-end server.

### Why This Exists

The Semantic Web vision relies on machine-readable, interlinked data, but making that data accessible to humans remains difficult. Existing tools for browsing or rendering RDF typically:

1. Require a back-end server or intermediary proxy.
2. Are tightly coupled to a specific JavaScript framework (React, Angular, Vue).
3. Demand significant boilerplate setup and programming knowledge.
4. Do not integrate automatically with the FAIR Signposting and content negotiation standards used by data publishers.

**RDF Web Components** addresses these gaps by providing four composable, standards-based Web Components that form a declarative pipeline: fetch RDF → extract structured data using SHACL shapes → render to HTML templates. The components run entirely in the browser, require zero framework dependencies, and can be embedded in any static HTML page with a single `<script>` tag.

**wrx** (Web Resource Extraction) addresses the complementary challenge of *discovering* RDF resources. Given an arbitrary URL, `wrx` applies a cascading strategy (content negotiation, FAIR Signposting, linkset resolution, embedded RDF scripts, DCAT/sitemap fallback) to find the best available RDF representation. This powers the `source-rdf` component and can also be used as a standalone library.

---

## Required Content Sections

### 1. Abstract (structured, ≤250 words)

Structure:
- **Background/Motivation**: difficulty of rendering RDF in the browser without framework lock-in.
- **Objective**: declarative, framework-agnostic Linked Data rendering via Web Components.
- **Methods**: four-component pipeline; SHACL-based shape extraction; cascading RDF discovery.
- **Results**: working implementation deployable via CDN; demonstrated on real Linked Data endpoints.
- **Conclusion**: lowers barrier to building Linked Data user interfaces.

### 2. Introduction

- Semantic Web and Linked Data as a growing data layer of the web.
- Gap: consuming RDF in the browser is hard — existing tools are server-side, framework-specific, or require custom code.
- Problem statement: how to enable declarative, browser-native RDF rendering for web developers without Semantic Web expertise.
- Contributions:
  1. `source-rdf` — browser-native RDF fetching with multiple strategies and caching.
  2. `rdf-lens` — SHACL-based structured data extraction.
  3. `lens-display` — Mustache/ES6 template rendering.
  4. `link-orchestration` — automatic pipeline composition from link scan rules.
  5. `wrx` — cascading RDF discovery library.
- Paper organisation.

### 3. Background and Related Work

- **RDF and Linked Data fundamentals** (brief) — RDF data model, SPARQL, SHACL.
- **Web Components standard** — Custom Elements, Shadow DOM, HTML Templates; framework-agnostic lifecycle.
- **FAIR Signposting** — typed HTTP link headers for FAIR data discovery.
- **Content negotiation** — HTTP Accept/Content-Type for multi-format RDF publishers.
- **Existing tools and related approaches**:
  - Server-side: Linked Data Fragments, Triple Pattern Fragments, Pubby, Linked Data Viewer.
  - Client-side: LDflex, Comunica (browser builds), YASGUI, RDFa processors, Solid/LDO.
  - Web Components for Linked Data: (prior art is limited — highlight novelty).
  - RDF discovery: VOID descriptions, DCAT catalogs, FAIR Signposting.
- Position this work relative to above.

### 4. Architecture and Design

#### 4.1 Design Goals
- Framework-agnostic (pure Custom Elements API).
- Declarative configuration in RDF/Turtle inline.
- Composable pipeline via Custom Element nesting and DOM events.
- Zero back-end dependency.
- Extensible via public events and getter APIs.

#### 4.2 The Four-Component Pipeline

For each component describe:
- Purpose / responsibility.
- Attributes and inline RDF config vocabulary (with namespace IRI).
- Events emitted and consumed.
- Public API (getters and methods).
- Code/HTML example.

Components:
- **`source-rdf`**: fetches and parses RDF; strategies: `file`, `sparql`, `cbd`; caching options.
- **`rdf-lens`**: applies SHACL-like shape extraction using `rdf-lens` library; emits structured JS objects.
- **`lens-display`**: renders extracted data to HTML using Mustache/ES6 template files.
- **`link-orchestration`**: scans the DOM for links, matches rules (CSS, XPath, URL patterns), and auto-mounts pipelines.

#### 4.3 Event-Based Composition

Describe the DOM event bus (`triplestore-ready` → `shape-processed` → `render-complete`) and how it enables loose coupling.

#### 4.4 RDF Configuration Vocabularies

Describe the namespace vocabularies (TTL files) published at stable IRIs for each component — this makes component configuration itself described in RDF and self-documenting.

#### 4.5 wrx — Cascading RDF Discovery

- Problem: given an arbitrary URL, find the RDF representation.
- Cascading strategy:
  1. Content negotiation (HTTP Accept header).
  2. FAIR Signposting (HTTP Link header, rel types).
  3. HTML link parsing (linkset, describe, alternate).
  4. Linkset document resolution.
  5. Embedded RDF scripts in HTML (`<script type="text/turtle">`).
  6. DCAT/sitemap fallback.
- Integration with `source-rdf` (`strategy: "cbd"` or URL auto-discovery).
- Standalone use as a Bun/Node library.

### 5. Implementation

- Technology choices: TypeScript, esbuild, Next.js for playground/docs.
- Bundle structure: per-component bundles + all-in-one bundle.
- Namespace pages as self-describing HTML + TTL vocabulary files.
- Playground pages for each component (interactive demos).
- Build and distribution via CDN-friendly static output.

### 6. Evaluation / Use Cases

Demonstrate the system on concrete Linked Data use cases:

1. **Rendering a person dataset** from a local Turtle file using `source-rdf` + `rdf-lens` + `lens-display`.
2. **Querying DBpedia via SPARQL** endpoint using the `sparql` strategy.
3. **Automatic link enrichment** with `link-orchestration` — embedding RDF previews next to hyperlinks on a static page.
4. **Discovery from an arbitrary URL** via `wrx` cascading strategy.

Evaluation criteria:
- Lines of HTML required vs. equivalent JavaScript approach.
- Zero-framework integration test (plain HTML file, no build step).
- Correctness of SHACL extraction against known datasets.
- Browser compatibility (target: all modern evergreen browsers).

### 7. Discussion

- Limitations: currently targets Bun runtime for `wrx`; browser CORS constraints require RDF publishers to set headers.
- Future work:
  - SPARQL CONSTRUCT/DESCRIBE support improvements.
  - More caching backends.
  - Solid Pod integration for authenticated RDF access.
  - LLM-assisted shape generation from natural language.
  - Packaging to npm for wider distribution.
- How this fits the broader Linked Data and FAIR Data ecosystem.

### 8. Conclusion

- Summary of contributions.
- Impact on democratising Linked Data consumption for web developers.
- Availability: open source, CDN-deployable.

### 9. Declaration on Generative AI (required by SEMANTiCS 2026)

Must explicitly state the use (or non-use) of LLMs/generative AI in the preparation of the paper and/or the research.

### 10. Ethical Considerations and Environmental Footprint

- **Ethics**: no personal data collected; RDF data processed client-side; components respect CORS policies.
- **Environmental footprint**: client-side processing eliminates server infrastructure; estimated energy for running browser-side JS is negligible; no training required.

### 11. References

Key references to include:
- RDF 1.1 Concepts (W3C).
- SHACL (W3C).
- Linked Data Principles (Berners-Lee).
- FAIR Signposting Profile.
- Web Components specifications (WHATWG/W3C).
- Comunica: a modular SPARQL query engine.
- LDflex.
- YASGUI.
- FAIR Data Principles (Wilkinson et al., 2016).
- Relevant prior work on client-side Linked Data consumption.

---

## Style and Formatting Notes

- **Template**: IOS Press Book Article LaTeX template (Overleaf or local).
- **Bibliography style**: Vancouver (`.bst` included in repository templates).
- **Anonymisation**: remove all identifying information; use Anonymous GitHub for code links.
- **Figures**: include pipeline architecture diagram; component nesting diagram; `wrx` discovery flowchart.
- **Page budget** (rough):
  - Abstract + Introduction: ~2 pages
  - Background and Related Work: ~2 pages
  - Architecture: ~5 pages
  - Evaluation/Use Cases: ~3 pages
  - Discussion + Conclusion: ~2 pages
  - Declaration + Ethics: ~0.5 pages
  - References: excluded from page count
