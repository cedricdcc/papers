# Nano Banana Infographic Prompt Templates & Style Presets

This guide provides parameterized prompt templates, pre-configured domain style presets, **4-Layer Visual Magnet Stage Integration rules**, and an interactive Human-in-the-Loop (HITL) refinement protocol for generating scientific infographics using **Nano Banana 2** (via the `scientific-schematics` generator).

---

## 1. The 70/30 Infographic Standard & Seamless Stage Integration

Scientific conference posters are visual communication instruments, not printed papers. Under the **70/30 Rule**:
- **70% of poster area** is reserved for high-impact visual storytelling (borderless hero infographic stage, experimental pipeline diagrams, focal results figures, and generous negative space).
- **30% of poster area** contains concise, scannable text (250–400 words total across the entire board).

### Viewing Distance & Anti-Box Graphic Constraints
When generated for an **A0 Portrait ($841 \times 1189\,\text{mm}$)** board viewed from 3 to 10 feet:
- **Zero Raw Prose**: Never generate sentences inside the infographic. Max 10 words total across labels.
- **Micro-Typography Rule**: Visual labels must be legible from 3–6 feet ($\ge 80\,\text{pt}$ at full print scale). Major numeric callouts $\ge 120\,\text{pt}$.
- **Generous Whitespace**: Maintain $50\text{--}60\%$ negative space within the infographic frame to avoid visual clutter.
- **Seamless Stage Integration (Anti-Box Rule)**:
  - Specify a pure, uniform outer background (`#FFFFFF` or soft sea-tint `#F4F9FA`) with **zero outer border frames, drop-shadow boxes, or cropped edges** so the graphic blends invisibly into the A0 canvas stage.
  - Include a subtle background flow ribbon (e.g., glowing teal-to-navy horizontal transit stream) spanning the full horizontal width from left to right to act as the poster's central visual magnet.
- **No Figure Numbers**: Do NOT bake "Figure 1", "Fig.", or captions into the image; the top **Billboard Hook Pill** and bottom pill caption are handled externally in the poster markup.

---

## 2. Layout Geometry & Aspect Ratio Presets

Select the aspect ratio that matches the author's approved A0 Portrait ASCII layout zone:

| Layout Zone | Aspect Ratio Flag | Recommended Dimensions | Typical Role |
| :--- | :--- | :--- | :--- |
| **Top / Mid Borderless Hero Stage** | `16:9` or `3:2` | Horizontal wide-span across columns | Project overview, end-to-end pipeline, landscape ecological transect |
| **Central Breakout Focal Stage** | `1:1` (Square) or `4:3` | Large centered borderless stage | Primary mechanism diagram, spatial GIS map, dominant empirical finding |
| **Vertical Column Feature** | `3:4` or `2:3` | Tall vertical slot (e.g. Methods column) | Stepwise sequential workflow, vertical water-column profile, apparatus schema |

---

## 3. Domain Style Presets & Atmospheric Motif Pairing

Combine the visual prompt with one of the following curated, color-accessible style presets. Each preset also pairs with a programmatic **Layer 0 Atmospheric Vector Motif** (which may be hybridized when combining institutional branding with technical topics):

### Preset A: VLIZ Marine Institute (Flanders Marine Institute Theme)
*Best for: Marine biology, oceanography, coastal ecology, maritime taxonomy, marine data systems.*
- **Primary Color Palette**: Sea-teal (`#91C8CD`), Deep Ocean Navy (`#002B49`), Corporate Navy (`#3057A5`), Vibrant Teal (`#31B7BC`), Soft Sea Stage (`#F4F9FA`), Coral Accent (`#E06D53`).
- **Paired Layer 0 Motif**: `bathymetry_waves` (bathymetric depth contours, acoustic sonar arcs, oceanic wave harmonics) or `hybrid_wave_mesh` (VLIZ wave harmonics in top banner + semantic node-link mesh in canvas corners).
- **Aesthetic Description**:
  ```text
  Clean modern scientific vector style tailored for marine science. Professional oceanographic illustration with sea-teal (#91C8CD), vibrant teal (#31B7BC), and deep ocean navy (#002B49) palette on a pure uniform background (#FFFFFF or #F4F9FA) with zero outer border frame. Minimalist vector elements, crisp line weights, subtle horizontal flow stream connecting left-to-right stages, high contrast, publication-ready finish. Zero clutter, generous white space.
  ```

### Preset B: Ecology, Biodiversity & Environmental Science
*Best for: Conservation biology, forestry, GIS spatial studies, ecological food webs.*
- **Primary Color Palette**: Forest Canopy Green (`#2D5A27`), Earth Ochre (`#C29B38`), River Teal (`#2B7A78`), Soft Sage (`#E8ECE9`), Deep Charcoal (`#222222`).
- **Paired Layer 0 Motif**: `topography` (topographic elevation isolines or botanical leaf venation vectors).
- **Aesthetic Description**:
  ```text
  Contemporary ecological scientific vector diagram. Clean nature-inspired palette using forest green (#2D5A27), earth ochre (#C29B38), and river teal (#2B7A78) on a seamless pure white background with zero outer border frame. Minimalist iconographic organisms and environmental flows, clean directional arrows, clear trophic/spatial hierarchy, ample negative space.
  ```

