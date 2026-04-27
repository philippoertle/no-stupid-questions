#!/usr/bin/env python3
"""
Regenerate diagnostic sweep figures and optionally plot field scores from CSV logs.

From the q001-telescope-builder directory:

    python scripts/plot_diagnostic_sweeps.py

Model-based figures (same as ``python model.py`` sweep step):

    plots/aperture_sweep_physics.png
    plots/baffle_sweep_concept.png

Optional — after filling in numeric columns in the log templates:

    python scripts/plot_diagnostic_sweeps.py --aperture-csv templates/aperture-sweep-log.csv
    python scripts/plot_diagnostic_sweeps.py --baffle-csv templates/baffle-sweep-log.csv
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _parse_float(s: str) -> float | None:
    t = (s or "").strip()
    if not t:
        return None
    try:
        return float(t)
    except ValueError:
        return None


def plot_aperture_scores_csv(csv_path: Path, output_dir: Path) -> Path | None:
    """Scatter / line of halo and detail vs aperture from a filled aperture sweep log."""
    import matplotlib.pyplot as plt

    rows: list[tuple[float, float, float]] = []
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            d = _parse_float(row.get("aperture_mm", "") or "")
            halo = _parse_float(row.get("halo_score_1to5", "") or "")
            detail = _parse_float(row.get("detail_score_1to5", "") or "")
            if d is None or halo is None:
                continue
            rows.append((d, halo, detail if detail is not None else float("nan")))

    if len(rows) < 2:
        print(f"Skipping aperture score plot: need >=2 rows with aperture_mm and halo_score in {csv_path}")
        return None

    rows.sort(key=lambda t: t[0])
    d_v = [r[0] for r in rows]
    h_v = [r[1] for r in rows]
    det_v = [r[2] for r in rows]

    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(d_v, h_v, "o-", color="tab:orange", linewidth=2, markersize=8, label="Halo (1=best)")
    if any(x == x for x in det_v):  # any non-NaN
        ax.plot(d_v, det_v, "s--", color="tab:blue", linewidth=2, markersize=7, label="Detail (5=best)")
    ax.set_xlabel("Stop diameter (mm)")
    ax.set_ylabel("Score (1–5)")
    ax.set_title("Aperture sweep — scores from field log")
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / "aperture_sweep_scores.png"
    fig.savefig(out, dpi=180)
    plt.close(fig)
    return out


def plot_baffle_scores_csv(csv_path: Path, output_dir: Path) -> Path | None:
    """Bar-style summary of veiling and halo by baffle_state from log."""
    import matplotlib.pyplot as plt
    import numpy as np

    by_state: dict[str, list[tuple[float, float]]] = {}
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            state = (row.get("baffle_state") or "").strip()
            if not state:
                continue
            v = _parse_float(row.get("veiling_score_1to5", "") or "")
            h = _parse_float(row.get("halo_score_1to5", "") or "")
            if v is None and h is None:
                continue
            by_state.setdefault(state, []).append(
                (v if v is not None else float("nan"), h if h is not None else float("nan"))
            )

    if len(by_state) < 2:
        print(f"Skipping baffle score plot: need >=2 distinct baffle_state rows with scores in {csv_path}")
        return None

    states = sorted(by_state.keys(), key=lambda s: (len(s), s))
    veil_m = []
    halo_m = []
    for s in states:
        pairs = by_state[s]
        vs = [p[0] for p in pairs if p[0] == p[0]]
        hs = [p[1] for p in pairs if p[1] == p[1]]
        veil_m.append(float(np.nanmean(vs)) if vs else float("nan"))
        halo_m.append(float(np.nanmean(hs)) if hs else float("nan"))

    x = np.arange(len(states))
    w = 0.35
    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.bar(x - w / 2, veil_m, w, label="Veiling (1=best)", color="tab:purple")
    ax.bar(x + w / 2, halo_m, w, label="Halo (1=best)", color="tab:orange")
    ax.set_xticks(x)
    ax.set_xticklabels(states)
    ax.set_ylabel("Mean score (1–5)")
    ax.set_title("Baffle sweep — mean scores by baffle state (from field log)")
    ax.grid(axis="y", alpha=0.25)
    ax.legend()
    fig.tight_layout()
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / "baffle_sweep_scores.png"
    fig.savefig(out, dpi=180)
    plt.close(fig)
    return out


def main() -> int:
    root = _repo_root()
    sys.path.insert(0, str(root))
    from model import TelescopeConfig, TemplateConfig, generate_diagnostic_sweep_plots

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--aperture-csv",
        type=Path,
        help="Filled aperture-sweep log (plots aperture_sweep_scores.png if enough data).",
    )
    parser.add_argument(
        "--baffle-csv",
        type=Path,
        help="Filled baffle-sweep log (plots baffle_sweep_scores.png if enough data).",
    )
    parser.add_argument(
        "--plots-dir",
        type=Path,
        default=root / "plots",
        help="Output directory for PNGs (default: ./plots).",
    )
    args = parser.parse_args()
    plots_dir = args.plots_dir if args.plots_dir.is_absolute() else root / args.plots_dir

    cfg = TelescopeConfig()
    tpl = TemplateConfig()
    paths = generate_diagnostic_sweep_plots(cfg, tpl, plots_dir)
    print("Wrote model-based sweep figures:")
    for p in paths:
        print(f"  {p}")

    if args.aperture_csv:
        p = args.aperture_csv if args.aperture_csv.is_absolute() else root / args.aperture_csv
        extra = plot_aperture_scores_csv(p, plots_dir)
        if extra:
            print(f"  {extra}")

    if args.baffle_csv:
        p = args.baffle_csv if args.baffle_csv.is_absolute() else root / args.baffle_csv
        extra = plot_baffle_scores_csv(p, plots_dir)
        if extra:
            print(f"  {extra}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
