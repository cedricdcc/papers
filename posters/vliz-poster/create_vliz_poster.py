#!/usr/bin/env python3
"""
Generate the VLIZ Scientific Conference Poster in PowerPoint (.pptx).
Matches the institutional VLIZ template:
- Top sea-teal banner (#91C8CD) with exact VLIZ logo and vliz.be
- Left-aligned Subtitle (vibrant teal #31B7BC), Title (navy #3057A5), and Authors (#231F20)
- Hybrid Central Highlight: Full-width hero callout / map section
- 3-column structured grid below for Context, Methods, and Results
"""

from __future__ import annotations

import argparse
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE


def hex_to_rgb(hex_str: str) -> RGBColor:
    hex_str = hex_str.lstrip("#")
    return RGBColor(int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16))


# Exact VLIZ Color Palette
COLOR_BANNER_BG = hex_to_rgb("#91C8CD")     # Exact Sea-teal from template
COLOR_SUBTITLE  = hex_to_rgb("#31B7BC")     # Vibrant teal uppercase
COLOR_TITLE     = hex_to_rgb("#3057A5")     # VLIZ Corporate Navy
COLOR_AUTHOR    = hex_to_rgb("#231F20")     # Dark Charcoal
COLOR_TEXT_MAIN = hex_to_rgb("#1E293B")     # Slate-800
COLOR_TEXT_MUTED= hex_to_rgb("#64748B")     # Slate-500
COLOR_CARD_BG   = hex_to_rgb("#FFFFFF")     # Clean White
COLOR_HERO_BG   = hex_to_rgb("#F8FAFC")     # Slate-50 (hero callout background)
COLOR_BORDER    = hex_to_rgb("#CBD5E1")     # Slate-300
COLOR_BORDER_HERO= hex_to_rgb("#94A3B8")    # Slate-400
COLOR_PAGE_BG   = hex_to_rgb("#FFFFFF")     # White poster base


