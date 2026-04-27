"""
Simple refractor telescope beam-path model.

Assumptions:
- Paraxial ray optics (small angles).
- Objective lens focal length is known.
- Keplerian visual setup: objective + eyepiece.
- Object at infinity for night-sky targets.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import pi
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class TelescopeConfig:
    objective_diameter_mm: float = 106.0
    objective_focal_length_mm: float = 900.0
    # Builder-confirmed: rack focus ±5 cm → 100 mm total travel (see README).
    focuser_travel_mm: float = 100.0
    eyepiece_focal_lengths_mm: tuple[float, ...] = (25.0, 10.0)
    eyepiece_apparent_fov_deg: float = 50.0
    # If unknown, keep this as a best-guess estimate and adjust after measurement.
    focuser_flange_to_field_stop_infocus_mm: float = 70.0
    focus_margin_mm: float = 25.0


@dataclass(frozen=True)
class EyepieceResult:
    eyepiece_focal_length_mm: float
    magnification_x: float
    exit_pupil_mm: float
    true_fov_deg: float


@dataclass(frozen=True)
class BuildGeometry:
    tube_length_mm: float
    target_focus_from_infocus_mm: float
    focus_window_min_mm: float
    focus_window_max_mm: float


@dataclass(frozen=True)
class TemplateConfig:
    # Tube assumptions for printable templates. Update to measured values.
    tube_outer_diameter_mm: float = 120.0
    tube_wall_mm: float = 2.0
    focuser_hole_diameter_mm: float = 55.0
    focuser_mount_hole_spacing_mm: float = 68.0
    focuser_mount_hole_diameter_mm: float = 4.2
    lens_outer_diameter_mm: float = 106.0
    lens_edge_thickness_mm: float = 8.0
    lens_clearance_mm: float = 0.4
    baffle_ring_thickness_mm: float = 2.4


def f_number(cfg: TelescopeConfig) -> float:
    return cfg.objective_focal_length_mm / cfg.objective_diameter_mm


def light_collecting_area_mm2(cfg: TelescopeConfig) -> float:
    radius = cfg.objective_diameter_mm / 2.0
    return pi * radius * radius


def diffraction_limit_arcsec(cfg: TelescopeConfig, wavelength_nm: float = 550.0) -> float:
    """
    Rayleigh criterion, circular aperture.
    theta = 1.22 * lambda / D  [radians]
    Converted to arcseconds.
    """
    wavelength_m = wavelength_nm * 1e-9
    diameter_m = cfg.objective_diameter_mm * 1e-3
    theta_rad = 1.22 * wavelength_m / diameter_m
    return theta_rad * 206265.0


def eyepiece_results(cfg: TelescopeConfig) -> list[EyepieceResult]:
    f_ratio = f_number(cfg)
    results: list[EyepieceResult] = []
    for f_eye in cfg.eyepiece_focal_lengths_mm:
        magnification = cfg.objective_focal_length_mm / f_eye
        exit_pupil = cfg.objective_diameter_mm / magnification
        # Approximation valid for common visual planning.
        true_fov = cfg.eyepiece_apparent_fov_deg / magnification
        # Alternate expression for exit pupil cross-check: f_eye / f_ratio
        assert abs(exit_pupil - (f_eye / f_ratio)) < 1e-9
        results.append(
            EyepieceResult(
                eyepiece_focal_length_mm=f_eye,
                magnification_x=magnification,
                exit_pupil_mm=exit_pupil,
                true_fov_deg=true_fov,
            )
        )
    return results


def estimate_tube_geometry(cfg: TelescopeConfig) -> BuildGeometry:
    """
    Returns a practical first-cut geometry:
    tube_length_mm is objective-seat to focuser-flange.
    """
    tube_length = (
        cfg.objective_focal_length_mm
        - cfg.focuser_flange_to_field_stop_infocus_mm
        - cfg.focus_margin_mm
    )
    # Place nominal infinity focus near middle of travel.
    target_focus = cfg.focuser_travel_mm / 2.0
    return BuildGeometry(
        tube_length_mm=tube_length,
        target_focus_from_infocus_mm=target_focus,
        focus_window_min_mm=0.0,
        focus_window_max_mm=cfg.focuser_travel_mm,
    )


def cone_clear_diameter_mm(
    objective_radius_mm: float, objective_to_point_mm: float, objective_focal_length_mm: float
) -> float:
    """
    Diameter of the converging cone at distance x from objective.
    r(x) = r0 * (1 - x/f)
    """
    if objective_to_point_mm < 0:
        raise ValueError("objective_to_point_mm must be >= 0")
    if objective_to_point_mm > objective_focal_length_mm:
        return 0.0
    radius = objective_radius_mm * (1.0 - objective_to_point_mm / objective_focal_length_mm)
    return max(0.0, 2.0 * radius)


def suggest_baffle_diameters_mm(
    cfg: TelescopeConfig, positions_from_objective_mm: Iterable[float], margin_mm: float = 2.0
) -> list[tuple[float, float]]:
    objective_radius = cfg.objective_diameter_mm / 2.0
    out: list[tuple[float, float]] = []
    for x in positions_from_objective_mm:
        clear_d = cone_clear_diameter_mm(
            objective_radius_mm=objective_radius,
            objective_to_point_mm=x,
            objective_focal_length_mm=cfg.objective_focal_length_mm,
        )
        out.append((x, clear_d + margin_mm))
    return out


def print_report(cfg: TelescopeConfig) -> None:
    print("Telescope Model Report")
    print("======================")
    print(f"Objective diameter:       {cfg.objective_diameter_mm:.1f} mm")
    print(f"Objective focal length:   {cfg.objective_focal_length_mm:.1f} mm")
    print(f"Focuser travel:           {cfg.focuser_travel_mm:.1f} mm")
    print(f"f-number:                 f/{f_number(cfg):.2f}")
    print(f"Light area:               {light_collecting_area_mm2(cfg):.0f} mm^2")
    print(f"Diffraction limit (@550): {diffraction_limit_arcsec(cfg):.2f} arcsec")
    print()

    geom = estimate_tube_geometry(cfg)
    print("First-cut build geometry")
    print("------------------------")
    print(f"Tube length (objective seat to focuser flange): {geom.tube_length_mm:.1f} mm")
    print(
        "Target infinity focus position "
        f"(from fully in): {geom.target_focus_from_infocus_mm:.1f} mm"
    )
    print(f"Focuser range: {geom.focus_window_min_mm:.1f} .. {geom.focus_window_max_mm:.1f} mm")
    print()

    print("Eyepiece performance")
    print("--------------------")
    for row in eyepiece_results(cfg):
        print(
            f"{row.eyepiece_focal_length_mm:>5.1f} mm  "
            f"M={row.magnification_x:>5.1f}x  "
            f"Exit pupil={row.exit_pupil_mm:>4.2f} mm  "
            f"TFOV~{row.true_fov_deg:>4.2f} deg"
        )
    print()

    print("Suggested baffle starting points")
    print("--------------------------------")
    baffles = suggest_baffle_diameters_mm(cfg, positions_from_objective_mm=(200.0, 450.0, 700.0))
    for x, d in baffles:
        print(f"x={x:>6.1f} mm  clear diameter >= {d:>5.1f} mm")


def write_template_dimensions(
    cfg: TelescopeConfig, tpl: TemplateConfig, output_dir: Path
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / "template_dimensions.md"
    geom = estimate_tube_geometry(cfg)
    baffles = suggest_baffle_diameters_mm(cfg, positions_from_objective_mm=(200.0, 450.0, 700.0))
    tube_inner_diameter = tpl.tube_outer_diameter_mm - 2.0 * tpl.tube_wall_mm

    lines = [
        "# Suggested Template Dimensions",
        "",
        "These are first-cut values for a 106/900 refractor.",
        "Update after measuring your actual focuser and tube.",
        "",
        "## Tube Geometry",
        f"- Tube length (objective seat to focuser flange): `{geom.tube_length_mm:.1f} mm`",
        f"- Tube outer diameter (assumed): `{tpl.tube_outer_diameter_mm:.1f} mm`",
        f"- Tube inner diameter (assumed): `{tube_inner_diameter:.1f} mm`",
        "",
        "## Focuser Drill Pattern",
        f"- Main focuser hole diameter: `{tpl.focuser_hole_diameter_mm:.1f} mm`",
        "- Bolt pattern: 4-hole square centered on focuser axis",
        f"- Hole spacing (x and y): `{tpl.focuser_mount_hole_spacing_mm:.1f} mm`",
        f"- Hole diameter: `{tpl.focuser_mount_hole_diameter_mm:.1f} mm`",
        "",
        "## Objective Cell",
        f"- Lens OD (nominal): `{tpl.lens_outer_diameter_mm:.1f} mm`",
        f"- Lens seat diameter: `{tpl.lens_outer_diameter_mm + tpl.lens_clearance_mm:.1f} mm`",
        f"- Lens edge thickness (assumed): `{tpl.lens_edge_thickness_mm:.1f} mm`",
        "- Retaining ring should not preload the lens; use light axial restraint only",
        "",
        "## Baffle Rings",
        f"- Ring thickness for printing: `{tpl.baffle_ring_thickness_mm:.1f} mm`",
    ]
    for i, (x, d) in enumerate(baffles, start=1):
        lines.append(f"- Baffle {i}: at x=`{x:.1f} mm`, clear diameter >= `{d:.1f} mm`")

    lines.extend(
        [
            "",
            "## 3D Printing Notes",
            "- Material: PETG or ASA preferred",
            "- Perimeters: 4-6",
            "- Infill: 35-50% for structural adapters, 15-25% for jigs",
            "- Print orientation: keep ring/cell faces flat and concentric features in XY plane",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def generate_plots(cfg: TelescopeConfig, output_dir: Path) -> list[Path]:
    """
    Generate simple visualization plots for README illustrations.
    """
    import matplotlib.pyplot as plt
    import numpy as np

    output_dir.mkdir(parents=True, exist_ok=True)
    generated: list[Path] = []

    # Plot 1: Objective cone and baffle diameters along optical axis.
    x = np.linspace(0.0, cfg.objective_focal_length_mm, 400)
    radius = (cfg.objective_diameter_mm / 2.0) * (1.0 - x / cfg.objective_focal_length_mm)
    baffle_positions = np.array([200.0, 450.0, 700.0])
    baffles = suggest_baffle_diameters_mm(cfg, baffle_positions.tolist())

    fig1, ax1 = plt.subplots(figsize=(10, 4.8))
    ax1.plot(x, +radius, color="tab:blue", label="Upper marginal ray")
    ax1.plot(x, -radius, color="tab:blue", label="Lower marginal ray")
    for pos, clear_d in baffles:
        r = clear_d / 2.0
        ax1.vlines(pos, -r, +r, color="tab:orange", linewidth=3)
        ax1.text(pos + 8, r + 2, f"{clear_d:.1f} mm", color="tab:orange", fontsize=9)
    ax1.axhline(0.0, color="black", linewidth=0.8)
    ax1.set_title("Converging Objective Cone and Suggested Baffles")
    ax1.set_xlabel("Distance from objective (mm)")
    ax1.set_ylabel("Ray height (mm)")
    ax1.grid(alpha=0.25)
    ax1.legend(loc="upper right")
    fig1.tight_layout()
    p1 = output_dir / "beam_cone_and_baffles.png"
    fig1.savefig(p1, dpi=180)
    plt.close(fig1)
    generated.append(p1)

    # Plot 2: Eyepiece performance bars.
    ep_rows = eyepiece_results(cfg)
    labels = [f"{r.eyepiece_focal_length_mm:.0f} mm" for r in ep_rows]
    mags = [r.magnification_x for r in ep_rows]
    pupils = [r.exit_pupil_mm for r in ep_rows]
    tfovs = [r.true_fov_deg for r in ep_rows]
    idx = np.arange(len(ep_rows))
    w = 0.24

    fig2, ax2 = plt.subplots(figsize=(9, 5))
    ax2.bar(idx - w, mags, w, label="Magnification (x)")
    ax2.bar(idx, pupils, w, label="Exit pupil (mm)")
    ax2.bar(idx + w, tfovs, w, label="TFOV (deg)")
    ax2.set_xticks(idx)
    ax2.set_xticklabels(labels)
    ax2.set_title("Eyepiece Performance at 900 mm Objective Focal Length")
    ax2.set_xlabel("Eyepiece")
    ax2.grid(axis="y", alpha=0.25)
    ax2.legend()
    fig2.tight_layout()
    p2 = output_dir / "eyepiece_performance.png"
    fig2.savefig(p2, dpi=180)
    plt.close(fig2)
    generated.append(p2)

    # Plot 3: Focus budget around focal plane and focuser travel.
    geom = estimate_tube_geometry(cfg)
    fig3, ax3 = plt.subplots(figsize=(9, 2.8))
    ax3.hlines(0.0, 0.0, cfg.focuser_travel_mm, linewidth=8, color="#D5E8D4", label="Focuser travel")
    ax3.vlines(
        geom.target_focus_from_infocus_mm,
        -0.28,
        +0.28,
        linewidth=3,
        color="tab:green",
        label="Target infinity focus",
    )
    ax3.text(
        geom.target_focus_from_infocus_mm + 1.5,
        0.18,
        f"{geom.target_focus_from_infocus_mm:.1f} mm",
        color="tab:green",
    )
    ax3.set_xlim(-2, cfg.focuser_travel_mm + 2)
    ax3.set_ylim(-0.5, 0.5)
    ax3.set_yticks([])
    ax3.set_xlabel("Drawtube position from fully in (mm)")
    ax3.set_title("Focus Budget Placement")
    ax3.grid(axis="x", alpha=0.25)
    ax3.legend(loc="upper right")
    fig3.tight_layout()
    p3 = output_dir / "focus_budget.png"
    fig3.savefig(p3, dpi=180)
    plt.close(fig3)
    generated.append(p3)

    return generated


def generate_template_plots(
    cfg: TelescopeConfig, tpl: TemplateConfig, output_dir: Path
) -> list[Path]:
    """
    Generate graphics to explain printable cut/drill templates.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.patches import Circle, Rectangle

    output_dir.mkdir(parents=True, exist_ok=True)
    generated: list[Path] = []

    geom = estimate_tube_geometry(cfg)
    tube_id = tpl.tube_outer_diameter_mm - 2.0 * tpl.tube_wall_mm
    baffles = suggest_baffle_diameters_mm(cfg, (200.0, 450.0, 700.0))

    # Plot 4: Tube drill/cut layout.
    fig4, ax4 = plt.subplots(figsize=(10.5, 4.8))
    ax4.hlines(0, 0, geom.tube_length_mm, linewidth=10, color="#D9EAD3")
    ax4.vlines(0, -0.25, 0.25, color="black", linewidth=2)
    ax4.text(0, 0.3, "Objective seat", ha="left")
    ax4.vlines(geom.tube_length_mm, -0.25, 0.25, color="black", linewidth=2)
    ax4.text(geom.tube_length_mm, 0.3, "Focuser flange", ha="right")
    for i, (x, d) in enumerate(baffles, start=1):
        ax4.vlines(x, -0.18, 0.18, color="tab:orange", linewidth=3)
        ax4.text(x, -0.32, f"B{i}: {d:.1f} mm", ha="center", color="tab:orange")
    ax4.text(
        geom.tube_length_mm * 0.53,
        0.05,
        f"Tube cut length ~ {geom.tube_length_mm:.1f} mm",
        ha="center",
        fontsize=11,
    )
    ax4.set_title("Tube Cut/Drill Layout (side view)")
    ax4.set_xlabel("Axial position from objective seat (mm)")
    ax4.set_yticks([])
    ax4.set_ylim(-0.45, 0.45)
    ax4.set_xlim(-20, geom.tube_length_mm + 20)
    ax4.grid(axis="x", alpha=0.25)
    fig4.tight_layout()
    p4 = output_dir / "template_tube_layout.png"
    fig4.savefig(p4, dpi=180)
    plt.close(fig4)
    generated.append(p4)

    # Plot 5: Focuser drilling template (end view).
    fig5, ax5 = plt.subplots(figsize=(6.2, 6.2))
    r_tube = tpl.tube_outer_diameter_mm / 2.0
    ax5.add_patch(Circle((0, 0), r_tube, fill=False, linewidth=2, color="black"))
    ax5.add_patch(Circle((0, 0), tpl.focuser_hole_diameter_mm / 2.0, fill=False, linewidth=2, color="tab:blue"))
    hs = tpl.focuser_mount_hole_spacing_mm / 2.0
    holes = [(-hs, -hs), (-hs, hs), (hs, -hs), (hs, hs)]
    for hx, hy in holes:
        ax5.add_patch(
            Circle((hx, hy), tpl.focuser_mount_hole_diameter_mm / 2.0, fill=False, linewidth=2, color="tab:red")
        )
    ax5.axhline(0, color="gray", linewidth=0.8)
    ax5.axvline(0, color="gray", linewidth=0.8)
    ax5.text(0, r_tube + 8, f"Tube OD {tpl.tube_outer_diameter_mm:.1f} mm", ha="center")
    ax5.text(0, -r_tube - 12, f"Main focuser hole {tpl.focuser_hole_diameter_mm:.1f} mm", ha="center", color="tab:blue")
    ax5.set_title("Focuser Drill Template (tube end view)")
    ax5.set_aspect("equal")
    ax5.set_xlim(-r_tube - 20, r_tube + 20)
    ax5.set_ylim(-r_tube - 20, r_tube + 20)
    ax5.set_xticks([])
    ax5.set_yticks([])
    fig5.tight_layout()
    p5 = output_dir / "template_focuser_drill.png"
    fig5.savefig(p5, dpi=180)
    plt.close(fig5)
    generated.append(p5)

    # Plot 6: Printed parts overview.
    fig6, ax6 = plt.subplots(figsize=(10.5, 4.2))
    ax6.add_patch(Rectangle((0, 0), 2.2, 1.2, fill=False, linewidth=2))
    ax6.text(1.1, 0.6, "Objective\nCell", ha="center", va="center")
    x_cursor = 2.7
    for i, (_, d) in enumerate(baffles, start=1):
        width = 1.25
        ax6.add_patch(Rectangle((x_cursor, 0.1), width, 1.0, fill=False, linewidth=2, edgecolor="tab:orange"))
        ax6.text(x_cursor + width / 2.0, 0.6, f"Baffle {i}\nØ{d:.1f}", ha="center", va="center", fontsize=9)
        x_cursor += 1.6
    ax6.add_patch(Rectangle((x_cursor + 0.2, 0), 2.2, 1.2, fill=False, linewidth=2, edgecolor="tab:blue"))
    ax6.text(x_cursor + 1.3, 0.6, "Focuser\nDrill Jig", ha="center", va="center")
    ax6.text(5.2, 1.45, f"Tube ID assumption: {tube_id:.1f} mm", ha="center")
    ax6.set_title("Suggested 3D-Printed Part Set")
    ax6.set_xlim(-0.2, x_cursor + 3.0)
    ax6.set_ylim(-0.2, 1.7)
    ax6.set_xticks([])
    ax6.set_yticks([])
    fig6.tight_layout()
    p6 = output_dir / "template_printed_parts_overview.png"
    fig6.savefig(p6, dpi=180)
    plt.close(fig6)
    generated.append(p6)

    return generated


