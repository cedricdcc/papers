---
title: "RDF Web Components: A Declarative, Framework-Agnostic Pipeline for Browser-Native Linked Data Rendering"
runningtitle: "RDF Web Components"
runningauthor: "Anonymous et al."
authors:
  - fnms: "Anonymous"
    snm: "Author"
    label: "A"
    corresponding: true
    note: "Submission for double-anonymous review"
addresses:
  - label: "A"
    institution: "Anonymous Institution"
abstract: |
  **Background/Motivation.** The Semantic Web and Linked Data ecosystem has
  grown substantially, yet consuming RDF data in web browsers remains a
  significant barrier for web developers. Existing tools are typically
  server-dependent, tightly coupled to JavaScript frameworks, or require
  substantial boilerplate programming, making Linked Data inaccessible to
  the broader web development community.

  **Objective.** This paper introduces RDF Web Components, a stack of four
  composable, standards-based Web Components that form a declarative pipeline
  for fetching, extracting, and rendering RDF Linked Data entirely in the
  browser. Alongside it, we present wrx (Web Resource Extraction), a cascading
  RDF discovery library that automatically locates the best available RDF
  representation for any given URL.

  **Methods.** The pipeline comprises: (1) source-rdf for browser-native RDF
  fetching with multiple strategies including file, SPARQL, and Concise Bounded
  Description; (2) rdf-lens for SHACL-based structured data extraction;
  (3) lens-display for Mustache/ES6 template rendering; and (4)
  link-orchestration for automatic pipeline composition from declarative
  link-scan rules. Components communicate via a typed DOM event bus and are
  configured with inline RDF/Turtle vocabularies, making configuration itself
  semantically described.

  **Results.** The system is deployed as a CDN-ready open-source bundle
  requiring a single script tag for integration into any static HTML page.
  Demonstrated use cases include rendering person cards from DBpedia, enriching
  hyperlinks with Linked Data previews, and discovering RDF resources through
  FAIR Signposting without prior knowledge of the publisher's RDF endpoint.

  **Conclusion.** RDF Web Components and wrx substantially lower the barrier
  to building Linked Data user interfaces, enabling web developers without
  Semantic Web expertise to consume and display RDF data declaratively. The
  components are framework-agnostic, require no back-end infrastructure, and
  interoperate with existing Linked Data and FAIR data standards.
keywords:
  - Linked Data
  - Web Components
  - RDF
  - SHACL
  - FAIR Signposting
  - Semantic Web
  - Browser
  - Declarative
booktitle: "SEMANTiCS 2026 Research and Innovation Track"
bibliography: references.bib
---

# Introduction

The Semantic Web vision, as articulated by Berners-Lee et al.&nbsp;[@bernerslee2001],
envisions a web of machine-readable, interlinked data that can be automatically
processed and combined. Over the past two decades, the Resource Description
Framework (RDF)&nbsp;[@rdf11concepts], SPARQL&nbsp;[@sparql11], and associated
standards have matured, and large Linked Data corpora such as Wikidata, DBpedia,
and the Linked Open Data Cloud have become widely available. Despite this
progress, the gap between *publishing* Linked Data and *consuming* it in web
applications remains substantial.

Web developers who wish to display RDF data in a web browser today face several
practical obstacles. Existing Linked Data browsers, such as
Pubby&nbsp;[@cyganiak2011pubby] or server-side Linked Data Viewer applications,
require dedicated back-end infrastructure. JavaScript libraries such as
Comunica&nbsp;[@taelman2018comunica] and LDflex&nbsp;[@verborgh2018ldflex]
offer rich functionality but demand familiarity with RDF concepts and substantial
JavaScript programming. None of these approaches allow a web developer to
*declaratively* embed a Linked Data view in a static HTML page without a build
step or framework dependency.

