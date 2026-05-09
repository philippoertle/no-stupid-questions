# M42/T2 Flange Replica (Open CAD)

This folder contains parametric open-source CAD models.

## Structure

- `cnc/source/`
  - `m42_t2_flange_replica_cadquery.py`
  - `m42_t2_flange_variant_csk_register_cadquery.py`
  - `generate_manufacturing_drawing.py`
- `cnc/exports/`
  - `m42_t2_flange_replica.step`
  - `m42_t2_flange_replica.stl`
  - `m42_t2_flange_variant_csk_register.step`
  - `m42_t2_flange_variant_csk_register.stl`
  - `m42_t2_flange_drawing.pdf`
- `print/source/` (for home-printer CAD, to be added)
- `print/exports/` (for home-printer mesh/slicer files)

## What this model captures

Based on publicly listed details from S.K. Grimes:
- M42x0.75 ("T-thread/T2") interface
- 63 mm flange outside diameter
- Fits 45 mm opening
- 4 mounting screws

Source:
- https://skgrimes.com/product/flange-42mm-75-pitch/

## Important manufacturing note

The script models a **tap bore** for the internal M42x0.75 thread (`t2_tap_bore_dia`).
For CNC, add this requirement in your quote notes:

- "Please machine internal thread M42x0.75 through center bore (thread-mill or tap)."

This is generally more robust than trying to encode full helical thread geometry in the STEP model.

## Before ordering from Protolabs

The product page does not publish full hole-pattern dimensions, so verify:
- `mount_hole_bcd`
- `mount_hole_dia`
- flange thickness you need

Then upload STEP to Protolabs:
- https://www.protolabs.com/de-de/

## Quick run

1. Install CadQuery (example):
   - `pip install cadquery`
2. From repo root (or any folder):
   - `python q004-samsung-nx300/cad/cnc/source/m42_t2_flange_replica_cadquery.py`
3. Upload generated `.step` file for CNC quote.

## Variant + drawing (next step)

- Variant model (register + counterbore):
  - `python q004-samsung-nx300/cad/cnc/source/m42_t2_flange_variant_csk_register_cadquery.py`
  - Exports:
    - `cnc/exports/m42_t2_flange_variant_csk_register.step`
    - `cnc/exports/m42_t2_flange_variant_csk_register.stl`

- One-page PDF manufacturing drawing:
  - `python q004-samsung-nx300/cad/cnc/source/generate_manufacturing_drawing.py`
  - Exports:
    - `cnc/exports/m42_t2_flange_drawing.pdf`