def generate_diagnostic_sweep_plots(
    cfg: TelescopeConfig,
    tpl: TemplateConfig,
    output_dir: Path,
) -> list[Path]:
    """
    Figures for README / diagnostics: aperture-stop physics and baffle ray concept.

    These are model-based (not from field scores). For plots from filled CSV logs,
    use scripts/plot_diagnostic_sweeps.py.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.patches import Rectangle

    output_dir.mkdir(parents=True, exist_ok=True)
    generated: list[Path] = []

    d_max = cfg.objective_diameter_mm
    f_obj = cfg.objective_focal_length_mm
    d = np.linspace(max(32.0, d_max * 0.32), d_max, 160)
    f_numbers = f_obj / d
    wavelength_m = 550e-9
    theta_arcsec = (1.22 * wavelength_m / (d * 1e-3)) * 206265.0
    relative_flux = (d / d_max) ** 2 * 100.0

    sweep_marks = [40.0, 60.0, 70.0, 80.0, d_max]

    fig_a, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(9, 6.4), sharex=True)
    ax_top.plot(d, f_numbers, color="tab:blue", linewidth=2.0, label="f/# = f_obj / D_stop")
    ax_top.set_ylabel("f-number")
    ax_top.grid(alpha=0.25)
    ax_top.legend(loc="upper right")
    ax_top.set_title("Aperture sweep (model): stop diameter vs speed and diffraction @ 550 nm")

    ax_twin = ax_top.twinx()
    ax_twin.plot(
        d,
        theta_arcsec,
        color="tab:orange",
        linewidth=2.0,
        linestyle="--",
        label="Rayleigh θ (arcsec)",
    )
    ax_twin.set_ylabel("Diffraction scale (arcsec)")
    ax_twin.legend(loc="center right")

    for mark in sweep_marks:
        if mark <= d_max + 1e-6:
            ax_top.axvline(mark, color="gray", linestyle=":", alpha=0.4)

    ax_bot.plot(d, relative_flux, color="tab:green", linewidth=2.0, label="vs full aperture")
    ax_bot.set_xlabel("Stop diameter D_stop (mm)")
    ax_bot.set_ylabel("Relative light grasp (%)")
    ax_bot.set_ylim(0, 105)
    ax_bot.grid(alpha=0.25)
    ax_bot.legend(loc="lower right")
    for mark in sweep_marks:
        if mark <= d_max + 1e-6:
            ax_bot.axvline(mark, color="gray", linestyle=":", alpha=0.4)
    ax_bot.set_title("Relative étendue scales as (D_stop / D_full)²")

    fig_a.tight_layout()
    path_a = output_dir / "aperture_sweep_physics.png"
    fig_a.savefig(path_a, dpi=180)
    plt.close(fig_a)
    generated.append(path_a)

    # Schematic: tube cross-section, on-axis cone vs wall scatter; baffles truncate stray paths.
    fig_b, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(11.0, 4.3))

    def _draw_schematic(ax, with_baffles: bool, title: str) -> None:
        z0, z1 = 0.0, 12.0
        y_lo, y_hi = -1.0, 1.0
        ax.set_xlim(-2.2, 13.0)
        ax.set_ylim(-2.0, 2.5)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.add_patch(
            Rectangle(
                (z0, y_lo),
                z1 - z0,
                y_hi - y_lo,
                facecolor="#EAEAEA",
                edgecolor="black",
                linewidth=1.4,
            )
        )
        ax.plot([z0, z0], [y_lo - 0.2, y_hi + 0.2], color="black", linewidth=4.0)
        ax.text(z0, y_hi + 0.35, "Objective", ha="center", fontsize=9)

        z_focus = 10.0
        h0 = 0.82
        ax.plot([z0, z_focus], [h0, 0.0], color="tab:blue", linewidth=1.8, label="Imaging rays")
        ax.plot([z0, z_focus], [-h0, 0.0], color="tab:blue", linewidth=1.8)
        ax.plot([z_focus, z_focus], [-0.35, 0.35], color="tab:green", linewidth=2.0)
        ax.text(z_focus, y_lo - 0.55, "Image space", ha="center", fontsize=9, color="tab:green")

        if with_baffles:
            ax.add_patch(Rectangle((2.85, 0.32), 0.18, y_hi - 0.32, facecolor="#2A2A2A", edgecolor="black"))
            ax.add_patch(Rectangle((5.85, y_lo), 0.18, 0.42, facecolor="#2A2A2A", edgecolor="black"))
            ax.text(4.5, y_hi + 0.35, "Blackened baffles", ha="center", fontsize=9)

        ax.plot([-1.6, 3.8], [2.05, y_hi], color="tab:red", linestyle="--", linewidth=1.6)
        ax.plot([3.8, 9.2], [y_hi, 0.22], color="tab:red", linestyle="--", linewidth=1.6)
        ax.plot([9.2, z_focus], [0.22, 0.05], color="tab:red", linestyle=":", linewidth=1.2, alpha=0.85)
        ax.text(-1.4, 2.1, "Bright\noff-axis sky", fontsize=8, color="tab:red", va="bottom")

        ax.set_title(title, fontsize=10)

    _draw_schematic(
        ax_l,
        False,
        "Concept: wall scatter adds veiling / ghosts",
    )
    _draw_schematic(
        ax_r,
        True,
        "Concept: baffles intercept non-imaging paths",
    )
    handles, labels = ax_l.get_legend_handles_labels()
    fig_b.legend(handles, labels, loc="lower center", ncol=1, frameon=True)
    tube_id = tpl.tube_outer_diameter_mm - 2.0 * tpl.tube_wall_mm
    fig_b.suptitle(
        "Baffle sweep (ray picture): stray light is tube geometry, not objective glass "
        f"(tube ID ~ {tube_id:.0f} mm in model)",
        fontsize=10,
        y=1.04,
    )
    fig_b.tight_layout()
    path_b = output_dir / "baffle_sweep_concept.png"
    fig_b.savefig(path_b, dpi=180, bbox_inches="tight")
    plt.close(fig_b)
    generated.append(path_b)

    return generated


if __name__ == "__main__":
    cfg = TelescopeConfig()
    tpl = TemplateConfig()
    print_report(cfg)
    try:
        base_dir = Path(__file__).resolve().parent
        output_paths = generate_plots(cfg, base_dir / "plots")
        output_paths.extend(generate_template_plots(cfg, tpl, base_dir / "plots"))
        output_paths.extend(generate_diagnostic_sweep_plots(cfg, tpl, base_dir / "plots"))
        dims_path = write_template_dimensions(cfg, tpl, base_dir / "templates")
        print()
        print("Generated plots")
        print("---------------")
        for p in output_paths:
            print(p)
        print()
        print("Generated template dimensions")
        print("-----------------------------")
        print(dims_path)
    except ImportError as exc:
        print()
        print("Plot generation skipped (missing dependency).")
        print(f"Install matplotlib and numpy to enable plots: {exc}")