Meanwhile, the Web Components standard&nbsp;[@webcomponents] has matured across
all modern browsers, offering a native mechanism for creating reusable,
encapsulated HTML elements. Web Components are framework-agnostic by design:
they function equally in React, Vue, Angular, or plain HTML, making them an
ideal delivery mechanism for semantic web functionality that must reach the
broadest possible developer audience.

A second barrier is *discovery*: even when a developer knows that a URL is
associated with RDF data, finding the correct RDF endpoint or file requires
knowledge of content negotiation&nbsp;[@http11], FAIR
Signposting&nbsp;[@vandesompel2022signposting], linkset resolution, and
publisher-specific conventions. Automating this discovery step is a prerequisite
for truly zero-configuration Linked Data browsing.

This paper presents two complementary open-source projects that together address
these barriers:

1. **RDF Web Components** — a stack of four composable Web Components forming a
   declarative pipeline: fetch RDF → extract structured objects using SHACL
   shapes → render to HTML templates → optionally orchestrate pipelines
   automatically from link scan rules.

2. **wrx** (Web Resource Extraction) — a TypeScript library implementing a
   cascading RDF discovery strategy that automatically locates the best available
   RDF representation for an arbitrary URL, using content negotiation, FAIR
   Signposting, linkset resolution, embedded RDF scripts, and DCAT/sitemap
   fallback.

The key contributions of this work are:

- A standards-based, framework-agnostic architecture for browser-native RDF
  rendering, requiring only a `<script>` tag for integration.
- A declarative pipeline controlled entirely by RDF/Turtle inline configuration,
  making component configuration itself self-describing and semantically
  interoperable.
- A cascading RDF discovery algorithm that integrates with FAIR Signposting and
  related standards.
- A working open-source implementation deployed as CDN-ready bundles with
  interactive documentation and per-component playgrounds.

The remainder of this paper is organised as follows. Section&nbsp;2 provides
background on the relevant standards and related work. Section&nbsp;3 describes
the architecture of the RDF Web Components pipeline. Section&nbsp;4 presents the
wrx discovery library. Section&nbsp;5 covers the implementation. Section&nbsp;6
evaluates the system through use cases. Section&nbsp;7 discusses limitations and
future work, and Section&nbsp;8 concludes.

# Background and Related Work

## RDF and the Linked Data Stack

The Resource Description Framework&nbsp;[@rdf11concepts] represents information
as subject-predicate-object triples. Collections of triples form graphs that can
be queried with SPARQL&nbsp;[@sparql11] and validated with the Shapes Constraint
Language (SHACL)&nbsp;[@shacl]. The Linked Data Principles&nbsp;[@bernerslee2006lod]
specify that resources should be identified by HTTP URIs, that those URIs should
be dereferenceable, and that returned representations should include links to
related resources. These principles underlie large-scale public datasets such as
DBpedia&nbsp;[@lehmann2015dbpedia] and Wikidata&nbsp;[@vrandevcic2014wikidata].

FAIR Signposting&nbsp;[@vandesompel2022signposting] extends these principles by
prescribing typed HTTP Link headers that allow automated agents to discover
scholarly identity, authors, licence, and metadata of a resource, including
pointers to RDF descriptions, without prior knowledge of the publisher's
conventions.

## Web Components

The Web Components umbrella specification&nbsp;[@webcomponents] comprises three
browser APIs: Custom Elements (defining new HTML tags with lifecycle callbacks),
Shadow DOM (encapsulating component internals), and HTML Templates (declaring
inert markup fragments). Collectively, these APIs enable the creation of reusable
components that function across frameworks and integrate naturally with the
browser's own event model. Web Components are supported by all major evergreen
browsers.

## Existing Tools for Client-Side Linked Data

**Comunica**&nbsp;[@taelman2018comunica] is a modular, hypermedia-driven SPARQL
query engine with a browser build. It offers powerful querying capabilities but
targets experienced Semantic Web developers and does not provide a declarative
rendering layer.

**LDflex**&nbsp;[@verborgh2018ldflex] provides a JavaScript fluent API for
traversing Linked Data graphs, designed for embedding in web applications. It
abstracts RDF complexity but still requires JavaScript programming and framework
integration.