### Preset C: Biomedical, Molecular & Genomics
*Best for: Cellular pathways, pharmacology, genetics, immunology, neurobiology.*
- **Primary Color Palette (Okabe-Ito Accessible)**: Slate Navy (`#2A4D69`), Coral Red (`#D55E00`), Sky Blue (`#56B4E9`), Soft Gold (`#E69F00`), Deep Charcoal (`#1A1A1A`).
- **Paired Layer 0 Motif**: `molecular` (abstract double-helix ribbons or cellular Voronoi tessellations).
- **Aesthetic Description**:
  ```text
  Publication-grade molecular biology and biomedical schematic. Clean Okabe-Ito colorblind-accessible vector rendering on a seamless solid white background with zero outer bounding box. Distinct cellular membranes, receptors, and signaling cascades using sharp geometric shapes and smooth vector curves. Redundant visual encoding (distinct shapes plus distinct colors). Zero visual noise.
  ```

### Preset D: Modern Tech, AI, Engineering & Semantic Systems
*Best for: Neural networks, bioinformatics pipelines, semantic web linksets, hardware architectures, robotics.*
- **Primary Color Palette**: Electric Indigo (`#4361EE`), Tech Cyan (`#4CC9F0`), Slate Grey (`#334155`), Muted Silver (`#F1F5F9`), Dark Slate (`#0F172A`).
- **Paired Layer 0 Motif**: `network_mesh` (isometric node-link constellation meshes or metro-circuit traces).
- **Aesthetic Description**:
  ```text
  State-of-the-art systems architecture and AI pipeline diagram. Clean modular node-and-flow layout on a seamless pure white background with zero outer border box. High-contrast 2D vector components, clear left-to-right data transit conduits, crisp tech cyan (#4CC9F0) and electric indigo (#4361EE) accents, minimal high-legibility sans-serif labels.
  ```

---

## 4. Master Prompt Assembly Template

Construct the Nano Banana 2 prompt using this standardized template:

```text
Create a publication-quality scientific infographic for an A0 portrait conference poster.

TOPIC / CORE NARRATIVE:
[Insert 1-2 sentence description of the scientific discovery or system]

KEY VISUAL COMPONENTS (Maximum 3 to 4 distinct elements):
1. [Element 1: e.g. Input organism / specimen / siloed bottleneck]
2. [Element 2: e.g. Core experimental mechanism / transformation / signpost]
3. [Element 3: e.g. Key quantitative outcome / transit network / comparative endpoint]
4. [Element 4: Optional directional flow arrows or inline visual legend]

VISUAL STYLE & DOMAIN THEME:
[Insert chosen domain preset description from Section 3 above, including hex codes]

SEAMLESS STAGE INTEGRATION (ANTI-BOX RULE):
- Specify a pure, uniform outer background (#FFFFFF or soft sea-tint #F4F9FA) with zero outer border frames, drop-shadow boxes, or cropped edges so the graphic blends invisibly into the A0 canvas stage.
- Include a subtle background flow ribbon (e.g., glowing teal-to-navy transit stream) spanning the full horizontal width from left to right to act as the poster's central visual magnet.

SPATIAL GEOMETRY & COMPOSITION:
- Target Layout Zone: [16:9 Wide Banner | 1:1 Central Focal Box | 3:4 Vertical Column]
- White Space: Maintain 50% to 60% clean empty background to allow comfortable eye navigation
- Reading Flow: Unambiguous left-to-right (or top-to-bottom) visual progression

STRICT NEGATIVE CONSTRAINTS:
- No outer border frames, rectangular container boxes, or drop shadows around the canvas edge
- No figure numbers (do NOT write "Figure 1", "Fig.", or captions; external caption handled in poster markup strictly <= 12-15 words)
- No narrative sentences or paragraphs of text; maximum 10 single-word structural labels total
- Unified 2D flat vector aesthetic across all panels/stages (prohibit mixing 3D glass, photorealism, and cartoon stick figures)
- Prohibit pseudo-3D translucent glass cubes, boxes, or nested flowchart containers with micro-text inside; use clean 2D node-and-link signposts
- Prohibit stacked duplicate labels on parallel arrows or connector lines
- High contrast, colorblind-friendly (zero red-green conflicts)
```

---

## 5. Execution Command

Run the generation script through `scientific-schematics`:

```bash
python .agents/skills/scientific-schematics/scripts/generate_schematic.py \
  "<assembled_master_prompt>" \
  -o posters/<poster-name>/figures/hero_infographic.png \
  --doc-type poster \
  --iterations 2
```

---

## 6. Interactive Human-in-the-Loop (HITL) Refinement Protocol

Never finalize the visual asset on a single automated shot. Execute the following 3-step conversational review loop:

```
[ Step 1: Draft Candidate Presentation ]
  - Generate candidate hero infographic (v1) and verify seamless edge blending
  - Display the image or provide absolute path for author inspection
  - Summarize: Theme applied, visual elements depicted, aspect ratio, white space ratio
                    │
                    ▼
[ Step 2: Author Critique & Feedback Prompting ]
  - Ask targeted review questions:
    1. "Does the visual narrative accurately capture your primary scientific mechanism?"
    2. "Are the visual weights, seamless stage edges, and colors aligned with your project branding?"
    3. "Do you want any elements added, removed, or repositioned?"
                    │
                    ▼
[ Step 3: Iterative Adjustment & Re-generation ]
  - If changes requested: Apply surgical prompt adjustments (e.g., "increase white space by 20%",
    "change accent color from green to VLIZ teal #91C8CD", "simplify element 2 to an icon")
  - Re-run generator (`v2`, `v3`) until the author explicitly responds with approval
```
