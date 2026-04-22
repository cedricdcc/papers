---
title: "Explorability of Web Sources: Automated Resource Discovery via the wrx Framework"
runningtitle: "wrx: Explorability of Web Sources"
runningauthor: "C. Decruw"
authors:
  - fnms: "Cedric"
    snm: "Decruw"
    label: "A"
    orcid: "0000-0001-6387-5988"
    corresponding: true
    note: "cedric.decruw@vliz.be"
  - fnms: "Marc"
    snm: "Portier"
    label: "A"
    orcid: "0000-0002-9648-6484"
  - fnms: "Katrina"
    snm: "Exter"
    label: "A"
    orcid: "0000-0002-5911-1536"
addresses:
  - label: "A"
    institution: "Flanders Marine Institute (VLIZ), Ostend, Belgium"
abstract: |
  **Background/Motivation.** Linked Open Data keeps growing, yet we still watch
  clients stall at the first hop because a human-facing URL rarely reveals where
  the RDF actually lives. Teams end up leaning on tribal knowledge about each
  publisher instead of following clues that should already be present on the web.

  **Objective.** We present wrx (Web Resource Extraction), a TypeScript
  framework that tries to make discovery feel less like a scavenger hunt. It
  leans on the signposts already defined by the web so automated agents can move
  from a landing page to a machine-actionable description without bespoke rules.

  **Methods.** wrx walks a cascading path: content negotiation, FAIR
  Signposting, RFC 9264 linksets, embedded RDF scripts, RFC 9727
  `/.well-known/api-catalog`, and DCAT/sitemap fallbacks. Each step is scored
  and captured in a trace so the journey can be inspected or reproduced.

  **Results.** Starting from a single URI, the framework resolves RDF across
  heterogeneous publisher setups and explains why a given representation was
  chosen through the recorded trace.

  **Conclusion.** wrx turns discovery from ad hoc endpoint guessing into a
  transparent, protocol-defined process that leaves readers and machines with a
  clear narrative of how RDF was found.
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

# Introduction: The Discovery Barrier

The Semantic Web vision relies on interlinked, machine-readable data, yet we
still spend far too much time coaxing RDF out of ordinary URLs. More often than
not, the location of a machine-actionable description sits in project
documentation, a wiki page, or behind a publisher-specific `/rdf` pattern that
only insiders know about. Automation stalls as soon as that tribal knowledge is
missing, leaving data technically published but effectively hidden from
machines.

Discovery patterns are also scattered. One site uses HTTP `Link` headers,
another expects content negotiation, and a third hides catalogue links inside a
separate portal. Each technique is standardised, but clients rarely stitch them
together. A bot that succeeds with content negotiation can still miss a richer
description tucked away in a linkset or an API catalogue. Without a shared way
to follow all of these signals, automation remains brittle.

We argue for making discovery boringly transparent: put the signposts on the
wire so a client can follow them without special knowledge. wrx automates that
idea. Given a single URI, it walks standard relations and catalogue structures
to build a graph of resources and their descriptions, leaving behind a
reproducible trace instead of a pile of guesswork. We also expect this client
framework to guide service developers in exposing the necessary discovery
hooks. We also anticipate browser plugins or native browser features that can
identify machine-actionable content and add user-facing affordances around it.

# Background and Specifications

Explorability is grounded in several IETF and W3C standards that already exist on
the web but are unevenly used. These standards define how resources can describe
related representations, profiles, and catalogue entries. wrx treats them as a
cascading set of hints that can be followed until an actionable RDF description
is obtained.

## RFC 8288: Web Linking

RFC 8288 defines the Web Linking model that underpins discovery on the web
[@rfc8288]. It standardises typed links between resources via HTTP `Link` headers
and HTML `<link>` elements. Each link is a relation between a source and a
context, described by a `rel` attribute. For example:

```
Link: <https://example.org/metadata.ttl>; rel="describedby"; type="text/turtle"
```

wrx uses this model throughout its cascade: it interprets relations such as
`describedby`, `alternate`, `self`, `profile`, and `linkset` as explicit
instructions for where to find metadata or alternative representations. RFC 8288
also allows additional link parameters (for example, `type`, `hreflang`, and
`title`) that help wrx validate candidate resources and choose among competing
links. The key strength of Web Linking is that it is content agnostic; a resource
can advertise RDF, JSON, or human-oriented documentation using the same
mechanism. This makes RFC 8288 the baseline protocol for uniform discovery.

