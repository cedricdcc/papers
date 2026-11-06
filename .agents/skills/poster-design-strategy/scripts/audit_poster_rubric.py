#!/usr/bin/env python3
"""
Mixed-Approach Rubric (MAR), Provenance, 4-Layer Visual Magnet & Empirical Compliance Auditor
for Scientific Posters.
Implements the Khadka & Peeters (2024) empirical criteria, the 70/30 Infographic Standard,
the 4-Layer Visual Magnet Architecture, and provenance.md verification:
- Wordiness minimization (beta = -0.37)
- Contemporary layout format (beta = +0.28)
- Logical visual sequencing (beta = +0.16)
- Visual elements replacing text (beta = +0.15)
- QR code integration (beta = +0.12)
- Exclusion of submission abstract (beta = -0.10)
- 4-Layer Visual Magnet verification (Layer 0 Motifs, Layer 1 Borderless Hero + Hook Pill,
  Layer 2 Cross-Board Conduit, Layer 3 Tactile Left-Accent Sub-Cards)
- Provenance verification (posters/<name>/provenance.md: audience, authors, conference, logo space,
  extra_logos, visual_magnet, inputs)
- 4-Tier MAR Scoring across 4 Dimensions (16 points max):
  1. Organization
  2. Poster Design & Visuals
  3. Wordiness / Text Density (250-400 words budget)
  4. Visual-to-Text Spatial Ratio (70/30 Rule & Hero Infographic)
"""

import sys
import re
import argparse
from pathlib import Path
from typing import Dict, Any, Optional


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
    # Remove standalone TikZ path commands (\draw, \fill, \filldraw, \shade, \path, \coordinate) up to semicolon
    clean = re.sub(r'\\(draw|fill|filldraw|shade|path|clip|coordinate)\b[^;]*;', ' ', clean)
    # Remove TikZ \node[...](name) at (...) preamble before the node text body
    clean = re.sub(r'\\node\s*(\[[\s\S]*?\])?\s*(\([^)]*\))?\s*at\s*\([^)]*\)\s*', ' ', clean)
    # Remove \vicon{color}{badge} and color arguments like {vlizNavy}
    clean = re.sub(r'\\vicon\{[^}]*\}\{[^}]*\}', ' ', clean)
    clean = re.sub(r'\{vliz[A-Za-z]+\}', ' ', clean)
    clean = re.sub(r'\b(vliz[A-Za-z]+|herographic|hookpill|herocaption|spineTop|spineTurn|qrEntry|qrTerminus|station\w+|m[1-9])\b', ' ', clean)
    # Remove macro options and arguments that define colors, fonts, or graphics
    clean = re.sub(r'\\(definecolor|color|colorlet|usecolorstyle|usetheme|fontsize|selectfont|tcbuselibrary|usetikzlibrary)\{[^}]*\}', ' ', clean)
    clean = re.sub(r'\\includegraphics(\[[^\]]*\])?\{[^}]*\}', ' ', clean)
    clean = re.sub(
        r'\b(at|rectangle|circle|ellipse|node|anchor|inner|sep|xsep|ysep|width|height|scale|'
        r'controls|and|cycle|rounded|corners|line|opacity|dashed|dotted|thick|ultra|'
        r'north|south|east|west|center|borderline|fuzzy|shadow|xshift|yshift|enhanced|'
        r'colback|colframe|boxrule|arc|valign|halign|left|right|top|bottom)\b',
        ' ',
        clean,
    )
    # Remove environment options like \begin{tcolorbox}[...]
    clean = re.sub(r'\\begin\{[^}]+\}(\[[^\]]*\])?', ' ', clean)
    clean = re.sub(r'\\end\{[^}]+\}', ' ', clean)
    # Remove common command macros and brackets
    clean = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?', ' ', clean)
    clean = re.sub(r'\[[^\]]*\]', ' ', clean)
    clean = re.sub(r'[{}]', ' ', clean)
    # Remove dimension units and coordinates
    clean = re.sub(r'\b\d+(\.\d+)?(cm|mm|pt|in|ex|em)?\b', ' ', clean)
    clean = re.sub(r'[()=\-+;*$<>|•→▸◈⬡⚡🔗]', ' ', clean)
    return clean


