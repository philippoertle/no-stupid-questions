# Field diagnostic script (evidence-aligned)

Use this script so each test **isolates one variable** and you do not repeat work that this build has already ruled out.

**Build baseline (confirmed):** `106 mm` clear aperture (nominal), **`900 mm` objective focal length**, **~`100 mm` total focuser rack travel (±50 mm)**, 25 mm and 10 mm eyepieces.

---

## What this telescope has already demonstrated

Do **not** treat the following as open questions—they are constraints on interpretation:

| Observation | Implication |
|---------------|-------------|
| **40 mm** front mask removes most halo | Marginal-ray **chromatic + spherical** (and related veiling) dominate at full aperture. |
| **40 mm** mask costs a lot of detail / brightness | You are trading resolution and light grasp for wavefront quality; **40 mm is an extreme stop**, not a permanent operating mode. |
| **Baffles not yet tested** (only proposed) | Keep baffling as a **separate experiment** after aperture-sweep results; it may reduce ghosts/veiling but will not correct intrinsic objective wavefront error. |
| **Eyepiece swap** (including microscope eyepiece) little change | **Do not spend the session chasing eyepieces** as the primary fix. |
| **Eye and camera look similar** | Smartphone coupling is **secondary**; optimize **visual** first, then repeat the same checks for imaging if needed. |

Your goal in the field is: **pick the smallest stop that gives acceptable halo**, verify **ghosts**, then **mechanics**—in that order.

**Budget ~25–30 minutes** for Phases A–C plus logging. Add Phase D if something still looks wrong after a sensible stop.

---

## 0) Preparation

**Tools**

- 25 mm eyepiece (always start here; higher power magnifies defects and makes focus harder).
- 10 mm eyepiece (optional; use only after 25 mm baseline is stable).
- **Several** front masks or an adjustable iris: at minimum **full open**, **~80 mm**, **~70 mm**, **~60 mm**, **40 mm** (40 mm is a sanity re-check, not the only comparison).
- Notebook or phone notes: you will log **halo (1–5)** and **detail (1–5)** at each stop.
- Optional: yellow or green planetary filter, small screwdriver for retaining ring check.

**Conditions**

- Stable mount; let the tube cool a few minutes.
- **Targets that actually show your problem:** bright planet **or** Moon near terminator—not only a faint star. Your halo issue is high-contrast driven.
- Same eyepiece and roughly same magnification when comparing stops (keep eyepiece fixed while changing masks).

**Logging (copy this table)**

| Step | Aperture | Halo 1–5 | Detail 1–5 | Ghosts Y/N | Notes |
|------|----------|----------|--------------|--------------|-------|
| A1   | 106 mm   |          |              |              |       |
| B1   | 80 mm    |          |              |              |       |
| B2   | 70 mm    |          |              |              |       |
| B3   | 60 mm    |          |              |              |       |
| B4   | 40 mm    |          |              |              |       |

---

## Phase A — Visual baseline (critical, ~5 min)

**Do this by eye first.** Camera comes later only if you need photos.

1. Full aperture (`106 mm`). Install **25 mm** eyepiece.
2. Point at your high-contrast target (planet or Moon).
3. Rack focus slowly through the **entire** focuser travel. Note **two** best-looking positions if the image “wanders” (color focus split can look like double best focus).
4. Pick the setting that gives the **best compromise** between sharp core and halo (not necessarily absolute minimum halo if the core goes mushy).
5. Record row **A1** in the table (halo, detail, ghosts if any).

**Interpretation**

- If halo is severe at any reasonable focus: proceed to Phase B; stopping down is the main lever for this objective class.
- If you find two distinct “good” focus zones separated along the rack: note it—**longitudinal chromatic** focal shift can present that way in white light.

---

## Phase B — Aperture sweep (critical, ~10–15 min)

**Rule:** after **every** mask change, **re-focus from scratch** (do not trust the previous focus position).

1. Keep **25 mm** eyepiece and the same target.
2. For each clear aperture in order: **106 mm → 80 mm → 70 mm → 60 mm → 40 mm** (skip sizes you do not have; keep order coarse to fine).
3. At each size:
   - re-focus through full travel, pick best compromise again;
   - log halo and detail in the table;
   - note whether **halo drops faster than detail** (ideal) or detail collapses before halo improves (then suspect focus, alignment, or ghosts).

**How to read results**

