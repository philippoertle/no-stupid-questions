// Parametric focuser drill jig for a cylindrical tube.
// Export as STL after adjusting dimensions to your hardware.

$fn = 160;

tube_od = 120.0;
jig_wall = 4.0;
jig_width = 42.0;
split_gap = 2.2;              // opening so clamp can flex
focuser_hole_d = 55.0;
focuser_spacing = 68.0;       // square bolt pattern, center-to-center
focuser_mount_hole_d = 4.2;

module ring_jig() {
    difference() {
        cylinder(h=jig_width, d=tube_od + 2 * jig_wall);
        translate([0, 0, -0.5]) cylinder(h=jig_width + 1, d=tube_od + 0.4);
        // split to allow clamp action
        translate([-split_gap / 2, -(tube_od + 2 * jig_wall), -1])
            cube([split_gap, 2 * (tube_od + 2 * jig_wall), jig_width + 2]);
    }
}

module drill_features() {
    // main focuser aperture
    rotate([90, 0, 0]) cylinder(h=tube_od + 2 * jig_wall + 4, d=focuser_hole_d, center=true);
    // 4 mounting holes
    for (x = [-focuser_spacing / 2, focuser_spacing / 2])
        for (z = [-focuser_spacing / 2, focuser_spacing / 2])
            translate([x, 0, z])
                rotate([90, 0, 0])
                    cylinder(h=tube_od + 2 * jig_wall + 4, d=focuser_mount_hole_d, center=true);
}

difference() {
    ring_jig();
    drill_features();
}