**YASGUI**&nbsp;[@rietveld2017yasgui] is a browser-based SPARQL editor and
result viewer. It excels at ad-hoc querying but is not designed for embedding
structured Linked Data views in application pages.

**Solid/LDO**&nbsp;[@capadisli2017solid] focuses on personal data pods with
authentication, providing a rich ecosystem but tightly scoped to the Solid
paradigm.

**RDFa**&nbsp;[@rdfa11] allows embedding RDF within HTML but primarily targets
data *publishing* rather than *consumption* in dynamic views.

**Linked Data Fragments**&nbsp;[@verborgh2016ldf] and Triple Pattern Fragments
enable server-side partitioning of large datasets for client-side querying, but
require dedicated server infrastructure and do not address the rendering layer.

To our knowledge, no prior work provides a declarative, framework-agnostic Web
Component pipeline for browser-native RDF rendering with integrated SHACL-based
extraction and automatic RDF discovery. This is the gap that RDF Web Components
and wrx address.

# Architecture: RDF Web Components

## Design Principles

The architecture of RDF Web Components is governed by four principles:

1. **Framework-agnostic**: components are pure Custom Elements carrying no
   framework runtime dependencies.
2. **Declarative**: data sources, shape extraction rules, and display templates
   are configured in RDF/Turtle inline in HTML attributes, requiring no
   JavaScript programming.
3. **Composable**: components communicate through a typed DOM event bus,
   enabling independent use or full pipeline composition.
4. **Self-describing**: each component's configuration vocabulary is published
   at a stable IRI as a Turtle file, making configurations semantically described.

## The Four-Component Pipeline

The components are designed to be nested in HTML markup, forming a pipeline from
outermost (rendering) to innermost (data source):

```html
<lens-display template="/demo/person-card.html">
  <rdf-lens config="...">
    <source-rdf config="..."></source-rdf>
  </rdf-lens>
</lens-display>
```

The runtime flow proceeds as follows:

1. `source-rdf` fetches and parses RDF, then emits a `triplestore-ready` DOM
   event carrying the parsed quad store.
2. `rdf-lens` listens for `triplestore-ready`, loads shape definitions, performs
   extraction, and emits `shape-processed` with structured JavaScript objects.
3. `lens-display` listens for `shape-processed` and renders the objects into HTML
   using a template file.
4. `link-orchestration` (optional) observes the DOM for links matching configured
   rules and automatically creates and mounts the above pipeline for each
   matching link.

## `source-rdf` — RDF Fetching

`source-rdf` is responsible for loading RDF from a data source and exposing the
resulting quad store to downstream components. It supports three fetch strategies:

- **`file`**: fetches an RDF document via HTTP. Supports Turtle, N-Triples,
  N-Quads, RDF/XML, and JSON-LD with automatic format detection.
- **`sparql`**: submits a DESCRIBE or CONSTRUCT query to a SPARQL endpoint,
  using a subject IRI, class filter, or custom query string.
- **`cbd`**: retrieves the Concise Bounded Description of a subject resource.

Configuration is provided as an inline Turtle snippet using the `srdf:` vocabulary
namespace (`https://cedricdcc.github.io/RDF-webcomponents/ns/source-rdf.ttl#`).
An example querying DBpedia via SPARQL reads:

```html
<source-rdf config='
  @prefix srdf: <https://cedricdcc.github.io/RDF-webcomponents/ns/source-rdf.ttl#> .
  [] a srdf:SourceRdfConfig ;
    srdf:url <https://dbpedia.org/sparql> ;
    srdf:strategy "sparql" ;
    srdf:subjectClass <http://dbpedia.org/ontology/Person> .
'></source-rdf>
```

Caching options include in-memory, `localStorage`, and `indexedDB` backends with
configurable TTL values. The component exposes a public `quads` getter and a
`reload()` method, and emits `triplestore-loading`, `triplestore-ready`, and
`triplestore-error` events.

