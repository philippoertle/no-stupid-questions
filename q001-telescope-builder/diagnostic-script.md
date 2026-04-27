# Diagnostic Script Index

The diagnostic protocol is now split into two separate experiments so evidence gathering stays clean:

1. [`diagnostic-aperture-sweep.md`](diagnostic-aperture-sweep.md)  
   Isolates aperture-driven effects (marginal-ray chromatic/spherical behavior, halo/detail tradeoff).

2. [`diagnostic-baffle-sweep.md`](diagnostic-baffle-sweep.md)  
   Isolates baffling effects (ghost/veiling suppression) after aperture baseline is established.

Recommended execution order:

1. Run **Script A** first and determine `A_ref` (reference aperture).
2. Run **Script B** using the same target and `A_ref`.
3. Update [`aberration-analysis.md`](aberration-analysis.md) with both result tables before revising conclusions.
