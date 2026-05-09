# Home-print CAD (Ender 3 V3, PLA)

This folder contains print-oriented CAD that avoids fine T2 printed threads.

## Model (current recommended path)

- `source/kipon_to_tube40x45_unified_cadquery.py`
  - One-piece adapter: Kipon split-clamp + tube40x45 interface
  - Exports:
    - `exports/kipon_to_tube40x45_unified.step`
    - `exports/kipon_to_tube40x45_unified.stl`
- `source/generate_unified_adapter_drawing.py`
  - Detailed drawing for the unified one-piece adapter
  - Exports:
    - `exports/kipon_to_tube40x45_unified_drawing.pdf`
- `source/t2_kipon_fit_test_ring_cadquery.py`
  - Quick calibration rings to tune fit on Kipon before full print
  - Exports:
    - `exports/t2_kipon_fit_test_ring_nominal.stl`
    - `exports/t2_kipon_fit_test_ring_plus0p10.stl`
    - `exports/t2_kipon_fit_test_ring_minus0p10.stl`
    - `exports/t2_kipon_fit_test_ring_plus0p20.stl`
    - `exports/t2_kipon_fit_test_ring_minus0p20.stl`
- `source/generate_fit_test_ring_drawings.py`
  - Multi-page PDF drawings for all fit-ring variants
  - Exports:
    - `exports/t2_kipon_fit_test_ring_drawings.pdf`

## Why this works for Ender 3 V3 + PLA

- No M42x0.75 printed internal thread required
- Clamp preload via M3 bolt + nut trap
- Tolerance can be tuned by editing `kipon_grip_dia`

## Suggested print settings (starting point)

- Layer height: 0.20 mm
- Nozzle: 0.4 mm
- Walls/perimeters: 5
- Top/bottom: 6
- Infill: 45-60% (gyroid or cubic)
- Material: PLA (prototype) or PETG (better long-term)
- Orientation: flat on bed (large circular face down)
- Supports: off (typically not required)

## Hardware

- 1x M3 screw (16-20 mm, depending on nut/washer stack)
- 1x M3 hex nut (for nut trap)
- Optional washers

## Tuning

- If fit is too tight: increase `kipon_grip_dia` by +0.2 mm
- If too loose: decrease `kipon_grip_dia` by -0.2 mm
- Reprint a small fit ring first if needed.

### Fast fit-ring workflow

1. Print `t2_kipon_fit_test_ring_nominal.stl` (0.2 mm layer, 3 walls, 15-20% infill).
2. If too tight, try `plus0p20`; if too loose, try `minus0p20`.
3. Copy winning offset into `kipon_grip_dia` in `kipon_to_tube40x45_unified_cadquery.py`.
4. Re-export and print the unified adapter.

## Caution

Prototype-only for initial testing. PLA can creep with heat/load. For final use, prefer CNC metal or at least PETG/nylon with conservative loading.
