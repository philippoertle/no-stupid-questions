"""
Schematic: why visual observing uses an eyepiece and prime-focus imaging does not.

Output: plots/visual_vs_camera_coupling.png
Run from q001-telescope-builder: python scripts/plot_visual_vs_camera_coupling.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "plots" / "visual_vs_camera_coupling.png"
OUT_SVG = ROOT / "plots" / "visual_vs_camera_coupling.svg"


def main() -> None:
    f_obj = 900.0  # mm, Q001 README
    f_eye = 25.0  # mm example Plossl
    theta_moon_deg = 0.52  # approximate lunar diameter

    plt.style.use("seaborn-v0_8-whitegrid")
    fig = plt.figure(figsize=(12.0, 7.8), constrained_layout=True)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.15, 1.0], width_ratios=[1.0, 1.0])

    ax_ray_vis = fig.add_subplot(gs[0, 0])
    ax_ray_cam = fig.add_subplot(gs[0, 1])
    ax_scale = fig.add_subplot(gs[1, :])

    _draw_visual_path(ax_ray_vis, f_obj=f_obj, f_eye=f_eye)
    _draw_camera_path(ax_ray_cam, f_obj)
    _draw_plate_scale_plot(ax_scale, f_obj, theta_moon_deg)

    fig.suptitle(
        "Q001 Kepler refractor (~900 mm): visual needs an eyepiece; camera samples the focal plane",
        fontsize=12,
        fontweight="bold",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=180)
    fig.savefig(OUT_SVG)
    plt.close(fig)
    print(f"Wrote {OUT}")
    print(f"Wrote {OUT_SVG}")


def _draw_visual_path(ax, f_obj: float, f_eye: float) -> None:
    ax.set_title("Manual (visual) observing", fontsize=11, fontweight="bold")
    ax.set_aspect("equal")
    ax.axis("off")

    # Horizontal layout: object rays left -> objective -> focal plane -> eyepiece -> eye right
    z_lens = 0.0
    z_fp = 4.0
    z_eye_lens = 6.2
    z_eye = 8.0

    y0, y1 = 0.35, -0.35
    # Light optical train background band for readability
    ax.add_patch(
        plt.Rectangle((-0.2, -0.5), 6.8, 1.0, facecolor="#eef5ff", edgecolor="none", alpha=0.6)
    )

    # Objective (thin lens symbol)
    ax.plot([z_lens, z_lens], [-0.55, 0.55], "k", lw=2)
    ax.text(z_lens, -0.72, "Objective\n(real image here)", ha="center", fontsize=8)

    # Parallel incoming rays (two-field-angle stylization)
    for y in (y0, 0.0, y1):
        ax.plot([-1.2, z_lens], [y, y], color="#1f77b4", lw=1.2, alpha=0.85)
    ax.text(-1.15, 0.62, "Distant object\n(near-parallel rays)", ha="left", fontsize=8, color="#1f77b4")

    # Converge to intermediate image region at focal plane
    fp_y = 0.0
    for y in (y0, 0.0, y1):
        ax.plot([z_lens, z_fp], [y, fp_y], color="#1f77b4", lw=1.0, alpha=0.85)

    ax.axvline(z_fp, color="#888", linestyle="--", lw=0.9)
    ax.fill_betweenx([-0.12, 0.12], z_fp - 0.06, z_fp + 0.06, color="#ffcc80", alpha=0.5)
    ax.text(z_fp, 0.68, "Intermediate\nreal image\n(small in space)", ha="center", fontsize=8)

    # Diverging to eyepiece (simplified: one zone)
    ax.plot([z_fp, z_eye_lens], [fp_y, 0.25], color="#1f77b4", lw=1.0, alpha=0.85)
    ax.plot([z_fp, z_eye_lens], [fp_y, -0.25], color="#1f77b4", lw=1.0, alpha=0.85)

    ax.plot([z_eye_lens, z_eye_lens], [-0.45, 0.45], "k", lw=2)
    ax.text(z_eye_lens, -0.62, "Eyepiece\n(magnifier)", ha="center", fontsize=8)

    # Exit: nearly parallel to eye
    ax.plot([z_eye_lens, z_eye], [0.25, 0.32], color="#d62728", lw=1.2)
    ax.plot([z_eye_lens, z_eye], [-0.25, -0.32], color="#d62728", lw=1.2)
    ax.add_patch(
        plt.Circle((z_eye, 0.0), 0.22, fill=True, facecolor="#fdd", edgecolor="k", lw=1)
    )
    ax.text(z_eye, 0.0, "Eye", ha="center", va="center", fontsize=8)
    m = f_obj / f_eye
    ax.text(
        z_eye + 0.05,
        -0.62,
        f"Brain needs a large\nangular size on retina\n(example: M ≈ {m:.0f}× for f_eye = {f_eye:.0f} mm)",
        ha="center",
        fontsize=8,
        color="#d62728",
    )

    ax.set_xlim(-1.4, 9.0)
    ax.set_ylim(-0.95, 0.95)
    ax.annotate(
        "",
        xy=(z_lens, -0.86),
        xytext=(z_fp, -0.86),
        arrowprops=dict(arrowstyle="<->", lw=1.1, color="#444"),
    )
    ax.text((z_lens + z_fp) / 2.0, -0.92, f"f_obj (~{f_obj:.0f} mm)", ha="center", va="top", fontsize=8, color="#444")


def _draw_camera_path(ax, f_obj: float) -> None:
    ax.set_title("Camera (prime focus)", fontsize=11, fontweight="bold")
    ax.set_aspect("equal")
    ax.axis("off")

    z_lens = 0.0
    z_fp = 4.0
    z_sensor = 4.35
    y0, y1 = 0.35, -0.35

    ax.add_patch(
        plt.Rectangle((-0.2, -0.5), 4.8, 1.0, facecolor="#eefaf0", edgecolor="none", alpha=0.7)
    )

    ax.plot([z_lens, z_lens], [-0.55, 0.55], "k", lw=2)
    ax.text(z_lens, -0.72, f"Objective\n(f_obj ≈ {f_obj:.0f} mm)", ha="center", fontsize=8)

    for y in (y0, 0.0, y1):
        ax.plot([-1.2, z_lens], [y, y], color="#1f77b4", lw=1.2, alpha=0.85)
    ax.text(-1.15, 0.62, "Same distant object", ha="left", fontsize=8, color="#1f77b4")

    fp_y = 0.0
    for y in (y0, 0.0, y1):
        ax.plot([z_lens, z_fp], [y, fp_y], color="#1f77b4", lw=1.0, alpha=0.85)

    # Sensor chip at focal surface
    chip_h = 0.55
    chip_w = 0.28
    ax.add_patch(
        plt.Rectangle(
            (z_sensor - chip_w / 2, -chip_h / 2),
            chip_w,
            chip_h,
            facecolor="#2ca02c",
            edgecolor="k",
            lw=1.2,
            alpha=0.35,
        )
    )
    ax.axvline(z_fp, color="#888", linestyle="--", lw=0.9)
    ax.text(z_fp + 0.15, 0.72, "Focal plane:\nirradiance vs (x, y)\nrecorded by pixels", ha="left", fontsize=8)

    ax.text(
        z_sensor,
        -0.78,
        "No eyepiece: sensor sits\nwhere the aerial image forms;\nno retinal angle needed.",
        ha="center",
        fontsize=8,
        color="#006400",
    )

    ax.set_xlim(-1.4, 6.5)
    ax.set_ylim(-0.95, 0.95)
    ax.annotate(
        "",
        xy=(z_lens, -0.86),
        xytext=(z_fp, -0.86),
        arrowprops=dict(arrowstyle="<->", lw=1.1, color="#444"),
    )
    ax.text((z_lens + z_fp) / 2.0, -0.92, f"f_obj (~{f_obj:.0f} mm)", ha="center", va="top", fontsize=8, color="#444")


def _draw_plate_scale_plot(ax, f_obj: float, theta_moon_deg: float) -> None:
    ax.set_title(
        "Same physics, different detector: linear scale at the focal plane (example numbers)",
        fontsize=10,
        fontweight="bold",
    )
    theta_rad = np.deg2rad(theta_moon_deg)
    h_mm = f_obj * theta_rad  # small-angle linear extent of full-disk image

    pixels = np.array([3.76, 4.3, 5.5, 7.3])  # µm common classes
    moon_px = h_mm * 1000.0 / pixels

    x = np.arange(len(pixels))
    bars = ax.bar(
        x,
        moon_px,
        color=["#4e79a7", "#f28e2b", "#e15759", "#76b7b2"],
        edgecolor="k",
        linewidth=0.8,
    )
    ax.set_xticks(x)
    ax.set_xticklabels([f"{p:.2f} µm pitch" for p in pixels])
    ax.set_ylabel("Approx. Moon diameter on sensor [pixels]")
    ax.grid(True, axis="y", alpha=0.25)
    ax.set_axisbelow(True)

    for rect, v in zip(bars, moon_px):
        ax.text(
            rect.get_x() + rect.get_width() / 2.0,
            rect.get_height() + 8,
            f"{v:.0f} px",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    ax.text(
        0.02,
        0.97,
        f"Moon ≈ {theta_moon_deg:.2f}° on sky → linear height h ≈ f_obj × θ ≈ {h_mm:.1f} mm at focal plane (f_obj = {f_obj:.0f} mm).\n"
        "The eyepiece does not create detail; it angularly magnifies that pattern for the eye. "
        "The camera counts pixels across the same physical pattern.",
        transform=ax.transAxes,
        va="top",
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor="#ccc", alpha=0.95),
    )


if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print("matplotlib and numpy are required.", file=sys.stderr)
        raise SystemExit(1) from e