## RFC 9110 and RFC 2045: HTTP Semantics and Media Types

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
with explicit RDF content types to minimise ambiguity. Because some publishers
use vendor-specific types, wrx also supports profile-driven recognition: a
profile URI can indicate RDF semantics even if the media type is a custom JSON
format.

## RFC 6906 and RFC 7284: Profiles and Profile Registries

RFC 6906 defines the `profile` link relation, which differentiates the *concept*
being represented from the bytes delivered on the wire [@rfc6906]. By linking to
profile URIs, a publisher can state that a resource representation conforms to a
specific conceptual model or shape. This is critical for automated clients that
need to choose between multiple representations of the same resource, eg, a
schema.org JSON-LD representation versus a DCAT catalogue entry. Profiles can be
applied through Link headers, HTML link tags, or the `profile` parameter on
`Content-Type` headers.

The Profile-URI registry (RFC 7284) standardises profile identifiers and
provides discovery for well-known profiles [@rfc7284]. wrx uses profile URIs as
first-class hints: if a link relation includes a profile that matches a known
RDF vocabulary (eg, RO-Crate), the corresponding
representation is ranked higher because it offers more predictable semantics.
Profiles are also used to align HTTP-level discovery with RDF-level profile
bridging (such as `dct:conformsTo` in DCAT catalogues), allowing wrx to unify
conceptual semantics with actual representations.

## RFC 9264: Linksets

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

## RFC 8615 and RFC 9727: `.well-known` and API Catalog Discovery

The `/.well-known/` mechanism is standardised in RFC 8615 (which obsoletes
RFC 5785) and provides a registered namespace for host-level discovery metadata
[@rfc8615]. RFC 9727 defines `api-catalog` as both a Well-Known URI suffix and
a link relation [@rfc9727]. Concretely, publishers expose an API catalog via
`/.well-known/api-catalog`, while also being able to advertise the same catalog
from other resources using `rel="api-catalog"`.

RFC 9727 requires the catalog to be available as a Linkset
(`application/linkset+json`, with the RFC 9727 profile URI), and allows
additional representations through content negotiation. wrx uses this in two
complementary ways: (1) it follows `api-catalog` links when they are present at
resource level, and (2) it probes `/.well-known/api-catalog` as a host-level
fallback. The resulting catalog links can then lead to API endpoints,
machine-readable API descriptions (for example OpenAPI), and related metadata,
which wrx incorporates into the broader RDF discovery graph.

## FAIR Signposting

FAIR Signposting defines a pragmatic profile of Web Linking to expose metadata
without requiring a dedicated API [@signposting]. It recommends link relations
such as `describedby`, `author`, `license`, and `cite-as` in HTTP headers to
advertise metadata objects and persistent identifiers. wrx treats these
relations as high-priority inputs because they express a direct path to
authoritative descriptions, often in RDF or JSON-LD. Signposting also establishes
conventions for identifying file format metadata, which wrx uses to normalise
representations and select the most semantically rich payload.

## RFC 9309 and Sitemaps: Host-Level Harvesting

RFC 9309 defines how crawlers retrieve and interpret `/robots.txt`, including
the rule language (`user-agent`, `allow`, `disallow`) and handling behavior for
redirects, unavailability, and caching [@rfc9309]. It also permits additional
records such as `Sitemap`, which lets a publisher advertise one or more sitemap
locations without coupling them to a specific `user-agent` group. wrx uses this
as a host-bootstrap mechanism: when direct resource-level signals are missing,
it resolves `/robots.txt`, extracts advertised sitemaps, and expands the
candidate URI set from there.

Sitemaps then provide structured URL inventories plus optional hints such as
`lastmod`, `changefreq`, and `priority` [@sitemaps]. wrx treats these as
ranking features rather than hard directives, and uses sitemap indexes to scale
across large catalogues. Because the base sitemap schema does not carry profile
semantics directly, wrx also relies on namespace extensions: in practice, the
`xhtml:link` pattern (commonly used for alternate links) can be reused to carry
relation and profile hints per URL entry, allowing profile semantics to travel
with host-level discovery data.

## DCAT and Catalogue Bridging

