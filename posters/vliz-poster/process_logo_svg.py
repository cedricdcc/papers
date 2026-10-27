#!/usr/bin/env python3
"""
Convert traced SVG logo to standardized VLIZ SVG and vector PDF.
- Wave lines -> #FFFFFF
- Logo & tagline typography -> #3057A5 (VLIZ Navy)
- Exports both vliz_logo.svg and vliz_logo.pdf (vector PDF for LaTeX pdflatex)
"""

import re
from pathlib import Path
import pymupdf

def process_logo():
    src_svg = Path("templates/posters/assets/test_logo.svg")
    text = src_svg.read_text(encoding="utf-8")

    def repl(m):
        c = m.group(1).upper()
        if c == "#FFFFFF":
            return 'fill="#FFFFFF"'
        return 'fill="#3057A5"'

    cleaned_svg = re.sub(r'fill="(#[0-9A-Fa-f]{6})"', repl, text)

    dest_paths = [
        Path("templates/posters/assets/vliz_logo.svg"),
        Path("posters/vliz-poster/assets/vliz_logo.svg")
    ]

    for p in dest_paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(cleaned_svg, encoding="utf-8")
        print(f"Wrote {p}")

    # Convert to vector PDF using PyMuPDF
    doc = pymupdf.open("templates/posters/assets/vliz_logo.svg")
    pdf_bytes = doc.convert_to_pdf()
    pdf_doc = pymupdf.open("pdf", pdf_bytes)

    for pdf_path in [
        Path("templates/posters/assets/vliz_logo.pdf"),
        Path("posters/vliz-poster/assets/vliz_logo.pdf")
    ]:
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        pdf_doc.save(str(pdf_path))
        print(f"Wrote vector PDF: {pdf_path}")

if __name__ == "__main__":
    process_logo()
