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
bibliography: references.bib
---

# 1. Introduction: The Discovery Barrier

The Semantic Web vision relies on interlinked, machine-readable data, yet web
publishers and web developers still struggle to move from a human-facing URL to
an actionable RDF representation. In practice, the location of RDF data is often
encoded in project documentation or in non-standard conventions (for example, a
publisher-specific /rdf endpoint). This makes discovery brittle: automated
clients must already know how a site exposes RDF in order to retrieve it. The
result is an ecosystem where data may exist, but remains inaccessible to machines
without human guidance.

Discovery is also fragmented across domains. Some publishers advertise metadata
via HTTP `Link` headers, others require content negotiation, and still others
publish catalogs in separate portals. These patterns are each standardized, but
clients seldom combine them into a unified discovery pipeline. As a consequence,
a digital assistant that can navigate a content negotiation endpoint may still
miss a richer RDF description that is available via a linkset, an API catalog, or
a DCAT distribution. Bridging these signals into a single exploratory process is
necessary for consistent automation.

This paper argues for radical transparency: lowering the amount of information a
client must know up front by embedding navigational signposts directly into the
fabric of the web. We propose wrx (Web Resource Extraction) as a tool to automate
this process. Given a single URI, wrx discovers a graph of conceptual resources
and their descriptions by traversing standardized relations and catalog
structures. The outcome is a reproducible, machine-actionable discovery trace
that replaces guesswork with protocol-defined signals.

# 2. Background and Specifications

Explorability is grounded in several IETF and W3C standards that already exist on
the web but are unevenly used. These standards define how resources can describe
related representations, profiles, and catalog entries. wrx treats them as a
cascading set of hints that can be followed until an actionable RDF description
is obtained.

## 2.1 RFC 8288: Web Linking

RFC 8288 defines the Web Linking model that underpins discovery on the web
[@rfc8288]. It standardizes typed links between resources via HTTP `Link` headers
and HTML `<link>` elements. Each link is a relation between a source and a
context, described by a `rel` attribute. For example:

```
Link: <https://example.org/metadata.ttl>; rel="describedby"; type="text/turtle"
```

wrx uses this model throughout its cascade: it interprets relations such as
`describedby`, `alternate`, `type`, `profile`, and `linkset` as explicit
instructions for where to find metadata or alternative representations. RFC 8288
also allows additional link parameters (for example, `type`, `hreflang`, and
`title`) that help wrx validate candidate resources and choose among competing
links. The key strength of Web Linking is that it is content agnostic; a resource
can advertise RDF, JSON, or human-oriented documentation using the same
mechanism. This makes RFC 8288 the baseline protocol for uniform discovery.

## 2.2 RFC 9110 and RFC 2045: HTTP Semantics and Media Types

HTTP semantics define how representations are negotiated, cached, and validated
[@rfc9110]. For RDF discovery, status codes and content negotiation rules matter
because they allow clients to request machine-readable formats without knowing
where they live. The `Accept` header and the `Vary` response header inform wrx
when to attempt content negotiation or fall back to link relations. wrx respects
redirects, content negotiation outcomes, and caching directives so that repeated
queries can avoid redundant network traffic.

Media types (RFC 2045) provide the vocabulary for identifying RDF encodings
[@rfc2045]. Common RDF types such as `text/turtle`, `application/ld+json`, and
`application/rdf+xml` are used as signals in both HTTP headers and link metadata.
wrx validates these media types to avoid false positives, and prefers responses
with explicit RDF content types to minimize ambiguity. Because some publishers
use vendor-specific types, wrx also supports profile-driven recognition: a
profile URI can indicate RDF semantics even if the media type is a custom JSON
format.

## 2.3 RFC 6906 and RFC 7284: Profiles and Profile Registries

