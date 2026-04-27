# Optical artifacts glossary (beginner-friendly)

Short definitions and **examples** for things you often read about when evaluating a telescope visually or in photos. Wording is aimed at **visual** use (eyepiece) and **afocal** phone shots through the eyepiece, like your first-build images.

For how we **score** halo, veiling, ghosts, and detail in the field logs, see [`templates/scoring-cheatsheet.md`](templates/scoring-cheatsheet.md).

---

## Halo

**What it is:** Bright light that spreads **around** a compact bright object (planet, Moon limb, bright star) as a **glow or colored fringe**, wider than the “true” sharp edge of the object.

**Why it happens (common causes):**

- **Chromatic aberration:** different colours focus at slightly different distances; one colour (often blue/violet) forms a fuzzy ring or skirt around the bright core.
- **Spherical aberration / zone errors:** rays from the outer part of the objective do not converge the same way as central rays, so the bright core sits in a broader glow.
- **Defocus:** if best focus is missed, a point source becomes a fuzzy disk with a soft halo.
- **Scattered light:** dust, rough or shiny tube walls, bright edges near the beam can add a diffuse glow (often confused with pure “lens aberration”).

**Example you might say out loud:**  
“Jupiter is a bright disk, but there is a **big soft blue-purple cushion** of light around it that eats contrast near the limb.”

**Not the same as:** a sharp **diffraction ring** pattern from a star at very high magnification (that is a wave-optics effect, usually structured rings, not a vague coloured fog).

---

## Ghost (ghost image / flare spot)

**What it is:** A **secondary bright feature** that is not the real object—often a spot, arc, or smeared copy. It comes from light reflecting **between optical surfaces** (lens–lens, lens–filter, eyepiece elements) or from a bright reflection inside the tube.

**Why it happens:**

- Uncoated or weakly coated surfaces, tilted flats, filter stacks, or sensor/phone glass can create **parasitic reflections**.
- Sometimes the ghost **tracks with the object** when you slew (optical path inside the telescope/eyepiece). Sometimes it stays **fixed in the eyepiece field** while the sky moves (often dirt on the eye lens or a phone reflection).

**Example:**  
“When I move Jupiter across the field, a **faint bright dot** stays in the same relative place on the planet image” → likely an internal reflection path.  
“When I slew and the dot **stays glued to one spot in the eyepiece circle**” → often eyepiece/phone/cornea-related, not the planet.

**Not the same as:** a **satellite trail** (straight line across the frame) or **vignetting** (darkening at the edge of the circular field).

---

## Veil / veiling glare

**What it is:** A **lifted fog** over darker areas of the image: the background or shadowed regions look **greyer or milky** near bright structure, and **fine contrast** is washed out even if you can still “see” large features.

**Why it happens:**

- **Stray light** inside the tube and near the focal region scatters into angles that reach your eye.
- **Poor blackening**, shiny baffle edges, or light leaking around a mask can add a broad low-level haze.
- Strong halos from aberration can also feel like veiling if they are wide enough to overlap nearby dark sky.

**Example:**  
“Along the Moon’s terminator, the shadow side should look black, but it looks **smoky grey** right next to the bright limb.”

**Not the same as:** **halo**, which is usually more **localized around the bright source**; veiling is more about **global or regional contrast loss**.

---

## Detail (what we mean in the scoring sheets)

**What it is:** How much **fine structure** you can resolve and hold steady—craterlets, festoons, rilles, fine cloud bands, split double stars, etc.

**What improves it (conceptually):**

- **Better wavefront** (optics, alignment, appropriate f/# for the object).
- **Stable air (“seeing”)** and a **solid mount**.
- **Appropriate magnification** (not always “more is better”; empty magnification shows a big soft blob).

**What hurts it:**

- Halos, veiling, and ghosts steal contrast and make edges soft.
- **Motion blur** (tracking, hand-held phone).
- **Thermal tube currents** (wavy or boiling detail right after bringing the scope outside).

**Example:**  
“At full aperture I see **big shapes**; when I stop down I lose brightness but **small craters pop**.” That is detail going up while total light goes down.

---

## Quick comparison table

| Term   | Typical look | Main lever to test |
|--------|--------------|--------------------|
| Halo   | Glow or colour skirt around a bright object | Aperture stop, focus, colour filter |
| Ghost  | Extra bright spot/copy not on the real object | Slew test, clean optics, baffles/blackening |
| Veil   | Grey fog over dark areas, low micro-contrast | Tube stray light, baffling, mask leaks |
| Detail | Fineness of structure you can trust | Aperture, seeing, magnification, focus |

---

## Links back into this project

- Image-based discussion: [`aberration-analysis.md`](aberration-analysis.md)
- Field protocols: [`diagnostic-aperture-sweep.md`](diagnostic-aperture-sweep.md), [`diagnostic-baffle-sweep.md`](diagnostic-baffle-sweep.md)
- Index: [`diagnostic-script.md`](diagnostic-script.md)