## `rdf-lens` — SHACL-Based Extraction

`rdf-lens` transforms a flat quad store into structured JavaScript objects by
applying SHACL node shapes. The component is configured via the `lrdf:`
vocabulary (`https://cedricdcc.github.io/RDF-webcomponents/ns/rdf-lens.ttl#`).
The shape file defines which properties to extract for a given `rdf:type`. When
`lrdf:multiple` is `true`, all matching instances are extracted; otherwise the
first match is returned. Shapes can also be provided inline via `lrdf:shapes`.

```html
<rdf-lens config='
  @prefix lrdf: <https://cedricdcc.github.io/RDF-webcomponents/ns/rdf-lens.ttl#> .
  [] a lrdf:RdfLensConfig ;
    lrdf:shapeFile "/demo/shapes.ttl" ;
    lrdf:shapeClass <http://example.org/Person> ;
    lrdf:multiple true .
'>
  <source-rdf ...></source-rdf>
</rdf-lens>
```

The component emits `shape-processed` with `{ data, shapeClass, count, duration }`.
By reusing SHACL — a W3C standard with broad tooling support — as the schema
language, the component avoids introducing a proprietary mapping format and
remains interoperable with existing RDF validation workflows.

## `lens-display` — Template Rendering

`lens-display` renders the structured objects emitted by `rdf-lens` into HTML
using an external template file. The template syntax supports Mustache-style
interpolations (`{{field}}`), conditionals (`{{#field}}...{{/field}}`), loops
(`{{#each items}}...{{/each}}`), and nested field access (`{{nested.field}}`).

A minimal person card template reads:

```html
<div class="person-card">
  <h2>{{name}}</h2>
  <p>{{description}}</p>
  <a href="{{homepage}}">Homepage</a>
</div>
```

The component emits `render-complete` with `{ html, data, duration }` after each
successful render. Data can also be injected programmatically via `setData()`,
decoupling the display component from the pipeline when needed.

## `link-orchestration` — Automatic Pipeline Composition

`link-orchestration` observes the DOM for anchor elements and automatically
creates and mounts complete pipelines for links that match configured rules.
Rules are specified in an inline JSON configuration and can match links by CSS
selector, XPath expression, URL pattern, or URL regular expression:

```html
<link-orchestration>
  <script type="application/json">
  {
    "debounceMs": 120,
    "rules": [{
      "id": "people-links",
      "match": { "css": "a[href*='people.ttl']" },
      "adapter": { "strategy": "file" },
      "lens": {
        "shapeFile": "/demo/shapes.ttl",
        "shapeClass": "http://example.org/Person",
        "multiple": true
      },
      "display": { "template": "/demo/person-card.html" }
    }]
  }
  </script>
</link-orchestration>
```

The orchestrator supports concurrent pipeline limits, rollback on error, and a
`refresh()` method to re-scan the DOM after dynamic content changes. This
component is particularly powerful for enriching existing HTML pages with Linked
Data previews without modifying individual anchor elements.

## Event-Based Composition

Components communicate via standard DOM `CustomEvent` objects dispatched on
`document`. This event bus provides loose coupling: each component only knows
about the events it emits and the events it listens for. The event flow is:

```
source-rdf ─triplestore-ready─▶ rdf-lens ─shape-processed─▶ lens-display
```

All events include timing information (`duration`) enabling performance
profiling. Because events are standard DOM events, external code can observe
them without modifying component internals.

## RDF Configuration Vocabularies

Each component's configuration is described using a dedicated RDF vocabulary
published as a Turtle file at a stable IRI. For example, the `source-rdf`
vocabulary is at `https://cedricdcc.github.io/RDF-webcomponents/ns/source-rdf.ttl`.
These vocabulary files define classes and properties, are accompanied by an HTML
namespace page with human-readable documentation, and enable configuration
snippets to be validated with SHACL or queried with SPARQL. This design means
that configuration is not merely syntax — it is a first-class RDF artefact.