RFC 6906 defines the `profile` link relation, which differentiates the *concept*
being represented from the bytes delivered on the wire [@rfc6906]. By linking to
profile URIs, a publisher can state that a resource representation conforms to a
specific conceptual model or shape. This is critical for automated clients that
need to choose between multiple representations of the same resource, e.g., a
schema.org JSON-LD representation versus a DCAT catalog entry. Profiles can be
applied through Link headers, HTML link tags, or the `profile` parameter on
`Content-Type` headers.

The Profile-URI registry (RFC 7284) standardizes profile identifiers and
provides discovery for well-known profiles [@rfc7284]. wrx uses profile URIs as
first-class hints: if a link relation includes a profile that matches a known
RDF vocabulary (e.g., DCAT, RO-Crate, or OGC API), the corresponding
representation is ranked higher because it offers more predictable semantics.
Profiles are also used to align HTTP-level discovery with RDF-level profile
bridging (such as `dct:conformsTo` in DCAT catalogs), allowing wrx to unify
conceptual semantics with actual representations.

## 2.4 RFC 9264: Linksets

RFC 9264 introduces linksets, a mechanism for grouping large collections of
links in a separate document [@rfc9264]. Linksets solve the scalability problem
of embedding numerous `Link` headers or HTML tags. A linkset is itself a
first-class resource that can be described in JSON or plain-text form, and it
uses the same relation types as RFC 8288. In wrx, linksets are treated as a
high-confidence source of discovery. When a resource advertises a linkset via
`rel="linkset"`, wrx dereferences the linkset, parses it, and incorporates its
links into the discovery graph.

Linksets also support anchors and context targets, enabling a single linkset to
describe relations for many resources. This makes them a natural fit for
repositories, APIs, and dataset portals where a resource may have multiple
representations or profile-specific descriptions. wrx uses linksets to locate
RDF distributions, profiles, and alternative entry points without requiring
publisher-specific URI templates.

## 2.5 RFC 5785 and RFC 9727: `.well-known` and API Catalogs

RFC 5785 standardizes the `/.well-known/` URI prefix as a location for
site-wide metadata [@rfc5785]. API Catalogs (RFC 9727) build on this mechanism by
defining `/.well-known/api-catalog` as a machine-readable description of API
entry points [@rfc9727]. The API catalog format is expressed as a linkset, which
means a catalog entry can describe both human and machine interfaces.

wrx uses API catalogs as a host-level discovery strategy. If resource-level
signals are absent, wrx probes for a host-level catalog to locate API endpoints,
schemas, or RDF profiles associated with a domain. Catalog entries can link to
OpenAPI, Hydra, or JSON Schema descriptions, and can also include `describedby`
relations to RDF metadata. This makes API catalogs a bridge between traditional
API documentation and Linked Data discovery.

## 2.6 FAIR Signposting

FAIR Signposting defines a pragmatic profile of Web Linking to expose metadata
without requiring a dedicated API [@signposting]. It recommends link relations
such as `describedby`, `author`, `license`, and `cite-as` in HTTP headers to
advertise metadata objects and persistent identifiers. wrx treats these
relations as high-priority inputs because they express a direct path to
authoritative descriptions, often in RDF or JSON-LD. Signposting also establishes
conventions for identifying file format metadata, which wrx uses to normalize
representations and select the most semantically rich payload.

## 2.7 RFC 9309 and Sitemaps: Host-Level Harvesting

The robots.txt protocol (RFC 9309) provides a standard location for crawler
instructions and, crucially, can list sitemap files [@rfc9309]. Sitemaps are an
industry-standard protocol for enumerating site content and associated metadata
[@sitemaps]. wrx uses robots.txt and sitemaps as a fallback strategy to harvest
possible dataset or catalog pages when direct discovery fails. This mirrors how
web crawlers bootstrap discovery at scale, but the focus here is on RDF and
machine-actionable resources rather than page indexing.

Sitemaps also provide metadata such as `lastmod`, `changefreq`, and `priority`.
While primarily intended for search engines, these properties can help wrx rank
candidate resources when multiple catalog pages exist. Sitemap indexes allow
large catalogs to be segmented by topic or region, which is useful when mapping
host-level resources to a specific URI.

