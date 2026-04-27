# Diagnostic Script A: Aperture Sweep

Use this script to isolate how much of the halo/veiling problem is driven by **aperture (marginal rays)** versus focus or mechanics.

## Purpose

- Quantify halo/detail tradeoff as aperture changes.
- Choose an operational stop diameter for bright targets (planets, bright lunar limb).
- Produce evidence for later comparison against baffle experiments.

## Build baseline (confirmed)

- Objective: `106 mm` nominal clear aperture, `900 mm` focal length.
- Focuser travel: about `100 mm` total (builder reports ±50 mm).
- Eyepieces: 25 mm and 10 mm.

## Rules for clean evidence

1. Change **one variable at a time** (aperture only in this script).
2. Use **same target** for the whole sweep (planet or Moon terminator).
3. Use **same eyepiece** (25 mm) for the sweep.
4. **Re-focus from scratch after every aperture change**.
5. Log each step before moving on.

## Equipment

- Aperture masks: `106 mm` (open), `80 mm`, `70 mm`, `60 mm`, `40 mm`.
- 25 mm eyepiece (mandatory for sweep), 10 mm optional confirmation.
- Notebook / table for scores.
- Optional: yellow/green filter for extension test.
- Optional CSV template: [`templates/aperture-sweep-log.csv`](templates/aperture-sweep-log.csv)
- Optional quick reference: [`templates/scoring-cheatsheet.md`](templates/scoring-cheatsheet.md)

## Scoring scale reference (1-5)

Use the same interpretation at every step.

### Halo score (lower is better)

- **1 (very low):** only a thin, faint glow close to object edge.
- **2 (low):** visible halo but compact; does not dominate nearby dark sky.
- **3 (medium):** clear halo around object; starts to reduce perceived edge contrast.
- **4 (high):** broad bright halo; dark sky near object is noticeably washed.
- **5 (very high):** dominant glow/flare; object appears embedded in luminous haze.

Interpretation bands:

- **Low halo:** `1-2`
- **Moderate halo:** `3`
- **High halo:** `4-5`

### Detail score (higher is better)

- **1 (very low):** only gross shape visible; fine structure largely lost.
- **2 (low):** coarse detail present; fine edges mostly blurred.
- **3 (medium):** moderate detail; some fine structure visible but unstable/soft.
- **4 (high):** good fine detail with mostly clean edges.
- **5 (very high):** crisp fine structure limited mainly by seeing/tracking.

Interpretation bands:

- **Low detail:** `1-2`
- **Moderate detail:** `3`
- **High detail:** `4-5`

## Logging table

| Step | Aperture | Halo (1-5) | Detail (1-5) | Ghosts (Y/N) | Best focus position note |
|------|----------|------------|--------------|--------------|--------------------------|
| A1 | 106 mm | | | | |
| A2 | 80 mm | | | | |
| A3 | 70 mm | | | | |
| A4 | 60 mm | | | | |
| A5 | 40 mm | | | | |

## Procedure

1. Start full aperture (`106 mm`) on chosen target with `25 mm` eyepiece.
2. Sweep focus over full rack, pick best compromise between core sharpness and halo.
3. Record row A1.
4. Repeat at `80 mm`, then `70 mm`, then `60 mm`, then `40 mm`:
   - install mask,
   - re-focus fully,
   - record one row each.
5. Optional: repeat your best two aperture settings with `10 mm` eyepiece to confirm trend.

## Interpretation

- Halo drops strongly by `70-80 mm` while detail remains acceptable:
  - aperture-driven CA/SA is dominant;
  - use `70-80 mm` as practical bright-target stop.
- Halo only becomes acceptable at `40 mm`:
  - objective rim residuals are strong;
  - expect severe light/detail tradeoff unless optics are upgraded.
- Little improvement even when stopping down:
  - suspect focus method, mask centering/leak, or alignment/pinch.

## Output for analysis

Provide:

- Completed table.
- Completed [`templates/aperture-sweep-log.csv`](templates/aperture-sweep-log.csv) (if used).
- One representative photo at `106 mm`.
- One representative photo at chosen operational stop.
- A one-line conclusion: "best compromise aperture = X mm".

Then run Script B ([`diagnostic-baffle-sweep.md`](diagnostic-baffle-sweep.md)) using this chosen aperture as reference.
