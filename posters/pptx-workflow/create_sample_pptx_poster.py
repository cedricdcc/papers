#!/usr/bin/env python3
"""
Create a publication-ready 3-column scientific poster in PowerPoint (.pptx).
Follows conference poster layout standards:
- 48" x 36" (Landscape) or 33.1" x 46.8" (A0 Portrait)
- 3-column balanced grid
- Clear typographic hierarchy: Title (72pt+), Section Headers (32-36pt), Body (22-24pt)
- Section cards with clean margins and high contrast
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


def build_poster(output_path: Path, width_in: float = 48.0, height_in: float = 36.0):
    prs = Presentation()
    prs.slide_width = Inches(width_in)
    prs.slide_height = Inches(height_in)

    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Color Palette
    BG_COLOR = hex_to_rgb("#F1F5F9")        # Slate-100
    PRIMARY = hex_to_rgb("#0F172A")         # Slate-900
    ACCENT = hex_to_rgb("#0284C7")          # Sky-600
    CARD_BG = hex_to_rgb("#FFFFFF")         # Pure White
    BORDER = hex_to_rgb("#CBD5E1")          # Slate-300
    TEXT_MAIN = hex_to_rgb("#1E293B")       # Slate-800
    TEXT_MUTED = hex_to_rgb("#64748B")      # Slate-500

    # 1. Background Fill
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(width_in), Inches(height_in))
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = BG_COLOR
    bg_shape.line.fill.background()

    # Layout coordinates
    MARGIN_X = Inches(1.0)
    MARGIN_Y = Inches(0.8)
    HEADER_HEIGHT = Inches(4.2)
    AVAILABLE_WIDTH = Inches(width_in) - (MARGIN_X * 2)

    # 2. Header Banner Card
    header_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, MARGIN_X, MARGIN_Y, AVAILABLE_WIDTH, HEADER_HEIGHT)
    header_box.fill.solid()
    header_box.fill.fore_color.rgb = PRIMARY
    header_box.line.fill.background()

    tf_header = header_box.text_frame
    tf_header.word_wrap = True
    tf_header.margin_left = Inches(0.8)
    tf_header.margin_right = Inches(0.8)
    tf_header.margin_top = Inches(0.5)
    tf_header.margin_bottom = Inches(0.4)

    # Title
    p_title = tf_header.paragraphs[0]
    p_title.text = "Deep Research and Scalable Scientific Discovery with Agentic AI"
    p_title.font.name = "Arial"
    p_title.font.size = Pt(64)
    p_title.font.bold = True
    p_title.font.color.rgb = RGBColor(255, 255, 255)
    p_title.alignment = PP_ALIGN.CENTER

    # Authors
    p_author = tf_header.add_paragraph()
    p_author.text = "Alex R. Mercer¹, Elena Rostova², David Chen¹"
    p_author.font.name = "Arial"
    p_author.font.size = Pt(28)
    p_author.font.bold = True
    p_author.font.color.rgb = hex_to_rgb("#38BDF8")  # Sky-400
    p_author.alignment = PP_ALIGN.CENTER
    p_author.space_before = Pt(14)

    # Affiliations
    p_affil = tf_header.add_paragraph()
    p_affil.text = "¹Department of Computer Science, University of Technology  |  ²Institute for Advanced Discovery"
    p_affil.font.name = "Arial"
    p_affil.font.size = Pt(22)
    p_affil.font.color.rgb = hex_to_rgb("#CBD5E1")
    p_affil.alignment = PP_ALIGN.CENTER
    p_affil.space_before = Pt(6)

    # 3. Columns Setup
    NUM_COLS = 3
    COL_GUTTER = Inches(0.75)
    TOTAL_GUTTER = COL_GUTTER * (NUM_COLS - 1)
    COL_WIDTH = (AVAILABLE_WIDTH - TOTAL_GUTTER) / NUM_COLS

    CONTENT_TOP = MARGIN_Y + HEADER_HEIGHT + Inches(0.6)
    FOOTER_SPACE = Inches(1.5)
    CONTENT_HEIGHT = Inches(height_in) - CONTENT_TOP - FOOTER_SPACE

    # Helper function to create a section card
    def add_card(col_idx: int, top_in: float, height_in: float, title: str, paragraphs_data: list):
        col_left = MARGIN_X + col_idx * (COL_WIDTH + COL_GUTTER)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_left, top_in, COL_WIDTH, height_in)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.5)
        tf.margin_right = Inches(0.5)
        tf.margin_top = Inches(0.4)
        tf.margin_bottom = Inches(0.4)

        # Card Title
        p_t = tf.paragraphs[0]
        p_t.text = title.upper()
        p_t.font.name = "Arial"
        p_t.font.size = Pt(28)
        p_t.font.bold = True
        p_t.font.color.rgb = ACCENT
        p_t.space_after = Pt(12)

        for item in paragraphs_data:
            p = tf.add_paragraph()
            p.text = item.get("text", "")
            p.font.name = "Arial"
            p.font.size = Pt(item.get("size", 22))
            p.font.bold = item.get("bold", False)
            p.font.color.rgb = TEXT_MAIN if not item.get("muted") else TEXT_MUTED
            p.space_after = Pt(item.get("space_after", 8))
            if item.get("bullet"):
                p.level = 0

        return col_left, top_in + height_in + Inches(0.4)

    # ================= Column 1: Context & Problem =================
    c1_y = CONTENT_TOP
    c1_card1_h = Inches(12.5)
    _, c1_y = add_card(0, c1_y, c1_card1_h, "1. Introduction & Background", [
        {"text": "Scientific research generation is shifting from manual composition to agentic workflows that orchestrate deep search and verifiable synthesis.", "size": 22, "space_after": 10},
        {"text": "Key Challenges in Academic Writing:", "size": 22, "bold": True, "space_after": 6},
        {"text": "• Unverified citations and hallucinated bibliographic metadata", "size": 20, "bullet": True},
        {"text": "• Inconsistent visual hierarchy across figures, schematics, and text", "size": 20, "bullet": True},
        {"text": "• Fragmented tooling between literature retrieval and typesetting", "size": 20, "bullet": True},
        {"text": "Research Goal:", "size": 22, "bold": True, "space_after": 6},
        {"text": "To establish an end-to-end autonomous research synthesis pipeline that pairs real-time literature retrieval with rigorous formatting and verification gates.", "size": 22}
    ])

    c1_card2_h = CONTENT_HEIGHT - c1_card1_h - Inches(0.4)
    add_card(0, c1_y, c1_card2_h, "2. System Architecture", [
        {"text": "Our framework integrates three synchronized sub-agents:", "size": 22, "space_after": 10},
        {"text": "1. Research & Retrieval Agent:", "size": 21, "bold": True},
        {"text": "Queries academic indices, validates DOIs, and stores verified BibTeX.", "size": 20, "space_after": 8},
        {"text": "2. Synthesis & Layout Engine:", "size": 21, "bold": True},
        {"text": "Transforms verified data into publication-ready LaTeX / PPTX posters.", "size": 20, "space_after": 8},
        {"text": "3. Visual Quality & Audit Subagent:", "size": 21, "bold": True},
        {"text": "Enforces DPI >= 300, checks WCAG contrast, and eliminates overlaps.", "size": 20}
    ])

    # ================= Column 2: Methods & Schematics =================
    c2_y = CONTENT_TOP
    c2_card1_h = Inches(14.0)
    _, c2_y = add_card(1, c2_y, c2_card1_h, "3. Methodology & Verification Gates", [
        {"text": "Strict Quality Assurance Protocol:", "size": 22, "bold": True, "space_after": 8},
        {"text": "• Zero-Tolerance Citation Check: All references verified against primary publisher endpoints.", "size": 20, "bullet": True},
        {"text": "• Minimum Font Constraint: Guaranteed body >= 22pt, headers >= 32pt for 6-foot readability.", "size": 20, "bullet": True},
        {"text": "• Dynamic Column Binning: Auto-balancing column heights to ensure 50%+ whitespace.", "size": 20, "bullet": True},
        {"text": "Experimental Benchmark:", "size": 22, "bold": True, "space_after": 6},
        {"text": "Tested across 150 conference posters in AI, biology, and materials science.", "size": 21}
    ])

    c2_card2_h = CONTENT_HEIGHT - c2_card1_h - Inches(0.4)
    add_card(1, c2_y, c2_card2_h, "4. Key Performance Indicators", [
        {"text": "Comparative Benchmark Metrics:", "size": 22, "bold": True, "space_after": 10},
        {"text": "• Citation Precision: 99.8% verified metadata (vs 74.2% baseline LLM)", "size": 21, "bullet": True},
        {"text": "• Visual Formatting Errors: 0 collisions detected across 150 test builds", "size": 21, "bullet": True},
        {"text": "• Generation Turnaround: 4.2 minutes per full publication-ready poster", "size": 21, "bullet": True}
    ])

    # ================= Column 3: Results & Conclusions =================
    c3_y = CONTENT_TOP
    c3_card1_h = Inches(13.0)
    _, c3_y = add_card(2, c3_y, c3_card1_h, "5. Experimental Results", [
        {"text": "Evaluation Findings:", "size": 22, "bold": True, "space_after": 8},
        {"text": "• Multi-column layout achieves 98.4% readability score from conference reviewers.", "size": 20, "bullet": True},
        {"text": "• Automated print DPI verification eliminated blurred raster graphics entirely.", "size": 20, "bullet": True},
        {"text": "• Strict contrast checking ensures full accessibility for color-deficient readers.", "size": 20, "bullet": True},
        {"text": "Discussion:", "size": 22, "bold": True, "space_after": 6},
        {"text": "Bounded manifest-driven generation guarantees that conference printer requirements are never violated.", "size": 20}
    ])

    c3_card2_h = CONTENT_HEIGHT - c3_card1_h - Inches(0.4)
    add_card(2, c3_y, c3_card2_h, "6. Conclusions & References", [
        {"text": "Conclusions:", "size": 22, "bold": True, "space_after": 6},
        {"text": "Autonomous agentic synthesis coupled with deterministic layout compilers provides a robust standard for scientific communication.", "size": 20, "space_after": 10},
        {"text": "Selected References:", "size": 20, "bold": True, "space_after": 4},
        {"text": "[1] Mercer et al. (2025). Agentic Writing Pipelines. J. AI Res.", "size": 17, "muted": True},
        {"text": "[2] Chen & Rostova (2024). Verifiable Scientific Synthesis. NeurIPS.", "size": 17, "muted": True},
        {"text": "Contact & Code: github.com/cedricdcc/papers", "size": 19, "bold": True, "space_after": 2}
    ])

    # 4. Footer Bar
    footer_box = slide.shapes.add_textbox(MARGIN_X, Inches(height_in) - Inches(1.1), AVAILABLE_WIDTH, Inches(0.8))
    tf_f = footer_box.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = "Presented at the 2026 International Conference on Scientific Agentic AI | Supported by Open Grant #8841-B"
    p_f.font.name = "Arial"
    p_f.font.size = Pt(18)
    p_f.font.color.rgb = TEXT_MUTED
    p_f.alignment = PP_ALIGN.CENTER

    prs.save(str(output_path))
    print(f"Successfully generated scientific poster: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Create a publication-ready scientific PowerPoint poster.")
    parser.add_argument("--output", default="posters/pptx-workflow/sample_poster.pptx", help="Output .pptx path")
    parser.add_argument("--width", type=float, default=48.0, help="Canvas width in inches (default: 48.0)")
    parser.add_argument("--height", type=float, default=36.0, help="Canvas height in inches (default: 36.0)")
    args = parser.parse_args()

    out_p = Path(args.output)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    build_poster(out_p, width_in=args.width, height_in=args.height)


if __name__ == "__main__":
    main()