## 2.8 DCAT and Catalog Bridging

The Data Catalog Vocabulary (DCAT) is a W3C standard for describing datasets and
distributions [@dcat]. It is often used to publish dataset metadata in RDF, and
its `dct:conformsTo` predicate can link datasets to formal profiles. wrx
leverages DCAT to bridge between catalogs and actual data distributions: if a
catalog entry describes a distribution with an RDF media type, wrx can resolve
that distribution as the actionable representation for a given resource.

DCAT provides explicit properties for `dcat:distribution`, `dcat:accessURL`, and
`dcat:downloadURL`, which let wrx distinguish between an API endpoint and a
static file distribution. Catalogs can also include `dcat:mediaType` or
`dcat:format` declarations, which wrx uses to validate that a distribution is
compatible with RDF. This makes DCAT a crucial bridge between catalog-level
metadata and resource-level access.

## 2.9 JSON-LD Contexts

JSON-LD contexts allow JSON payloads to be interpreted as RDF by providing an
external semantic mapping [@jsonld11]. This is critical for legacy APIs that
emit JSON without embedded RDF semantics. wrx treats JSON-LD contexts as a
conversion path: when a JSON response includes a `@context` or links to a
context document, wrx can convert that payload into RDF and treat it as a valid
representation. This extends explorability into ecosystems that are not
explicitly RDF-native.

In practice, many APIs include lightweight JSON responses but publish a context
file that maps keys to RDF vocabularies. wrx detects these contexts via HTTP
headers, `Link` relations, or JSON-LD metadata embedded in the response. The
conversion pipeline allows wrx to recover RDF semantics without requiring the
publisher to expose separate RDF endpoints.

## 2.10 Additional Profile Registries and Community Standards

Beyond IETF and W3C standards, domain communities maintain profile registries
and catalog conventions. Examples include OAI-PMH for scholarly metadata
harvesting [@oaipmh], RO-Crate for research object packaging [@rocrate], Linked
Data Event Streams (LDES) for streaming updates [@ldes], OGC API standards for
geospatial resources [@ogcapi], and scientific data conventions such as ERDDAP
[@erddap], OPeNDAP [@opendap], and CF Conventions [@cfconventions]. wrx treats
these as profile families: if a linkset, API catalog, or profile URI points to
one of these registries, wrx can prioritize the corresponding metadata or
endpoint because it aligns with established community semantics.

For example, an OAI-PMH endpoint often exposes a standard `?verb=Identify`
response that can be converted into RDF, while RO-Crate defines a canonical
`ro-crate-metadata.json` entry that describes a research object. LDES resources
describe streams that can be consumed incrementally, and OGC APIs frequently
publish machine-readable OpenAPI descriptions alongside JSON or GeoJSON
representations. These profiles expand the reach of explorability into domains
that already maintain discovery infrastructure, even if they are not explicitly
RDF-first.

# 3. Concept: Explorability vs. Findability

Findability creates a chicken-and-egg problem: a resource is findable only if a
client already knows where a publisher placed it, or if it is registered in a
specific catalog. Explorability avoids this by placing a navigation map within
or alongside the resource itself. In this analogy:

- The URI is the "You are here" marker.
- `rel="profile"` functions as the legend explaining the conceptual type of the
  resource.
- Linksets define nearby routes and alternative representations.
- Sitemaps and robots.txt act as the region map.
- API catalogs describe the road network for programmatic interfaces.

Explorability focuses on *conceptual resources* rather than only byte-level
representations. HTTP semantics distinguish between a resource and its
representations [@rfc9110]. wrx therefore treats a landing page, a JSON-LD
representation, and an RDF distribution as different manifestations of a common
concept. By traversing links and catalogs, wrx constructs a graph that maps these
manifestations and provides a reproducible trail of how each representation was
found.

Table&nbsp;1 summarizes how core specifications contribute to the exploration
strategy.

