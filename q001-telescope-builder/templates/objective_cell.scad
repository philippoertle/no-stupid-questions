// Parametric objective cell for round lens.
// Keep retaining pressure very light to avoid lens stress.

$fn = 180;

lens_od = 106.0;
lens_clearance = 0.40;      // radial+diameter fit margin
lens_edge_thickness = 8.0;
cell_wall = 4.0;
cell_back_thickness = 3.0;
retainer_thickness = 2.0;
retainer_overlap = 1.2;      // how much front ring overlaps lens edge
mount_flange_od = 122.0;
mount_flange_thickness = 3.0;

module cell_body() {
    difference() {
        union() {
            cylinder(h=cell_back_thickness + lens_edge_thickness + 1.0, d=lens_od + 2 * (cell_wall + lens_clearance));
            cylinder(h=mount_flange_thickness, d=mount_flange_od);
        }
        // lens seat pocket
        translate([0, 0, cell_back_thickness])
            cylinder(h=lens_edge_thickness + 2.0, d=lens_od + lens_clearance);
    }
}

module retainer_ring() {
    difference() {
        cylinder(h=retainer_thickness, d=lens_od + 2 * (cell_wall + lens_clearance));
        translate([0, 0, -0.5]) cylinder(h=retainer_thickness + 1, d=lens_od - retainer_overlap);
    }
}

// Preview both parts side by side.
translate([-70, 0, 0]) cell_body();
translate([70, 0, 0]) retainer_ring();