The Data Catalog Vocabulary (DCAT) is a W3C standard for describing datasets and
distributions [@dcat]. It is often used to publish dataset metadata in RDF, and
its `dct:conformsTo` predicate can link datasets to formal profiles. wrx
uses DCAT as the semantic refinement stage *after* host-level harvesting via
RFC 9309 and sitemaps. In other words, robots/sitemap discovery identifies
candidate catalogue resources; DCAT then bridges those catalogue entries to
concrete data distributions. If a discovered catalogue entry advertises a
distribution with an RDF media type, wrx can resolve that distribution as the
actionable representation for the target resource.

DCAT provides explicit properties for `dcat:distribution`, `dcat:accessURL`, and
`dcat:downloadURL`, which let wrx distinguish between an API endpoint and a
static file distribution. Catalogues can also include `dcat:mediaType` or
`dcat:format` declarations, which wrx uses to validate that a distribution is
compatible with RDF. This makes DCAT the connective layer between host-level
URL discovery (robots/sitemaps) and resource-level machine-actionable access.

## JSON-LD Contexts

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

## Additional Profile Registries and Community Standards

Beyond IETF and W3C standards, domain communities maintain profile registries
and catalogue conventions. Examples include OAI-PMH for scholarly metadata
harvesting [@oaipmh], RO-Crate for research object packaging [@rocrate], Linked
Data Event Streams (LDES) for streaming updates [@ldes], and scientific data conventions such as ERDDAP
[@erddap], OPeNDAP [@opendap], and CF Conventions [@cfconventions]. wrx treats
these as profile families: if a linkset, API catalogue, or profile URI points to
one of these registries, wrx can prioritise the corresponding metadata or
endpoint because it aligns with established community semantics.

For example, an OAI-PMH endpoint often exposes a standard `?verb=Identify`
response that can be converted into RDF, while RO-Crate defines a canonical
`ro-crate-metadata.json` entry that describes a research object. LDES resources
describe streams that can be consumed incrementally. These profiles expand the reach of explorability into domains
that already maintain discovery infrastructure, even if they are not explicitly
RDF-first.

# Concept: Explorability vs. Findability

Findability creates a chicken-and-egg problem: a resource is findable only if a
client already knows where a publisher placed it, or if it is registered in a
specific catalogue. Explorability avoids this by placing a navigation map within
or alongside the resource itself. In this analogy:

- The URI is the "You are here" marker.
- `rel="profile"` functions as the legend explaining the conceptual type of the
  resource.
- Linksets define nearby routes and alternative representations.
- Sitemaps and robots.txt act as the region map.
- API catalogues describe the road network for programmatic interfaces.

Explorability focuses on *conceptual resources* rather than only byte-level
representations. HTTP semantics distinguish between a resource and its
representations [@rfc9110]. wrx therefore treats a landing page, a JSON-LD
representation, and an RDF distribution as different manifestations of a common
concept. By traversing links and catalogues, wrx constructs a graph that maps these
manifestations and provides a reproducible trail of how each representation was
found.

Table&nbsp;1 summarises how core standards and mechanisms contribute to the exploration
strategy.

| Standard / mechanism | Discovery role in wrx | Typical signal |
| --- | --- | --- |
| RFC 8288 | Base linking model for discovery | `Link` headers, HTML `<link>` tags |
| HTML + JSON-LD embedding | In-document RDF extraction | `<script type="application/ld+json">` blocks |
| RFC 6906 | Conceptual profile identification | `rel="profile"` |
| RFC 9264 | External link collections | `rel="linkset"` + linkset document |
| RFC 9727 | Host-level API discovery | `/.well-known/api-catalog` |
| RFC 9309 + Sitemaps | Domain-level harvesting | `robots.txt`, sitemap indexes |
| DCAT | Catalogue to distribution bridge | `dcat:distribution` with RDF media type |
| JSON-LD | Semantify JSON representations | `@context` or context link |

Explorability also reframes interoperability: instead of requiring every client
to implement bespoke discovery rules, publishers can expose standardised signposts
that any conforming agent can follow. This reduces coupling and allows data
producers to evolve their infrastructure without breaking downstream consumers.

# The wrx Discovery Framework