| Specification | Discovery role in wrx | Typical signal |
| --- | --- | --- |
| RFC 8288 | Base linking model for discovery | `Link` headers, HTML `<link>` tags |
| RFC 6906 | Conceptual profile identification | `rel="profile"` |
| RFC 9264 | External link collections | `rel="linkset"` + linkset document |
| RFC 9727 | Host-level API discovery | `/.well-known/api-catalog` |
| RFC 9309 + Sitemaps | Domain-level harvesting | `robots.txt`, sitemap indexes |
| DCAT | Catalog to distribution bridge | `dcat:distribution` with RDF media type |
| JSON-LD | Semantify JSON representations | `@context` or context link |

Explorability also reframes interoperability: instead of requiring every client
to implement bespoke discovery rules, publishers can expose standardized signposts
that any conforming agent can follow. This reduces coupling and allows data
producers to evolve their infrastructure without breaking downstream consumers.

# 4. The wrx Discovery Framework

wrx (Web Resource Extraction) is a TypeScript module targeting the Bun runtime.
It implements a cascading discovery algorithm that starts with the most precise
signals and gracefully relaxes to more generic strategies. The client supplies
a URI, and wrx returns the best available RDF representation plus a trace of the
steps taken.

## 4.1 Design Goals

The library is guided by four design goals:

1. **Protocol-first discovery**: only follow standardized signals, avoiding
   publisher-specific heuristics.
2. **Graceful degradation**: return the first acceptable RDF representation but
   allow deeper exploration when needed.
3. **Traceability**: provide a structured log of discovery steps and their
   confidence levels.
4. **Interoperability**: support multiple RDF serializations and profiles with
   minimal configuration.

## 4.2 Discovery Cascade

The current implementation supports the following strategies, ordered from most
specific to most general:

1. **Direct content negotiation**: issue HTTP requests with RDF `Accept` headers
   and capture negotiated representations. This leverages RFC 9110 semantics and
   RFC 2045 media types to detect RDF on the first request.
2. **FAIR Signposting**: inspect HTTP `Link` headers for `describedby`, `type`,
   `author`, and `license` relations to locate metadata objects.
3. **HTML link parsing**: scan HTML for `rel="alternate"`, `rel="describedby"`,
   and `rel="linkset"` declarations that point to RDF or linkset documents.
4. **Linkset resolution**: fetch and parse RFC 9264 linkset documents to find
   additional representations or profiles. Each linkset is validated for
   supported media types and profile relations.
5. **Embedded RDF scripts**: extract RDF from `<script type="application/ld+json">`
   blocks and other embedded data scripts when present, converting JSON-LD to
   RDF when necessary.
6. **API catalog discovery**: resolve `/.well-known/api-catalog` endpoints as
   described in RFC 9727 to enumerate API entry points and schemas.
7. **Robots.txt + sitemap harvesting**: parse `robots.txt` (RFC 9309) and
   sitemaps to discover catalog pages or dataset distributions.
8. **Catalog bridging**: follow DCAT catalogs to locate RDF distributions and
   cross-reference `dct:conformsTo` profile assertions.

Each step includes validation of media types, profiles, and dereferenceability
to avoid false positives. The cascade is intentionally conservative: any step
that yields an authoritative RDF representation can terminate the process, while
subsequent steps are used to enrich the discovery graph.

## 4.3 Indirect, Direct, and Host Harvesting

wrx groups discovery into three modes that correspond to increasing scope:

- **Indirect harvesting**: link relations and linksets discovered in headers or
  HTML, where the publisher explicitly describes the resource.
- **Direct harvesting**: content negotiation and embedded scripts, where the
  representation itself contains RDF or RDF-compatible data.
- **Host harvesting**: catalogs, sitemaps, and well-known endpoints that expose
  domain-wide metadata.

This stratification allows clients to choose a latency and completeness tradeoff
by configuring how far the cascade should proceed. For example, a UI that needs
fast rendering might stop after indirect or direct harvesting, while a batch
harvester can proceed into host-level discovery for maximum completeness.

