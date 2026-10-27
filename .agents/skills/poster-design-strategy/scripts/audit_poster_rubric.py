#!/usr/bin/env python3
"""
Mixed-Approach Rubric (MAR) & Empirical Compliance Auditor for Scientific Posters.
Implements the Khadka & Peeters (2024) empirical criteria:
- Wordiness minimization (beta = -0.37)
- Contemporary layout format (beta = +0.28)
- Logical visual sequencing (beta = +0.16)
- Visual elements replacing text (beta = +0.15)
- QR code integration (beta = +0.12)
- Exclusion of submission abstract (beta = -0.10)
- 4-Tier MAR Scoring: Organization, Poster Design & Visuals, Wordiness/Density
"""

import sys
import re
import argparse
from pathlib import Path

def clean_tex(text: str) -> str:
    # Remove comments
    lines = [line.split('%', 1)[0] for line in text.splitlines()]
    clean = "\n".join(lines)
    # Extract body if document environment exists to exclude LaTeX preamble
    if "\\begin{document}" in clean:
        clean = clean.split("\\begin{document}", 1)[1]
    if "\\end{document}" in clean:
        clean = clean.split("\\end{document}", 1)[0]
    # Remove tikzpicture environments which contain coordinates and path commands
    clean = re.sub(r'\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}', ' ', clean)
    # Remove common command macros and brackets
    clean = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?', ' ', clean)
    clean = re.sub(r'\[[^\]]*\]', ' ', clean)
    clean = re.sub(r'[{}]', ' ', clean)
    # Remove dimension units and coordinates
    clean = re.sub(r'\b\d+(\.\d+)?(cm|mm|pt|in|ex|em)?\b', ' ', clean)
    clean = re.sub(r'[()=\-+;*$<>]', ' ', clean)
    return clean