wrx is a TypeScript module targeting the Bun runtime.
It implements a cascading discovery algorithm that starts with the most precise
signals and gracefully relaxes to more generic strategies. The client supplies
a URI, and wrx returns the best available RDF representation plus a trace of the
steps taken.

## Design Goals

The library is guided by four design goals:

1. **Protocol-first discovery**: only follow standardised signals, avoiding
   publisher-specific heuristics.
2. **Graceful degradation**: return the first acceptable RDF representation but
   allow deeper exploration when needed.
3. **Traceability**: provide a structured log of discovery steps and their
   confidence levels.
4. **Interoperability**: support multiple RDF serialisations and profiles with
   minimal configuration.

## Discovery Cascade

The current implementation supports the following strategies, ordered from most
specific to most general:

1. **Direct content negotiation**: issue HTTP requests with RDF `Accept` headers
   and capture negotiated representations. This leverages RFC 9110 semantics and
   RFC 2045 media types to detect RDF on the first request.
2. **FAIR Signposting**: inspect HTTP `Link` headers for `describedby`, `type`,
   `self`, and `linkset` relations to locate metadata objects.
3. **HTML link parsing**: scan HTML for `rel="alternate"`, `rel="describedby"`,
   and `rel="linkset"` declarations that point to RDF or linkset documents.
4. **Linkset resolution**: fetch and parse RFC 9264 linkset documents to find
   additional representations or profiles. Each linkset is validated for
   supported media types and profile relations.
5. **Embedded RDF scripts**: extract RDF from `<script type="application/ld+json">`
   blocks and other embedded data scripts when present, converting JSON-LD to
   RDF when necessary.
6. **API catalogue discovery**: resolve `/.well-known/api-catalog` endpoints as
   described in RFC 9727 to enumerate API entry points and schemas.
7. **Robots.txt + sitemap harvesting**: parse `robots.txt` (RFC 9309) and
   sitemaps to discover catalogue pages or dataset distributions and link semantic hints.
8. **Catalogue bridging**: follow DCAT catalogues to locate RDF distributions and
   cross-reference `dct:conformsTo` profile assertions.

Each step includes validation of media types, profiles, and dereferenceability
to avoid false positives. The cascade is intentionally conservative: any step
that yields an authoritative RDF representation can terminate the process, while
subsequent steps are used to enrich the discovery graph.

![Strategic overview of the wrx discovery framework and how cascading discovery modes relate to one another.](wrx_overview.drawio.svg)

## Indirect, Direct, and Host Harvesting

wrx groups discovery into three modes that correspond to increasing scope:

- **Indirect harvesting**: link relations and linksets discovered in headers or
  HTML, where the publisher explicitly describes the resource.
- **Direct harvesting**: content negotiation and embedded scripts, where the
  representation itself contains RDF or RDF-compatible data.
- **Host harvesting**: catalogues, sitemaps, and well-known endpoints that expose
  domain-wide metadata.

This stratification allows clients to choose a latency and completeness tradeoff
by configuring how far the cascade should proceed. For example, a UI that needs
fast rendering might stop after indirect or direct harvesting, while a batch
harvester can proceed into host-level discovery for maximum completeness.

![Detailed strategy breakdown used by wrx to evaluate and combine discovery signals.](strategies.drawio.svg)

## Scoring and Trace Model

Each discovery step generates a trace entry capturing: (1) the source URL; (2)
relation types followed; (3) the media type and profile; (4) a confidence score;
and (5) any conversion steps applied. Scores are higher when the signal is
explicit (for example, `rel="describedby"` with an RDF media type) and lower when
inferred (for example, a sitemap entry lacking format metadata). The trace model
is essential for observability: it allows downstream systems to explain how a
representation was found and to select the most reliable version when multiple
options are available.

## Conversion to RDF

Not all discoverable representations are RDF-native. JSON-LD contexts, API
catalogue entries in JSON, and HTML-embedded microdata can all be converted into
RDF. wrx provides conversion hooks that interpret JSON-LD payloads or fetch
context documents to transform structured JSON into RDF graphs. This allows wrx
not only to locate RDF data but also to *derive* RDF from semantically annotated
representations.

## Example Walkthrough