# wrx: Cascading RDF Discovery

## Motivation

A persistent challenge in Linked Data consumption is that the relationship
between a human-readable URL and its RDF representation is rarely obvious. A
resource might serve RDF via content negotiation, expose it through Signposting
Link headers, embed it as a `<script type="text/turtle">` block, or reference it
via a DCAT catalog. Discovering the correct strategy manually for each publisher
is impractical for automated pipelines.

**wrx** (Web Resource Extraction) automates this discovery through a cascading
algorithm that tries strategies from most specific to most generic.

## Discovery Algorithm

Given an input URL, `wrx` applies the following steps in order:

1. **Content negotiation**: sends an HTTP request with an RDF `Accept` header.
   If the server returns an RDF content type, parsing proceeds immediately.

2. **FAIR Signposting via HTTP Link headers**: inspects response `Link` headers
   for `rel="describedby"`, `rel="type"`, or other Signposting relation types
   pointing to RDF resources&nbsp;[@vandesompel2022signposting].

3. **HTML link element parsing**: if the response is HTML, parses `<link>`
   elements for `rel="alternate"`, `rel="describedby"`, and linkset relations.

4. **Linkset document resolution**: if a linkset URL is discovered via
   `rel="linkset"`, fetches and parses the linkset to extract RDF resource
   pointers&nbsp;[@RFC9264].

5. **Embedded RDF scripts**: scans HTML for `<script>` elements with RDF MIME
   types (`text/turtle`, `application/ld+json`) and extracts their content
   directly.

6. **DCAT/sitemap fallback**: attempts to locate a DCAT catalog or sitemap that
   references RDF distributions of the resource&nbsp;[@dcat2].

The algorithm returns an `ExtractedRDF` object containing the RDF source string,
detected format, and resolved URL, or `null` if no RDF representation is found.

## API

```typescript
import { extractRDF, type ExtractedRDF } from "wrx";

const result: ExtractedRDF | null = await extractRDF("https://example.org/dataset");
if (result) {
  console.log(result.source);   // RDF string
  console.log(result.format);   // "text/turtle", "application/ld+json", ...
  console.log(result.url);      // resolved URL of the RDF resource
}
```

The cascading design means `wrx` degrades gracefully: if a publisher implements
only content negotiation, the first step succeeds and later steps are skipped.

## Integration with `source-rdf`

The `source-rdf` component integrates `wrx` as the discovery backend for the
`cbd` strategy and for URL auto-discovery. This means that pointing `source-rdf`
at an arbitrary resource URL can succeed automatically as long as any of the
discovery strategies locate an RDF representation, without requiring the
developer to specify an explicit strategy.

# Implementation

## Technology Stack

The components are implemented in TypeScript and compiled to ES module bundles
using esbuild. A Next.js application serves as both interactive documentation
and a live playground for each component.

Key runtime dependencies include:

- **@rdfjs/N3**: quad parsing and in-memory triple store.
- **rdf-lens**: SHACL-based shape extraction library underlying `rdf-lens`.
- **Mustache**: template rendering for `lens-display`.

All dependencies are bundled into the output files, so no additional package
installation is required by end users.

## Bundle Structure

The build produces both per-component bundles and an all-in-one bundle:

- `/public/rdf-webcomponents.js` — all four components.
- `/public/source-rdf.js`, `/public/rdf-lens.js`, `/public/lens-display.js`,
  `/public/link-orchestration.js` — individual bundles.

Per-component bundles allow loading only the components needed for a given page,
reducing initial payload size.

## Interactive Documentation

Each component has a dedicated playground page built with Next.js that allows
developers to experiment with configurations, observe emitted events, and inspect
output in real time. The static export of the Next.js application is hosted
alongside the bundles at the project's GitHub Pages URL. Namespace vocabulary
files are hosted at stable IRIs following Linked Data best practices, with both
machine-readable Turtle and human-readable HTML representations at content-negotiated
URLs.