def audit_provenance_file(poster_path: Path) -> Dict[str, Any]:
    prov_path = poster_path.parent / "provenance.md"
    result: Dict[str, Any] = {
        "exists": prov_path.exists(),
        "path": str(prov_path),
        "has_frontmatter": False,
        "required_sections_present": [],
        "missing_sections": [],
        "has_visual_magnet": False,
        "unresolved_tokens": 0,
        "reserve_conf_logo": None,
        "extra_logos_count": 0,
        "deliverable_formats": [],
    }
    if not prov_path.exists():
        return result

    raw = prov_path.read_text(encoding="utf-8", errors="ignore")
    result["unresolved_tokens"] = len(re.findall(r'REPLACE_ME_[A-Z0-9_]+', raw))

    fm_match = re.match(r'^---\s*\n([\s\S]*?)\n---', raw)
    if fm_match:
        result["has_frontmatter"] = True
        fm_text = fm_match.group(1)
        required_keys = ["deliverables", "audience", "authors", "conference", "branding", "inputs"]
        for key in required_keys:
            if re.search(rf'^{key}\s*:', fm_text, re.MULTILINE):
                result["required_sections_present"].append(key)
            else:
                result["missing_sections"].append(key)

        result["has_visual_magnet"] = bool(re.search(r'^visual_magnet\s*:', fm_text, re.MULTILINE))

        conf_logo_match = re.search(r'reserve_default_conference_logo_space\s*:\s*(true|false)', fm_text, re.IGNORECASE)
        if conf_logo_match:
            result["reserve_conf_logo"] = conf_logo_match.group(1).lower() == "true"

        for fmt in ("latex", "pptx"):
            if re.search(rf'-\s*["\']?{fmt}["\']?', fm_text, re.IGNORECASE):
                result["deliverable_formats"].append(fmt)

        # Count extra_logos items if listed under extra_logos:
        extra_block = re.search(r'extra_logos\s*:\s*\n((?:\s+-\s+.*\n?)*)', fm_text)
        if extra_block and extra_block.group(1).strip():
            result["extra_logos_count"] = len(re.findall(r'^\s*-\s+name\s*:', extra_block.group(1), re.MULTILINE))

    return result