Consider a DOI landing page that returns HTML. wrx first attempts content
negotiation for RDF types; if that fails, it inspects HTTP `Link` headers for
`describedby` relations. Suppose a `describedby` link points to a JSON record with
an accompanying JSON-LD context. wrx resolves the link, detects the `@context`,
converts the JSON to RDF, and returns the RDF graph along with a trace noting the
signposting link and the conversion step. If no `describedby` link exists, wrx
falls back to parsing HTML link elements, then to a linkset, and finally to
host-level catalogues.

This walkthrough illustrates how wrx can discover RDF even when the initial
resource lacks explicit RDF representations, by chaining standardised hints and
semantic conversions.

# Implementation Details

The wrx library is implemented in TypeScript and targets the Bun runtime for
modern web-compatible HTTP APIs and high-performance parsing. Key components
include:

- **HTTP client layer**: executes requests with configurable headers, retries,
  and redirect handling consistent with RFC 9110 semantics.
- **Link parser**: normalises RFC 8288 links from HTTP headers and HTML `<link>`
  tags into a unified internal representation.
- **Linkset parser**: reads RFC 9264 linkset documents in JSON or text format
  and extracts typed link relations.
- **Conversion module**: handles JSON-LD expansion and RDF serialisation
  selection based on requested or detected media types.

Implementation choices prioritise deterministic behaviour. For example, wrx
avoids crawling arbitrary HTML links unless a defined relation is present. It
also limits cross-domain traversal to avoid accidental drift into unrelated
resources, unless the publisher explicitly provides cross-domain relations.

## Data Model

wrx models discovery as three connected layers rather than a single flat graph.
First, it keeps a **resource graph** in which nodes are conceptual resources
and edges are typed relations (`describedby`, `alternate`, `profile`,
`linkset`, `api-catalog`, etc.). Second, it keeps an **observation graph** that
records where each relation was seen (HTTP `Link` header, HTML `<link>`,
linkset record, sitemap entry, or embedded JSON-LD script), so relation claims
are traceable to concrete web evidence. Third, it keeps a **process trace** with
step mode (`indirect`, `direct`, `host`), source URI, dereference outcome,
normalisation decisions, and conversion events.

This structure follows the exploration model used in the design material:
`indirect` mode prioritises link-based navigation (headers, embedded links,
linksets, redirects), `direct` mode prioritises immediate representation
retrieval (content negotiation, redirects, embedded RDF), and `host` mode
bootstraps from `/robots.txt` to sitemaps and catalogues. Linksets and sitemap
hints are converted into RDF statements and attached to the same graph with
provenance-style annotations, so clients can query either the resulting
resource relations or the evidence chain that produced them.

## Normalisation

Discovery evidence often arrives in different URI forms across headers, embedded
HTML links, linksets, sitemaps, and catalogues. wrx applies a normalisation
step before graph insertion: it resolves relative references against their
context URI, follows redirects to a stable absolute URI, and applies syntax
normalisation while preserving semantics (including meaningful fragments).
Source location, discovery mode, and retrieval metadata remain attached as
provenance.

Example: a page at `https://example.org/catalog/` exposes
`<link rel="describedby" href="../meta/42.jsonld">`, while the server redirects
that target to `https://data.example.org/meta/42`. wrx resolves the relative
link against the page context, follows the redirect, and stores the normalised
target as `https://data.example.org/meta/42` in the discovery graph, with trace
metadata recording the original relative `href` and redirect chain.

## Extensibility

The cascade is implemented as a pipeline of strategy modules. Each module
receives the current discovery graph and can append new nodes and edges. This
allows deployments to insert custom strategies (for example, a domain-specific
catalogue format) without rewriting the core. The scoring model can also be
configured to favor certain profiles or media types.

# Evaluation and Use Cases

Because wrx is a discovery library rather than a single application, evaluation
focuses on practical discovery outcomes. Pilot experiments against FAIR-compliant
repositories show that a single `describedby` link often resolves directly to an
RDF metadata record. In less curated environments, wrx typically succeeds by
following HTML alternates to linksets and then to profile descriptions.

Representative use cases include:

- **Pre-flight discovery for digital assistants:** before invoking an API, wrx
  extracts the API catalogue and profiles to select the correct endpoint and
  representation.
- **Metadata completion for research objects:** given only a DOI landing page,
  wrx follows signposts to authoritative RDF descriptions suitable for repository
  ingest and curation.
