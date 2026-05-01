# Stray-Light Retrofit Plan (Minimal, Testable)

This guide defines a low-risk retrofit sequence to reduce internal reflections and veiling glare in the current refractor tube.

Use it together with:

- [`diagnostic-aperture-sweep.md`](diagnostic-aperture-sweep.md)
- [`diagnostic-baffle-sweep.md`](diagnostic-baffle-sweep.md)
- CSV logs in [`templates/`](templates/)

## Field Photos (current evidence)

### Through-the-tube moon capture (stray-light pattern)

![Through-the-tube moon capture](C:/Users/phili/.cursor/projects/c-Users-phili-git-repos-personal-no-stupid-questions/assets/c__Users_phili_AppData_Roaming_Cursor_User_workspaceStorage_9d19ef6c7afb0c1716cb97fec716a8f4_images_WhatsApp_Image_2026-05-01_at_08.55.01-146e2adb-8616-4a54-959c-c86d7cbf5c1b.png)

### Interior coating spray used

![Spray paint can used for tube interior](C:/Users/phili/.cursor/projects/c-Users-phili-git-repos-personal-no-stupid-questions/assets/c__Users_phili_AppData_Roaming_Cursor_User_workspaceStorage_9d19ef6c7afb0c1716cb97fec716a8f4_images_image-f6cb4ce4-65b8-4d1d-8dec-9a3368610601.png)

---

## Photo Interpretation Update (important context)

Builder clarification: the moon photo was taken with a **60 mm stop** (not full `106 mm` aperture).

Implication for interpretation:

- The image contains both tube stray-light behavior **and** stop-related effects.
- It is **not** a clean full-aperture proof of tube paint quality by itself.

For this telescope (`f_obj = 900 mm`):

- Full aperture mode: `106 mm` -> about `f/8.5`
- Stopped mode: `60 mm` -> about `f/15`

At `60 mm`, outer objective zones are suppressed, so objective-driven halo often drops.  
Residual glow can still come from stop-edge scatter, tube reflectivity, and other internal reflections.

---

## Paint Analysis and Recommendation

### Why generic black spray can still fail

A coating may look black in room light but remain reflective at shallow incidence angles inside a telescope tube.  
For optical internals, low **grazing-angle reflectance** matters more than visual "blackness."

### Recommended interior darkening strategy

1. **Best overall:** flocking material in high-impact zones (near and opposite focuser).
2. **Second layer:** ultra-flat/camouflage matte black paint on remaining interior.
3. **Avoid relying on:** standard acrylic matte sprays as the only mitigation.

### Practical paint classes to prefer

- Ultra-flat camouflage black sprays
- Very low-sheen high-temperature matte blacks (only if verified matte after cure)

### Selection test before repainting tube

On scrap pieces, compare current paint vs candidate paint using a shallow-angle flashlight test:

- lower sheen / fewer specular glints -> better candidate
- if difference is small, prioritize flocking over repainting

---

## 1) Goal and Scope

**Goal:** reduce tube-driven halo/veil/ghost contribution without changing objective optics.

**Not a cure for:** intrinsic objective chromatic/spherical residuals.  
Those remain primarily controlled by aperture choice, focus discipline, and optical alignment.

---

## 2) Success Criteria

A retrofit stage is successful if, at matched conditions:

- veiling score drops,
- halo score drops or shrinks spatially,
- ghost count/brightness drops,
- local contrast near bright lunar/planetary edges improves.

Record evidence in CSV `comments_observations`.

---

## 3) Retrofit Stages (in order)

## Stage 1 — Focuser-side wall suppression (highest impact first)

Target zones:

1. **Opposite-focuser strip** on the inside wall (same axial region as focuser).
2. **Focuser-neighborhood annulus** near the drawtube entry.

Suggested geometry (adjust to actual ID/mechanics):

- Axial length per zone: about `80-180 mm`.
- Strip width: about `1/3` of inner circumference centered opposite focuser.

Preferred material:

- adhesive flocking paper / telescope velvet (best),
- deep-matte fabric/felt (acceptable with caution),
- matte paint only (weakest for grazing incidence).

Checklist:

- [ ] Surfaces cleaned and dry before application
- [ ] No loose edges visible from focuser viewpoint
- [ ] No obstruction of imaging cone

---

## Stage 2 — Baffle edge blackening

Actions:

- Blacken baffle ring edges and any exposed shiny ring faces.
- Remove/gloss-kill reflections from screws, burrs, and adhesive seams visible from focal region.

Checklist:

- [ ] Baffle edges are deep matte (no specular glints under flashlight)
- [ ] No diameter clipping introduced

---

## Stage 3 — Objective-end suppression

Actions:

- Add a short flocked band near objective-side interior.
- Add/extend dew-light shield with matte interior if practical.

