# 10-Minute Aberration Diagnostic Script

Use this script to isolate whether the first-build image quality is limited mainly by:

- chromatic/spherical aberration
- focus error
- alignment/decenter/pinch
- eyepiece issues
- smartphone afocal coupling artifacts

This script matches the current build baseline: **`106 mm` clear aperture**, **`900 mm` objective focal length (confirmed)**, 25 mm and 10 mm eyepieces.

## 1) Preparation (2 minutes)

Tools:

- 25 mm eyepiece (start here)
- 10 mm eyepiece (later)
- temporary stop-down mask (70-80 mm clear opening)
- small screwdriver for retaining ring preload check
- phone adapter (if imaging) or handheld phone for comparison

Conditions:

- stable mount
- target: bright star or distant point-like terrestrial light
- allow optics to thermally settle for a few minutes

Record fields for each step:

- visual sharpness score (1-5)
- halo strength (1-5)
- asymmetry direction/shape notes
- phone-vs-eye mismatch (low/medium/high)

## 1.1) Existing Observation to Carry Into This Test

Before running the script, note the already observed behavior:

- `40 mm` front stop strongly reduces halo.
- Full `106 mm` aperture shows strong glow/stray halo.

Use this as a baseline clue that objective edge-ray aberration is likely a major contributor.

## 2) Baseline Focus Pass (2 minutes)

1. Insert `25 mm` eyepiece.
2. Focus by eye only for best sharpness.
3. Capture one phone image through eyepiece.

Interpretation:

- If visual is good but phone is poor: camera coupling is likely dominant.
- If both are poor: continue; primary optical/mechanical issue likely.

## 3) Stop-Down Test (2 minutes)

1. First confirm known `40 mm` mask behavior (sanity check).
2. Then test `60 mm`, `70 mm`, and `80 mm` masks (if available).
2. Re-focus with `25 mm`.
3. Compare to baseline (eye first, then phone).

Pass/fail meaning:

- **Strongly better** (less halo, cleaner edge): geometric aberrations (spherical/chromatic) are dominant.
- **No material change**: focus/alignment/coupling likely dominates.
- **Best compromise at 60-80 mm**: use that range as operational aperture for bright planets.

## 4) Eyepiece Swap and Rotation Test (2 minutes)

1. Switch to `10 mm` eyepiece, refocus carefully.
2. Note whether asymmetry increases.
3. Rotate eyepiece by ~90 degrees and observe whether asymmetry rotates with it.

Interpretation:

- Asymmetry rotates with eyepiece -> eyepiece contribution likely.
- Asymmetry fixed in tube frame -> objective alignment/cell stress contribution likely.

## 5) Mechanical Stress and Centering Check (2 minutes)

1. Lightly loosen retaining ring (no lens rattle, no preload).
2. Verify objective appears centered in cell.
3. Confirm focuser axis points to objective center.
4. Re-run quick focus on 25 mm.

Interpretation:

- Improvement after relieving preload -> pinched/stressed lens was significant.
- No improvement -> likely inherent objective correction limit and/or remaining alignment error.

## 6) Decision Matrix

- **A:** Stop-down helps strongly + color halo persists  
  -> Primary: chromatic + spherical residuals. Keep stopped-down for better visual quality.

- **B:** Visual good, phone bad  
  -> Primary: phone afocal alignment. Use rigid phone adapter and precise centering.

- **C:** Asymmetry fixed to tube, unaffected by eyepiece rotation  
  -> Primary: objective/focuser alignment or lens seating issue.

- **D:** Asymmetry follows eyepiece rotation  
  -> Primary: eyepiece issue.

## 7) Recommended Immediate Actions

1. Operate initially with a stop-down mask in the `60-80 mm` range (pick best compromise from Step 3).
2. Lock best-focus workflow on 25 mm before switching to 10 mm.
3. Keep objective retaining force minimal.
4. Improve focuser-objective axis alignment using shims/jig.
5. For imaging, use a fixed phone adapter and repeatable centering procedure.

## 8) Optional Extension (if you have 10 extra minutes)

- Repeat the same test on a monochromatic/greenish target or with a mild green filter.
- If image quality improves substantially, chromatic aberration is confirmed as a major limitation.
