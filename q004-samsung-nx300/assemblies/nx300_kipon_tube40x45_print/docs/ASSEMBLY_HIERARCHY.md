# Assembly Hierarchy (NX300 -> Kipon -> Tube40x45)

## A0 - System Assembly

- **A0.1 Camera side**
  - **P-001** Samsung NX300 camera body (purchased)
  - **P-002** Kipon 19556 (Samsung NX -> T2) adapter (purchased)
- **A0.2 Unified print adapter**
  - **A1** One-piece printed adapter (`kipon_to_tube40x45_unified`)
- **A0.3 Telescope side**
  - **P-003** Telescope tube interface (given):
    - Inner diameter: 40 mm
    - Outer diameter: 45 mm
- **A0.4 Fasteners (optional)**
  - **H-001** M3 screw for split clamp tightening (1x)
  - **H-002** M3 hex nut for clamp nut trap (1x)
  - **H-003** M4 radial lock screws for tube side (0-3x, optional)

---

## A1 - Unified Print Adapter Assembly

- **A1.1 Main body / clamp + tube interface (single printed part)**
  - **Part ID:** `PR-001`
  - **CAD source:** `parts/kipon_to_tube40x45_adapter/print/source/kipon_to_tube40x45_unified_cadquery.py`
  - **Exports:**
    - `parts/kipon_to_tube40x45_adapter/print/exports/kipon_to_tube40x45_unified.step`
    - `parts/kipon_to_tube40x45_adapter/print/exports/kipon_to_tube40x45_unified.stl`
    - `parts/kipon_to_tube40x45_adapter/print/exports/kipon_to_tube40x45_unified_drawing.pdf`

- **A1.2 Fit calibration helpers**
  - **Part family ID:** `PR-TEST-00x`
  - **CAD source:** `parts/kipon_fit_test_ring/print/source/t2_kipon_fit_test_ring_cadquery.py`
  - **Variants:**
    - `t2_kipon_fit_test_ring_minus0p20`
    - `t2_kipon_fit_test_ring_minus0p10`
    - `t2_kipon_fit_test_ring_nominal`
    - `t2_kipon_fit_test_ring_plus0p10`
    - `t2_kipon_fit_test_ring_plus0p20`
  - **Drawings:**
    - Combined: `parts/kipon_fit_test_ring/print/exports/t2_kipon_fit_test_ring_drawings.pdf`
    - Individual per variant: `..._drawing.pdf`

---

## Functional Interface Map

- **I-001 (Camera mount):** Samsung NX300 <-> Kipon 19556 (native purchased interface)
- **I-002 (Clamp interface):** Kipon T2-side OD <-> unified adapter split clamp
- **I-003 (Tube insert interface):** unified adapter spigot <-> telescope tube ID 40 mm
- **I-004 (Tube pilot interface):** unified adapter OD pilot <-> telescope tube OD 45 mm seat
- **I-005 (Lock interface, optional):** radial lock screws <-> tube wall contact

---

## Build Order (practical)

1. Print fit-test rings and determine best `kipon_grip_dia` offset.
2. Apply winning offset in `kipon_to_tube40x45_unified_cadquery.py`.
3. Print `kipon_to_tube40x45_unified.stl`.
4. Install M3 clamp hardware.
5. Mount on Kipon and verify clamp preload.
6. Insert into tube40x45 interface and apply optional radial lock screws.
