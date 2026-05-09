"""
Parametric replica-style flange for M42x0.75 ("T2") interface.

Goal:
- Open-source CAD source that can be exported to STEP for CNC quoting.
- Geometry follows publicly listed specs from the referenced product page:
  - OD: 63 mm
  - Fits 45 mm opening
  - 4 mounting screws
  - M42x0.75 internal thread (implemented as pre-tap bore + note)

Important:
- This model intentionally uses a pre-tap bore for the T2 female thread.
  In CNC production, call out "tap/thread-mill M42x0.75 internal thread".
- Hole pattern dimensions are not published on that page; defaults are
  reasonable starting values and should be measured/validated before order.
"""

import cadquery as cq
from pathlib import Path


# ----------------------------
# User parameters (millimeters)
# ----------------------------
flange_od = 63.0
flange_thickness = 4.0

# Center opening that fits in host plate/lensboard
center_register_dia = 45.0

# Internal T2 thread target: M42x0.75 female
# For manufacturable CAD, model the pilot bore and specify thread in notes.
t2_major_dia = 42.0
t2_pitch = 0.75
t2_tap_bore_dia = 41.2  # Typical pilot for M42x0.75 internal thread

# Mounting holes
hole_count = 4
mount_hole_dia = 2.4  # #2 clearance approximation (~2.2-2.4 mm)
mount_hole_bcd = 54.0  # Assumed; verify against your mating part

# Optional countersink/counterbore for screw heads
add_counterbore = False
counterbore_dia = 4.5
counterbore_depth = 1.5


def build_flange() -> cq.Workplane:
    # Base disk
    part = cq.Workplane("XY").circle(flange_od / 2.0).extrude(flange_thickness)

    # Central pilot bore for later tapping/thread milling to M42x0.75
    part = part.faces(">Z").workplane().hole(t2_tap_bore_dia)

    # Optional register pocket (if you want a stepped fit into 45 mm opening)
    # Disabled by default: most use-cases only need OD + through bore + screws.
    # Enable by uncommenting if needed:
    # register_depth = 1.0
    # part = (
    #     part.faces("<Z")
    #     .workplane()
    #     .circle(center_register_dia / 2.0)
    #     .cutBlind(-register_depth)
    # )

    # Mounting holes
    wp = part.faces(">Z").workplane()
    wp = wp.polarArray(
        radius=mount_hole_bcd / 2.0,
        startAngle=0.0,
        angle=360.0,
        count=hole_count,
        fill=True,
    )
    if add_counterbore:
        part = wp.cboreHole(
            diameter=mount_hole_dia,
            cboreDiameter=counterbore_dia,
            cboreDepth=counterbore_depth,
        )
    else:
        part = wp.hole(mount_hole_dia)

    return part


def export(part: cq.Workplane, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    step_path = out_dir / "m42_t2_flange_replica.step"
    stl_path = out_dir / "m42_t2_flange_replica.stl"
    cq.exporters.export(part, str(step_path))
    cq.exporters.export(part, str(stl_path))
    print(f"Exported: {step_path}")
    print(f"Exported: {stl_path}")


if __name__ == "__main__":
    model = build_flange()
    export(model, Path(__file__).parent.parent / "exports")
