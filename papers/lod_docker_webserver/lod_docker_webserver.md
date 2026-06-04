---
title: "LOD Docker Webserver: A Multi-Channel Testbed for Linked Data Discovery and Web-Scale Metadata Signposting"
runningtitle: "LOD Docker Webserver Testbed"
runningauthor: "C. Decruw"
authors:
  - fnms: "Cedric"
    snm: "Decruw"
    label: "A"
    orcid: "0000-0001-6387-5988"
    corresponding: true
    note: "cedric.decruw@vliz.be"
addresses:
  - label: "A"
    institution: "Flanders Marine Institute (VLIZ), Ostend, Belgium"
abstract: |
  **Background/Motivation.** Linked Data discovery still fails in practice when
  clients must guess where machine-readable descriptions are hidden. Although
  standards already exist, they are typically fragmented across HTTP headers,
  HTML metadata, feeds, well-known endpoints, and domain catalogs.

  **Objective.** This paper documents the `lod_docker_webserver` project as a
  concrete, reproducible testbed that operationalizes these standards into an
  inspectable matrix of discovery channels.

  **Methods.** We analyze the generator-driven architecture, Nginx serving
  configuration, and channel taxonomy used by the project, with a detailed deep
  dive into the `wrx_discovery_classification.md` model and its 30 discovery
  methods.

  **Results.** The repository generates a realistic static topology (up to 150
  pages) in which resource-level and domain-level discovery methods can be
  tested in isolation and in combination, including direct RDF channels and
  inferenced channels.

  **Conclusion.** `lod_docker_webserver` functions as both a compliance
  playground and a design reference for implementing robust Linked Data
  discoverability that aligns with core web principles.
keywords:
  - Linked Open Data
  - discovery testbed
  - Docker
  - Nginx
  - RDF discovery
  - FAIR Signposting
  - metadata interoperability
bibliography: references.bib
---

# Introduction

Linked Data promises machine-actionable interoperability, but practical
adoption is often blocked by one repeated problem: discovery. A URI may resolve
for humans while failing to reveal where RDF is exposed, which relation types
are advertised, or which domain-level catalogs should be followed. The result
is brittle crawler logic, ecosystem-specific heuristics, and low
reproducibility.

The `lod_docker_webserver` repository addresses this by providing a controlled
environment in which discovery signals are intentionally exposed through many
channels at once. Instead of testing one metadata pattern in isolation, the
project generates an integrated landscape in which clients can evaluate
resource-level techniques (e.g., HTML metadata, Link headers, embedded RDF) and
domain-level techniques (e.g., robots, sitemaps, feeds, and well-known
endpoints) using a consistent baseline [@lodrepo].

This paper presents a deep dive into that repository as an implementation
artifact and as a web architecture study. Particular emphasis is placed on the
`wrx_discovery_classification.md` taxonomy, because it codifies not only a list
of strategies, but also the expected extraction semantics for each strategy and
a blueprint for orchestration [@lodclass].

# Repository Overview and Generation Pipeline

The project combines a TypeScript generator with a Dockerized Nginx runtime.
The build step (`npm run generate`) creates all static assets under `dist/` and
the server step (`docker compose up`) serves these assets with explicit header
and MIME behavior.

At a high level, the generated output includes:

- A matrix of synthetic resource pages.
- Alternate RDF serializations for resources (Turtle, JSON-LD, RDF/XML).
- Domain-level discovery artifacts (RSS, Atom, sitemap, robots, manifests,
  well-known endpoints).
- Navigation and channel pages that expose channel-specific behavior.

The generator orchestrator in `generator/index.ts` constructs this topology in
phases: clean/prepare output folders, generate page matrix, serialize resources,
render per-page discovery markup, emit Nginx per-page headers, and generate
channel documentation pages [@lodrepo]. This staged process mirrors how many
real systems compose discovery from application logic plus web server behavior,
which makes the testbed operationally realistic.

# Containerized Web Infrastructure and Delivery Semantics

The runtime is intentionally minimal: one Nginx service in Docker, exposing port
8080. This choice has two benefits. First, the environment is reproducible and
portable. Second, the serving logic is explicit and inspectable in configuration
files instead of hidden in framework middleware.

The Nginx configuration reveals several important interoperability choices
[@lodrepo]:

- Global CORS headers are enabled to support cross-origin extraction clients.
- `/rdf/` applies RDF-relevant MIME mappings (`text/turtle`,
  `application/ld+json`, `application/rdf+xml`).
- `/manifests/` serves web manifests with the expected media type.
- A generated include file (`nginx-headers.conf`) injects strategy-specific HTTP
  headers per page.

This demonstrates a key web principle: discoverability is not purely a payload
concern. It is also an HTTP concern. Correct content types, typed links, and
header-level relations are first-class interoperability mechanisms
[@rfc9110;@rfc8288].

# Web Principles Operationalized by the Testbed

## Principle 1: Dereferenceable HTTP URIs and Representation Selection

The testbed enforces HTTP URI dereferenceability and allows multiple
representations per conceptual resource. This aligns with Linked Data guidance
that URIs should identify resources and provide useful representations upon
resolution [@linkeddata]. Content negotiation and alternate format links are
used as explicit pathways instead of hidden conventions.

## Principle 2: Typed Linking over Ad-hoc Endpoint Guessing

Rather than requiring hardcoded URI templates, the project emphasizes typed
relations (`describedby`, `alternate`, `canonical`, `next`, `prev`, `collection`,
`api-catalog`, `linkset`) as explicit machine hints [@rfc8288;@rfc6596;@rfc9727].
This promotes automation that is standards-driven and explainable.

