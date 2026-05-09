"""
Generate a one-page manufacturing drawing PDF (English) for CNC quoting.

Output:
  m42_t2_flange_drawing.pdf
"""

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from datetime import date


# Drawing dimensions (mm)
OD = 63.0
THK = 5.0
TAP_BORE = 41.2
REGISTER_DIA = 45.0
REGISTER_DEPTH = 1.0
HOLE_COUNT = 4
HOLE_DIA = 2.4
HOLE_BCD = 54.0
CBORE_DIA = 4.8
CBORE_DEPTH = 1.6

# Title block metadata (edit as needed)
DRAWING_TITLE = "M42x0.75 FLANGE"
DRAWING_NO = "NX300-T2-FLANGE-001"
REVISION = "A"
DRAWN_BY = "philippoertle"
DRAWING_DATE = date.today().strftime("%Y-%m-%d")


def draw_top_view(ax):
    # Outer and center bore
    ax.add_patch(Circle((0, 0), OD / 2, fill=False, linewidth=1.5))
    ax.add_patch(Circle((0, 0), TAP_BORE / 2, fill=False, linewidth=1.2))

    # Mounting holes
    import math
    for i in range(HOLE_COUNT):
        ang = math.radians(i * 360 / HOLE_COUNT)
        x = (HOLE_BCD / 2) * math.cos(ang)
        y = (HOLE_BCD / 2) * math.sin(ang)
        ax.add_patch(Circle((x, y), HOLE_DIA / 2, fill=False, linewidth=1.0))

    ax.set_aspect("equal")
    ax.set_xlim(-40, 40)
    ax.set_ylim(-40, 40)
    ax.set_title("TOP VIEW")
    ax.axis("off")


def draw_section(ax):
    # Simple section block
    ax.add_patch(Rectangle((-OD / 2, -THK / 2), OD, THK, fill=False, linewidth=1.5))
    # Center bore
    ax.add_patch(Rectangle((-TAP_BORE / 2, -THK / 2), TAP_BORE, THK, fill=False, linewidth=1.2))
    # Register step on backside
    ax.add_patch(
        Rectangle(
            (-REGISTER_DIA / 2, -THK / 2),
            REGISTER_DIA,
            REGISTER_DEPTH,
            fill=False,
            linewidth=1.2,
        )
    )

    ax.set_aspect("equal")
    ax.set_xlim(-40, 40)
    ax.set_ylim(-8, 8)
    ax.set_title("SECTION A-A")
    ax.axis("off")


def add_notes(fig):
    notes = f"""
PART: M42x0.75 FLANGE (REPLICA-STYLE, OPEN CAD)
UNITS: mm
MATERIAL: 6061-T6 ALUMINUM (or equivalent)
FINISH: DEBURR, BLACK ANODIZE OPTIONAL

CRITICAL DIMENSIONS:
- OD: {OD:.2f}
- THICKNESS: {THK:.2f}
- CENTER BORE PRE-TAP: {TAP_BORE:.2f} (THREAD AFTER MACHINING)
- INTERNAL THREAD: M42x0.75 THROUGH
- REGISTER: {REGISTER_DIA:.2f} DIA x {REGISTER_DEPTH:.2f} DEEP (BACK SIDE)
- 4X MOUNTING HOLES: {HOLE_DIA:.2f} DIA ON {HOLE_BCD:.2f} BCD
- 4X COUNTERBORE: {CBORE_DIA:.2f} DIA x {CBORE_DEPTH:.2f} DEEP (TOP SIDE)

GENERAL TOLERANCE (UNLESS NOTED): +/-0.10 mm
THREAD TOLERANCE: STANDARD INTERNAL METRIC FOR MATING T2 COMPONENTS
"""
    quote_notes = """
QUOTE / RFQ NOTES (FOR SUPPLIER):
1) MACHINE INTERNAL THREAD M42x0.75 THROUGH (THREAD MILL OR TAP)
2) MAINTAIN COAXIALITY OF THREADED BORE TO OD <= 0.05 mm TIR (TARGET)
3) BREAK SHARP EDGES 0.2-0.5 mm
4) NO BURRS ALLOWED IN THREAD START/EXIT
5) INSPECTION REPORT: CRITICAL DIMS + THREAD GO/NO-GO CHECK
6) DO NOT SUBSTITUTE THREAD PITCH
"""
    fig.text(0.05, 0.02, notes, family="monospace", fontsize=8, va="bottom")
    fig.text(0.56, 0.02, quote_notes, family="monospace", fontsize=8, va="bottom")


def add_title_block(fig):
    # Border box in bottom-right area
    x0, y0, w, h = 0.70, 0.82, 0.27, 0.14
    rect = Rectangle((x0, y0), w, h, transform=fig.transFigure, fill=False, linewidth=1.2)
    fig.patches.append(rect)

    # Internal separators
    fig.lines.append(plt.Line2D([x0, x0 + w], [y0 + h * 0.62, y0 + h * 0.62], transform=fig.transFigure, linewidth=0.8, color="black"))
    fig.lines.append(plt.Line2D([x0, x0 + w], [y0 + h * 0.35, y0 + h * 0.35], transform=fig.transFigure, linewidth=0.8, color="black"))
    # Make right-bottom cell wider so DATE text fits
    split_x = x0 + w * 0.64
    fig.lines.append(plt.Line2D([split_x, split_x], [y0, y0 + h * 0.35], transform=fig.transFigure, linewidth=0.8, color="black"))

    # Text fields
    fig.text(x0 + 0.01, y0 + h * 0.78, f"TITLE: {DRAWING_TITLE}", fontsize=8, family="monospace")
    fig.text(x0 + 0.01, y0 + h * 0.49, f"DWG NO: {DRAWING_NO}", fontsize=8, family="monospace")
    fig.text(x0 + 0.01, y0 + h * 0.18, f"DRAWN BY: {DRAWN_BY}", fontsize=8, family="monospace")
    fig.text(split_x + 0.006, y0 + h * 0.18, f"REV: {REVISION}", fontsize=8, family="monospace")
    fig.text(split_x + 0.006, y0 + h * 0.06, f"DATE: {DRAWING_DATE}", fontsize=7.5, family="monospace")


def main():
    fig = plt.figure(figsize=(11.69, 8.27))  # A4 landscape
    gs = fig.add_gridspec(2, 2, height_ratios=[2, 1], width_ratios=[1, 1])
    ax_top = fig.add_subplot(gs[0, 0])
    ax_sec = fig.add_subplot(gs[0, 1])
    draw_top_view(ax_top)
    draw_section(ax_sec)
    add_notes(fig)
    add_title_block(fig)

    fig.suptitle("MANUFACTURING DRAWING - M42x0.75 FLANGE", fontsize=14, y=0.98)
    out = Path(__file__).parent.parent / "exports" / "m42_t2_flange_drawing.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=300, bbox_inches="tight")
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
