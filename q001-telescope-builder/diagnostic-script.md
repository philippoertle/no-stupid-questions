# Diagnostic Script Index

The diagnostic protocol is now split into two separate experiments so evidence gathering stays clean:

New to the vocabulary? Read [`optical-artifacts-glossary.md`](optical-artifacts-glossary.md) first.

Model figures for the sweeps (regenerate with `python model.py` or `python scripts/plot_diagnostic_sweeps.py`): [`plots/aperture_sweep_physics.png`](plots/aperture_sweep_physics.png), [`plots/baffle_sweep_concept.png`](plots/baffle_sweep_concept.png). Optional score charts from filled CSV columns: see [`README.md`](README.md) Quick Start (`--aperture-csv` / `--baffle-csv`).

1. [`diagnostic-aperture-sweep.md`](diagnostic-aperture-sweep.md)  
   Isolates aperture-driven effects (marginal-ray chromatic/spherical behavior, halo/detail tradeoff).

2. [`diagnostic-baffle-sweep.md`](diagnostic-baffle-sweep.md)  
   Isolates baffling effects (ghost/veiling suppression) after aperture baseline is established.

Recommended execution order:

1. Run **Script A** first and determine `A_ref` (reference aperture).
2. Run **Script B** using the same target and `A_ref`.
3. Fill the CSV logs:
   - [`templates/aperture-sweep-log.csv`](templates/aperture-sweep-log.csv)
   - [`templates/baffle-sweep-log.csv`](templates/baffle-sweep-log.csv)
4. Update [`aberration-analysis.md`](aberration-analysis.md) with both result tables before revising conclusions.

## Condition control requirement (applies to both scripts)

For interpretable results, keep imaging conditions **near-identical** between compared rows:

- same target class and similar altitude,
- same eyepiece/camera/exposure approach,
- similar transparency and seeing (no step-to-step cloud swings).

If conditions drift, record it in CSV `comments_observations` and treat those rows as lower-confidence.
