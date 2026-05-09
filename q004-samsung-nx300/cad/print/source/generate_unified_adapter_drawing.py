"""
Detailed drawing for unified one-piece print adapter.

Output:
- cad/print/exports/kipon_to_tube40x45_unified_drawing.pdf
"""

from pathlib import Path
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


OD = 68.0
THK = 8.0
GRIP = 42.6
SPLIT = 3.0
EAR_L = 12.0
EAR_W = 12.0
CLAMP_BOLT = 3.2
NUT_AF = 5.7
TUBE_ID = 40.0
TUBE_OD = 45.0
SPIGOT_D = 39.7
SPIGOT_L = 18.0
PILOT_D = 45.2
PILOT_Z = 2.0
LOCK_D = 3.2
LOCK_N = 3


def draw_top(ax):
    ax.add_patch(Circle((0, 0), OD / 2, fill=False, linewidth=1.5))
    ax.add_patch(Circle((0, 0), GRIP / 2, fill=False, linewidth=1.2))
    x_edge = OD / 2
    y_off = SPLIT / 2 + EAR_W / 2
    ax.add_patch(Rectangle((x_edge, y_off - EAR_W / 2), EAR_L, EAR_W, fill=False, linewidth=1.2))
    ax.add_patch(Rectangle((x_edge, -y_off - EAR_W / 2), EAR_L, EAR_W, fill=False, linewidth=1.2))
    ax.add_patch(Rectangle((-OD / 2 - 2, -SPLIT / 2), OD + EAR_L + 6, SPLIT, fill=False, linewidth=1.0, linestyle="--"))
    ax.set_aspect("equal")
    ax.set_xlim(-45, 55)
    ax.set_ylim(-45, 45)
    ax.set_title("TOP VIEW (KIPON CLAMP SIDE)")
    ax.axis("off")


def draw_section(ax):
    ax.add_patch(Rectangle((-OD / 2, 0), OD, THK, fill=False, linewidth=1.5))
    ax.add_patch(Rectangle((-SPIGOT_D / 2, -SPIGOT_L), SPIGOT_D, SPIGOT_L, fill=False, linewidth=1.2))
    ax.add_patch(Rectangle((-PILOT_D / 2, 0), PILOT_D, -PILOT_Z, fill=False, linewidth=1.0, linestyle="--"))
    ax.add_patch(Rectangle((-16, 0), 32, THK, fill=False, linewidth=1.0))  # clear aperture 32
    ax.set_aspect("equal")
    ax.set_xlim(-45, 45)
    ax.set_ylim(-24, 14)
    ax.set_title("SECTION A-A (ONE-PIECE)")
    ax.axis("off")


def main():
    fig = plt.figure(figsize=(11.69, 8.27))
    gs = fig.add_gridspec(2, 2, height_ratios=[2, 1], width_ratios=[1, 1])
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    draw_top(ax1)
    draw_section(ax2)

    notes_l = f"""
PART: KIPON TO TUBE40x45 UNIFIED ADAPTER (3D PRINT)
UNITS: mm

KEY DIMS:
- Main OD: {OD:.2f}
- Body thickness: {THK:.2f}
- Kipon grip bore: {GRIP:.2f}
- Split gap: {SPLIT:.2f}
- Ear size: {EAR_L:.2f} x {EAR_W:.2f}
- Clamp bolt hole: {CLAMP_BOLT:.2f}
- Nut trap AF: {NUT_AF:.2f}
"""
    notes_r = f"""
TUBE INTERFACE:
- Tube ID target: {TUBE_ID:.2f}
- Tube OD target: {TUBE_OD:.2f}
- Spigot dia: {SPIGOT_D:.2f}
- Spigot length: {SPIGOT_L:.2f}
- OD pilot dia/depth: {PILOT_D:.2f} / {PILOT_Z:.2f}
- Radial lock pilots: {LOCK_N} x {LOCK_D:.2f}

PRINT (ENDER 3 V3, PLA):
- 0.2 mm layer, 5 walls, 50% infill
- Use fit-test ring before full print
"""
    fig.text(0.05, 0.03, notes_l, family="monospace", fontsize=8.5, va="bottom")
    fig.text(0.53, 0.03, notes_r, family="monospace", fontsize=8.5, va="bottom")

    # title block
    x0, y0, w, h = 0.68, 0.82, 0.29, 0.14
    fig.patches.append(Rectangle((x0, y0), w, h, transform=fig.transFigure, fill=False, linewidth=1.2))
    fig.lines.append(plt.Line2D([x0, x0 + w], [y0 + h * 0.62, y0 + h * 0.62], transform=fig.transFigure, linewidth=0.8, color="black"))
    fig.lines.append(plt.Line2D([x0, x0 + w], [y0 + h * 0.35, y0 + h * 0.35], transform=fig.transFigure, linewidth=0.8, color="black"))
    split_x = x0 + w * 0.62
    fig.lines.append(plt.Line2D([split_x, split_x], [y0, y0 + h * 0.35], transform=fig.transFigure, linewidth=0.8, color="black"))
    fig.text(x0 + 0.01, y0 + h * 0.78, "TITLE: UNIFIED KIPON->TUBE40x45", fontsize=8, family="monospace")
    fig.text(x0 + 0.01, y0 + h * 0.49, "DWG NO: NX300-PRINT-UNI-001", fontsize=8, family="monospace")
    fig.text(x0 + 0.01, y0 + h * 0.18, "DRAWN BY: philippoertle", fontsize=8, family="monospace")
    fig.text(split_x + 0.006, y0 + h * 0.18, "REV: A", fontsize=8, family="monospace")
    fig.text(split_x + 0.006, y0 + h * 0.06, f"DATE: {date.today().strftime('%Y-%m-%d')}", fontsize=7.5, family="monospace")

    fig.suptitle("MANUFACTURING DRAWING - UNIFIED PRINT ADAPTER", fontsize=14, y=0.98)
    out = Path(__file__).parent.parent / "exports" / "kipon_to_tube40x45_unified_drawing.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=300, bbox_inches="tight")
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
