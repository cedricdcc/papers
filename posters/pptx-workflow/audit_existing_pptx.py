#!/usr/bin/env python3
"""
Scientific Poster Audit & Layout Analyzer for PowerPoint (.pptx)
Based on Claude Scientific Writer poster standards & best practices.

Inspects an existing .pptx poster file to analyze:
- Physical canvas size & print scale factor (A0, A1, 36x48, etc.)
- Multi-column layout structure and margins
- Typography hierarchy & readability (title, headings, body text)
- Figure placement, aspect ratios, and effective print DPI
- Shape overlaps and whitespace utilization
- Accessibility & contrast guidelines
"""

from __future__ import annotations

import argparse
import io
import json
import math
import sys
import zipfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    from pptx.util import Inches, Pt
    HAS_PYTHON_PPTX = True
except ImportError:
    HAS_PYTHON_PPTX = False

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# Standard poster target dimensions in inches (width, height)
STANDARD_TARGETS = {
    "A0_PORTRAIT": (33.11, 46.81),
    "A0_LANDSCAPE": (46.81, 33.11),
    "A1_PORTRAIT": (23.39, 33.11),
    "A1_LANDSCAPE": (33.11, 23.39),
    "US_36x48_LANDSCAPE": (48.0, 36.0),
    "US_36x48_PORTRAIT": (36.0, 48.0),
    "US_48x36": (48.0, 36.0),
    "US_48x48": (48.0, 48.0),
}


@dataclass
class TextRunInfo:
    text: str
    font_name: Optional[str]
    font_size_pt: Optional[float]
    bold: Optional[bool]


@dataclass
class ShapeInfo:
    id: int
    name: str
    shape_type: str
    left_in: float
    top_in: float
    width_in: float
    height_in: float
    right_in: float
    bottom_in: float
    text_content: str = ""
    font_sizes: List[float] = field(default_factory=list)
    font_names: List[str] = field(default_factory=list)
    image_effective_dpi: Optional[float] = None
    image_pixels: Optional[Tuple[int, int]] = None


@dataclass
class LayoutAuditReport:
    file_path: str
    num_slides: int
    slide_width_in: float
    slide_height_in: float
    slide_width_cm: float
    slide_height_cm: float
    orientation: str
    detected_target: str
    scale_factor: float
    total_shapes: int
    total_words: int
    columns_detected: int
    column_boundaries: List[Dict[str, float]]
    font_inventory: Dict[str, int]
    min_font_size_pt: Optional[float]
    max_font_size_pt: Optional[float]
    images_audited: List[Dict[str, Any]]
    overlaps_detected: List[Dict[str, Any]]
    warnings: List[str]
    recommendations: List[str]
    compliance_score: int  # 0 to 100


