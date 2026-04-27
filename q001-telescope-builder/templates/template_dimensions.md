# Suggested Template Dimensions

These are first-cut values for a 106/900 refractor.
Update after measuring your actual focuser and tube.

Related files:

- [Main project guide](../README.md)
- [Objective cell template](objective_cell.scad)
- [Baffle ring template](baffle_ring.scad)
- [Focuser drill jig template](focuser_drill_jig.scad)

## Tube Geometry
- Tube length (objective seat to focuser flange): `805.0 mm`
- Tube outer diameter (assumed): `120.0 mm`
- Tube inner diameter (assumed): `116.0 mm`

## Focuser Drill Pattern
- Main focuser hole diameter: `55.0 mm`
- Bolt pattern: 4-hole square centered on focuser axis
- Hole spacing (x and y): `68.0 mm`
- Hole diameter: `4.2 mm`

## Objective Cell
- Lens OD (nominal): `106.0 mm`
- Lens seat diameter: `106.4 mm`
- Lens edge thickness (assumed): `8.0 mm`
- Retaining ring should not preload the lens; use light axial restraint only

## Baffle Rings
- Ring thickness for printing: `2.4 mm`
- Baffle 1: at x=`200.0 mm`, clear diameter >= `84.4 mm`
- Baffle 2: at x=`450.0 mm`, clear diameter >= `55.0 mm`
- Baffle 3: at x=`700.0 mm`, clear diameter >= `25.6 mm`

## 3D Printing Notes
- Material: PETG or ASA preferred
- Perimeters: 4-6
- Infill: 35-50% for structural adapters, 15-25% for jigs
- Print orientation: keep ring/cell faces flat and concentric features in XY plane
