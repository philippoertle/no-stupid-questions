# Diagnostic Script B: Baffle Sweep

Use this script **after** the aperture sweep to test whether baffling improves ghosting/veiling beyond the chosen aperture strategy.

## Prerequisite

Run [`diagnostic-aperture-sweep.md`](diagnostic-aperture-sweep.md) first and choose:

- `A_ref`: reference aperture (usually full `106 mm` and/or best compromise stop, e.g. `70-80 mm`).
- `F_ref`: repeatable best-focus method.

Do not change objective, eyepiece type, or target class while running this script.

## Purpose

- Measure effect of baffling on:
  - ghost spots,
  - veiling glare,
  - local contrast near bright edges.
- Separate what baffling can fix (stray light paths) from what it cannot (intrinsic wavefront/color error).

## Baffle states to test

Define at least these states:

- `B0`: no added baffles (baseline).
- `B1`: first internal baffle set (as currently installed).
- `B2`: improved baffle set (after one geometry/material adjustment).

If you only have one baffle setup, compare `B0` vs `B1`.

## Controls (must remain constant)

- Same target type (planet or lunar limb).
- Same eyepiece (25 mm for primary run).
- Same aperture per run (`A_ref`).
- Same camera/exposure approach if capturing photos.
- Same approximate altitude/time window where practical.
- Optional CSV template: [`templates/baffle-sweep-log.csv`](templates/baffle-sweep-log.csv)
- Optional quick reference: [`templates/scoring-cheatsheet.md`](templates/scoring-cheatsheet.md)

## Scoring scale reference (1-5)

Apply these anchors consistently across baffle states.

### Halo score (lower is better)

- **1:** minimal glow, barely extends past object edge.
- **2:** small compact halo, limited effect on local contrast.
- **3:** moderate halo, clearly visible around target.
- **4:** strong halo, obvious wash into nearby dark regions.
- **5:** severe flare-like halo dominates local field.

Bands:

- **Low:** `1-2`
- **Moderate:** `3`
- **High:** `4-5`

### Veiling score (lower is better)

- **1:** background remains dark; little to no lifted black level.
- **2:** slight background lift near bright structures.
- **3:** moderate haze reduces contrast near high-brightness regions.
- **4:** strong veil across a broad area; local contrast clearly suppressed.
- **5:** heavy veil; fine contrast mostly buried.

Bands:

- **Low veiling:** `1-2`
- **Moderate veiling:** `3`
- **High veiling:** `4-5`

### Ghost brightness score (lower is better)

- **1:** ghost barely detectable.
- **2:** faint but repeatable ghost.
- **3:** clearly visible ghost, not dominant.
- **4:** bright ghost competes with nearby detail.
- **5:** very bright ghost strongly disrupts observation.

Bands:

- **Low ghost brightness:** `1-2`
- **Moderate:** `3`
- **High:** `4-5`

### Detail score (higher is better)

- **1:** only coarse structure visible.
- **2:** low fine-detail recovery.
- **3:** moderate fine detail.
- **4:** good fine detail with stable edge contrast.
- **5:** very high detail, near seeing/tracking limit.

Bands:

- **Low detail:** `1-2`
- **Moderate detail:** `3`
- **High detail:** `4-5`

## Logging table

| Step | Baffle state | Aperture | Halo (1-5) | Veiling (1-5) | Ghost count | Ghost brightness (1-5) | Detail (1-5) | Notes |
|------|--------------|----------|------------|---------------|-------------|-------------------------|--------------|-------|
| B0-1 | B0 | A_ref | | | | | | |
| B1-1 | B1 | A_ref | | | | | | |
| B2-1 | B2 | A_ref | | | | | | |

## Procedure

1. Set aperture to `A_ref`, use 25 mm eyepiece.
2. Test `B0` first:
   - focus with same method as Script A,
   - inspect bright limb/planet for halo, veiling, and ghost spots,
   - record scores and capture one representative frame.
3. Install `B1`, repeat exactly.
4. Install `B2` (if available), repeat exactly.
5. Optional confirmation:
   - run one additional pass at full aperture (`106 mm`) and one at compromise stop to see if baffle effect is aperture-dependent.

## Interpretation

- Veiling and ghost metrics improve, but color fringe/halo core remains:
  - baffling is helping stray-light paths;
  - primary CA/SA still objective-driven.
- Minimal change across baffle states:
  - current issue is dominated by intrinsic objective behavior, focus, or alignment;
  - prioritize optical/mechanical correction before more baffle iteration.
- Improvement only at one aperture:
  - baffle geometry may be clipping or ineffective at other cones; revisit baffle diameters/positions.

## What baffling can and cannot prove

- Can prove reduction of **stray light and ghosting**.
- Cannot prove removal of **chromatic focal shift** or intrinsic spherical residuals.

## Output for analysis

Provide:

- Completed baffle table.
- Completed [`templates/baffle-sweep-log.csv`](templates/baffle-sweep-log.csv) (if used).
- Side-by-side images for `B0` vs best baffle state at same aperture and target.
- One-line conclusion: "baffles improved X (yes/no), strongest effect on Y".

Then update [`aberration-analysis.md`](aberration-analysis.md) with baffle evidence and confidence changes.
