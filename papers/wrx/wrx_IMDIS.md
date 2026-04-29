---
title: "Radical Transparency Approach to Interoperability"
runningtitle: "Radical Transparency and Interoperability"
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
addresses:
  - label: "A"
    institution: "Flanders Marine Institute (VLIZ), Ostend, Belgium"
abstract: |
  **Background.** Current data discovery practices rely on hidden, publisher-specific conventions that create artificial interoperability barriers. Teams depend on tribal knowledge rather than standardised signals, leading to brittleness and fragmentation in data integration ecosystems.

  **Core Problem.** The field faces a critical choice: either accept closed conformity through undisclosed mechanisms, or embrace clear diversity through transparent, explorable protocols. Clear diversity beats assumed (claimed, but hidden) conformity because transparency enables genuine machine automation and human understanding alike.

  **Solution: Radical Transparency.** We present wrx, a TypeScript framework implementing radical transparency as a discovery strategy. Rather than encoding assumptions into bespoke client logic, wrx requires agreement to declare profiles and conformity to various standardised approaches. This shift avoids the cliff of assumptions that collapses when publisher conventions shift unexpectedly.

  **Methods and Architecture.** wrx walks a cascading path grounded in IETF and W3C standards: content negotiation, FAIR Signposting, RFC 9264 linksets, embedded RDF scripts, RFC 9727 API catalogues, and DCAT/sitemap fallbacks. Each step is scored and captured in an explorable trace so the journey can be inspected, reproduced, and audited. Importantly, wrx stretches automatically into making things measurable too—every discovery decision is logged with confidence scores, source provenance, and conversion metadata, transforming discovery from a black box into an observable process.

  **Why Evolution and Diversity Matter.** We need evolution and diversity because no single format or protocol will ever encompass all data ecosystems. By making discovery explorable through standardised signposting rather than hardcoded expectations, we enable systems to evolve independently while remaining interoperable. Publishers can adopt new patterns or combine existing ones without breaking clients that follow the transparent protocol stack.

  **Key Contribution.** wrx turns discovery from ad hoc endpoint guessing and hidden tribal knowledge into a transparent, protocol-defined process that leaves readers and machines with a clear, auditable narrative of how and why a particular representation was chosen. The framework demonstrates that interoperability thrives when built on radical transparency: open signals, declared conformity, measurable traces, and respect for legitimate diversity.

  **Conclusion.** By embracing radical transparency, standardised signposting, and explorable decision trails, organisations can achieve genuine interoperability without sacrificing flexibility or forcing artificial conformity. This approach scales across heterogeneous publisher setups, supports multiple profiles and formats, and creates the foundation for evolving data ecosystems that remain interoperable as they grow and change.
bibliography: references.bib
---
