---
title: "Marine Term Translations (MTT): A Self-Hosted Platform for Multilingual Marine Terminology Interoperability"
runningtitle: "Marine Term Translations (MTT)"
runningauthor: "Decruw Cedric"
authors:
  - fnms: "Decruw"
    snm: "Cedric"
    label: "VLIZ"
    orcid: "0000-0001-6387-5988"
    corresponding: true
    note: "cedric.decruw@vliz.be"
addresses:
  - label: "VLIZ"
    institution: "Flanders Marine Institute (VLIZ), Ostend, Belgium"
abstract: |
  The Marine Term Translations (MTT) platform is a lightweight, self-hostable
  open-source solution for creating, managing, translating, and publishing
  controlled marine vocabularies. Built with a React frontend, Node.js backend,
  PostgreSQL database, and ORCID authentication, MTT supports collaborative term
  editing, AI-assisted translation, versioning, and export in CSV, SKOS, and
  JSON-LD formats. A key innovation is the automatic generation of Linked Data
  Event Streams (LDES), enabling real-time, machine-readable publication of
  terminology. In beta testing, 25% of the BODC P02 Parameter Discovery
  Vocabulary collection was translated into Dutch and French, demonstrating
  practical multilingual enrichment of widely used marine standards.
keywords:
  - marine terminology
  - multilingual
  - controlled vocabularies
  - Linked Data Event Streams
  - FAIR
  - SeaDataNet
  - EMODnet
booktitle: "IMDIS 2026"
---

The management of marine data increasingly relies on consistent, multilingual
terminology to achieve semantic interoperability across languages, institutions,
and systems. Inconsistent terms hinder effective data integration in major
initiatives such as EMODnet, SeaDataNet, and the UN Ocean Decade. The Marine
Term Translations (MTT) platform addresses this by offering a lightweight,
self-hostable open-source solution for creating, managing, translating, and
publishing controlled marine vocabularies.

MTT (available at mtt.vliz.be and https://github.com/marine-term-translations/mtt-self-host-platform)
is built with a modern technology stack including a React frontend, Node.js
backend, PostgreSQL database, and ORCID authentication for secure editorial
workflows. Core features comprise collaborative term editing with definitions
and translations, AI-assisted translation suggestions, versioning, and export
in common formats (CSV, SKOS, JSON-LD). A key innovation is the automatic
generation of Linked Data Event Streams (LDES), enabling real-time,
machine-readable publication of terminology that other systems can harvest and
synchronize efficiently.

This design strongly supports FAIR principles, with particular emphasis on
Interoperability and Reusability, while allowing institutions to maintain
sovereign control over their data. MTT complements existing marine
infrastructures by focusing on the semantic layer rather than raw observations.

In beta testing, 25% of the BODC P02 Parameter Discovery Vocabulary collection
was translated into Dutch and French. The resulting terminology is published as
an LDES feed at https://mtt.vliz.be/api/ldes/data/1/latest.ttl, demonstrating
practical multilingual enrichment of widely used marine standards.

![Landing page and interface of the MTT platform (mtt.vliz.be), highlighting project features including standardization based on the NERC Vocabulary Server, interoperability via LDES, and international accessibility.](figure1.png)

![Architectural overview of the MTT self-hosted platform, showing the main components (frontend, backend, database, authentication), translation workflow, and LDES publication stream.](figure2.png)

The platform is already supporting VLIZ-led and international marine projects
by reducing language barriers and improving cross-lingual data discovery and
integration. Future developments will expand language coverage and further
enhance integration with global marine data systems.

# References {-}

- Marine Term Translations GitHub repository: https://github.com/marine-term-translations/mtt-self-host-platform
- MTT platform: https://mtt.vliz.be/
- NERC Vocabulary Server (BODC P02 collection): https://vocab.seadatanet.org/v_bodc_vocab_v2/search.asp?lib=P02