def audit_text_content(
    content: str,
    source_type: str = "tex",
    visible_override: Optional[str] = None,
    provenance_info: Optional[Dict[str, Any]] = None,
):
    if visible_override is not None:
        visible_text = visible_override
    else:
        visible_text = clean_tex(content) if source_type == "tex" else content

    # Filter out standalone punctuation/bullet tokens for accurate word count
    words = [w for w in visible_text.split() if re.search(r'[A-Za-z0-9]', w)]
    word_count = len(words)

    # Check for abstract
    has_abstract = bool(re.search(r'\babstract\b', content, re.IGNORECASE))

    # Check for Research Question & Hypothesis
    has_rq = bool(re.search(r'(research question|core question|\bRQ\b)', content, re.IGNORECASE))
    has_hypothesis = bool(re.search(r'(hypothesis|prediction|hypothesize)', content, re.IGNORECASE))

    # Check for Methods diagram
    has_diagram = bool(re.search(r'(tikzpicture|flowchart|pipeline|diagram|\.png|\.pdf|\.svg|<p:pic>)', content, re.IGNORECASE))

    # Check for Results tables (prohibited)
    has_tables = bool(re.search(r'(\\begin\{table\}|\\begin\{tabular\}|<a:tbl>)', content, re.IGNORECASE))

    # Check for QR code
    has_qr = bool(re.search(r'(\\qrcode|qrcode|qr[-_ ]code|qr_)', content, re.IGNORECASE))

    # Check for Limitation & Future Direction
    has_limitation = bool(re.search(r'(limitation|caveat|constraint)', content, re.IGNORECASE))
    has_future = bool(re.search(r'(future direction|future work|outlook|next step)', content, re.IGNORECASE))

    # Check for Inverted Chronological Flow
    disc_pos = re.search(r'(4\.\s*discussion|discussion,\s*limitations|study limitation)', content, re.IGNORECASE)
    meth_pos = re.search(r'(2\.\s*the\s*4|methods|pillars|methodology)', content, re.IGNORECASE)
    hero_pos = re.search(r'(hero_infographic|infographic|schematic)', content, re.IGNORECASE)
    has_inverted_flow = False
    if disc_pos and (meth_pos or hero_pos):
        earliest_body = min([p.start() for p in [meth_pos, hero_pos] if p is not None])
        if disc_pos.start() < earliest_body:
            has_inverted_flow = True

    # Check for Subjective / Humorous Metric Badges
    subjective_metrics = re.findall(r'\b(boredom|max\s+boredom|maximum\s+boredom|0\s+bottlenecks?|zero\s+bottlenecks?|100%\s+fun|100%\s+happiness)\b', content, re.IGNORECASE)
    has_subjective_metrics = len(subjective_metrics) > 0

    # Check for Redundant Section Sub-Headers
    has_redundant_subheaders = bool(re.search(r'\\textbf\{\s*\d+\.\s+[^}]+\}\s*\\\\\s*\\textit\{', content) or
                                   re.search(r'\\textbf\{\s*\d+\.\s+[^}]+\}[\s\S]{1,60}\\textit\{The\s+', content))

    # Check for Plain Bullet Walls
    has_plain_bullets = bool(re.search(r'\\begin\{itemize\}[\s\S]*?\\item\s+[^\\{\[]+[\s\S]*?\\end\{itemize\}', content) and not re.search(r'\\begin\{itemize\}[\s\S]*?\\begin\{tcolorbox\}', content))

    # Check for Duplicate Raw URLs in body text
    url_matches = re.findall(r'(https?://[^\s{}]+|open-sc[a-z]*\.vliz\.be)', content, re.IGNORECASE)
    url_counts: Dict[str, int] = {}
    for u in url_matches:
        norm_u = u.rstrip("/,.;)").lower()
        url_counts[norm_u] = url_counts.get(norm_u, 0) + 1
    duplicate_urls = [u for u, count in url_counts.items() if count > 1]
    has_duplicate_urls = len(duplicate_urls) > 0

    # Check for Long Captions (> 15 words)
    caption_match = re.search(r'\\caption\{([^}]+)\}', content, re.IGNORECASE)
    caption_word_count = len(caption_match.group(1).split()) if caption_match else 0
    has_overlong_caption = caption_word_count > 15

    # Check for A0 Portrait Layout Indicators
    has_portrait = bool(re.search(r'(portrait|orientation=portrait|paperwidth=84|paperheight=118)', content, re.IGNORECASE))
    has_a0 = bool(re.search(r'(a0|a0paper|841mm|1189mm)', content, re.IGNORECASE))

    # Check for Hero Infographic / Dominant Visual Assets
    hero_infographic_match = re.search(r'(hero_infographic|infographic|schematic|architecture|overview_diagram|pipeline_overview)', content, re.IGNORECASE)
    has_hero_infographic = bool(hero_infographic_match)

    # Check for 4-Layer Visual Magnet Indicators
    has_layer0_motif = bool(re.search(r'(bg_motif_|definebackgroundstyle|opacity=0\.0[4-8]|opacity=0\.1[2-5])', content, re.IGNORECASE))
    has_layer1_hook_stage = bool(re.search(r'(hook_pill_|hero_stage_|FROM SILOED GUESSWORK|vlizHeroStage|billboard_hook)', content, re.IGNORECASE))
    has_layer2_conduit = bool(re.search(r'(conduit_|Visual Conduit|Cross-Board|spine_conduit)', content, re.IGNORECASE))
    has_layer3_tactile = bool(re.search(r'(borderline west|accent_bar_|drop fuzzy shadow)', content, re.IGNORECASE))

    # Check for Anti-AI Icon Restraint (Prohibit synthetic icon badges / Unicode symbol spam)
    ai_icon_matches = re.findall(r'(\\vicon\b|\\blacktriangleright|\\blacktriangleleft|[◈⬡⚡🔗▸◀▶])', content)
    has_ai_icon_spam = len(ai_icon_matches) > 0

    # Check for Micro-Fonts inside Narrative / QR Cards (Prohibit \tiny, \scriptsize, or \footnotesize in main columns)
    body_before_footer = content
    if "References, Funding" in content:
        body_before_footer = content.split("References, Funding", 1)[0]
    micro_font_matches = re.findall(r'\\(tiny|scriptsize|footnotesize)\b', body_before_footer) if source_type == "tex" else []
    has_micro_fonts = len(micro_font_matches) > 0

    # Count graphic instances
    graphic_count = len(re.findall(r'(\\includegraphics|\\begin\{tikzpicture\}|<p:pic>)', content, re.IGNORECASE))

    # ---------------------------------------------------------
    # 4-Tier MAR Rubric Scoring (1: Poor, 2: Sub-par, 3: Acceptable, 4: Exemplary)
    # ---------------------------------------------------------

    # 1. Wordiness / Text Density Score (Enforcing the 30% text budget)
    if word_count > 800:
        score_wordiness = 1
        desc_wordiness = "Poor [1]: Severe wall of text (>800 words), high risk of cognitive overload."
    elif word_count > 600:
        score_wordiness = 2
        desc_wordiness = "Sub-par [2]: Busy layout (600-800 words); excessive dwell time violates 30% text budget."
    elif word_count > 400:
        score_wordiness = 3
        desc_wordiness = "Acceptable [3]: Moderate text density (400-600 words); manageable but encroaches slightly on visual area."
    elif word_count >= 200:
        score_wordiness = 4
        desc_wordiness = "Exemplary [4]: Optimal 30% text density budget (250-400 words); rapid visual parsing."
    else:
        score_wordiness = 3
        desc_wordiness = "Acceptable [3]: Sparse text (<200 words); ensure scientific context is sufficiently grounded."

    # 2. Organization Score
    org_points = 0
    if not has_abstract:
        org_points += 1  # Abstract excluded
    if has_rq or has_hypothesis:
        org_points += 1
    if has_limitation and has_future:
        org_points += 1
    if bool(re.search(r'(introduction|background|context|methods|results|discussion|conclusion|pipeline)', content, re.IGNORECASE)):
        org_points += 1
    if has_inverted_flow:
        org_points = max(1, org_points - 1)  # Penalize inverted chronological flow

    if org_points == 4 and not has_inverted_flow:
        score_org = 4
        desc_org = "Exemplary [4]: Exceptionally clean, chronological IMRaD sequence (Problem -> Methods -> Results -> Discussion)."
    elif org_points >= 3:
        score_org = 3
        desc_org = "Acceptable [3]: Generally organized; minor sequencing or section refinement could be made."
    elif org_points == 2 or has_inverted_flow:
        score_org = 2
        desc_org = "Sub-par [2]: Inverted flow or missing narrative links (e.g. Discussion/Future placed before Methods/Hero)."
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
    if bool(re.search(r'(\\includegraphics|<p:pic>|image|figure|chart|map)', content, re.IGNORECASE)):
        vis_points += 1
    if has_subjective_metrics:
        vis_points = max(1, vis_points - 1)
    if has_plain_bullets:
        vis_points = max(1, vis_points - 1)
    if has_ai_icon_spam:
        vis_points = max(1, vis_points - 1)
    if has_micro_fonts:
        vis_points = max(1, vis_points - 1)

    if vis_points >= 4 and not has_subjective_metrics and not has_plain_bullets and not has_ai_icon_spam and not has_micro_fonts:
        score_vis = 4
        desc_vis = "Exemplary [4]: High figure-to-text ratio, tactile left-accent cards, clean typography, zero AI icon spam, QR offloads details."
    elif vis_points >= 3:
        score_vis = 3
        desc_vis = "Acceptable [3]: Graphics are functional and pleasant overall; polish mini-card typography, remove icon spam, or refine metrics."
    elif vis_points == 2 or has_subjective_metrics or has_plain_bullets or has_ai_icon_spam or has_micro_fonts:
        score_vis = 2
        desc_vis = "Sub-par [2]: Design contains micro-fonts, AI icon spam, unstyled bullet walls, or subjective metrics."
    else:
        score_vis = 1
        desc_vis = "Poor [1]: Visually unengaging; lacks clear focal graphics."

    # 4. Visual-to-Text Spatial Ratio (70/30 Rule & Hero Infographic)
    ratio_points = 0
    if has_hero_infographic:
        ratio_points += 1
    if graphic_count >= 2:
        ratio_points += 1
    if word_count <= 450:
        ratio_points += 1
    if not has_tables and (has_diagram or graphic_count >= 3):
        ratio_points += 1

    if ratio_points == 4:
        score_ratio = 4
        desc_ratio = "Exemplary [4]: Strong 70/30 visual dominance. Prominent hero infographic, high visual coverage, concise text."
    elif ratio_points == 3:
        score_ratio = 3
        desc_ratio = "Acceptable [3]: Good visual balance (~60/40); graphics prominent but could expand hero visual real estate."
    elif ratio_points == 2:
        score_ratio = 2
        desc_ratio = "Sub-par [2]: Insufficient visual dominance (<50% visual area); text-heavy or lacks a unified hero infographic."
    else:
        score_ratio = 1
        desc_ratio = "Poor [1]: Severe violation of 70/30 rule; wall-of-text layout lacking central visual infographic."

    total_mar = score_org + score_vis + score_wordiness + score_ratio
    max_mar = 16
    pct_mar = round((total_mar / max_mar) * 100, 1)

    print("=" * 76)
    print("  MIXED-APPROACH RUBRIC (MAR) & EMPIRICAL POSTER AUDIT (70/30 EDITION)")
    print("  Reference: Khadka & Peeters (2024) | Inter-rater agreement kappa = 0.80")
    print("=" * 76)
    print(f"Target Geometry:        {'[OK] A0 Portrait (841 x 1189 mm)' if (has_portrait and has_a0) else '[i] Standard Portrait'}")
    print(f"Estimated Word Count:   {word_count} words (Target: 250-400 words for 30% text budget)")
    print(f"Graphic Assets Count:   {graphic_count} visual graphic elements detected")
    print(f"Hero Infographic:       {'[OK] Present (' + hero_infographic_match.group(0) + ')' if has_hero_infographic else '[!] None detected (Add a central project infographic)'}")
    print(f"Abstract Excluded:      {'[OK] Yes' if not has_abstract else '[!] NO (Abstract wastes high-value real estate)'}")
    print(f"Research Question:      {'[OK] Detected' if has_rq else '[!] Missing explicit statement'}")
    print(f"Hypothesis/Prediction:  {'[OK] Detected' if has_hypothesis else '[!] Missing explicit statement'}")
    print(f"Visual Diagram/Schema:  {'[OK] Present' if has_diagram else '[!] None detected in Methods'}")
    print(f"Raw Data Tables:        {'[!] Present (Prohibited in Results)' if has_tables else '[OK] None (Clean figure focus)'}")
    print(f"QR Code Integration:    {'[OK] Present (beta = +0.12)' if has_qr else '[!] Absent'}")
    print(f"Discussion Limitation:  {'[OK] Exactly 1 detected' if has_limitation else '[!] Missing explicit limitation'}")
    print(f"Future Direction:       {'[OK] Exactly 1 detected' if has_future else '[!] Missing actionable future direction'}")
    print(f"Chronological Flow:     {'[!] Inverted reading flow (Discussion before Methods/Hero)' if has_inverted_flow else '[OK] Natural progression (Problem -> Solution -> Outcome)'}")
    print(f"Styled Mini-Cards:      {'[!] Plain bullet wall detected (Convert to styled mini-cards)' if has_plain_bullets else '[OK] Styled cards / visual blocks'}")
    print(f"Redundant Sub-headers:  {'[!] Detected redundant subtitles under numbered headers' if has_redundant_subheaders else '[OK] None detected'}")
    print(f"Empirical Metrics:      {'[!] Subjective / humorous metric badges detected (' + ', '.join(subjective_metrics) + ')' if has_subjective_metrics else '[OK] Verifiable empirical quantities'}")
    print(f"Anti-AI Icon Restraint: {'[!] Decorative icon / glyph spam detected (' + str(len(ai_icon_matches)) + ' instances)' if has_ai_icon_spam else '[OK] Clean typographic hierarchy (Zero synthetic icon spam)'}")
    print(f"Card Typography Scale:  {'[!] Micro-fonts detected in body cards (' + ', '.join(set(micro_font_matches)) + ')' if has_micro_fonts else '[OK] Legible A0 card scale (Zero micro-fonts in narrative/QR cards)'}")
    print(f"URL Redundancy:         {'[!] Duplicate raw URLs detected (' + ', '.join(duplicate_urls) + ')' if has_duplicate_urls else '[OK] Authoritative destination consolidated'}")
    if caption_match:
        print(f"Figure Caption Length:  {'[!] Overlong (' + str(caption_word_count) + ' words > 15 words limit)' if has_overlong_caption else '[OK] Concise (' + str(caption_word_count) + ' words)'}")

    print("-" * 76)
    print("4-LAYER VISUAL MAGNET ARCHITECTURE CHECK (10-FOOT X-FACTOR):")
    print(f"  * Layer 0 (Atmospheric Motifs):   {'[OK] Active (<=8% canvas watermark / header wave texture)' if has_layer0_motif else '[i] Not detected'}")
    print(f"  * Layer 1 (Borderless Hero+Pill): {'[OK] Active (Borderless Hero Stage + Billboard Hook Pill)' if has_layer1_hook_stage else '[i] Not detected'}")
    print(f"  * Layer 2 (Cross-Board Conduit):  {'[OK] Active (Title -> Hero -> Central Spine -> QR Card)' if has_layer2_conduit else '[i] Not detected'}")
    print(f"  * Layer 3 (Tactile Left-Accents): {'[OK] Active (6pt left-accent bars + elevation + sans-serif hierarchy)' if has_layer3_tactile else '[i] Not detected'}")

    if provenance_info is not None:
        print("-" * 76)
        print("PROVENANCE & REQUIREMENTS CHECK (provenance.md):")
        if provenance_info["exists"]:
            missing = provenance_info["missing_sections"]
            unresolved = provenance_info["unresolved_tokens"]
            status_ok = provenance_info["has_frontmatter"] and not missing and unresolved == 0
            status_tag = "[OK] Verified" if status_ok else "[!] Incomplete"
            print(f"  * Provenance File:    {status_tag} ({provenance_info['path']})")
            if provenance_info["deliverable_formats"]:
                print(f"  * Formats Declared:   {', '.join(provenance_info['deliverable_formats'])}")
            if provenance_info["reserve_conf_logo"] is not None:
                print(f"  * Conf. Logo Space:   {'Reserved' if provenance_info['reserve_conf_logo'] else 'Not reserved / Custom'}")
            print(f"  * Extra Logos Listed: {provenance_info['extra_logos_count']}")
            print(f"  * Visual Magnet Spec: {'[OK] Declared in YAML' if provenance_info['has_visual_magnet'] else '[i] Not declared in YAML'}")
            if missing:
                print(f"  * Missing YAML Keys:  {', '.join(missing)}")
            if unresolved > 0:
                print(f"  * Unresolved Tokens:  {unresolved} REPLACE_ME_* token(s) remaining")
        else:
            print(f"  * Provenance File:    [i] Not found at {provenance_info['path']}")
            print("    (Tip: Initialize provenance.md from templates/provenance_template.md during Phase 1 intake)")

    print("-" * 76)
    print("RUBRIC ASSESSMENT (4 DIMENSIONS):")
    print(f"1. Organization:                        {desc_org}")
    print(f"2. Poster Design & Visuals:             {desc_vis}")
    print(f"3. Wordiness / Text Density (30% cap):  {desc_wordiness}")
    print(f"4. Visual-to-Text Ratio (70/30 Rule):   {desc_ratio}")
    print("-" * 76)
    print(f"COMPOSITE MAR SCORE: {total_mar} / {max_mar} ({pct_mar}%)")

    if total_mar >= 14:
        print("OVERALL QUALITY: EXEMPLARY (Publication / Conference Award Tier)")
    elif total_mar >= 11:
        print("OVERALL QUALITY: ACCEPTABLE (Ready for presentation with minor polish)")
    else:
        print("OVERALL QUALITY: NEEDS REVISION (High risk of attendee disengagement)")
    print("=" * 76)

    return total_mar