## 4.4 Scoring and Trace Model

Each discovery step generates a trace entry capturing: (1) the source URL; (2)
relation types followed; (3) the media type and profile; (4) a confidence score;
and (5) any conversion steps applied. Scores are higher when the signal is
explicit (for example, `rel="describedby"` with an RDF media type) and lower when
inferred (for example, a sitemap entry lacking format metadata). The trace model
is essential for observability: it allows downstream systems to explain how a
representation was found and to select the most reliable version when multiple
options are available.

## 4.5 Conversion to RDF

Not all discoverable representations are RDF-native. JSON-LD contexts, API
catalog entries in JSON, and HTML-embedded microdata can all be converted into
RDF. wrx provides conversion hooks that interpret JSON-LD payloads or fetch
context documents to transform structured JSON into RDF graphs. This allows wrx
not only to locate RDF data but also to *derive* RDF from semantically annotated
representations.

## 4.6 Example Walkthrough

Consider a DOI landing page that returns HTML. wrx first attempts content
negotiation for RDF types; if that fails, it inspects HTTP `Link` headers for
`describedby` relations. Suppose a `describedby` link points to a JSON record with
an accompanying JSON-LD context. wrx resolves the link, detects the `@context`,
converts the JSON to RDF, and returns the RDF graph along with a trace noting the
signposting link and the conversion step. If no `describedby` link exists, wrx
falls back to parsing HTML link elements, then to a linkset, and finally to
host-level catalogs.

This walkthrough illustrates how wrx can discover RDF even when the initial
resource lacks explicit RDF representations, by chaining standardized hints and
semantic conversions.

# 5. Implementation Details

The wrx library is implemented in TypeScript and targets the Bun runtime for
modern web-compatible HTTP APIs and high-performance parsing. Key components
include:

- **HTTP client layer**: executes requests with configurable headers, retries,
  and redirect handling consistent with RFC 9110 semantics.
- **Link parser**: normalizes RFC 8288 links from HTTP headers and HTML `<link>`
  tags into a unified internal representation.
- **Linkset parser**: reads RFC 9264 linkset documents in JSON or text format
  and extracts typed link relations.
- **Profile matcher**: validates and ranks profile URIs against known registries
  (RFC 7284, DCAT, RO-Crate, OGC, etc.).
- **Conversion module**: handles JSON-LD expansion and RDF serialization
  selection based on requested or detected media types.

Implementation choices prioritize deterministic behaviour. For example, wrx
avoids crawling arbitrary HTML links unless a defined relation is present. It
also limits cross-domain traversal to avoid accidental drift into unrelated
resources, unless the publisher explicitly provides cross-domain relations.

## 5.1 Data Model

wrx represents discovery results as a compact graph: nodes are resources, and
edges are typed link relations annotated with media type, profile, and
confidence. This data model mirrors the Web Linking semantics while capturing
additional metadata needed for ranking. The model is intentionally minimal to
allow serialization into JSON for use in logs or dashboards.

## 5.2 Normalization and Deduplication

Discovery sources often overlap. A single representation can be referenced via
headers, HTML, and linksets. wrx normalizes URLs, resolves relative references,
merges duplicate links, and preserves the provenance of each signal. If two links
point to the same resource but specify different media types, wrx retains both
until validation resolves the preferred type.

## 5.3 Extensibility

The cascade is implemented as a pipeline of strategy modules. Each module
receives the current discovery graph and can append new nodes and edges. This
allows deployments to insert custom strategies (for example, a domain-specific
catalog format) without rewriting the core. The scoring model can also be
configured to favor certain profiles or media types.

# 6. Evaluation and Use Cases

Because wrx is a discovery library rather than a single application, evaluation
focuses on practical discovery outcomes. Pilot experiments against FAIR-compliant
repositories show that a single `describedby` link often resolves directly to an
RDF metadata record. In less curated environments, wrx typically succeeds by
following HTML alternates to linksets and then to profile descriptions.