def create_vliz_poster(output_path: Path):
    prs = Presentation()
    # Standard A0 Portrait: 33.11" x 46.81" (84.1 cm x 118.9 cm)
    WIDTH_IN = 33.11
    HEIGHT_IN = 46.81
    prs.slide_width = Inches(WIDTH_IN)
    prs.slide_height = Inches(HEIGHT_IN)

    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # 1. Page Background (Pure White)
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(WIDTH_IN), Inches(HEIGHT_IN))
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_PAGE_BG
    bg.line.fill.background()

    LEFT_MARGIN = Inches(2.2)     # Exact 8.8% left margin as in template
    CONTENT_W   = Inches(WIDTH_IN) - (LEFT_MARGIN * 2)

    # 2. Top Banner (Exact VLIZ Header)
    BANNER_H = Inches(5.5)
    
    # 2a. Background Sea-Teal Rectangle
    top_banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(WIDTH_IN), BANNER_H)
    top_banner.fill.solid()
    top_banner.fill.fore_color.rgb = COLOR_BANNER_BG
    top_banner.line.fill.background()

    # 2b. Traced Vector Logo on Left (Crisp White Wave + Corporate Navy)
    candidates_logo = [
        Path("posters/vliz-poster/assets/vliz_logo_vector_hd.png"),
        Path("templates/posters/assets/vliz_logo_vector_hd.png"),
    ]
    logo_img_path = next((p for p in candidates_logo if p.exists()), None)
    if logo_img_path and logo_img_path.exists():
        LOGO_H = Inches(3.2)
        LOGO_W = Inches(3.2 * (8534.0 / 2309.0))  # Preserves exact aspect ratio (~11.8 inches)
        LOGO_TOP = (BANNER_H - LOGO_H) / 2
        slide.shapes.add_picture(str(logo_img_path), LEFT_MARGIN, LOGO_TOP, width=LOGO_W, height=LOGO_H)

    # 2c. Sharp Vector Text for vliz.be on Right
    URL_BOX_W = Inches(5.0)
    URL_BOX_H = Inches(1.2)
    URL_TOP = (BANNER_H - URL_BOX_H) / 2
    url_box = slide.shapes.add_textbox(Inches(WIDTH_IN) - LEFT_MARGIN - URL_BOX_W, URL_TOP, URL_BOX_W, URL_BOX_H)
    tf_url = url_box.text_frame
    tf_url.word_wrap = False
    p_url = tf_url.paragraphs[0]
    p_url.alignment = PP_ALIGN.RIGHT
    p_url.text = "vliz.be"
    p_url.font.name = "Arial"
    p_url.font.size = Pt(36)
    p_url.font.bold = True
    p_url.font.color.rgb = COLOR_TITLE

    # 3. Header Section (Subtitle, Title, Authors)
    # Subtitle Box
    sub_box = slide.shapes.add_textbox(LEFT_MARGIN, Inches(6.0), CONTENT_W, Inches(0.8))
    tf_sub = sub_box.text_frame
    tf_sub.word_wrap = True
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "SUBTITLE / RESEARCH TOPIC"
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(26)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_SUBTITLE

    # Title Box
    title_box = slide.shapes.add_textbox(LEFT_MARGIN, Inches(6.8), CONTENT_W, Inches(2.8))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = "Title poster here Lorem ipsum dolor sit amet, consectetur veniam."
    p_title.font.name = "Arial"
    p_title.font.size = Pt(54)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_TITLE
    p_title.space_after = Pt(8)

    # Author Box
    author_box = slide.shapes.add_textbox(LEFT_MARGIN, Inches(10.0), CONTENT_W, Inches(1.5))
    tf_author = author_box.text_frame
    tf_author.word_wrap = True
    p_auth = tf_author.paragraphs[0]
    p_auth.text = "Jan Peeters, Peter Jansens, Anne De Smet"
    p_auth.font.name = "Arial"
    p_auth.font.size = Pt(24)
    p_auth.font.bold = True
    p_auth.font.color.rgb = COLOR_AUTHOR

    # Affiliations & Contact
    p_affil = tf_author.add_paragraph()
    p_affil.text = "Flanders Marine Institute (VLIZ), InnovOcean Campus, Jacobsenstraat 1, 8400 Oostende, Belgium  |  Contact: info@vliz.be"
    p_affil.font.name = "Arial"
    p_affil.font.size = Pt(18)
    p_affil.font.color.rgb = COLOR_TEXT_MUTED
    p_affil.space_before = Pt(6)

    # =========================================================================
    # 4. HYBRID CENTRAL HIGHLIGHT (Hero Takeaway / Map Section)
    # Spans full width across columns
    # =========================================================================
    HERO_TOP = Inches(12.0)
    HERO_H   = Inches(7.5)
    HERO_LEFT = Inches(1.8)
    HERO_W    = Inches(WIDTH_IN) - (HERO_LEFT * 2)

    hero_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, HERO_LEFT, HERO_TOP, HERO_W, HERO_H)
    hero_card.fill.solid()
    hero_card.fill.fore_color.rgb = COLOR_HERO_BG
    hero_card.line.color.rgb = COLOR_SUBTITLE
    hero_card.line.width = Pt(2.5)

    # Hero Badge / Header inside card
    hero_title_box = slide.shapes.add_textbox(HERO_LEFT + Inches(0.5), HERO_TOP + Inches(0.4), HERO_W - Inches(1.0), Inches(0.8))
    tf_ht = hero_title_box.text_frame
    p_ht = tf_ht.paragraphs[0]
    p_ht.text = "CENTRAL HIGHLIGHT & KEY FINDING"
    p_ht.font.name = "Arial"
    p_ht.font.size = Pt(26)
    p_ht.font.bold = True
    p_ht.font.color.rgb = COLOR_TITLE

    # Hero Summary Text (Left Side of Card)
    hero_text_w = Inches(16.5)
    hero_text_box = slide.shapes.add_textbox(HERO_LEFT + Inches(0.5), HERO_TOP + Inches(1.3), hero_text_w, HERO_H - Inches(1.6))
    tf_htxt = hero_text_box.text_frame
    tf_htxt.word_wrap = True

    p_h1 = tf_htxt.paragraphs[0]
    p_h1.text = "Key Scientific Takeaway:"
    p_h1.font.name = "Arial"
    p_h1.font.size = Pt(22)
    p_h1.font.bold = True
    p_h1.font.color.rgb = COLOR_TEXT_MAIN
    p_h1.space_after = Pt(8)

    p_h2 = tf_htxt.add_paragraph()
    p_h2.text = "• Long-term acoustic telemetry and benthic monitoring reveal significant spatial redistribution of pelagic species in the Belgian Part of the North Sea (BPNS)."
    p_h2.font.name = "Arial"
    p_h2.font.size = Pt(20)
    p_h2.font.color.rgb = COLOR_TEXT_MAIN
    p_h2.space_after = Pt(8)

    p_h3 = tf_htxt.add_paragraph()
    p_h3.text = "• Environmental Drivers: Salinity gradients and sediment grain-size variance explain 68% of community turnover (p < 0.001), establishing a baseline for marine conservation."
    p_h3.font.name = "Arial"
    p_h3.font.size = Pt(20)
    p_h3.font.color.rgb = COLOR_TEXT_MAIN

    # Hero Figure Placeholder (Right Side of Card)
    fig_w = Inches(11.2)
    fig_h = HERO_H - Inches(1.4)
    fig_left = HERO_LEFT + HERO_W - fig_w - Inches(0.5)
    fig_top = HERO_TOP + Inches(0.9)

    fig_box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, fig_left, fig_top, fig_w, fig_h)
    fig_box.fill.solid()
    fig_box.fill.fore_color.rgb = hex_to_rgb("#E2E8F0")   # Slate-200 placeholder
    fig_box.line.color.rgb = COLOR_BORDER
    fig_box.line.width = Pt(1.5)

    tf_fig = fig_box.text_frame
    tf_fig.word_wrap = True
    p_fig = tf_fig.paragraphs[0]
    p_fig.text = "[ Central Figure / Study Area Map ]\n\nInsert high-resolution focal visual\n(DPI >= 300 recommended)\ne.g. North Sea Sampling Map or Heatmap"
    p_fig.font.name = "Arial"
    p_fig.font.size = Pt(18)
    p_fig.font.color.rgb = COLOR_TEXT_MUTED
    p_fig.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # 5. SUPPORTING 3-COLUMN GRID (Context, Methods, Results)
    # =========================================================================
    GRID_TOP   = HERO_TOP + HERO_H + Inches(0.7)
    NUM_COLS   = 3
    COL_GUTTER = Inches(0.8)
    COL_WIDTH  = (HERO_W - (COL_GUTTER * (NUM_COLS - 1))) / NUM_COLS
    AVAIL_GRID_H = Inches(HEIGHT_IN) - GRID_TOP - Inches(1.6)

    def add_section_card(col_idx: int, top_in: float, height_in: float, title: str, paragraphs: list):
        col_left = HERO_LEFT + col_idx * (COL_WIDTH + COL_GUTTER)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_left, top_in, COL_WIDTH, height_in)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_BORDER
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.4)
        tf.margin_right = Inches(0.4)
        tf.margin_top = Inches(0.35)
        tf.margin_bottom = Inches(0.35)

        # Title
        p_t = tf.paragraphs[0]
        p_t.text = title.upper()
        p_t.font.name = "Arial"
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TITLE
        p_t.space_after = Pt(10)

        for item in paragraphs:
            p = tf.add_paragraph()
            p.text = item.get("text", "")
            p.font.name = "Arial"
            p.font.size = Pt(item.get("size", 19))
            p.font.bold = item.get("bold", False)
            p.font.color.rgb = COLOR_TEXT_MAIN if not item.get("muted") else COLOR_TEXT_MUTED
            p.space_after = Pt(item.get("space_after", 6))

        return col_left, top_in + height_in + Inches(0.5)

    # ---- COLUMN 1: Context & Objectives ----
    c1_y = GRID_TOP
    c1_h1 = Inches(12.0)
    _, c1_y = add_section_card(0, c1_y, c1_h1, "1. Introduction & Background", [
        {"text": "Marine ecosystems face compounding anthropogenic and climate pressures in shallow coastal waters.", "size": 19, "space_after": 8},
        {"text": "Research Motivation:", "size": 19, "bold": True, "space_after": 4},
        {"text": "• Assess coastal biodiversity trends using multi-sensor mooring stations.", "size": 18},
        {"text": "• Evaluate ecosystem resilience across marine protected areas (MPAs).", "size": 18},
        {"text": "• Provide open data infrastructure via the European Marine Observation Network (EMODnet).", "size": 18, "space_after": 8},
        {"text": "Key Objectives:", "size": 19, "bold": True, "space_after": 4},
        {"text": "1. Characterize benthic-pelagic coupling dynamics over a 5-year observation window.", "size": 18},
        {"text": "2. Benchmark automated acoustic species classification algorithms.", "size": 18}
    ])

    c1_h2 = AVAIL_GRID_H - c1_h1 - Inches(0.5)
    add_section_card(0, c1_y, c1_h2, "2. Study Site & Sampling", [
        {"text": "Geographic Scope:", "size": 19, "bold": True, "space_after": 4},
        {"text": "Field research conducted across 12 permanent stations in the Southern Bight of the North Sea.", "size": 18, "space_after": 6},
        {"text": "Sensor Deployment:", "size": 19, "bold": True, "space_after": 4},
        {"text": "• Continuous CTD, turbidity, and fluorometry recordings.", "size": 18},
        {"text": "• Acoustic telemetry receiver grids tracking tagged migratory fauna.", "size": 18}
    ])

    # ---- COLUMN 2: Methods & Data Pipeline ----
    c2_y = GRID_TOP
    c2_h1 = Inches(13.0)
    _, c2_y = add_section_card(1, c2_y, c2_h1, "3. Methodology & Instrumentation", [
        {"text": "Integrated Marine Monitoring Pipeline:", "size": 19, "bold": True, "space_after": 6},
        {"text": "• Hydrodynamic & Biogeochemical Profiling:", "size": 19, "bold": True},
        {"text": "RV Simon Stevin cruises sampled water column properties quarterly (2021-2025).", "size": 18, "space_after": 6},
        {"text": "• High-Throughput Environmental DNA (eDNA):", "size": 19, "bold": True},
        {"text": "12S & COI metabarcoding identified 142 distinct marine taxa with 99.4% confidence.", "size": 18, "space_after": 6},
        {"text": "• Spatial Machine Learning:", "size": 19, "bold": True},
        {"text": "Gradient boosted trees mapped spatial vulnerability indices across dredge-disposal sites.", "size": 18}
    ])

    c2_h2 = AVAIL_GRID_H - c2_h1 - Inches(0.5)
    add_section_card(1, c2_y, c2_h2, "4. Data Quality & Standards", [
        {"text": "FAIR Marine Data Principles:", "size": 19, "bold": True, "space_after": 4},
        {"text": "All raw acoustic telemetry and biodiversity occurrence records are deposited in EurOBIS and Marine Data Archive (MDA).", "size": 18, "space_after": 6},
        {"text": "Standardized via Darwin Core Archive (DwC-A) standards.", "size": 17, "muted": True}
    ])

    # ---- COLUMN 3: Results & Conclusions ----
    c3_y = GRID_TOP
    c3_h1 = Inches(11.5)
    _, c3_y = add_section_card(2, c3_y, c3_h1, "5. Results & Discussion", [
        {"text": "Key Findings:", "size": 19, "bold": True, "space_after": 6},
        {"text": "• Taxa Richness Trends: 24% increase in demersal fish diversity adjacent to artificial reef foundations.", "size": 18, "space_after": 4},
        {"text": "• Temporal Stability: Seasonal biomass peak shifted earlier by 14 days over the last decade.", "size": 18, "space_after": 4},
        {"text": "• Anthropogenic Attenuation: MPA buffer zones mitigated seabed disturbance significantly.", "size": 18}
    ])

    c3_h2 = AVAIL_GRID_H - c3_h1 - Inches(0.5)
    add_section_card(2, c3_y, c3_h2, "6. Conclusions & References", [
        {"text": "Conclusions:", "size": 19, "bold": True, "space_after": 4},
        {"text": "Synchronized multi-sensor observatories provide crucial evidence for ecosystem-based marine spatial planning.", "size": 18, "space_after": 8},
        {"text": "Selected References:", "size": 17, "bold": True, "space_after": 2},
        {"text": "[1] Peeters et al. (2025). North Sea Observation Network. J. Mar. Sci.", "size": 15, "muted": True},
        {"text": "[2] Jansens & De Smet (2024). Coastal Telemetry Baselines. Oceanol.", "size": 15, "muted": True, "space_after": 6},
        {"text": "Scan QR for Data & Open Access Paper:", "size": 16, "bold": True},
        {"text": "https://www.vliz.be | Marine Data Archive", "size": 15, "muted": True}
    ])

    # 6. Bottom Baseline Footer
    footer_box = slide.shapes.add_textbox(LEFT_MARGIN, Inches(HEIGHT_IN) - Inches(1.1), CONTENT_W, Inches(0.8))
    tf_f = footer_box.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = "Flanders Marine Institute (VLIZ)  •  InnovOcean Campus, Oostende, Belgium  •  VLIZ Marine Science Day 2026"
    p_f.font.name = "Arial"
    p_f.font.size = Pt(17)
    p_f.font.color.rgb = COLOR_TEXT_MUTED
    p_f.alignment = PP_ALIGN.CENTER

    prs.save(str(output_path))
    print(f"Successfully generated VLIZ PowerPoint poster: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate VLIZ scientific conference poster (.pptx).")
    parser.add_argument("--output", default="posters/vliz-poster/vliz_poster_template.pptx", help="Output .pptx path")
    args = parser.parse_args()

    out_p = Path(args.output)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    create_vliz_poster(out_p)


if __name__ == "__main__":
    main()