def analyze_pptx(pptx_path: Path, target_preset: Optional[str] = None) -> LayoutAuditReport:
    if not pptx_path.exists():
        raise FileNotFoundError(f"File not found: {pptx_path}")

    if not HAS_PYTHON_PPTX:
        raise RuntimeError("python-pptx is required to analyze .pptx files. Run: pip install python-pptx")

    prs = Presentation(str(pptx_path))
    num_slides = len(prs.slides)
    if num_slides == 0:
        raise ValueError("Presentation has no slides.")

    slide_w_in = prs.slide_width.inches
    slide_h_in = prs.slide_height.inches
    slide_w_cm = slide_w_in * 2.54
    slide_h_cm = slide_h_in * 2.54
    orientation = "landscape" if slide_w_in >= slide_h_in else "portrait"

    # Match target
    best_target = "Custom"
    min_diff = float("inf")
    best_scale = 1.0

    for name, (tw, th) in STANDARD_TARGETS.items():
        ratio_slide = slide_w_in / slide_h_in
        ratio_target = tw / th
        if abs(ratio_slide - ratio_target) < 0.05:
            scale = tw / slide_w_in
            diff = abs(ratio_slide - ratio_target)
            if diff < min_diff:
                min_diff = diff
                best_target = name
                best_scale = scale

    slide = prs.slides[0]
    shapes_info: List[ShapeInfo] = []
    total_words = 0
    font_counter: Dict[str, int] = {}
    all_font_sizes: List[float] = []

    # Map image parts to PIL sizes if Pillow is installed
    image_cache: Dict[str, Tuple[int, int]] = {}
    if HAS_PIL:
        try:
            with zipfile.ZipFile(str(pptx_path), "r") as zf:
                for fname in zf.namelist():
                    if fname.startswith("ppt/media/"):
                        try:
                            img_data = zf.read(fname)
                            with Image.open(io.BytesIO(img_data)) as im:
                                image_cache[fname] = im.size
                        except Exception:
                            pass
        except Exception:
            pass

    for idx, shape in enumerate(slide.shapes):
        left = shape.left.inches
        top = shape.top.inches
        width = shape.width.inches
        height = shape.height.inches
        right = left + width
        bottom = top + height

        stype = "OTHER"
        text_str = ""
        fsizes = []
        fnames = []
        dpi = None
        img_px = None

        if shape.has_text_frame:
            stype = "TEXT_BOX"
            for p in shape.text_frame.paragraphs:
                for r in p.runs:
                    txt = r.text.strip()
                    if txt:
                        text_str += txt + " "
                        if r.font.name:
                            fname = r.font.name
                            fnames.append(fname)
                            font_counter[fname] = font_counter.get(fname, 0) + len(txt)
                        if r.font.size:
                            pt = r.font.size.pt
                            fsizes.append(pt)
                            all_font_sizes.append(pt)

        words_in_shape = len(text_str.split())
        total_words += words_in_shape

        if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
            stype = "PICTURE"
            try:
                img_part = shape.image
                blob = img_part.blob
                if HAS_PIL:
                    with Image.open(io.BytesIO(blob)) as im:
                        img_px = im.size
                        if width > 0 and height > 0:
                            dpi_w = img_px[0] / width
                            dpi_h = img_px[1] / height
                            dpi = round(min(dpi_w, dpi_h), 1)
            except Exception:
                pass

        elif shape.shape_type == MSO_SHAPE_TYPE.TABLE:
            stype = "TABLE"
            table = shape.table
            for row in table.rows:
                for cell in row.cells:
                    cell_text = cell.text.strip()
                    if cell_text:
                        text_str += cell_text + " "
                        total_words += len(cell_text.split())

        shapes_info.append(
            ShapeInfo(
                id=idx,
                name=shape.name,
                shape_type=stype,
                left_in=round(left, 2),
                top_in=round(top, 2),
                width_in=round(width, 2),
                height_in=round(height, 2),
                right_in=round(right, 2),
                bottom_in=round(bottom, 2),
                text_content=text_str.strip()[:100],
                font_sizes=fsizes,
                font_names=list(set(fnames)),
                image_effective_dpi=dpi,
                image_pixels=img_px,
            )
        )

    # Detect multi-column structure
    # Header zone is typically top 18-20% of the canvas
    header_threshold = slide_h_in * 0.22
    content_shapes = [s for s in shapes_info if s.top_in >= header_threshold and s.height_in > 1.5]

    columns_detected = 1
    col_boundaries = []
    if content_shapes:
        # Cluster shapes by their X centers
        x_centers = sorted([s.left_in + s.width_in / 2.0 for s in content_shapes])
        # Bin into candidate columns (2, 3, 4)
        for cand_cols in (3, 4, 2):
            col_w = slide_w_in / cand_cols
            bins = [[] for _ in range(cand_cols)]
            for s in content_shapes:
                center = s.left_in + s.width_in / 2.0
                bin_idx = min(cand_cols - 1, int(center / col_w))
                bins[bin_idx].append(s)
            # If all columns have items and width is roughly uniform
            if all(len(b) > 0 for b in bins):
                columns_detected = cand_cols
                for i in range(cand_cols):
                    col_boundaries.append({
                        "column": i + 1,
                        "left_in": round(i * col_w, 2),
                        "right_in": round((i + 1) * col_w, 2),
                        "elements": len(bins[i])
                    })
                break

    # Detect overlaps
    overlaps = []
    for i in range(len(shapes_info)):
        for j in range(i + 1, len(shapes_info)):
            s1 = shapes_info[i]
            s2 = shapes_info[j]
            # Ignore background shapes spanning > 80% width and height
            if (s1.width_in > slide_w_in * 0.8 and s1.height_in > slide_h_in * 0.8) or \
               (s2.width_in > slide_w_in * 0.8 and s2.height_in > slide_h_in * 0.8):
                continue

            # Ignore intentional container-and-child nesting (card background holding text/figures)
            s1_contains_s2 = (s2.left_in >= s1.left_in - 0.15 and s2.right_in <= s1.right_in + 0.15 and
                              s2.top_in >= s1.top_in - 0.15 and s2.bottom_in <= s1.bottom_in + 0.15)
            s2_contains_s1 = (s1.left_in >= s2.left_in - 0.15 and s1.right_in <= s2.right_in + 0.15 and
                              s1.top_in >= s2.top_in - 0.15 and s1.bottom_in <= s2.bottom_in + 0.15)
            if s1_contains_s2 or s2_contains_s1:
                continue

            # Check bounding box collision
            overlap_w = max(0.0, min(s1.right_in, s2.right_in) - max(s1.left_in, s2.left_in))
            overlap_h = max(0.0, min(s1.bottom_in, s2.bottom_in) - max(s1.top_in, s2.top_in))
            if overlap_w > 0.3 and overlap_h > 0.3:
                overlaps.append({
                    "shape_a": f"{s1.name} (#{s1.id})",
                    "shape_b": f"{s2.name} (#{s2.id})",
                    "overlap_width_in": round(overlap_w, 2),
                    "overlap_height_in": round(overlap_h, 2),
                    "types": f"{s1.shape_type} / {s2.shape_type}"
                })

    # Warnings & Recommendations
    warnings = []
    recommendations = []
    compliance_score = 100

    if num_slides > 1:
        warnings.append(f"Presentation has {num_slides} slides. Research posters must be exactly 1 slide.")
        compliance_score -= 20

    min_fs = min(all_font_sizes) if all_font_sizes else None
    max_fs = max(all_font_sizes) if all_font_sizes else None

    # Check font sizes
    if min_fs and min_fs < 18:
        warnings.append(f"Minimum font size is {min_fs:.1f}pt. Text smaller than 20-24pt is unreadable from standard viewing distance (3-6 feet).")
        recommendations.append("Increase body text font sizes to at least 22-26pt.")
        compliance_score -= 15
    elif min_fs and min_fs < 22:
        warnings.append(f"Body font size ({min_fs:.1f}pt) is slightly below the recommended 24pt baseline.")
        compliance_score -= 5

    if max_fs and max_fs < 54:
        warnings.append(f"Title font size ({max_fs:.1f}pt) is small. Major poster titles should be 72-120pt+ for conference readability.")
        recommendations.append("Increase main poster title size to 72pt+ to ensure visibility across the hall.")
        compliance_score -= 10

    # Word count check
    if total_words > 900:
        warnings.append(f"Total word count ({total_words} words) exceeds the recommended poster limit (300-800 words).")
        recommendations.append("Condense dense paragraphs into concise bullet points (3-4 points per block).")
        compliance_score -= 15
    elif total_words < 200:
        warnings.append(f"Total word count ({total_words} words) is quite low. Ensure adequate context and captions are provided.")

    # Image DPI check
    images_audited = []
    for s in shapes_info:
        if s.shape_type == "PICTURE":
            img_item = {
                "name": s.name,
                "placed_width_in": s.width_in,
                "placed_height_in": s.height_in,
                "resolution_px": f"{s.image_pixels[0]}x{s.image_pixels[1]}" if s.image_pixels else "unknown",
                "effective_dpi": s.image_effective_dpi
            }
            images_audited.append(img_item)
            if s.image_effective_dpi and s.image_effective_dpi < 150:
                warnings.append(f"Image '{s.name}' has low effective DPI ({s.image_effective_dpi} DPI). Physical printing requires >= 150-300 DPI.")
                recommendations.append(f"Replace '{s.name}' with a higher-resolution raster (300 DPI) or vector format (SVG/PDF).")
                compliance_score -= 10

    if overlaps:
        warnings.append(f"Detected {len(overlaps)} overlapping shape bounding boxes.")
        recommendations.append("Adjust spacing to eliminate unintentional shape overlaps and maintain clear white space.")
        compliance_score -= min(15, len(overlaps) * 5)

    # Safe margin check (at least 0.5 inches margin on canvas borders)
    margin_violations = [s.name for s in shapes_info if s.left_in < 0.25 or s.top_in < 0.25 or
                         (slide_w_in - s.right_in) < 0.25 or (slide_h_in - s.bottom_in) < 0.25]
    # Filter out whole-slide background rectangles
    margin_violations = [m for m in margin_violations if not any(s.name == m and s.width_in > slide_w_in * 0.9 for s in shapes_info)]
    if margin_violations:
        warnings.append(f"{len(margin_violations)} shapes are dangerously close to the canvas edges (< 0.25 in margin).")
        recommendations.append("Ensure at least 0.75-1.0 inch safe margin inside trim edges to avoid printer cut-off.")
        compliance_score -= 5

    compliance_score = max(0, min(100, compliance_score))

    return LayoutAuditReport(
        file_path=str(pptx_path),
        num_slides=num_slides,
        slide_width_in=round(slide_w_in, 2),
        slide_height_in=round(slide_h_in, 2),
        slide_width_cm=round(slide_w_cm, 2),
        slide_height_cm=round(slide_h_cm, 2),
        orientation=orientation,
        detected_target=best_target,
        scale_factor=round(best_scale, 2),
        total_shapes=len(shapes_info),
        total_words=total_words,
        columns_detected=columns_detected,
        column_boundaries=col_boundaries,
        font_inventory=font_counter,
        min_font_size_pt=min_fs,
        max_font_size_pt=max_fs,
        images_audited=images_audited,
        overlaps_detected=overlaps,
        warnings=warnings,
        recommendations=recommendations,
        compliance_score=compliance_score
    )


