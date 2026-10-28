#!/usr/bin/env python3
"""
Generate the Marine Term Translations (MTT) VLIZ Scientific Conference Poster in PowerPoint (.pptx).

Matches posters/marine-term-translations/poster.tex & official VLIZ branding:
- Standard A0 Portrait canvas: 33.11" x 46.81" (841 x 1189 mm)
- Top sea-teal banner (#91C8CD) with high-resolution VLIZ wave logo and vliz.be
- Left-aligned Subtitle (#31B7BC), Title (#3057A5), and Author/ORCID metadata (#231F20)
- Full-width Hero Architecture Card with high-DPI continuous LDES pipeline infographic
- 3-Column Audience-Targeted Evidence Grid (Ontology Stewards, Term Translators, Downstream Widgets)
  with aligned bottom baselines, native rounded sub-cards, metric callout badges, and vector-sharp QR code
- Full-width Footer with References, AI Disclosure, and Institutional Links
"""

from __future__ import annotations

import argparse
import io
from pathlib import Path
from PIL import Image, ImageFilter
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


def hex_to_rgb(hex_str: str) -> RGBColor:
    hex_str = hex_str.lstrip("#")
    return RGBColor(int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16))


# ==============================================================================
# VLIZ Institutional Color Palette (matching poster.tex)
# ==============================================================================
COLOR_BANNER_BG  = hex_to_rgb("#91C8CD")  # vlizBanner: Sea-teal top banner
COLOR_SUBTITLE   = hex_to_rgb("#31B7BC")  # vlizTeal: Vibrant teal subtitle & accents
COLOR_TITLE      = hex_to_rgb("#3057A5")  # vlizNavy: Corporate Navy
COLOR_AUTHOR     = hex_to_rgb("#231F20")  # vlizCharcoal: Dark Charcoal author text
COLOR_TEXT_MAIN  = hex_to_rgb("#1E293B")  # vlizSlateText: Main body text (Slate-800)
COLOR_TEXT_MUTED = hex_to_rgb("#64748B")  # vlizSlateMuted: Muted text (Slate-500)
COLOR_CARD_BG    = hex_to_rgb("#FFFFFF")  # vlizCardBg: White card background
COLOR_HERO_BG    = hex_to_rgb("#F8FAFC")  # vlizHeroBg: Soft slate sub-card background
COLOR_BORDER     = hex_to_rgb("#CBD5E1")  # vlizBorder: Card border (Slate-300)
COLOR_LIGHT_TEAL = hex_to_rgb("#E6F7F8")  # vlizLightTeal: Light teal callout background
COLOR_PAGE_BG    = hex_to_rgb("#FFFFFF")  # Pure white poster canvas