- **Zero-configuration UI composition:** paired with RDF Web Components, wrx can
  feed a client-side renderer that turns arbitrary URIs into templated views.
- **Cross-domain dataset federation:** by following DCAT catalogues and profile
  links, wrx can locate RDF distributions across multiple organisations without
  prior agreements on endpoint naming.
- **Containerised standards-conformant LOD testbed:** a reproducible LOD server
  can be hosted via Docker (https://github.com/vliz-be-opsci/lod_docker_webserver),
  exposing resources that implement the paper's discovery standards (for
  example Web Linking, linksets, profiles, API catalogues, and sitemap-based
  host discovery). This provides a practical environment for wrx validation,
  interoperability testing, and demonstration.

Even when discovery fails, the trace reveals which signals were missing, which
can inform publishers on how to improve explorability.

# Related Work and Positioning

Several systems have addressed RDF discovery through either content negotiation
or specialised endpoints. Linked Data browsers and SPARQL services provide rich
interfaces but require prior knowledge of where the data lives. Metadata
harvesters rely on catalogues but are limited to domains that publish them. wrx
positions itself between these extremes by combining lightweight protocol
signals (link headers, profiles, and linksets) with catalogue-level discovery. This
hybrid approach supports both immediate resource-level discovery and broader
host-level exploration.

# Discussion: Adoption and Limitations

Explorability depends on publishers emitting meaningful links. wrx cannot conjure
metadata that is absent, and it inherits the availability and correctness of
remote resources. Adoption challenges include incomplete use of link relations,
inconsistent media type declarations, and uneven operational quality of
discovery endpoints (stale linksets, incomplete API catalogues, or missing
robots/sitemap maintenance). In practice, discovery failures are often not
protocol failures but publication-governance failures: relations are present but
underspecified, outdated, or disconnected from the actual resource lifecycle.

Another structural limitation is the insufficient cross-domain adoption and
curation of profile URI registries, despite the existence of registry
mechanisms. This is a major issue for linking semantics on the web: without
stable and discoverable profile identifiers, clients cannot
reliably interpret what a declared `rel="profile"` actually means, compare
equivalence across publishers, or rank competing representations with confidence.
The result is semantic fragmentation, where links remain technically valid but
operationally ambiguous.

RDF conversion from JSON or HTML also relies on consistent context publication;
for JSON-LD-derived interpretation paths, missing or invalid contexts prevent
unambiguous semantic interpretation.
Likewise, host-level harvesting can expose candidate resources but cannot by
itself guarantee conceptual alignment unless profile declarations and catalogue
metadata are maintained with the same rigor as the primary data endpoints.

Nevertheless, the framework demonstrates that existing standards are sufficient
for discovery when they are used consistently. wrx encourages small, incremental
publisher changes (eg, adding a `Link` header or a `.well-known/api-catalog`)
that can improve machine-accessible transparency quickly. The trace model also
provides actionable feedback to publishers by highlighting which signposts are
missing or inconsistent.

# Future Work

Future work focuses on richer profile negotiation, and
optional caching layers to reduce redundant exploration of large sites. Another
priority is expanding support for community profile registries, allowing wrx to better serve domain-specific data ecosystems.
The trace model could also be extended with provenance metadata so that discovery
paths can be cited or audited in scholarly contexts.

# Conclusion

Explorability reframes discovery as an on-the-fly, standards-driven process
rather than a catalogue lookup. wrx demonstrates that existing web standards are
sufficient to automate this journey today. By cascading through signposts,
linksets, catalogues, and embedded scripts, wrx turns a URL into a
machine-actionable graph with minimal prior knowledge, moving the Semantic Web
closer to everyday automation.


# Declaration on Generative AI

This manuscript was prepared with support from generative AI tooling for
language refinement and structural editing. The system
description was defined by the authors.

# Ethical Considerations and Environmental Footprint

**Ethical considerations.** wrx processes publicly accessible web resources and follows explicit protocol-level discovery signals exposed by publishers. It does not bypass access controls, and it inherits usage constraints and licensing terms from the discovered resources and endpoints.

**Environmental footprint.** The framework is designed for lightweight HTTP-based discovery with bounded cascading steps and optional caching, reducing redundant requests and computational overhead during repeated discovery workflows.

# References {-}

<!-- Bibliography is loaded from references.bib -->