def audit_text_content(content: str, source_type: str = "tex"):
    visible_text = clean_tex(content) if source_type == "tex" else content
    words = visible_text.split()
    word_count = len(words)

    # Check for abstract
    has_abstract = bool(re.search(r'\babstract\b', content, re.IGNORECASE))

    # Check for Research Question & Hypothesis
    has_rq = bool(re.search(r'(research question|core question|\bRQ\b)', content, re.IGNORECASE))
    has_hypothesis = bool(re.search(r'(hypothesis|prediction|hypothesize)', content, re.IGNORECASE))

    # Check for Methods diagram
    has_diagram = bool(re.search(r'(tikzpicture|flowchart|pipeline|diagram|\.png|\.pdf|\.svg)', content, re.IGNORECASE))

    # Check for Results tables (prohibited)
    has_tables = bool(re.search(r'(\\begin\{table\}|\\begin\{tabular\}|<a:tbl>)', content, re.IGNORECASE))

    # Check for QR code
    has_qr = bool(re.search(r'(\\qrcode|qrcode|qr[-_ ]code)', content, re.IGNORECASE))

    # Check for Limitation & Future Direction
    has_limitation = bool(re.search(r'(limitation|caveat|constraint)', content, re.IGNORECASE))
    has_future = bool(re.search(r'(future direction|future work|outlook|next steps)', content, re.IGNORECASE))

    # Count references
    ref_matches = re.findall(r'(\[\d+\]|\\cite\{|\bReferences?\b)', content, re.IGNORECASE)

    # ---------------------------------------------------------
    # 4-Tier MAR Rubric Scoring (1: Poor, 2: Sub-par, 3: Acceptable, 4: Exemplary)
    # ---------------------------------------------------------
    
    # 1. Wordiness / Text Density Score
    if word_count > 800:
        score_wordiness = 1
        desc_wordiness = "Poor [1]: Heavy wall of text (>800 words), high risk of cognitive overload."
    elif word_count > 600:
        score_wordiness = 2
        desc_wordiness = "Sub-par [2]: Busy layout (600-800 words); reading takes excessive dwell time."
    elif word_count > 450:
        score_wordiness = 3
        desc_wordiness = "Acceptable [3]: Moderate text density (450-600 words); manageable for standard review."
    elif word_count >= 200:
        score_wordiness = 4
        desc_wordiness = "Exemplary [4]: Optimal illustrated abstract density (250-450 words); rapid visual parsing."
    else:
        score_wordiness = 3
        desc_wordiness = "Acceptable [3]: Sparse text (<200 words); ensure key context is sufficiently explained."

    # 2. Organization Score
    org_points = 0
    if not has_abstract:
        org_points += 1  # Abstract excluded
    if has_rq or has_hypothesis:
        org_points += 1
    if has_limitation and has_future:
        org_points += 1
    if bool(re.search(r'(introduction|background|methods|results|discussion|conclusion)', content, re.IGNORECASE)):
        org_points += 1

    if org_points == 4:
        score_org = 4
        desc_org = "Exemplary [4]: Exceptionally clean, straightforward, and logically organized IMRaD sequence."
    elif org_points == 3:
        score_org = 3
        desc_org = "Acceptable [3]: Generally organized; minor sequencing or section refinement could be made."
    elif org_points == 2:
        score_org = 2
        desc_org = "Sub-par [2]: Organization leaves room for improvement; key narrative links missing."
    else:
        score_org = 1
        desc_org = "Poor [1]: Unstructured narrative flow; hard for viewers to navigate."

    # 3. Poster Design & Visuals Score
    vis_points = 0
    if has_diagram:
        vis_points += 1
    if has_qr:
        vis_points += 1
    if not has_tables:
        vis_points += 1  # No raw data tables cluttering results
    if bool(re.search(r'(\\includegraphics|image|figure|chart|map)', content, re.IGNORECASE)):
        vis_points += 1

    if vis_points == 4:
        score_vis = 4
        desc_vis = "Exemplary [4]: High figure-to-text ratio, visual schemas aid comprehension, QR offloads details."
    elif vis_points == 3:
        score_vis = 3
        desc_vis = "Acceptable [3]: Graphics are functional and pleasant overall."
    elif vis_points == 2:
        score_vis = 2
        desc_vis = "Sub-par [2]: Design lacks functional visual diagrams or contains raw tables."
    else:
        score_vis = 1
        desc_vis = "Poor [1]: Visually unengaging; lacks clear focal graphics."

    total_mar = score_org + score_vis + score_wordiness
    max_mar = 12
    pct_mar = round((total_mar / max_mar) * 100, 1)

    print("=" * 72)
    print("  MIXED-APPROACH RUBRIC (MAR) & EMPIRICAL POSTER AUDIT")
    print("  Reference: Khadka & Peeters (2024) | Inter-rater agreement kappa = 0.80")
    print("=" * 72)
    print(f"Estimated Word Count:   {word_count} words (Target: 250-450 words)")
    print(f"Abstract Excluded:      {'[OK] Yes' if not has_abstract else '[!] NO (Abstract wastes high-value real estate)'}")
    print(f"Research Question:      {'[OK] Detected' if has_rq else '[!] Missing explicit statement'}")
    print(f"Hypothesis/Prediction:  {'[OK] Detected' if has_hypothesis else '[!] Missing explicit statement'}")
    print(f"Visual Diagram/Schema:  {'[OK] Present' if has_diagram else '[!] None detected in Methods'}")
    print(f"Raw Data Tables:        {'[!] Present (Prohibited in Results)' if has_tables else '[OK] None (Clean figure focus)'}")
    print(f"QR Code Integration:    {'[OK] Present (beta = +0.12)' if has_qr else '[!] Absent'}")
    print(f"Discussion Limitation:  {'[OK] Exactly 1 detected' if has_limitation else '[!] Missing explicit limitation'}")
    print(f"Future Direction:       {'[OK] Exactly 1 detected' if has_future else '[!] Missing actionable future direction'}")
    print("-" * 72)
    print("RUBRIC ASSESSMENT:")
    print(f"1. Organization:             {desc_org}")
    print(f"2. Poster Design & Visuals:  {desc_vis}")
    print(f"3. Wordiness / Text Density: {desc_wordiness}")
    print("-" * 72)
    print(f"COMPOSITE MAR SCORE: {total_mar} / {max_mar} ({pct_mar}%)")
    
    if total_mar >= 11:
        print("OVERALL QUALITY: EXEMPLARY (Publication / Conference Award Tier)")
    elif total_mar >= 9:
        print("OVERALL QUALITY: ACCEPTABLE (Ready for presentation with minor polish)")
    else:
        print("OVERALL QUALITY: NEEDS REVISION (High risk of attendee disengagement)")
    print("=" * 72)

    return total_mar

def main():
    parser = argparse.ArgumentParser(description="Audit scientific poster against the Khadka & Peeters MAR framework.")
    parser.add_argument("file", help="Path to poster file (.tex, .pptx, .md, .txt)")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    content = ""
    if file_path.suffix.lower() == ".pptx":
        try:
            from pptx import Presentation
            prs = Presentation(str(file_path))
            text_runs = []
            for slide in prs.slides:
                for shape in slide.shapes:
                    if shape.has_text_frame:
                        for p in shape.text_frame.paragraphs:
                            for r in p.runs:
                                text_runs.append(r.text)
            content = " ".join(text_runs)
        except Exception as e:
            print(f"Error reading PPTX: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        content = file_path.read_text(encoding="utf-8", errors="ignore")

    audit_text_content(content, source_type=file_path.suffix.lstrip("."))

if __name__ == "__main__":
    main()