def print_report(rep: LayoutAuditReport):
    # Ensure stdout handles unicode if possible, or fall back cleanly
    print("=" * 72)
    print("  SCIENTIFIC POSTER AUDIT & LAYOUT REPORT (.pptx)")
    print("=" * 72)
    print(f"File:        {rep.file_path}")
    status_str = "[OK]" if rep.num_slides == 1 else "[WARN: Multiple slides detected]"
    print(f"Slides:      {rep.num_slides} (Status: {status_str})")
    print(f"Canvas Size: {rep.slide_width_in}\" x {rep.slide_height_in}\" ({rep.slide_width_cm:.1f} x {rep.slide_height_cm:.1f} cm)")
    print(f"Orientation: {rep.orientation.upper()}")
    print(f"Print Target Match: {rep.detected_target} (Scale factor: {rep.scale_factor}x)")
    print("-" * 72)
    print(f"LAYOUT & CONTENT METRICS:")
    print(f"  * Total Shapes / Elements: {rep.total_shapes}")
    print(f"  * Estimated Word Count:   {rep.total_words} words (Target: 300-800)")
    print(f"  * Detected Column Grid:   {rep.columns_detected}-column layout")
    if rep.min_font_size_pt and rep.max_font_size_pt:
        print(f"  * Font Sizes Observed:    {rep.min_font_size_pt:.1f}pt (min) to {rep.max_font_size_pt:.1f}pt (max)")
    print(f"  * Fonts Used:             {', '.join(rep.font_inventory.keys()) if rep.font_inventory else 'Default'}")
    print(f"  * Images Audited:         {len(rep.images_audited)}")

    if rep.images_audited:
        print("\nIMAGE RESOLUTION & DPI:")
        for img in rep.images_audited:
            dpi_str = f"{img['effective_dpi']} DPI" if img['effective_dpi'] else "N/A"
            status = "[OK]" if (img['effective_dpi'] and img['effective_dpi'] >= 150) else "[WARN: Low DPI]"
            print(f"  * {img['name']} ({img['resolution_px']}): {dpi_str} {status}")

    if rep.overlaps_detected:
        print(f"\nOVERLAPPING ELEMENTS ({len(rep.overlaps_detected)}):")
        for ov in rep.overlaps_detected[:5]:
            print(f"  [!] {ov['shape_a']} overlaps with {ov['shape_b']} ({ov['overlap_width_in']}\" x {ov['overlap_height_in']}\")")
        if len(rep.overlaps_detected) > 5:
            print(f"  ... and {len(rep.overlaps_detected) - 5} more.")

    print("\n" + "-" * 72)
    print(f"POSTER QUALITY SCORE: {rep.compliance_score} / 100")
    if rep.warnings:
        print("\nWARNINGS:")
        for w in rep.warnings:
            print(f"  [!] {w}")

    if rep.recommendations:
        print("\nRECOMMENDED ACTIONS:")
        for r in rep.recommendations:
            print(f"  [->] {r}")

    print("=" * 72)


def main():
    parser = argparse.ArgumentParser(description="Audit and validate a scientific PowerPoint poster layout.")
    parser.add_argument("pptx", help="Path to PowerPoint (.pptx) poster file")
    parser.add_argument("--json-out", help="Optional path to write full JSON audit report")
    parser.add_argument("--target", help="Optional target poster size (A0_PORTRAIT, A0_LANDSCAPE, US_36x48_LANDSCAPE, etc.)")
    args = parser.parse_args()

    pptx_path = Path(args.pptx)
    try:
        report = analyze_pptx(pptx_path, target_preset=args.target)
        print_report(report)
        if args.json_out:
            out_p = Path(args.json_out)
            out_p.parent.mkdir(parents=True, exist_ok=True)
            with open(out_p, "w", encoding="utf-8") as f:
                json.dump(asdict(report), f, indent=2)
            print(f"\nSaved JSON audit report to: {out_p}")
        return 0
    except Exception as e:
        print(f"Error analyzing poster: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
