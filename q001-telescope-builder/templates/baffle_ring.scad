// Parametric baffle ring for telescope tube.
// Generate one STL per baffle diameter.

$fn = 180;

tube_id = 116.0;           // tube inner diameter (example)
ring_thickness = 2.4;      // axial thickness
clear_aperture = 55.0;     // set this per baffle location
fit_clearance = 0.35;      // clearance for sliding fit

difference() {
    cylinder(h=ring_thickness, d=tube_id - fit_clearance);
    translate([0, 0, -0.5]) cylinder(h=ring_thickness + 1, d=clear_aperture);
}
