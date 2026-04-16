---
title: "Explorability of Web Sources: Automated Resource Discovery via the wrx Framework"
runningtitle: "wrx: Explorability of Web Sources"
runningauthor: "C. Decruw"
authors:
  - fnms: "Cedric"
    snm: "Decruw"
    label: "VLIZ"
    orcid: "0000-0001-6387-5988"
    corresponding: true
    note: "cedric.decruw@vliz.be"
addresses:
  - label: "VLIZ"
    institution: "Flanders Marine Institute (VLIZ), Ostend, Belgium"
abstract: |
  While the Semantic Web has matured, a significant barrier remains in the
  transition from human-readable URLs to machine-actionable RDF data. This
  paper introduces the concept of Explorability - pre-flight discovery for
  automated digital assistants - to move beyond mere Findability, which often
  relies on centralized catalogs. We present wrx (Web Resource Extraction), a
  TypeScript library that implements a cascading discovery strategy. By
  leveraging existing but underused web standards such as FAIR Signposting,
  RFC 9264 (Linksets), and RFC 9727 (API-Catalog), wrx enables radical
  transparency in web resource navigation.
keywords:
  - RDF discovery
  - FAIR Signposting
  - Linkset
  - API Catalog
  - content negotiation
  - Semantic Web
  - wrx
---

# 1. Introduction: The Discovery Barrier

The Semantic Web vision relies on interlinked, machine-readable data, yet web
developers frequently struggle to locate the correct RDF representation for a
given URL. Existing discovery methods are often fragmented, requiring prior
knowledge of a publisher's specific conventions. This paper argues for radical
transparency - lowering the amount of information a client must know up front
by embedding navigational signposts directly into the fabric of the web. We
propose wrx as a tool to automate this process, transforming a simple URI into
a rich graph of conceptual resources that can be resolved without human hints.

# 2. Background and Specifications

Explorability is grounded in several key IETF and W3C standards that already
exist on the web but are unevenly used:

- **RFC 8288 (Web Linking):** Defines the model for expressing relations between
  URLs via HTTP Link headers and HTML link tags.
- **RFC 9264 (Linksets):** Externalizes and groups web-linking information,
  essential for resources with many alternative representations.
- **RFC 9727 (API-Catalog):** Enables web-native self-description of APIs via
  a .well-known/api-catalog endpoint.
- **FAIR Signposting:** Prescribes typed HTTP Link headers (for example,
  rel="describedby") to let automated agents find metadata without prior
  endpoint knowledge.
- **RFC 6906 (Profiles):** Describes the concept or profile of a resource rather
  than only its bytes, enabling clients to request specific shapes of data.

These specifications provide a ready-made contract for discovery. wrx treats
them as a cascading set of hints that can be followed until an actionable RDF
description is obtained.

# 3. Concept: Explorability vs. Findability

Findability often creates a chicken-and-egg problem: a resource is findable
only if a client knows where a publisher placed it or if it is registered in a
specific catalog. Explorability avoids this by placing a navigation map within
the resource itself. In this analogy:

- The URI is the "You are here" marker.
- rel="profile" functions as the legend explaining what kind of thing is at the
  location.
- Linksets define nearby routes and alternative representations.
- Sitemaps and robots.txt act as the region map.

Explorability lowers coupling between publishers and consumers. A general
purpose agent can move from a landing page to its richest available RDF without
any out-of-band knowledge.

# 4. The wrx Discovery Framework

wrx (Web Resource Extraction) is a TypeScript module targeting the Bun runtime.
It implements a cascading discovery algorithm that starts with the most precise
signals and gracefully relaxes to more generic strategies. The client supplies
a URI, and wrx returns the best available RDF representation plus a trace of the
steps taken.

## 4.1 Implementation Status

The current implementation supports the following strategies:

- **Content Negotiation:** Issue HTTP requests with RDF Accept headers and
  capture negotiated representations.
- **FAIR Signposting:** Inspect HTTP Link headers for describedby, type,
  author, and license relations to locate metadata.
- **HTML Link Parsing:** Scan HTML for rel="alternate" and rel="linkset"
  declarations that point to RDF or linkset documents.
- **Linkset Resolution:** Fetch and parse RFC 9264 linkset documents to find
  additional representations or profiles.
- **Embedded Scripts:** Extract RDF from `<script type="application/ld+json">`
  blocks and other embedded data scripts when present.
- **API Catalog Discovery:** Resolve .well-known/api-catalog endpoints as
  described in RFC 9727 to enumerate API entrypoints and schemas.
- **Sitemaps and DCAT:** Fallback to sitemaps or DCAT catalogs when available
  to broaden the search space.

Each step includes validation of media types, profiles, and dereferenceability
to avoid false positives.

## 4.2 Discovery Cascade and Scoring

wrx orders strategies from most to least authoritative. Link headers with
explicit profiles are prioritized over HTML alternates; linksets are preferred
over generic sitemaps. A simple scoring model tracks confidence per step,
helping calling applications decide whether to return early (for low-latency
use cases) or continue exploring for higher-quality RDF. Traces are emitted for
debugging and reproducibility.

## 4.3 Integration

The library exports a minimal, promise-based interface suitable for both server
and edge runtimes. It can operate standalone or feed downstream consumers such
as RDF Web Components for rendering. Because wrx returns structured traces, it
can be embedded into observability pipelines to show how metadata was located
and which standards were exercised.

# 5. Evaluation and Use Cases

In pilot runs against FAIR-compliant repositories, wrx resolved RDF
representations in a single hop via describedby links. In less curated
environments, it succeeded by following HTML alternates to linksets and then to
profiles. Typical scenarios include:

- **Pre-flight discovery for digital assistants:** Before invoking an API,
  wrx extracts the API catalog and profiles to select the correct endpoint and
  representation.
- **Metadata completion for research objects:** Given only a DOI landing page,
  wrx follows signposts to authoritative RDF descriptions suitable for
  repository ingest.
- **Zero-configuration UI composition:** Paired with RDF Web Components, wrx can
  feed a client-side renderer that turns arbitrary URIs into templated views.

# 6. Future Work and Limitations

Discovery depends on publishers emitting meaningful links. wrx cannot conjure
metadata that is absent, and it inherits the availability and correctness of
remote resources. Planned enhancements include richer profile negotiation,
pluggable rankers for domain-specific tie-breaking, and optional caching layers
to reduce redundant exploration of large sites.

# 7. Conclusion

Explorability reframes discovery as an on-the-fly, standards-driven process
rather than a catalog lookup. wrx demonstrates that existing web standards are
sufficient to automate this journey today. By cascading through signposts,
linksets, catalogs, and embedded scripts, wrx turns a URL into a machine-actionable
graph with minimal prior knowledge, moving the Semantic Web closer to everyday
automation.