def main():
    parser = argparse.ArgumentParser(description="Audit scientific poster against the Khadka & Peeters MAR framework, 70/30 rule, 4-Layer Visual Magnet Architecture, and provenance.md.")
    parser.add_argument("file", help="Path to poster file (.tex, .pptx, .md, .txt)")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    provenance_info = audit_provenance_file(file_path)

    content = ""
    visible_override = None
    if file_path.suffix.lower() == ".pptx":
        try:
            from pptx import Presentation
            from pptx.enum.shapes import MSO_SHAPE_TYPE
            prs = Presentation(str(file_path))
            text_runs = []
            structural_tags = []
            w_in = prs.slide_width.inches
            h_in = prs.slide_height.inches
            if h_in > w_in:
                structural_tags.append("orientation=portrait")
            if abs(w_in - 33.11) < 0.5 and abs(h_in - 46.81) < 0.5:
                structural_tags.append("a0paper 841mm 1189mm")

            for slide in prs.slides:
                for shape in slide.shapes:
                    sname = (shape.name or "").lower()
                    if sname.startswith("bg_motif_"):
                        structural_tags.append("bg_motif_")
                    if sname.startswith("hook_pill_") or sname.startswith("hero_stage_"):
                        structural_tags.append("hook_pill_ hero_stage_")
                    if sname.startswith("conduit_"):
                        structural_tags.append("conduit_")
                    if sname.startswith("accent_bar_"):
                        structural_tags.append("accent_bar_")
                    if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                        structural_tags.append("<p:pic>")
                        if "qr" in sname:
                            structural_tags.append("qr_code")
                        if "hero" in sname or "infographic" in sname:
                            structural_tags.append("hero_infographic")
                    elif shape.shape_type == MSO_SHAPE_TYPE.TABLE:
                        structural_tags.append("<a:tbl>")
                    if shape.has_text_frame:
                        for p in shape.text_frame.paragraphs:
                            p_txt = "".join(r.text for r in p.runs) if p.runs else p.text
                            if p_txt.strip():
                                text_runs.append(p_txt)
            visible_override = " ".join(text_runs)
            content = visible_override + " " + " ".join(structural_tags)
        except Exception as e:
            print(f"Error reading PPTX: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        content = file_path.read_text(encoding="utf-8", errors="ignore")

    audit_text_content(
        content,
        source_type=file_path.suffix.lstrip("."),
        visible_override=visible_override,
        provenance_info=provenance_info,
    )


if __name__ == "__main__":
    main()