def load_high_dpi_image_stream(img_path: Path, min_width_px: int = 5000) -> tuple[io.BytesIO, int, int]:
    """Return an image stream guaranteed to meet >=150-300 effective print DPI when placed."""
    with Image.open(img_path) as im:
        w, h = im.size
        if w < min_width_px:
            scale = max(2, int((min_width_px + w - 1) // w))
            up = im.resize((w * scale, h * scale), Image.Resampling.LANCZOS)
            if up.mode in ("RGB", "L"):
                up = up.filter(ImageFilter.UnsharpMask(radius=1.2, percent=125, threshold=2))
            buf = io.BytesIO()
            up.save(buf, format="PNG", optimize=True)
            buf.seek(0)
            return buf, up.width, up.height
        buf = io.BytesIO(img_path.read_bytes())
        buf.seek(0)
        return buf, w, h


def add_rounded_card(
    slide,
    left_in: float,
    top_in: float,
    width_in: float,
    height_in: float,
    fill_color: RGBColor,
    border_color: RGBColor,
    border_pt: float = 2.0,
    radius: float = 0.02,
):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left_in),
        Inches(top_in),
        Inches(width_in),
        Inches(height_in),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(border_pt)
    try:
        shape.adjustments[0] = radius
    except Exception:
        pass
    return shape


def add_subcard(
    slide,
    left_in: float,
    top_in: float,
    width_in: float,
    height_in: float,
    title: str,
    body_lines: list[tuple[str, str]],
    fill_color: RGBColor,
    border_color: RGBColor,
    border_pt: float = 1.75,
):
    """
    Create a styled tcolorbox-equivalent rounded sub-card with bold navy title and body lines.
    body_lines is a list of (prefix_bold, text_regular) tuples.
    """
    card = add_rounded_card(
        slide,
        left_in,
        top_in,
        width_in,
        height_in,
        fill_color=fill_color,
        border_color=border_color,
        border_pt=border_pt,
        radius=0.06,
    )
    tf = card.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.28)
    tf.margin_right = Inches(0.28)
    tf.margin_top = Inches(0.18)
    tf.margin_bottom = Inches(0.18)

    p_title = tf.paragraphs[0]
    p_title.space_after = Pt(4)
    r_t = p_title.add_run()
    r_t.text = title
    r_t.font.name = "Arial"
    r_t.font.size = Pt(22)
    r_t.font.bold = True
    r_t.font.color.rgb = COLOR_TITLE

    for idx, (prefix_bold, body_text) in enumerate(body_lines):
        p = tf.add_paragraph()
        p.space_after = Pt(2 if idx < len(body_lines) - 1 else 0)
        p.font.name = "Arial"
        p.font.size = Pt(18.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        if prefix_bold:
            r_b = p.add_run()
            r_b.text = prefix_bold
            r_b.font.name = "Arial"
            r_b.font. bold = True
            r_b.font.color.rgb = COLOR_TEXT_MAIN
        r_txt = p.add_run()
        r_txt.text = body_text
        r_txt.font.name = "Arial"
        r_txt.font.bold = False
        r_txt.font.color.rgb = COLOR_TEXT_MAIN

    return card


def create_mtt_poster(output_path: Path) -> None:
    prs = Presentation()
    # Standard A0 Portrait: 33.11" x 46.81" (84.1 cm x 118.9 cm)
    WIDTH_IN = 33.11
    HEIGHT_IN = 46.81
    prs.slide_width = Inches(WIDTH_IN)
    prs.slide_height = Inches(HEIGHT_IN)

    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # ==========================================================================
    # 1. Pure White Page Background
    # ==========================================================================
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(WIDTH_IN), Inches(HEIGHT_IN))
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_PAGE_BG
    bg.line.fill.background()

    # ==========================================================================
    # 2. Top VLIZ Institutional Sea-Teal Banner (y = 0.0" .. 5.38")
    # ==========================================================================
    BANNER_H = 5.38
    HEADER_MARGIN_X = 2.91  # 8.8% institutional VLIZ margin
    top_banner = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, Inches(WIDTH_IN), Inches(BANNER_H)
    )
    top_banner.fill.solid()
    top_banner.fill.fore_color.rgb = COLOR_BANNER_BG
    top_banner.line.fill.background()

    logo_candidates = [
        Path("posters/marine-term-translations/assets/vliz_logo.png"),
        Path("posters/vliz-poster/assets/vliz_logo_vector_hd.png"),
        Path("templates/posters/assets/vliz_logo_vector_hd.png"),
    ]
    logo_path = next((p for p in logo_candidates if p.exists()), None)
    if logo_path:
        LOGO_H = 3.04
        LOGO_W = LOGO_H * (8534.0 / 2309.0)  # ~11.24"
        LOGO_TOP = (BANNER_H - LOGO_H) / 2.0
        slide.shapes.add_picture(
            str(logo_path),
            Inches(HEADER_MARGIN_X),
            Inches(LOGO_TOP),
            width=Inches(LOGO_W),
            height=Inches(LOGO_H),
        )

    # Sharp native typography for vliz.be on the right
    URL_W = 4.50
    URL_H = 1.10
    URL_LEFT = WIDTH_IN - HEADER_MARGIN_X - URL_W
    URL_TOP = (BANNER_H - URL_H) / 2.0
    url_box = slide.shapes.add_textbox(
        Inches(URL_LEFT), Inches(URL_TOP), Inches(URL_W), Inches(URL_H)
    )
    tf_url = url_box.text_frame
    tf_url.word_wrap = False
    p_url = tf_url.paragraphs[0]
    p_url.alignment = PP_ALIGN.RIGHT
    r_url = p_url.add_run()
    r_url.text = "vliz.be"
    r_url.font.name = "Arial"
    r_url.font.size = Pt(34)
    r_url.font.bold = True
    r_url.font.color.rgb = COLOR_TITLE

    # ==========================================================================
    # 3. Left-Aligned Title & Author Block (y = 5.70" .. 10.10")
    # ==========================================================================
    TITLE_W = WIDTH_IN - HEADER_MARGIN_X - 1.20  # 29.00"

    # Subtitle / Audience Callout
    sub_box = slide.shapes.add_textbox(
        Inches(HEADER_MARGIN_X), Inches(5.70), Inches(TITLE_W), Inches(0.65)
    )
    tf_sub = sub_box.text_frame
    tf_sub.word_wrap = True
    p_sub = tf_sub.paragraphs[0]
    r_sub = p_sub.add_run()
    r_sub.text = "MULTILINGUAL MARINE VOCABULARIES   |   mtt.vliz.be   |   FOR TRANSLATORS & ONTOLOGY STEWARDS"
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(24)
    r_sub.font.bold = True
    r_sub.font.color.rgb = COLOR_SUBTITLE

    # Main Poster Title
    title_box = slide.shapes.add_textbox(
        Inches(HEADER_MARGIN_X), Inches(6.42), Inches(TITLE_W), Inches(2.05)
    )
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    r_title = p_title.add_run()
    r_title.text = (
        "Marine Term Translations (MTT): Continuous LDES Ingestion, "
        "Collaborative Multilingual Curation, and Downstream Vocabulary Widgets"
    )
    r_title.font.name = "Arial"
    r_title.font.size = Pt(54)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_TITLE

    # Author & Affiliation
    auth_box = slide.shapes.add_textbox(
        Inches(HEADER_MARGIN_X), Inches(8.60), Inches(TITLE_W), Inches(1.40)
    )
    tf_auth = auth_box.text_frame
    tf_auth.word_wrap = True
    p_auth = tf_auth.paragraphs[0]
    p_auth.space_after = Pt(4)
    r_auth = p_auth.add_run()
    r_auth.text = "Cedric Decruw"
    r_auth.font.name = "Arial"
    r_auth.font.size = Pt(26)
    r_auth.font.bold = True
    r_auth.font.color.rgb = COLOR_AUTHOR

    p_affil = tf_auth.add_paragraph()
    p_affil.font.name = "Arial"
    p_affil.font.size = Pt(19)
    p_affil.font.color.rgb = COLOR_TEXT_MUTED
    r_affil = p_affil.add_run()
    r_affil.text = (
        "Flanders Marine Institute (VLIZ), InnovOcean Campus, 8400 Oostende, Belgium   |   "
        "cedric.decruw@vliz.be   |   ORCID: 0000-0001-6387-5988"
    )
    r_affil.font.name = "Arial"
    r_affil.font.color.rgb = COLOR_TEXT_MUTED

    # ==========================================================================
    # 4. Hero Architecture Infographic Block (y = 10.30" .. 23.55")
    # ==========================================================================
    MARGIN_X = 0.85
    CONTENT_W = WIDTH_IN - (MARGIN_X * 2.0)  # 31.41"
    HERO_TOP = 10.30
    HERO_H = 13.25

    add_rounded_card(
        slide,
        MARGIN_X,
        HERO_TOP,
        CONTENT_W,
        HERO_H,
        fill_color=COLOR_CARD_BG,
        border_color=COLOR_BORDER,
        border_pt=2.0,
        radius=0.015,
    )

    # Hero Header
    hero_hdr = slide.shapes.add_textbox(
        Inches(MARGIN_X + 0.40), Inches(10.50), Inches(CONTENT_W - 0.80), Inches(0.75)
    )
    tf_hh = hero_hdr.text_frame
    tf_hh.word_wrap = True
    p_hh = tf_hh.paragraphs[0]
    p_hh.alignment = PP_ALIGN.CENTER
    r_hh = p_hh.add_run()
    r_hh.text = "Central Architecture: Continuous LDES Ingestion, MTT Curation & vocab.vliz.be Widgets"
    r_hh.font.name = "Arial"
    r_hh.font.size = Pt(30)
    r_hh.font.bold = True
    r_hh.font.color.rgb = COLOR_TITLE

    # Hero Pipeline Image (mtt-ldes-continuous-pipeline.png)
    pipeline_path = Path("posters/marine-term-translations/assets/mtt-ldes-continuous-pipeline.png")
    if pipeline_path.exists():
        img_stream, px_w, px_h = load_high_dpi_image_stream(pipeline_path, min_width_px=5200)
        aspect = px_w / float(px_h)
        IMG_W = 29.80
        IMG_H = IMG_W / aspect  # ~10.61"
        IMG_LEFT = MARGIN_X + (CONTENT_W - IMG_W) / 2.0
        IMG_TOP = 11.38
        slide.shapes.add_picture(
            img_stream,
            Inches(IMG_LEFT),
            Inches(IMG_TOP),
            width=Inches(IMG_W),
            height=Inches(IMG_H),
        )

    # Hero Figure Caption
    hero_cap = slide.shapes.add_textbox(
        Inches(MARGIN_X + 0.40), Inches(22.15), Inches(CONTENT_W - 0.80), Inches(1.15)
    )
    tf_hc = hero_cap.text_frame
    tf_hc.word_wrap = True
    p_hc = tf_hc.paragraphs[0]
    p_hc.alignment = PP_ALIGN.CENTER
    p_hc.font.name = "Arial"
    p_hc.font.size = Pt(19)
    p_hc.font.color.rgb = COLOR_TEXT_MUTED

    r_hc1 = p_hc.add_run()
    r_hc1.text = "Figure 1: "
    r_hc1.font.name = "Arial"
    r_hc1.font.bold = True
    r_hc1.font.color.rgb = COLOR_TEXT_MUTED

    r_hc2 = p_hc.add_run()
    r_hc2.text = (
        "Continuous semantic pipeline: Upstream LDES ingestion → mtt.vliz.be translation workbench "
        "(AI suggestions + ORCID peer gate) → Outgoing LDES publication → Live reuse in vocab.vliz.be widgets."
    )
    r_hc2.font.name = "Arial"
    r_hc2.font.color.rgb = COLOR_TEXT_MUTED

    # ==========================================================================
    # 5. Supporting 3-Column Evidence Grid (y = 23.95" .. 43.95")
    # ==========================================================================
    GRID_TOP = 23.95
    GRID_H = 20.00
    COL_GUTTER = 0.46
    COL_W = (CONTENT_W - (COL_GUTTER * 2.0)) / 3.0  # 10.1633"

    col_lefts = [MARGIN_X + i * (COL_W + COL_GUTTER) for i in range(3)]
    for c_left in col_lefts:
        add_rounded_card(
            slide,
            c_left,
            GRID_TOP,
            COL_W,
            GRID_H,
            fill_color=COLOR_CARD_BG,
            border_color=COLOR_BORDER,
            border_pt=2.0,
            radius=0.018,
        )

    # --------------------------------------------------------------------------
    # COLUMN 1: For Ontology Stewards: Ingestion & Sync
    # --------------------------------------------------------------------------
    c1_left = col_lefts[0]
    c1_inner_x = c1_left + 0.35
    c1_inner_w = COL_W - 0.70

    c1_top_box = slide.shapes.add_textbox(
        Inches(c1_inner_x), Inches(24.20), Inches(c1_inner_w), Inches(8.35)
    )
    tf_c1 = c1_top_box.text_frame
    tf_c1.word_wrap = True

    p_c1_title = tf_c1.paragraphs[0]
    p_c1_title.alignment = PP_ALIGN.CENTER
    p_c1_title.space_after = Pt(10)
    r_c1_t = p_c1_title.add_run()
    r_c1_t.text = "1. For Ontology Stewards: Ingestion & Sync"
    r_c1_t.font.name = "Arial"
    r_c1_t.font.size = Pt(26)
    r_c1_t.font.bold = True
    r_c1_t.font.color.rgb = COLOR_TITLE

    def add_heading_and_bullets(tf, heading: str, bullets: list[tuple[str, bool]], space_after_last: int = 8):
        p_h = tf.add_paragraph()
        p_h.space_after = Pt(3)
        r_h = p_h.add_run()
        r_h.text = heading
        r_h.font.name = "Arial"
        r_h.font.size = Pt(22)
        r_h.font.bold = True
        r_h.font.color.rgb = COLOR_TEXT_MAIN

        for i, (b_txt, is_italic) in enumerate(bullets):
            p_b = tf.add_paragraph()
            p_b.space_after = Pt(3 if i < len(bullets) - 1 else space_after_last)
            p_b.font.name = "Arial"
            p_b.font.size = Pt(19)
            p_b.font.color.rgb = COLOR_TEXT_MAIN
            r_b = p_b.add_run()
            r_b.text = f"• {b_txt}"
            r_b.font.name = "Arial"
            r_b.font.italic = is_italic
            r_b.font.color.rgb = COLOR_TEXT_MAIN

    add_heading_and_bullets(
        tf_c1,
        "Operational Context:",
        [
            ("Marine registries (e.g. BODC P02, SeaDataNet) publish authoritative terms in English.", False),
            ("Static snapshot downloads cause sync latency, manual drift, and URI churn.", False),
        ],
    )
    add_heading_and_bullets(
        tf_c1,
        "Research Question (RQ):",
        [("How to ingest ontologies and enrich them multilingually while preserving concept identities?", True)],
    )
    add_heading_and_bullets(
        tf_c1,
        "Hypothesis & Prediction:",
        [("Streaming LDES ingestion with decoupled concept modeling eliminates sync lag without URI churn.", True)],
    )

    p_c1_val = tf_c1.add_paragraph()
    r_c1_val = p_c1_val.add_run()
    r_c1_val.text = "Platform Value for Stewards:"
    r_c1_val.font.name = "Arial"
    r_c1_val.font.size = Pt(22)
    r_c1_val.font.bold = True
    r_c1_val.font.color.rgb = COLOR_TEXT_MAIN

    c1_cards = [
        (
            "Continuous LDES Ingestion",
            [("", "Ingests upstream LDES event feeds, tracking term updates incrementally without bulk downloads.")],
            COLOR_LIGHT_TEAL,
            COLOR_BANNER_BG,
        ),
        (
            "Zero Concept URI Churn",
            [("", "Persistent concept URIs remain immutable as multilingual labels evolve, ensuring stable references.")],
            COLOR_LIGHT_TEAL,
            COLOR_BANNER_BG,
        ),
        (
            "Institutional Data Sovereignty",
            [("", "100% self-hostable open stack (React, Node.js, PostgreSQL) deployable on local infrastructure.")],
            COLOR_LIGHT_TEAL,
            COLOR_BANNER_BG,
        ),
        (
            "Standards-Based Interoperability",
            [("", "Dual export pathways: CSV, SKOS, JSON-LD, and continuous Linked Data Event Streams.")],
            COLOR_HERO_BG,
            COLOR_BORDER,
        ),
    ]
    c1_card_y = 32.70
    c1_card_h = 2.50
    c1_card_gap = 0.31
    for title, lines, bg_col, bd_col in c1_cards:
        add_subcard(
            slide,
            c1_inner_x,
            c1_card_y,
            c1_inner_w,
            c1_card_h,
            title=title,
            body_lines=lines,
            fill_color=bg_col,
            border_color=bd_col,
        )
        c1_card_y += c1_card_h + c1_card_gap

    # --------------------------------------------------------------------------
    # COLUMN 2: For Translators: Curation & Credit
    # --------------------------------------------------------------------------
    c2_left = col_lefts[1]
    c2_inner_x = c2_left + 0.35
    c2_inner_w = COL_W - 0.70

    c2_top_box = slide.shapes.add_textbox(
        Inches(c2_inner_x), Inches(24.20), Inches(c2_inner_w), Inches(4.65)
    )
    tf_c2 = c2_top_box.text_frame
    tf_c2.word_wrap = True

    p_c2_title = tf_c2.paragraphs[0]
    p_c2_title.alignment = PP_ALIGN.CENTER
    p_c2_title.space_after = Pt(10)
    r_c2_t = p_c2_title.add_run()
    r_c2_t.text = "2. For Translators: Curation & Credit"
    r_c2_t.font.name = "Arial"
    r_c2_t.font.size = Pt(26)
    r_c2_t.font.bold = True
    r_c2_t.font.color.rgb = COLOR_TITLE

    add_heading_and_bullets(
        tf_c2,
        "The Translation Bottleneck:",
        [
            ("Domain experts are deterred by complex semantic tools (Protégé, raw RDF) and unstructured spreadsheets.", False),
            ("Linguistic translations often go uncredited in academic pipelines.", False),
        ],
    )

    p_c2_wb = tf_c2.add_paragraph()
    r_c2_wb = p_c2_wb.add_run()
    r_c2_wb.text = "The mtt.vliz.be Workbench:"
    r_c2_wb.font.name = "Arial"
    r_c2_wb.font.size = Pt(22)
    r_c2_wb.font.bold = True
    r_c2_wb.font.color.rgb = COLOR_TEXT_MAIN

    c2_cards = [
        (
            "1. Side-by-Side Comparison UI",
            [("", "Distraction-free browser interface comparing source terms directly with translations.")],
        ),
        (
            "2. AI-Assisted Candidate Drafting",
            [("", "Contextual suggestions accelerate initial drafting velocity by 2× across batches.")],
        ),
        (
            "3. Human-in-the-Loop Review Gate",
            [("", "Machine suggestions remain provisional until validated by domain specialists.")],
        ),
        (
            "4. Citable ORCID Attribution",
            [("", "Every approved label is bound to ORCID, guaranteeing citable academic credit.")],
        ),
    ]
    c2_card_y = 29.00
    c2_card_h = 2.25
    c2_card_gap = 0.25
    for title, lines in c2_cards:
        add_subcard(
            slide,
            c2_inner_x,
            c2_card_y,
            c2_inner_w,
            c2_card_h,
            title=title,
            body_lines=lines,
            fill_color=COLOR_HERO_BG,
            border_color=COLOR_BORDER,
        )
        c2_card_y += c2_card_h + c2_card_gap

    # Governance note
    gov_box = slide.shapes.add_textbox(
        Inches(c2_inner_x), Inches(38.95), Inches(c2_inner_w), Inches(1.05)
    )
    tf_gov = gov_box.text_frame
    tf_gov.word_wrap = True
    p_gov = tf_gov.paragraphs[0]
    p_gov.font.name = "Arial"
    p_gov.font.size = Pt(19.5)
    p_gov.font.color.rgb = COLOR_TEXT_MAIN
    r_gov1 = p_gov.add_run()
    r_gov1.text = "Governance: "
    r_gov1.font.name = "Arial"
    r_gov1.font.bold = True
    r_gov1.font.color.rgb = COLOR_TEXT_MAIN
    r_gov2 = p_gov.add_run()
    r_gov2.text = "Role-aware permissions and complete version audit logs."
    r_gov2.font.name = "Arial"
    r_gov2.font.color.rgb = COLOR_TEXT_MAIN

    # Community Participation & Impact Sub-card (ends at y = 43.63", matching Column 1)
    add_subcard(
        slide,
        c2_inner_x,
        40.20,
        c2_inner_w,
        3.43,
        title="Community Participation & Impact",
        body_lines=[
            ("Translators: ", "Review and curate terminology in your native language."),
            ("Stewards: ", "Register ontologies for automated continuous ingestion."),
        ],
        fill_color=COLOR_LIGHT_TEAL,
        border_color=COLOR_SUBTITLE,
    )

    # --------------------------------------------------------------------------
    # COLUMN 3: Outgoing LDES & vocab.vliz.be Widgets
    # --------------------------------------------------------------------------
    c3_left = col_lefts[2]
    c3_inner_x = c3_left + 0.35
    c3_inner_w = COL_W - 0.70

    c3_top_box = slide.shapes.add_textbox(
        Inches(c3_inner_x), Inches(24.20), Inches(c3_inner_w), Inches(1.90)
    )
    tf_c3 = c3_top_box.text_frame
    tf_c3.word_wrap = True

    p_c3_title = tf_c3.paragraphs[0]
    p_c3_title.alignment = PP_ALIGN.CENTER
    p_c3_title.space_after = Pt(10)
    r_c3_t = p_c3_title.add_run()
    r_c3_t.text = "3. Outgoing LDES & vocab.vliz.be Widgets"
    r_c3_t.font.name = "Arial"
    r_c3_t.font.size = Pt(26)
    r_c3_t.font.bold = True
    r_c3_t.font.color.rgb = COLOR_TITLE

    p_c3_sub = tf_c3.add_paragraph()
    r_c3_sub = p_c3_sub.add_run()
    r_c3_sub.text = "Downstream Delivery Pipeline:"
    r_c3_sub.font.name = "Arial"
    r_c3_sub.font.size = Pt(22)
    r_c3_sub.font.bold = True
    r_c3_sub.font.color.rgb = COLOR_TEXT_MAIN

    add_subcard(
        slide,
        c3_inner_x,
        26.25,
        c3_inner_w,
        2.35,
        title="Outgoing LDES Stream Broadcast",
        body_lines=[
            ("", "Approved translations emitted as immutable RDF event feeds, eliminating bulk snapshot downloads.")
        ],
        fill_color=COLOR_LIGHT_TEAL,
        border_color=COLOR_BANNER_BG,
    )

    add_subcard(
        slide,
        c3_inner_x,
        28.85,
        c3_inner_w,
        2.35,
        title="vocab.vliz.be Widgets Endgoal",
        body_lines=[
            ("", "Curated terms power drop-in autocomplete and search widgets across marine portals.")
        ],
        fill_color=COLOR_LIGHT_TEAL,
        border_color=COLOR_BANNER_BG,
    )

    # Empirical Results Heading
    emp_box = slide.shapes.add_textbox(
        Inches(c3_inner_x), Inches(31.40), Inches(c3_inner_w), Inches(0.55)
    )
    tf_emp = emp_box.text_frame
    tf_emp.word_wrap = True
    p_emp = tf_emp.paragraphs[0]
    r_emp = p_emp.add_run()
    r_emp.text = "Empirical Results (BODC P02 Beta):"
    r_emp.font.name = "Arial"
    r_emp.font.size = Pt(22)
    r_emp.font.bold = True
    r_emp.font.color.rgb = COLOR_TEXT_MAIN

    # Two Side-by-Side Metric Callout Badges
    badge_w = (c3_inner_w - 0.36) / 2.0  # 4.55"
    badge_h = 2.05
    badge_y = 32.10

    badge1 = add_rounded_card(
        slide,
        c3_inner_x,
        badge_y,
        badge_w,
        badge_h,
        fill_color=COLOR_LIGHT_TEAL,
        border_color=COLOR_TITLE,
        border_pt=2.0,
        radius=0.08,
    )
    tf_b1 = badge1.text_frame
    tf_b1.word_wrap = True
    tf_b1.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_b1_num = tf_b1.paragraphs[0]
    p_b1_num.alignment = PP_ALIGN.CENTER
    r_b1_num = p_b1_num.add_run()
    r_b1_num.text = "25%"
    r_b1_num.font.name = "Arial"
    r_b1_num.font.size = Pt(34)
    r_b1_num.font.bold = True
    r_b1_num.font.color.rgb = COLOR_TITLE

    p_b1_lbl = tf_b1.add_paragraph()
    p_b1_lbl.alignment = PP_ALIGN.CENTER
    p_b1_lbl.font.name = "Arial"
    p_b1_lbl.font.size = Pt(18.5)
    p_b1_lbl.font.color.rgb = COLOR_TEXT_MAIN
    r_b1_lbl = p_b1_lbl.add_run()
    r_b1_lbl.text = "P02 Translated"
    r_b1_lbl.font.name = "Arial"
    r_b1_lbl.font.color.rgb = COLOR_TEXT_MAIN

    badge2 = add_rounded_card(
        slide,
        c3_inner_x + badge_w + 0.36,
        badge_y,
        badge_w,
        badge_h,
        fill_color=COLOR_HERO_BG,
        border_color=COLOR_SUBTITLE,
        border_pt=2.0,
        radius=0.08,
    )
    tf_b2 = badge2.text_frame
    tf_b2.word_wrap = True
    tf_b2.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_b2_num = tf_b2.paragraphs[0]
    p_b2_num.alignment = PP_ALIGN.CENTER
    r_b2_num = p_b2_num.add_run()
    r_b2_num.text = "2×"
    r_b2_num.font.name = "Arial"
    r_b2_num.font.size = Pt(34)
    r_b2_num.font.bold = True
    r_b2_num.font.color.rgb = COLOR_SUBTITLE

    p_b2_lbl = tf_b2.add_paragraph()
    p_b2_lbl.alignment = PP_ALIGN.CENTER
    p_b2_lbl.font.name = "Arial"
    p_b2_lbl.font.size = Pt(18.5)
    p_b2_lbl.font.color.rgb = COLOR_TEXT_MAIN
    r_b2_lbl = p_b2_lbl.add_run()
    r_b2_lbl.text = "Drafting Speed"
    r_b2_lbl.font.name = "Arial"
    r_b2_lbl.font.color.rgb = COLOR_TEXT_MAIN

    # Discussion Bullets (Hypothesis, Limitation, Future Direction)
    disc_box = slide.shapes.add_textbox(
        Inches(c3_inner_x), Inches(34.35), Inches(c3_inner_w), Inches(3.65)
    )
    tf_disc = disc_box.text_frame
    tf_disc.word_wrap = True
    disc_items = [
        ("• Supported Hypothesis: ", "Zero URI churn; continuous sync proven."),
        ("• 1 Study Limitation: ", "Throughput bounded by reviewer bandwidth."),
        ("• Actionable Future Direction: ", "Deploy automated confidence triage."),
    ]
    for idx, (b_head, b_body) in enumerate(disc_items):
        p_d = tf_disc.paragraphs[0] if idx == 0 else tf_disc.add_paragraph()
        p_d.space_after = Pt(6 if idx < len(disc_items) - 1 else 0)
        p_d.font.name = "Arial"
        p_d.font.size = Pt(19)
        p_d.font.color.rgb = COLOR_TEXT_MAIN
        r_dh = p_d.add_run()
        r_dh.text = b_head
        r_dh.font.name = "Arial"
        r_dh.font.bold = True
        r_dh.font.color.rgb = COLOR_TEXT_MAIN
        r_db = p_d.add_run()
        r_db.text = b_body
        r_db.font.name = "Arial"
        r_db.font.color.rgb = COLOR_TEXT_MAIN

    # QR Code Callout Card (ends at y = 43.63", matching Columns 1 & 2)
    QR_CARD_TOP = 38.20
    QR_CARD_H = 5.43
    add_rounded_card(
        slide,
        c3_inner_x,
        QR_CARD_TOP,
        c3_inner_w,
        QR_CARD_H,
        fill_color=COLOR_LIGHT_TEAL,
        border_color=COLOR_TITLE,
        border_pt=1.75,
        radius=0.05,
    )

    qr_hdr_box = slide.shapes.add_textbox(
        Inches(c3_inner_x + 0.20), Inches(38.32), Inches(c3_inner_w - 0.40), Inches(0.60)
    )
    tf_qrh = qr_hdr_box.text_frame
    tf_qrh.word_wrap = True
    p_qrh = tf_qrh.paragraphs[0]
    p_qrh.alignment = PP_ALIGN.CENTER
    r_qrh = p_qrh.add_run()
    r_qrh.text = "Test the Live Platform & Widgets (Scan QR Code)"
    r_qrh.font.name = "Arial"
    r_qrh.font.size = Pt(22)
    r_qrh.font.bold = True
    r_qrh.font.color.rgb = COLOR_TITLE

    qr_img_path = Path("posters/marine-term-translations/assets/qr_mtt_vliz_be.png")
    if qr_img_path.exists():
        QR_SIZE = 3.55
        QR_LEFT = c3_inner_x + (c3_inner_w - QR_SIZE) / 2.0
        QR_TOP = 39.02
        slide.shapes.add_picture(
            str(qr_img_path),
            Inches(QR_LEFT),
            Inches(QR_TOP),
            width=Inches(QR_SIZE),
            height=Inches(QR_SIZE),
        )

    qr_url_box = slide.shapes.add_textbox(
        Inches(c3_inner_x + 0.20), Inches(42.68), Inches(c3_inner_w - 0.40), Inches(0.75)
    )
    tf_qru = qr_url_box.text_frame
    tf_qru.word_wrap = True
    p_qru = tf_qru.paragraphs[0]
    p_qru.alignment = PP_ALIGN.CENTER
    p_qru.font.name = "Arial"
    p_qru.font.size = Pt(19)
    p_qru.font.color.rgb = COLOR_TEXT_MAIN
    r_qru = p_qru.add_run()
    r_qru.text = "mtt.vliz.be   |   https://mtt.vliz.be/"
    r_qru.font.name = "Arial"
    r_qru.font.bold = True
    r_qru.font.color.rgb = COLOR_TEXT_MAIN

    # ==========================================================================
    # 6. Full-Width Bottom Footer Block (y = 44.30" .. 46.05")
    # ==========================================================================
    FOOTER_TOP = 44.30
    FOOTER_H = 1.75
    add_rounded_card(
        slide,
        MARGIN_X,
        FOOTER_TOP,
        CONTENT_W,
        FOOTER_H,
        fill_color=COLOR_CARD_BG,
        border_color=COLOR_BORDER,
        border_pt=2.0,
        radius=0.04,
    )

    f_left_box = slide.shapes.add_textbox(
        Inches(MARGIN_X + 0.35), Inches(44.45), Inches(22.50), Inches(1.45)
    )
    tf_fl = f_left_box.text_frame
    tf_fl.word_wrap = True
    tf_fl.vertical_anchor = MSO_ANCHOR.MIDDLE

    p_ref = tf_fl.paragraphs[0]
    p_ref.space_after = Pt(4)
    p_ref.font.name = "Arial"
    p_ref.font.size = Pt(18)
    p_ref.font.color.rgb = COLOR_TEXT_MAIN
    r_ref_b = p_ref.add_run()
    r_ref_b.text = "References: "
    r_ref_b.font.name = "Arial"
    r_ref_b.font.bold = True
    r_ref_b.font.color.rgb = COLOR_TEXT_MAIN
    r_ref_t = p_ref.add_run()
    r_ref_t.text = "[1] Wilkinson et al. (2016). Sci. Data.    [2] BODC (2024). NERC P02.    [3] Van de Vyvere et al. (2022). LDES."
    r_ref_t.font.name = "Arial"
    r_ref_t.font.color.rgb = COLOR_TEXT_MAIN

    p_ai = tf_fl.add_paragraph()
    p_ai.font.name = "Arial"
    p_ai.font.size = Pt(18)
    p_ai.font.color.rgb = COLOR_TEXT_MAIN
    r_ai_b = p_ai.add_run()
    r_ai_b.text = "AI Disclosure: "
    r_ai_b.font.name = "Arial"
    r_ai_b.font.bold = True
    r_ai_b.font.color.rgb = COLOR_TEXT_MAIN
    r_ai_t = p_ai.add_run()
    r_ai_t.text = "Assisted with language polish and schematic layout; system design and evaluation by the author."
    r_ai_t.font.name = "Arial"
    r_ai_t.font.color.rgb = COLOR_TEXT_MAIN

    f_right_box = slide.shapes.add_textbox(
        Inches(MARGIN_X + CONTENT_W - 8.20), Inches(44.45), Inches(7.85), Inches(1.45)
    )
    tf_fr = f_right_box.text_frame
    tf_fr.word_wrap = True
    tf_fr.vertical_anchor = MSO_ANCHOR.MIDDLE

    p_fr1 = tf_fr.paragraphs[0]
    p_fr1.alignment = PP_ALIGN.RIGHT
    p_fr1.space_after = Pt(4)
    p_fr1.font.name = "Arial"
    p_fr1.font.size = Pt(18.5)
    p_fr1.font.color.rgb = COLOR_TEXT_MAIN
    r_fr1 = p_fr1.add_run()
    r_fr1.text = "Flanders Marine Institute (VLIZ)"
    r_fr1.font.name = "Arial"
    r_fr1.font.bold = True
    r_fr1.font.color.rgb = COLOR_TEXT_MAIN

    p_fr2 = tf_fr.add_paragraph()
    p_fr2.alignment = PP_ALIGN.RIGHT
    p_fr2.font.name = "Arial"
    p_fr2.font.size = Pt(18)
    p_fr2.font.color.rgb = COLOR_TEXT_MUTED
    r_fr2 = p_fr2.add_run()
    r_fr2.text = "mtt.vliz.be   |   vocab.vliz.be"
    r_fr2.font.name = "Arial"
    r_fr2.font.color.rgb = COLOR_TEXT_MUTED

    output_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(output_path))
    print(f"Successfully generated Marine Term Translations PowerPoint poster: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Marine Term Translations (MTT) VLIZ scientific conference poster (.pptx)."
    )
    parser.add_argument(
        "--output",
        default="posters/marine-term-translations/poster.pptx",
        help="Output .pptx path (default: posters/marine-term-translations/poster.pptx)",
    )
    args = parser.parse_args()
    create_mtt_poster(Path(args.output))


if __name__ == "__main__":
    main()