Representative use cases include:

- **Pre-flight discovery for digital assistants:** before invoking an API, wrx
  extracts the API catalog and profiles to select the correct endpoint and
  representation.
- **Metadata completion for research objects:** given only a DOI landing page,
  wrx follows signposts to authoritative RDF descriptions suitable for repository
  ingest and curation.
- **Zero-configuration UI composition:** paired with RDF Web Components, wrx can
  feed a client-side renderer that turns arbitrary URIs into templated views.
- **Cross-domain dataset federation:** by following DCAT catalogs and profile
  links, wrx can locate RDF distributions across multiple organizations without
  prior agreements on endpoint naming.

Even when discovery fails, the trace reveals which signals were missing, which
can inform publishers on how to improve explorability.

## 6.1 Qualitative Comparison

Traditional discovery approaches often require manual configuration, such as
hard-coded SPARQL endpoints or publisher-specific metadata APIs. wrx reduces this
configuration burden by using standardized signals. In environments where
publishers already implement FAIR Signposting or linksets, wrx achieves immediate
success. In environments without such signals, the host-level strategies still
provide a safety net through catalogs and sitemaps.

## 6.2 Example Scenarios

- **Institutional repository:** A repository landing page links to a linkset that
  enumerates metadata and file distributions. wrx resolves the linkset, selects
  the RDF distribution, and returns a complete metadata record.
- **Marine data portal:** The portal publishes a DCAT catalog and OGC API
  endpoints. wrx identifies the catalog via `/.well-known/api-catalog`, then
  follows `dct:conformsTo` to select the OGC profile and the RDF distribution.
- **Legacy JSON API:** A JSON API adds a JSON-LD context file. wrx follows the
  context link, converts JSON to RDF, and yields a semantically enriched graph.

# 7. Related Work and Positioning

Several systems have addressed RDF discovery through either content negotiation
or specialized endpoints. Linked Data browsers and SPARQL services provide rich
interfaces but require prior knowledge of where the data lives. Metadata
harvesters rely on catalogs but are limited to domains that publish them. wrx
positions itself between these extremes by combining lightweight protocol
signals (link headers, profiles, and linksets) with catalog-level discovery. This
hybrid approach supports both immediate resource-level discovery and broader
host-level exploration.

# 8. Discussion: Adoption and Limitations

Explorability depends on publishers emitting meaningful links. wrx cannot conjure
metadata that is absent, and it inherits the availability and correctness of
remote resources. Adoption challenges include incomplete use of link relations,
inconsistent media type declarations, and the lack of widely adopted profile
registries for some domains. Another limitation is that RDF conversion from JSON
or HTML relies on consistent contexts; without a valid JSON-LD context, wrx
cannot unambiguously interpret semantics.

Nevertheless, the framework demonstrates that existing standards are sufficient
for discovery when they are used consistently. wrx encourages small, incremental
publisher changes (e.g., adding a `Link` header or a `.well-known/api-catalog`)
that immediately increase machine-accessible transparency. The trace model also
provides actionable feedback to publishers by highlighting which signposts are
missing or inconsistent.

# 9. Future Work

Future work focuses on richer profile negotiation, pluggable ranking models, and
optional caching layers to reduce redundant exploration of large sites. Another
priority is expanding support for community profile registries such as OGC and
CF-conventions, allowing wrx to better serve domain-specific data ecosystems.
The trace model could also be extended with provenance metadata so that discovery
paths can be cited or audited in scholarly contexts. Additional work includes
formalizing a test corpus of explorability scenarios to benchmark discovery
quality across domains.

# 10. Conclusion

Explorability reframes discovery as an on-the-fly, standards-driven process
rather than a catalog lookup. wrx demonstrates that existing web standards are
sufficient to automate this journey today. By cascading through signposts,
linksets, catalogs, and embedded scripts, wrx turns a URL into a
machine-actionable graph with minimal prior knowledge, moving the Semantic Web
closer to everyday automation.