Checklist:

- [ ] Objective cell remains stress-free (no pinching from added material)
- [ ] Clear aperture unchanged

---

## 4) Test Protocol After Each Stage

Run one short standardized capture set after each stage:

1. Same target class and similar altitude.
2. Same eyepiece and camera/exposure approach.
3. Same focus method.
4. Similar seeing/transparency (avoid clouds for one stage and clear sky for another).

If conditions drift, mark in `comments_observations` and treat those rows as lower confidence.

### 4-frame A/B mini-protocol (separates aperture vs paint/tube effects)

Capture under near-identical conditions:

1. `106 mm` aperture, **no temporary flocking patch**
2. `106 mm` aperture, **with temporary flocking patch** (near focuser/opposite-focuser region)
3. `60 mm` aperture, **no temporary flocking patch**
4. `60 mm` aperture, **with temporary flocking patch**

Interpretation:

- Improvement in both apertures with flocking -> tube/internal reflectivity is a meaningful contributor.
- Improvement only at one aperture -> likely mixed mechanism (stop geometry + stray-light paths).
- Minimal change with flocking -> prioritize objective/alignment/focus path next.

---

## 5) Quick Logging Table (for notes before CSV entry)

| Stage | Aperture | Eyepiece | Halo (1-5) | Veiling (1-5) | Ghost count | Ghost brightness (1-5) | Detail (1-5) | Comments / observations |
|------|----------|----------|------------|---------------|-------------|-------------------------|--------------|-------------------------|
| Baseline | | | | | | | | |
| Stage 1 | | | | | | | | |
| Stage 2 | | | | | | | | |
| Stage 3 | | | | | | | | |

Then transfer values into:

- [`templates/aperture-sweep-log.csv`](templates/aperture-sweep-log.csv)
- [`templates/baffle-sweep-log.csv`](templates/baffle-sweep-log.csv)

---

## 6) Fast Daylight Screening (optional)

Use a shallow-angle flashlight test inside the tube:

- Strong sheen/specular glints -> surface is still too reflective.
- Uniform dark, low-sheen response -> good suppression.

This is a pre-filter only; night target testing remains the real validation.

---

## 7) Stop Conditions and Escalation

If Stage 1 and Stage 2 produce little change under matched conditions:

1. Re-check objective/focuser alignment and lens stress.
2. Re-check focus procedure repeatability.
3. Re-run aperture sweep to separate objective-limited behavior from tube-limited behavior.
4. Consider objective upgrade path if full-aperture bright-target performance remains unacceptable.

---

## 8) Swiss-Focused Shopping Shortlist (Paint + Flocking)

Prices and stock are snapshots and can change quickly.

### Flocking (first priority)

1. **First Light Optics — Black Velour Flocking (45 cm x 1 m)**
   - URL: <https://www.firstlightoptics.com/misc/black-velour-telescope-flocking-material.html>
   - Price signal: about `GBP 7.50` (roughly `CHF 8-11`, excluding shipping/import handling)
   - Typical status signal: often in stock
   - Role: best first-step material for focuser/opposite-focuser zones

2. **First Light Optics — Protostar Hi-Tack Flocking (1 m roll)**
   - URL: <https://www.firstlightoptics.com/telescope-flocking-material/protostar-self-adhesive-hi-tack-flocking-material-1m-roll.html>
   - Price signal: about `GBP 25.00` (roughly `CHF 28-34`, excluding shipping/import handling)
   - Typical status signal: can have longer lead times / backorder
   - Role: premium flocking option if available

### Ultra-matte black spray (second layer)

3. **Krylon Camouflage Ultra-Flat Black (EU reseller example)**
   - URL: <https://www.armed.eu/en/camouflage-spray-paint-black-krylon/?currency=EUR>
   - Price signal: about `EUR 18.73` (roughly `CHF 18-22`)
   - Note: verify aerosol shipping constraints to Switzerland before ordering
   - Role: paint remaining non-flocked interior areas and edges

4. **RS Switzerland — RS PRO Matt Black Spray 400 ml**
   - URL: <https://ch.rs-online.com/web/p/farbspray/7643039>
   - Price signal: about `CHF 10.55`
   - Role: practical Swiss-local fallback paint

5. **Birrer (Switzerland) — Matt Black Spray**
   - URL: <https://www.birrer-hydraulikshop.ch/en/workshop-supplies/lubrication-technology/31/matt-black-spray-paint.html>
   - Price signal: about `CHF 19.00`
   - Role: Swiss-local matte black option; validate with grazing-angle flashlight test

### Buy order when stock is limited

1. Buy **flocking** first (highest impact).
2. Buy one **ultra-matte spray** for remaining areas and baffle-edge touch-up.
3. If premium flocking is backordered, start with available velour flocking and continue testing.