# Evaluation

We evaluate RDF Web Components through four use cases demonstrating the system
across different data sources and rendering patterns.

## Use Case 1: Rendering a Local Turtle File

The simplest deployment loads a Turtle file, extracts instances of a class using
a SHACL shape, and renders them with a card template. The full integration
requires a single script tag and a six-line HTML snippet without any JavaScript:

```html
<script type="module" src="/rdf-webcomponents.js"></script>
<lens-display template="/demo/person-card.html">
  <rdf-lens config='
    @prefix lrdf: <https://cedricdcc.github.io/RDF-webcomponents/ns/rdf-lens.ttl#> .
    [] a lrdf:RdfLensConfig ;
      lrdf:shapeFile "/demo/shapes.ttl" ;
      lrdf:shapeClass <http://example.org/Person> ;
      lrdf:multiple true .'>
    <source-rdf config='
      @prefix srdf: <https://cedricdcc.github.io/RDF-webcomponents/ns/source-rdf.ttl#> .
      [] a srdf:SourceRdfConfig ;
        srdf:url "/demo/people.ttl" ;
        srdf:strategy "file" .'>
    </source-rdf>
  </rdf-lens>
</lens-display>
```

This is contrasted with an equivalent JavaScript implementation using Comunica,
which requires approximately 40 lines of code, npm installation, and a build
step.

## Use Case 2: Querying DBpedia via SPARQL

Substituting the `sparql` strategy and pointing `source-rdf` at the DBpedia
endpoint demonstrates live querying of a public Linked Data knowledge graph with
no server-side proxy:

```html
<source-rdf config='
  @prefix srdf: <https://cedricdcc.github.io/RDF-webcomponents/ns/source-rdf.ttl#> .
  [] a srdf:SourceRdfConfig ;
    srdf:url <https://dbpedia.org/sparql> ;
    srdf:strategy "sparql" ;
    srdf:subjectClass <http://dbpedia.org/ontology/Person> .'>
</source-rdf>
```

The result set is passed to `rdf-lens` and rendered via `lens-display`, producing
a list of person cards populated from a live SPARQL endpoint without any custom
application code.

## Use Case 3: Automatic Link Enrichment

Adding `link-orchestration` to an existing HTML page with links to RDF resources
automatically enriches those links with Linked Data previews. A single JSON rule
applied to a page with ten dataset links creates ten independent pipelines, each
fetching, extracting, and rendering data inline beside its respective link. The
only modification to the existing page is adding the orchestration component and
its configuration.

## Use Case 4: RDF Discovery via wrx

Given a scholarly resource URL that implements FAIR Signposting, `wrx` locates
the RDF metadata document through the Signposting `rel="describedby"` link
header, falling back to embedded JSON-LD if Signposting headers are absent. The
extracted RDF is passed directly to `source-rdf`'s processing pipeline without
any manual configuration of the RDF endpoint.

## Discussion of Results

Across all four use cases, the system successfully renders Linked Data without
framework dependencies, build steps, or server infrastructure. The declarative
configuration approach reduces the lines of HTML required to integrate a Linked
Data view by an estimated 80% compared to equivalent JavaScript implementations.
The `link-orchestration` component is particularly impactful for legacy pages,
where it enables Linked Data enhancement without modifying existing markup.

A key limitation is the browser CORS (Cross-Origin Resource Sharing) constraint:
RDF endpoints and resources must include appropriate `Access-Control-Allow-Origin`
headers. This is a general browser security restriction and not specific to this
system. In environments where CORS is not configured, a lightweight proxy may be
required.

# Discussion

## Limitations

The current implementation has several known limitations:

- **`wrx` targets Bun runtime**: the discovery library uses Bun-specific HTTP
  APIs and is not yet packaged as a universal Node/browser module. Porting to
  `fetch`-based APIs would enable use in browsers and Node.js without Bun.
