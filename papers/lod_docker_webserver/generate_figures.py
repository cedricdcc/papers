import os

def create_svg(title, input_type, input_lines, mapping_lines, output_lines):
    width = 800
    height = 300
    
    css = """
    .title { font-family: 'Inter', system-ui, sans-serif; font-size: 15px; font-weight: 700; fill: #f8fafc; }
    .label { font-family: 'Inter', system-ui, sans-serif; font-size: 11px; font-weight: 600; fill: #cbd5e1; }
    .header-text { font-family: 'Inter', system-ui, sans-serif; font-size: 12px; font-weight: 700; fill: #ffffff; }
    .code { font-family: 'Consolas', 'Fira Code', 'Courier New', monospace; font-size: 8.5px; fill: #cbd5e1; }
    .code-rdf { font-family: 'Consolas', 'Fira Code', 'Courier New', monospace; font-size: 8.5px; fill: #34d399; }
    .map-text { font-family: 'Inter', system-ui, sans-serif; font-size: 9.5px; font-weight: 600; fill: #ffffff; }
    .shadow { filter: drop-shadow(0px 8px 12px rgba(0, 0, 0, 0.4)); }
    """
    
    input_list_str = ""
    for idx, line in enumerate(input_lines):
        y_pos = 115 + idx * 13
        line_esc = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
        input_list_str += f'<text x="55" y="{y_pos}" class="code">{line_esc}</text>\n'
        
    output_list_str = ""
    for idx, line in enumerate(output_lines):
        y_pos = 115 + idx * 13
        line_esc = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
        output_list_str += f'<text x="495" y="{y_pos}" class="code-rdf">{line_esc}</text>\n'
        
    mapping_list_str = ""
    n_lines = len(mapping_lines)
    start_y = 165 - (n_lines - 1) * 6.5 + 3.5
    for idx, line in enumerate(mapping_lines):
        y_pos = start_y + idx * 13
        mapping_list_str += f'<text x="400" y="{y_pos}" text-anchor="middle" class="map-text">{line}</text>\n'
        
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <style>
      {css}
    </style>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="input-header" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
    <linearGradient id="output-header" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#064e3b"/>
      <stop offset="100%" stop-color="#0f766e"/>
    </linearGradient>
    <linearGradient id="pill-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#cbd5e1"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="{width}" height="{height}" fill="url(#bg-grad)" rx="12"/>
  
  <!-- Outer border -->
  <rect x="1" y="1" width="{width-2}" height="{height-2}" fill="none" stroke="#312e81" stroke-width="2" rx="11"/>

  <!-- Title -->
  <text x="400" y="35" text-anchor="middle" class="title">{title}</text>

  <!-- Input Card -->
  <g class="shadow">
    <rect x="40" y="65" width="280" height="200" rx="8" fill="#1e293b" opacity="0.6"/>
    <rect x="40" y="65" width="280" height="200" rx="8" fill="none" stroke="#475569" stroke-width="1.5"/>
    <path d="M 40 73 A 8 8 0 0 1 48 65 L 312 65 A 8 8 0 0 1 320 73 L 320 100 L 40 100 Z" fill="url(#input-header)"/>
    <text x="55" y="87" class="header-text">Source Payload ({input_type})</text>
    {input_list_str}
  </g>

  <!-- Connecting Arrows and Extraction Pill -->
  <path d="M 320 165 L 330 165" fill="none" stroke="#cbd5e1" stroke-width="2"/>
  
  <g class="shadow">
    <rect x="330" y="125" width="140" height="80" rx="10" fill="url(#pill-grad)"/>
    <rect x="330" y="125" width="140" height="80" rx="10" fill="none" stroke="#60a5fa" stroke-width="1.5"/>
    {mapping_list_str}
  </g>
  
  <path d="M 470 165 L 480 165" fill="none" stroke="#cbd5e1" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Output Card -->
  <g class="shadow">
    <rect x="480" y="65" width="280" height="200" rx="8" fill="#022c22" opacity="0.6"/>
    <rect x="480" y="65" width="280" height="200" rx="8" fill="none" stroke="#065f46" stroke-width="1.5"/>
    <path d="M 480 73 A 8 8 0 0 1 488 65 L 752 65 A 8 8 0 0 1 760 73 L 760 100 L 480 100 Z" fill="url(#output-header)"/>
    <text x="495" y="87" class="header-text">Inferred RDF Graph (Turtle)</text>
    {output_list_str}
  </g>
