"""
Unified one-piece adapter (recommended):
- Kipon-side split clamp + tube40x45 interface in one printable component.

Target stack:
Samsung NX300 -> Kipon 19556 -> [THIS ONE-PIECE PRINT] -> Telescope tube (ID 40 / OD 45)
"""

from pathlib import Path
import cadquery as cq


# --- Kipon clamp zone ---
outer_dia = 68.0
body_thickness = 8.0
kipon_grip_dia = 42.6
split_gap = 3.0
ear_length = 12.0
ear_width = 12.0
ear_thickness = 8.0
clamp_bolt_dia = 3.2
nut_trap_af = 5.7
nut_trap_depth = 2.8

# --- Tube interface ---
tube_id = 40.0
tube_od = 45.0
id_fit_clearance = 0.30
od_pilot_clearance = 0.20
insert_len = 18.0
insert_dia = tube_id - id_fit_clearance
pilot_depth = 2.0
pilot_dia = tube_od + od_pilot_clearance

# --- Utility / fastening ---
mount_hole_count = 4
mount_hole_bcd = 54.0
mount_hole_dia = 3.4
add_radial_lock_holes = True
lock_hole_count = 3
lock_hole_dia = 3.2
lock_hole_z = -insert_len * 0.45


def build_part() -> cq.Workplane:
    # Main clamp ring
    part = cq.Workplane("XY").circle(outer_dia / 2).extrude(body_thickness)
    part = part.faces(">Z").workplane().hole(kipon_grip_dia)

    # Clamp ears
    x_edge = outer_dia / 2
    y_off = split_gap / 2 + ear_width / 2
    ear_top = (
        cq.Workplane("XY")
        .center(x_edge + ear_length / 2, y_off)
        .rect(ear_length, ear_width)
        .extrude(ear_thickness)
    )
    ear_bot = (
        cq.Workplane("XY")
        .center(x_edge + ear_length / 2, -y_off)
        .rect(ear_length, ear_width)
        .extrude(ear_thickness)
    )
    part = part.union(ear_top).union(ear_bot)

    # Split slot
    slot_len = outer_dia + ear_length + 4
    part = (
        part.faces(">Z")
        .workplane()
        .center(x_edge / 2 + ear_length / 2, 0)
        .rect(slot_len, split_gap)
        .cutBlind(-ear_thickness - 1)
    )

    # Clamp bolt + nut trap
    bolt_z = ear_thickness / 2
    bolt_x = x_edge + ear_length / 2
    bolt_cut = (
        cq.Workplane("XZ")
        .center(bolt_x, bolt_z)
        .circle(clamp_bolt_dia / 2)
        .extrude(2 * (ear_width + split_gap), both=True)
    )
    part = part.cut(bolt_cut)
    nut_vertex_dia = nut_trap_af / 0.8660254
    nut_start_y = -(split_gap / 2 + ear_width)
    nut_cut = (
        cq.Workplane("XZ")
        .transformed(offset=(0, nut_start_y, 0))
        .center(bolt_x, bolt_z)
        .polygon(6, nut_vertex_dia)
        .extrude(nut_trap_depth + 0.2)
    )
    part = part.cut(nut_cut)

    # Tube OD pilot pocket
    part = (
        part.faces("<Z")
        .workplane()
        .circle(pilot_dia / 2)
        .cutBlind(-pilot_depth)
    )

    # Tube ID insert spigot
    spigot = (
        cq.Workplane("XY")
        .circle(insert_dia / 2)
        .extrude(insert_len)
        .translate((0, 0, -insert_len))
    )
    part = part.union(spigot)

    # Through aperture
    clear_aperture = 32.0
    part = part.faces(">Z").workplane().hole(clear_aperture)

    # Mount holes (kept for optional future compatibility/jigging)
    part = (
        part.faces(">Z")
        .workplane()
        .polarArray(radius=mount_hole_bcd / 2, startAngle=45, angle=360, count=mount_hole_count, fill=True)
        .hole(mount_hole_dia)
    )

    # Optional radial lock screw pilots
    if add_radial_lock_holes:
        for i in range(lock_hole_count):
            cutter = (
                cq.Workplane("YZ")
                .center(0, lock_hole_z)
                .circle(lock_hole_dia / 2)
                .extrude(outer_dia, both=True)
                .rotate((0, 0, 0), (0, 0, 1), i * 360 / lock_hole_count)
            )
            part = part.cut(cutter)

    return part


def export(part: cq.Workplane, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    step_path = out_dir / "kipon_to_tube40x45_unified.step"
    stl_path = out_dir / "kipon_to_tube40x45_unified.stl"
    cq.exporters.export(part, str(step_path))
    cq.exporters.export(part, str(stl_path))
    print(f"Exported: {step_path}")
    print(f"Exported: {stl_path}")


if __name__ == "__main__":
    model = build_part()
    export(model, Path(__file__).parent.parent / "exports")