- **Halo drops strongly between 106 and 70–80 mm** with acceptable detail → adopt **~70–80 mm** as your practical “bright object” operating stop until optics or mechanics are upgraded.
- **Halo only really cleans at 40 mm** → objective residuals are large at the rim; your working stop will be a **strong** compromise until hardware changes.
- **Little change from 106 down to 70 mm** → suspect **gross defocus, alignment, or a loose mask** (light leaks around mask, mask not centered on optical axis).

**Critical mistake to avoid:** using **only** the 40 mm mask as proof “the telescope works” and never testing **60–80 mm**. The project goal is the **smallest** stop that balances halo and detail—not the smallest hole possible.

---

## Phase C — Ghost check (recommended, ~5 min)

Still at a stop where the planet or Moon limb is bright enough to see artifacts (often full aperture or 80 mm).

1. Identify any **secondary bright spot** or smudge away from the real object.
2. **Slew** so the target moves across the field (or rotate the tube in altitude slowly while watching).

**Interpretation**

- Ghost **moves with the target** (stays in the same apparent place on the planet/Moon): likely **objective / eyepiece internal reflection** path—blacken edges, check tilted flats, add baffling near focal region, reduce stray reflections.
- Artifact **stays fixed in the eyepiece field** while the sky moves: often **dust / smudge on eyepiece eye lens or phone lens**, or a **fixed reflection** in the eyepiece; clean optics and retry.

---

## Phase D — Mechanical checks (if Phases B–C are still confusing, ~5 min)

Do this **after** you understand aperture behavior, so you are not chasing mechanics while the dominant issue is full-aperture wavefront error.

1. **Objective retaining ring:** loosen slightly so there is **no pinch** (no deformation pressure on the rim); re-tighten only enough to prevent rattling.
2. **Centering:** objective should look centered in the cell; focuser axis should point at objective center (visual estimate or template).
3. Repeat **Phase A** at full aperture only.

**Interpretation**

- Clear improvement after relieving pinch → **mechanical stress** was a real contributor.
- No change → do not keep iterating cell hardware; return to **stop strategy** and long-term **objective / baffle / coating** improvements.

---

## Phase E — Eyepiece and rotation (optional, low priority for this build)

**Skip unless** you still suspect a bad eyepiece or a specific eyepiece-only artifact.

1. With your best compromise aperture from Phase B, switch **25 mm → 10 mm**, refocus, compare halo/detail.
2. Rotate the eyepiece ~90° in the focuser and see if asymmetric artifacts **rotate with the eyepiece**.

**Interpretation**

- Rotation tracks eyepiece → replace or service that eyepiece.
- No rotation → back to objective / tube train.

Given your prior **eyepiece swap test**, treat this phase as **confirmation only**, not the main diagnostic.

---

## Phase F — Spectral check (optional, ~5 min)

On a bright planet or lunar limb, try a **yellow or green** filter (if available).

- **Strong improvement** in fringe and haze → **chromatic** contribution is major; filters and slower effective f/# help; long-term fix is better color correction in the objective.
- **Little change** → spherical / defocus / ghosts may dominate in that configuration; keep Phase B stop strategy.

---

## Decision summary (after you have filled the table)

| Outcome pattern | Most likely cause | What to do next |
|-----------------|-------------------|-----------------|
| Halo improves a lot from 106 → 70–80 mm, detail still OK | Marginal-ray CA + SA | Operate bright targets at **70–80 mm**; improve mechanics; plan objective/filter upgrades. |
| Halo only clean at 40 mm | Strong rim error or very fast effective beam at full aperture | Use **40 mm** only for demos; otherwise accept heavy stop or upgrade objective. |
| Halo barely changes with mask | Focus, alignment, mask leak, or wrong mask placement | Re-check focus sweep, centered mask, and Phase D. |
| Ghosts move with target | Internal reflections in OTA / eyepiece | Edge blackening, baffle geometry near focus, tilted uncoated surfaces; see `aberration-analysis.md`. |
| Eye vs camera still differ a lot | Imaging path | Rigid adapter, centered exit pupil, exposure not clipping highlights. |

---

## What **not** to do (common time-wasters)

1. **Do not** expect tube baffles alone to remove a **full-aperture colored halo** on Jupiter if Phase B shows strong aperture dependence—that is mostly **objective wavefront + color**, not wall scatter only.
2. **Do not** lock the telescope to **40 mm** as the only “good” configuration without trying **60–80 mm** first.
3. **Do not** spend most of the night swapping eyepieces for this symptom **before** completing Phase B (already de-prioritized by your prior tests).
4. **Do not** compare stops at different magnifications or different targets without noting it—**change one variable at a time**.

---

## Link to deeper write-up

For embedded images, evidence table, and physics discussion, see [`aberration-analysis.md`](aberration-analysis.md).