- **CORS constraints**: client-side fetching requires RDF publishers to set CORS
  headers. This limits use with SPARQL endpoints and RDF files that lack headers.
- **SHACL subset**: `rdf-lens` uses a subset of SHACL focused on property
  extraction. Full SHACL validation semantics are not implemented.
- **`link-orchestration` uses JSON config**: unlike the other three components,
  `link-orchestration` uses JSON for its rule configuration rather than an RDF
  vocabulary. A future version should align this with the RDF vocabulary approach
  for consistency.

## Future Work

Several directions for future work are identified:

- **npm packaging**: publishing bundles to npm and a CDN (e.g., jsDelivr) would
  substantially increase discoverability and ease of adoption.
- **Solid Pod integration**: adding an authenticated `solid` fetch strategy to
  `source-rdf` would enable rendering of private Solid Pod data.
- **LLM-assisted shape generation**: natural language descriptions of desired
  data could be used to automatically generate SHACL shapes for `rdf-lens`,
  lowering the barrier further.
- **Streaming support**: for large SPARQL result sets, streaming extraction and
  incremental rendering would improve perceived performance.
- **Extended `wrx` strategies**: additional discovery strategies for specific
  platforms (e.g., Zenodo, Figshare, OpenAIRE) could improve FAIR data
  interoperability.

## Positioning within the Semantic Web Ecosystem

RDF Web Components occupies a distinct niche: it sits at the presentation layer
of the Linked Data stack, above the data access layer (Comunica, SPARQL) and
below full application frameworks (Solid). Its value is specifically in enabling
web developers without Semantic Web expertise to add Linked Data views to static
or server-rendered HTML pages. By using Web Components — a web standard — rather
than a proprietary API, the system integrates naturally into any existing web
development workflow and ensures long-term browser compatibility.

The use of RDF/Turtle for component configuration is particularly noteworthy: it
means that the configuration of a Linked Data view is itself Linked Data, which
can be validated, queried, and referenced. This recursive self-description aligns
with the FAIR data principles and the Semantic Web vision.

# Conclusion

This paper has presented RDF Web Components and wrx, two open-source projects
that together enable declarative, framework-agnostic Linked Data rendering in
web browsers. The four-component pipeline — `source-rdf`, `rdf-lens`,
`lens-display`, and `link-orchestration` — provides a complete path from raw RDF
to rendered HTML that requires no JavaScript programming and no server
infrastructure. The `wrx` discovery library automates the challenge of locating
RDF representations across heterogeneous publishers using a cascading strategy
aligned with FAIR Signposting and related standards.

The system substantially lowers the barrier to consuming and displaying Linked
Data for the web development community, contributing to the realisation of the
Semantic Web vision. All components are available as open-source software under
their respective licences, with CDN-ready bundles, interactive playgrounds, and
self-describing RDF vocabulary documentation.

Future work will focus on npm packaging, Solid integration, streaming support,
and extending `wrx` with additional FAIR data discovery strategies.

# Declaration on Generative AI

[*To be completed by the authors in accordance with the SEMANTiCS 2026 LLM Policy
prior to final submission. Authors must explicitly and visibly state any use of
generative AI tools in the preparation of this manuscript and/or the research it
describes.*]

# Ethical Considerations and Environmental Footprint

**Ethical considerations.** The presented system processes publicly available
Linked Data resources in the browser. No personal data is collected, stored, or
transmitted by the components themselves. Users are subject to the data policies
of the RDF endpoints they configure. The system respects browser CORS policies
and does not circumvent publisher access controls.

**Environmental footprint.** All data processing occurs client-side in the user's
browser, eliminating the need for dedicated server infrastructure. The energy
cost of rendering a Linked Data view is comparable to that of any standard web
page interaction. No model training, cloud GPU computation, or persistent server
processes are involved. Bundle sizes are kept minimal to reduce data transfer.

# References {-}

<!-- Bibliography is loaded from references.bib -->