## Principle 3: Layered Discovery (Resource-Level and Domain-Level)

The taxonomy formalizes two discovery locations: directly at the resource and at
host/domain scope. This reflects real deployments where some signals exist only
at domain level (e.g., robots/sitemap/feed/well-known) while others are
resource-local. Robust clients must combine both.

## Principle 4: Distinguishing Native RDF from Inference Pipelines

The project separates channels where payload is already RDF (Direct RDF) from
channels requiring parsing and semantic mapping (Inferenced RDF). This explicit
separation is architecturally important because confidence, validation, and
failure behavior differ between both classes [@jsonld11;@rdfa11;@microdata].

## Principle 5: Provenance, Identity, and Graph Connectivity

The included strategy set goes beyond format discovery. It also models identity
alignment (`owl:sameAs`), social/semantic relations (FOAF/SKOS), structural
membership, reverse links, and cyclic graph handling. This acknowledges that
web-scale discovery is not only about finding bytes but also about preserving
graph semantics and traversal integrity [@owl2;@skos;@foaf].

# Deep Dive: `wrx_discovery_classification.md`

The classification document structures discovery into a 2x2 matrix:

- **Location dimension**: Resource vs Domain.
- **Extraction dimension**: Direct RDF vs Inferenced RDF.

This produces four quadrants that can be interpreted as execution phases in a
crawler:

1. Resource-Direct (high-confidence semantic acquisition).
2. Resource-Inferenced (HTML/header metadata interpretation).
3. Domain-Direct (catalog/linkset style direct graph acquisition).
4. Domain-Inferenced (host-level bootstrap and mapping).

The document analyzes **30 methods**, each with specification origin, usage
context, quadrant recommendations, and often a proposed RDF retrieval mapping
[@lodclass]. This is especially valuable because it bridges protocol syntax and
semantic outcomes.

## Quadrant 1: Resource-Level Direct RDF

Representative channels include content negotiation outcomes, Link headers that
point directly to RDF, embedded JSON-LD/Turtle, FOAF/SKOS statements,
`owl:sameAs`, and RDF collection constructs. In this quadrant, parsing yields
native triples with minimal semantic ambiguity.

## Quadrant 2: Resource-Level Inferenced RDF

Methods such as HTML links, RDFa, Microdata, Open Graph, Dublin Core metadata,
canonical links, pagination relations, and structural HTTP link relations
require extraction rules to map source syntax to RDF. The document provides
concrete mapping recipes (e.g., Open Graph keys to `schema:` predicates,
canonical to identity relations).

## Quadrant 3: Domain-Level Direct RDF

Domain-level direct channels are presented as shared/conditional in the
repository design, especially for well-known and resource-map patterns when
represented as RDF/linkset structures. This quadrant models the case where a
host exposes high-value catalogs without requiring per-page metadata scraping.

## Quadrant 4: Domain-Level Inferenced RDF

RSS, Atom, sitemap, robots, manifest, and API discovery catalogs are treated as
bootstrap artifacts requiring parser logic plus semantic translation. These
channels provide breadth-first entry points for crawl expansion and are critical
fallbacks when resource-level hints are sparse.

## Why this deep dive matters

The classification document is more than descriptive documentation. It provides:

- A strategy contract (what to parse, where, and why).
- A confidence model (direct versus inferenced acquisition).
- A modular architecture proposal for pluggable strategy execution.
- A roadmap for orchestrating cascades without collapsing all channels into a
  monolithic sequential list.

This makes it directly reusable for implementing resilient crawlers and
compliance validators.

# Strategy Surface and Compliance Value

The repository operationalizes strategy metadata in `generator/strategies.ts`,
where each channel includes human-readable description, standards provenance,
location/extraction classification, and optional proposed retrieval design
[@lodrepo]. This creates a single source of truth for:

- Rendering channel documentation pages.
- Injecting matching markup/header artifacts.
- Enabling machine test plans that verify expected channel behavior.

In compliance terms, the matrix acts as a validation corpus for testing whether
a discovery client can:

- Detect direct RDF opportunities before expensive inference.
- Correctly parse and map inferenced metadata channels.
- Move from resource-local hints to domain-wide catalogs.
- Handle navigational structures (pagination, collections, backlinks, cycles)
  without over-crawling or semantic drift.

# Discussion

A major strength of `lod_docker_webserver` is that it treats web architecture as
a first-class test artifact. HTTP behavior, HTML metadata, RDF serializations,
and host-level documents are all generated from one controlled model and served
in one reproducible container deployment.

The implementation status note in the repository is also important: while the
payload ecosystem is richly generated, not every listed strategy is yet fully
executed by automated harvester logic [@lodrepo]. This is not a weakness of the
testbed concept; it is an explicit separation between *channel availability*
and *client implementation completeness*. In research and engineering practice,
that separation is healthy because it enables independent benchmarking of
crawler maturity.

# Conclusion

`lod_docker_webserver` is a substantial contribution to practical Linked Data
discovery engineering. It transforms abstract standards into a navigable,
runnable, and inspectable testbed where discovery behavior can be studied under
controlled conditions.

Its most distinctive value is the explicit taxonomy-driven framing from
`wrx_discovery_classification.md`: a structured model that links protocol
standards, extraction mechanics, and orchestration design. For teams building
robust LOD clients, FAIR-compliant metadata services, or conformance tests, this
repository provides both implementation scaffolding and conceptual clarity.