</svg>"""
    return svg_content

figures_data = [
    {
        "filename": "fig_html_links.svg",
        "title": "HTML Links Extraction Process (HTML_LINKS)",
        "input_type": "HTML Body",
        "input_lines": [
            "<body>",
            "  <h1>Welcome to LOD</h1>",
            "  <a href=\"/dataset/1\">Dataset 1</a>",
            "  <a href=\"/dataset/2\">Dataset 2</a>",
            "</body>"
        ],
        "mapping_lines": [
            "Extract HTML <a>",
            "hyperlinks & anchor",
            "Map to xhtml:link",
            "RDF blank nodes"
        ],
        "output_lines": [
            "@prefix xhtml: <http://www.w3.org/1999/xhtml#> .",
            "",
            "[] a xhtml:link ;",
            "   xhtml:anchor <source> ;",
            "   xhtml:rel \"relatedLink\" ;",
            "   xhtml:href <dataset/1> .",
            "",
            "[] a xhtml:link ;",
            "   xhtml:anchor <source> ;",
            "   xhtml:rel \"relatedLink\" ;",
            "   xhtml:href <dataset/2> ."
        ]
    },
    {
        "filename": "fig_rdfa.svg",
        "title": "RDFa Semantic Extraction (RDFA)",
        "input_type": "HTML with RDFa Attributes",
        "input_lines": [
            "<div about=\"/book/1\"",
            "     typeof=\"schema:Book\">",
            "  <span property=\"schema:name\">",
            "    RDFa Handbook",
            "  </span>",
            "</div>"
        ],
        "mapping_lines": [
            "Traverse DOM Tree",
            "Resolve Namespaces",
            "Extract Statements",
            "& properties"
        ],
        "output_lines": [
            "@prefix schema: <https://schema.org/> .",
            "",
            "<https://example.org/book/1>",
            "  a schema:Book ;",
            "  schema:name \"RDFa Handbook\" ."
        ]
    },
    {
        "filename": "fig_microdata.svg",
        "title": "Microdata Semantic Translation (MICRODATA)",
        "input_type": "HTML with Microdata",
        "input_lines": [
            "<div itemscope",
            "     itemtype=\"https://schema.org/Book\"",
            "     itemid=\"/book/1\">",
            "  <span itemprop=\"name\">",
            "    Microdata Book",
            "  </span>",
            "</div>"
        ],
        "mapping_lines": [
            "Identify scopes",
            "Map itemtype to type",
            "Convert itemprops",
            "to predicates"
        ],
        "output_lines": [
            "@prefix schema: <https://schema.org/> .",
            "",
            "<https://example.org/book/1>",
            "  a schema:Book ;",
            "  schema:name \"Microdata Book\" ."
        ]
    },
    {
        "filename": "fig_open_graph.svg",
        "title": "Open Graph to Schema.org Mapping (OPEN_GRAPH)",
        "input_type": "HTML Head Meta Tags",
        "input_lines": [
            "<meta property=\"og:title\"",
            "      content=\"Ocean Dataset\" />",
            "<meta property=\"og:type\"",
            "      content=\"dataset\" />",
            "<meta property=\"og:url\"",
            "      content=\"/dataset/42\" />"
        ],
        "mapping_lines": [
            "Parse og:* tags",
            "Map og:title to schema:name",
            "Map og:url to schema:url",
            "Infer rdf:type"
        ],
        "output_lines": [
            "@prefix schema: <https://schema.org/> .",
            "",
            "<https://example.org/dataset/42>",
            "  a schema:Dataset ;",
            "  schema:name \"Ocean Dataset\" ;",
            "  schema:url <https://example.org/dataset/42> ."
        ]
    },
    {
        "filename": "fig_dublin_core.svg",
        "title": "Dublin Core Semantic Translation (DUBLIN_CORE)",
        "input_type": "HTML Head Meta Tags",
        "input_lines": [
            "<meta name=\"DC.title\"",
            "      content=\"Marine Report\" />",
            "<meta name=\"DC.creator\"",
            "      content=\"C. Decruw\" />",
            "<meta name=\"DC.identifier\"",
            "      content=\"doi:10.12/34\" />"
        ],
        "mapping_lines": [
            "Parse DC.* tags",
            "Map to DCMI terms",
            "namespace prefix",
            "(dcterms:)"
        ],
        "output_lines": [
            "@prefix dcterms: <http://purl.org/dc/terms/> .",
            "",
            "<>",
            "  dcterms:title \"Marine Report\" ;",
            "  dcterms:creator \"C. Decruw\" ;",
            "  dcterms:identifier \"doi:10.12/34\" ."
        ]
    },
    {
        "filename": "fig_canonical.svg",
        "title": "Canonical Link Identity Resolution (CANONICAL)",
        "input_type": "HTML Head Link Tag",
        "input_lines": [
            "<link rel=\"canonical\"",
            "      href=\"/dataset/main\" />"
        ],
        "mapping_lines": [
            "Extract canonical",
            "relation target",
            "Map to xhtml:link",
            "RDF blank node"
        ],
        "output_lines": [
            "@prefix xhtml: <http://www.w3.org/1999/xhtml#> .",
            "",
            "[] a xhtml:link ;",
            "   xhtml:anchor <current> ;",
            "   xhtml:rel \"canonical\" ;",
            "   xhtml:href <dataset/main> ."
        ]
    },
    {
        "filename": "fig_rss_feed.svg",
        "title": "RSS XML to Data Catalog Inference (RSS_FEED)",
        "input_type": "RSS Feed XML",
        "input_lines": [
            "<rss version=\"2.0\">",
            "  <channel>",
            "    <title>VLIZ Feed</title>",
            "    <item>",
            "      <title>Dataset 1</title>",
            "      <link>/ds1</link>",
            "    </item>",
            "  </channel>",
            "</rss>"
        ],
        "mapping_lines": [
            "Parse RSS XML structure",
            "Map channel to Catalog",
            "Map items to Datasets",
            "and parent relations"
        ],
        "output_lines": [
            "@prefix schema: <https://schema.org/> .",
            "",
            "<feed.xml> a schema:DataCatalog ;",
            "  schema:name \"VLIZ Feed\" .",
            "",
            "<dataset/1> a schema:Dataset ;",
            "  schema:name \"Dataset 1\" ;",
            "  schema:isPartOf <feed.xml> ."
        ]
    },
    {
        "filename": "fig_atom_feed.svg",
        "title": "Atom XML to Data Catalog Inference (ATOM_FEED)",
        "input_type": "Atom Feed XML",
        "input_lines": [
            "<feed xmlns=\"...\">",
            "  <title>VLIZ Atom</title>",
            "  <entry>",
            "    <title>Dataset A</title>",
            "    <link href=\"/dsa\"/>",
            "  </entry>",
            "</feed>"
        ],
        "mapping_lines": [
            "Parse Atom XML structure",
            "Map entries and links",
            "to Dataset nodes",
            "and properties"
        ],
        "output_lines": [
            "@prefix schema: <https://schema.org/> .",
            "",
            "<feed.atom> a schema:DataCatalog ;",
            "  schema:name \"VLIZ Atom\" .",
            "",
            "<dataset/a> a schema:Dataset ;",
            "  schema:name \"Dataset A\" ;",
            "  schema:isPartOf <feed.atom> ."
        ]
    },
    {
        "filename": "fig_sitemap.svg",
        "title": "XML Sitemap to DCAT Catalog Inference (SITEMAP)",
        "input_type": "Sitemap XML",
        "input_lines": [
            "<urlset xmlns=\"...\">",
            "  <url>",
            "    <loc>/dataset/42</loc>",
            "    <lastmod>2026-06-04</lastmod>",
            "  </url>",
            "</urlset>"
        ],
        "mapping_lines": [
            "Parse locs & lastmods",
            "Map urls to CatalogRecord",
            "Map lastmod timestamp",
            "to listingDate"
        ],
        "output_lines": [
            "@prefix dcat: <http://www.w3.org/ns/dcat#> .",
            "@prefix schema: <https://schema.org/> .",
            "",
            "<sitemap.xml> a dcat:Catalog .",
            "",
            "<dataset/42> a dcat:CatalogRecord ;",
            "  dcat:listingDate \"2026-06-04\" ;",
            "  schema:isPartOf <sitemap.xml> ."
        ]
    },
    {
        "filename": "fig_robots.svg",
        "title": "Robots.txt Sitemap Extraction (ROBOTS)",
        "input_type": "Robots.txt Text",
        "input_lines": [
            "User-agent: *",
            "Disallow: /admin/",
            "Sitemap: /sitemap.xml",
            "Sitemap: /sitemap-data.xml"
        ],
        "mapping_lines": [
            "Parse text lines",
            "Extract Sitemap:",
            "directive URIs",
            "Map links to WebSite"
        ],
        "output_lines": [
            "@prefix schema: <https://schema.org/> .",
            "",
            "<https://example.org/>",
            "  a schema:WebSite ;",
            "  schema:hasPart",
            "    <sitemap.xml> , <sitemap-data.xml> ."
        ]
    },
    {
        "filename": "fig_manifest.svg",
        "title": "Web App Manifest to RDF Schema (MANIFEST)",
        "input_type": "Manifest JSON",
        "input_lines": [
            "{",
            "  \"name\": \"LOD Portal\",",
            "  \"start_url\": \"/index.html\",",
            "  \"description\": \"VLIZ LOD App\"",
            "}"
        ],
        "mapping_lines": [
            "Parse JSON payload",
            "Map manifest keys to",
            "schema:WebApplication",
            "properties"
        ],
        "output_lines": [
            "@prefix schema: <https://schema.org/> .",
            "",
            "<https://example.org/>",
            "  a schema:WebApplication ;",
            "  schema:name \"LOD Portal\" ;",
            "  schema:description \"VLIZ LOD App\" ;",
            "  schema:targetUrl <index.html> ."
        ]
    },
    {
        "filename": "fig_well_known.svg",
        "title": "Well-Known JSON to Web API Mapping (WELL_KNOWN)",
        "input_type": "Well-Known JSON Config",
        "input_lines": [
            "{",
            "  \"api_catalog\": \"/api/catalog.json\",",
            "  \"sitemaps\": [\"/sitemap.xml\"]",
            "}"
        ],
        "mapping_lines": [
            "Probe well-known path",
            "Parse JSON config keys",
            "Map to schema:WebAPI",
            "& EntryPoint node"
        ],
        "output_lines": [
            "@prefix schema: <https://schema.org/> .",
            "",
            "<https://example.org/>",
            "  a schema:WebAPI ;",
            "  schema:entryPoint [",
            "    a schema:EntryPoint ;",
            "    schema:urlTemplate \"/.well-known/...\"",
            "  ] ."
        ]
    },
    {
        "filename": "fig_api_discovery.svg",
        "title": "JSON API Catalog Discovery (API_DISCOVERY)",
        "input_type": "JSON API Response",
        "input_lines": [
            "{",
            "  \"links\": {",
            "    \"datasets\": \"/api/v1/datasets\"",
            "  }",
            "}"
        ],
        "mapping_lines": [
            "Parse JSON payload keys",
            "Match relation link fields",
            "Map API endpoint to",
            "dcat:DataService node"
        ],
        "output_lines": [
            "@prefix dcat: <http://www.w3.org/ns/dcat#> .",
            "",
            "<api/v1> a dcat:DataService ;",
            "  dcat:endpointURL <api/v1> ;",
            "  dcat:servesDataset <datasets> ."
        ]
    },
    {
        "filename": "fig_http_link_relations.svg",
        "title": "HTTP Link Headers to Structural Relations (HTTP_LINK_RELATIONS)",
        "input_type": "HTTP Link Headers",
        "input_lines": [
            "HTTP/1.1 200 OK",
            "Link: </col/1>; rel=\"collection\"",
            "Link: </parent>; rel=\"up\""
        ],
        "mapping_lines": [
            "Parse HTTP Link",
            "headers & rels",
            "Map to xhtml:link",
            "RDF blank nodes"
        ],
        "output_lines": [
            "@prefix xhtml: <http://www.w3.org/1999/xhtml#> .",
            "",
            "[] a xhtml:link ;",
            "   xhtml:anchor <current> ;",
            "   xhtml:rel \"collection\" ;",
            "   xhtml:href <col/1> .",
            "",
            "[] a xhtml:link ;",
            "   xhtml:anchor <current> ;",
            "   xhtml:rel \"up\" ;",
            "   xhtml:href <parent> ."
        ]
    },
    {
        "filename": "fig_pagination.svg",
        "title": "HTML Head Link Pagination Resolution (PAGINATION)",
        "input_type": "HTML Link Tags",
        "input_lines": [
            "<link rel=\"next\" href=\"/page/3\" />",
            "<link rel=\"prev\" href=\"/page/1\" />"
        ],
        "mapping_lines": [
            "Parse HTML head",
            "pagination links",
            "Map to xhtml:link",
            "RDF blank nodes"
        ],
        "output_lines": [
            "@prefix xhtml: <http://www.w3.org/1999/xhtml#> .",
            "",
            "[] a xhtml:link ;",
            "   xhtml:anchor <current> ;",
            "   xhtml:rel \"next\" ;",
            "   xhtml:href <page/3> .",
            "",
            "[] a xhtml:link ;",
            "   xhtml:anchor <current> ;",
            "   xhtml:rel \"prev\" ;",
            "   xhtml:href <page/1> ."
        ]
    },
    {
        "filename": "fig_resource_map.svg",
        "title": "Custom JSON Resource Map Mapping (RESOURCE_MAP)",
        "input_type": "Resource Map JSON",
        "input_lines": [
            "{",
            "  \"aggregates\": [",
            "    \"/resource/42\",",
            "    \"/metadata/42.ttl\"",
            "  ]",
            "}"
        ],
        "mapping_lines": [
            "Parse JSON aggregates",
            "Map aggregated objects",
            "to OAI-ORE aggregation",
            "triples"
        ],
        "output_lines": [
            "@prefix ore: <http://www.openarchives.org/ore/terms/> .",
            "",
            "<map.json> a ore:ResourceMap ;",
            "  ore:describes <aggUri> .",
            "<aggUri> a ore:Aggregation ;",
            "  ore:aggregates <resource/42> , <metadata/42.ttl> ."
        ]
    },
    {
        "filename": "fig_reverse_links.svg",
        "title": "Reciprocal Backlink Verification (REVERSE_LINKS)",
        "input_type": "HTML Hyperlink Graph",
        "input_lines": [
            "<!-- Page A (current) -->",
            "<a href=\"/pageB\">Page B</a>",
            "",
            "<!-- Page B (target) -->",
            "<a href=\"/pageA\">Page A</a>"
        ],
        "mapping_lines": [
            "Crawl target resource",
            "Verify reciprocal links",
            "Map to xhtml:link",
            "RDF blank nodes"
        ],
        "output_lines": [
            "@prefix xhtml: <http://www.w3.org/1999/xhtml#> .",
            "",
            "[] a xhtml:link ;",
            "   xhtml:anchor <pageA> ;",
            "   xhtml:rel \"relatedLink\" ;",
            "   xhtml:href <pageB> .",
            "",
            "[] a xhtml:link ;",
            "   xhtml:anchor <pageB> ;",
            "   xhtml:rel \"relatedLink\" ;",
            "   xhtml:href <pageA> ."
        ]
    },
    {
        "filename": "fig_circular_graphs.svg",
        "title": "Topological Cycle Detection (CIRCULAR_GRAPHS)",
        "input_type": "HTML Link Cycles",
        "input_lines": [
            "Page A references Page B",
            "Page B references Page C",
            "Page C references Page A"
        ],
        "mapping_lines": [
            "Trace crawler page path",
            "Detect loop cycles",
            "Map to xhtml:link",
            "RDF blank nodes"
        ],
        "output_lines": [
            "@prefix xhtml: <http://www.w3.org/1999/xhtml#> .",
            "",
            "[] a xhtml:link ;",
            "   xhtml:anchor <pageA> ;",
            "   xhtml:rel \"relatedLink\" ;",
            "   xhtml:href <pageB> .",
            "",
            "[] a xhtml:link ;",
            "   xhtml:anchor <pageB> ;",
            "   xhtml:rel \"relatedLink\" ;",
            "   xhtml:href <pageC> ."
        ]
    }
]

def main():
    target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "images"))
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created directory: {target_dir}")
        
    for fig in figures_data:
        svg_code = create_svg(
            title=fig["title"],
            input_type=fig["input_type"],
            input_lines=fig["input_lines"],
            mapping_lines=fig["mapping_lines"],
            output_lines=fig["output_lines"]
        )
        filepath = os.path.join(target_dir, fig["filename"])
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_code)
        print(f"Generated SVG: {filepath}")

if __name__ == "__main__":
    main()
