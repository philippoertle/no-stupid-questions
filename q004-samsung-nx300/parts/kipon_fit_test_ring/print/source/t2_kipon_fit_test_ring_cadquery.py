"""
Quick fit-test ring for Kipon 19556 T2-side clamping diameter.

Purpose:
- Very fast print to calibrate bore fit before full split-clamp print.
- Avoid wasting material/time on full part iterations.

Outputs:
- cad/print/exports/t2_kipon_fit_test_ring_nominal.stl
- cad/print/exports/t2_kipon_fit_test_ring_plus0p10.stl
- cad/print/exports/t2_kipon_fit_test_ring_minus0p10.stl
- cad/print/exports/t2_kipon_fit_test_ring_plus0p20.stl
- cad/print/exports/t2_kipon_fit_test_ring_minus0p20.stl
"""

from pathlib import Path
import cadquery as cq


# Baseline from split-clamp model
baseline_grip_dia = 42.6

# Ring geometry (small + quick print)
outer_dia = 52.0
ring_thickness_z = 4.0

# Add simple grip tabs so ring is easier to handle by hand
tab_len = 8.0
tab_w = 10.0


def build_ring(grip_dia: float) -> cq.Workplane:
    ring = cq.Workplane("XY").circle(outer_dia / 2).extrude(ring_thickness_z)
    ring = ring.faces(">Z").workplane().hole(grip_dia)

    # Two opposite handling tabs
    tab1 = (
        cq.Workplane("XY")
        .center(outer_dia / 2 + tab_len / 2 - 1, 0)
        .rect(tab_len, tab_w)
        .extrude(ring_thickness_z)
    )
    tab2 = (
        cq.Workplane("XY")
        .center(-(outer_dia / 2 + tab_len / 2 - 1), 0)
        .rect(tab_len, tab_w)
        .extrude(ring_thickness_z)
    )
    ring = ring.union(tab1).union(tab2)
    return ring


def export_variant(name: str, grip_dia: float, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    part = build_ring(grip_dia)
    stl_path = out_dir / f"{name}.stl"
    step_path = out_dir / f"{name}.step"
    cq.exporters.export(part, str(stl_path))
    cq.exporters.export(part, str(step_path))
    print(f"Exported: {stl_path}")
    print(f"Exported: {step_path}")


if __name__ == "__main__":
    out = Path(__file__).parent.parent / "exports"
    export_variant("t2_kipon_fit_test_ring_nominal", baseline_grip_dia, out)
    export_variant("t2_kipon_fit_test_ring_plus0p10", baseline_grip_dia + 0.10, out)
    export_variant("t2_kipon_fit_test_ring_minus0p10", baseline_grip_dia - 0.10, out)
    export_variant("t2_kipon_fit_test_ring_plus0p20", baseline_grip_dia + 0.20, out)
    export_variant("t2_kipon_fit_test_ring_minus0p20", baseline_grip_dia - 0.20, out)
