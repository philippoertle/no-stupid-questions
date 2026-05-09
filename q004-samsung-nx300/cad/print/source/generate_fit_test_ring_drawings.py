"""
Generate PDF drawing sheets for fit-test ring variants.

Output:
- cad/print/exports/t2_kipon_fit_test_ring_drawings.pdf
- cad/print/exports/t2_kipon_fit_test_ring_<variant>_drawing.pdf
"""

from pathlib import Path
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Circle, Rectangle


BASELINE = 42.6
VARIANTS = [
    ("minus0p20", BASELINE - 0.20),
    ("minus0p10", BASELINE - 0.10),
    ("nominal", BASELINE),
    ("plus0p10", BASELINE + 0.10),
    ("plus0p20", BASELINE + 0.20),
]

OUTER_DIA = 52.0
THICKNESS = 4.0
TAB_LEN = 8.0
TAB_W = 10.0


def draw_page(name: str, grip_dia: float):
    fig = plt.figure(figsize=(11.69, 8.27))  # A4 landscape
    gs = fig.add_gridspec(2, 2, height_ratios=[2, 1], width_ratios=[1, 1])
    ax_top = fig.add_subplot(gs[0, 0])
    ax_sec = fig.add_subplot(gs[0, 1])

    # Top
    ax_top.add_patch(Circle((0, 0), OUTER_DIA / 2, fill=False, linewidth=1.5))
    ax_top.add_patch(Circle((0, 0), grip_dia / 2, fill=False, linewidth=1.2))
    ax_top.add_patch(Rectangle((OUTER_DIA / 2 - 1, -TAB_W / 2), TAB_LEN, TAB_W, fill=False, linewidth=1.0))
    ax_top.add_patch(Rectangle((-(OUTER_DIA / 2 + TAB_LEN - 1), -TAB_W / 2), TAB_LEN, TAB_W, fill=False, linewidth=1.0))
    ax_top.set_aspect("equal")
    ax_top.set_xlim(-40, 40)
    ax_top.set_ylim(-35, 35)
    ax_top.set_title("TOP VIEW")
    ax_top.axis("off")

    # Section
    ax_sec.add_patch(Rectangle((-OUTER_DIA / 2, -THICKNESS / 2), OUTER_DIA, THICKNESS, fill=False, linewidth=1.5))
    ax_sec.add_patch(Rectangle((-grip_dia / 2, -THICKNESS / 2), grip_dia, THICKNESS, fill=False, linewidth=1.2))
    ax_sec.set_aspect("equal")
    ax_sec.set_xlim(-35, 35)
    ax_sec.set_ylim(-8, 8)
    ax_sec.set_title("SECTION")
    ax_sec.axis("off")

    notes = f"""
FIT-TEST RING VARIANT: {name}
DATE: {date.today().strftime("%Y-%m-%d")}
UNITS: mm

DIMENSIONS:
- OUTER DIA: {OUTER_DIA:.2f}
- THICKNESS: {THICKNESS:.2f}
- BORE (KIPON FIT): {grip_dia:.2f}
- TAB: {TAB_LEN:.2f} x {TAB_W:.2f} (2x)

PRINT:
- 0.2 mm layer
- 3 walls
- 15-20% infill
- PLA
"""
    fig.text(0.05, 0.04, notes, family="monospace", fontsize=9, va="bottom")
    fig.suptitle(f"T2 KIPON FIT-TEST RING - {name}", fontsize=16, y=0.98)
    return fig


def main():
    out_dir = Path(__file__).parent.parent / "exports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "t2_kipon_fit_test_ring_drawings.pdf"
    with PdfPages(out_path) as pdf:
        for name, dia in VARIANTS:
            fig = draw_page(name, dia)
            pdf.savefig(fig, bbox_inches="tight")
            single_out = out_dir / f"t2_kipon_fit_test_ring_{name}_drawing.pdf"
            fig.savefig(single_out, dpi=300, bbox_inches="tight")
            print(f"Saved: {single_out}")
            plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
