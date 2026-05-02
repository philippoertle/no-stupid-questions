# Comparison Report: Current Telescope Eyepieces vs BRESSER MikrOkular LF

## Executive summary (Moon and planets)

For this specific comparison set, the eyepiece most suited to Moon and planet visual observing is:

1. **Plossl 10 mm (current eyepiece)** - best of the listed options for planetary-scale visual magnification (`90x`) on your `900 mm` scope.
2. **Plossl 25 mm (current eyepiece)** - useful for wide lunar framing and target acquisition, but usually too low magnification for fine planetary detail (`36x`).
3. **BRESSER MikrOkular LF** - not a visual telescope eyepiece; this is a microscope camera module and therefore not the right replacement for eyepiece-based Moon/planet observing.

Bottom line: for visual Moon/planet work in this report, keep using the `10 mm` eyepiece as the primary choice.

This report is rebuilt from scratch for the specific proposed product:

- `https://www.bresser.com/p/bresser-mikrokular-lf-full-hd-microscope-eyepiece-camera-refurbished-R5913800`

## 1) Recommendation

For the Q001 telescope as currently configured, the **BRESSER MikrOkular LF is not a better eyepiece choice** because it is **not a telescope eyepiece**. It is a **microscope camera module** intended to replace a microscope eyepiece or mount in a microscope photo tube.

Decision:

- **Do not buy it as an eyepiece replacement** for visual observing.
- Consider it only as an experimental camera module if you explicitly want a custom mechanical adaptation project.

## 2) Q001 baseline (current setup)

From `README.md`:

- Telescope: Kepler refractor
- Objective: `f_obj = 900 mm`, `D = 106 mm` (nominal)
- Focal ratio: `f/# = 900 / 106 ~= 8.5`
- Current eyepieces: `1.25"` Plossl `25 mm` and `10 mm` (~50 deg AFOV)

Visual equations:

- `M = f_obj / f_eye`
- `D_exit = D / M = f_eye / (f/#)`
- `TFOV ~= AFOV / M`

Current visual numbers:

- `25 mm`: `M = 36x`, `D_exit ~= 2.94 mm`, `TFOV ~= 1.39 deg`
- `10 mm`: `M = 90x`, `D_exit ~= 1.18 mm`, `TFOV ~= 0.56 deg`

## 3) Proposed product (what it actually is)

From the product listing text:

- Product class: **Microscope eyepiece camera**
- Sensor: `1920 x 1080`, pixel `3 x 3 um`, sensor size `5.86 x 3.28 mm`
- Mechanical insertion: `23.2 mm` microscope standard (with `30 mm` / `30.5 mm` microscope adapters)
- Frame rate: up to `25 fps`
- Software/host: Windows software; USB connection

Important: these specs describe a **digital microscope imaging camera**, not an astronomical visual eyepiece with a telescope AFOV/focal length spec.

## 4) Compatibility comparison

| Criterion | Current eyepieces (Plossl 25/10 mm) | BRESSER MikrOkular LF | Result |
|---|---|---|---|
| Intended use | Telescope visual observing | Microscope imaging | Mismatch |
| Telescope eyepiece standard | `1.25"` barrel (`31.7 mm`) | `23.2 mm` microscope insertion | Mismatch |
| Visual parameters available (`f_eye`, AFOV) | Yes | No (camera sensor specs instead) | Not directly comparable as eyepiece |
| Visual observing through eye | Yes | No (camera output workflow) | Not a visual replacement |
| Plug-and-play in Q001 focuser | Yes | No, requires custom adaptation path | High integration risk |

## 5) Imaging implications if used experimentally

If treated as a camera experiment (not eyepiece):

- Small sensor (`5.86 x 3.28 mm`) at `900 mm` focal length gives a narrow field.
- Approximate plate scale:
  - `arcsec/pixel ~= 206265 * (0.003 mm / 900 mm) ~= 0.69 arcsec/pixel`
- Approximate field of view:
  - width: `(5.86 / 900) * 57.3 ~= 0.373 deg` (~22.4 arcmin)
  - height: `(3.28 / 900) * 57.3 ~= 0.209 deg` (~12.5 arcmin)

These values can be useful for lunar/planetary framing, but the module is still not a practical replacement for your visual eyepiece path.

## 6) Tradeoffs and risk

- **Pros (only for experimentation):**
  - Low refurbished price
  - Full HD output and documented pixel size
- **Cons (for your stated eyepiece comparison goal):**
  - Wrong optical/mechanical ecosystem (microscope-first)
  - Missing telescope-native interface (`1.25"` / T2 workflow)
  - No direct visual use; does not replace observing eyepieces
  - Added integration uncertainty (adapters, back focus, stability)

## 7) Final conclusion for this proposal

Against the current `25 mm` and `10 mm` telescope eyepieces in this project:

- **As an eyepiece replacement: No, it is not better.**
- **As a camera experiment: possible, but not the recommended first path** for Q001 compared with standard telescope camera coupling (`1.25"` nosepiece to T2 / dedicated astro camera path).

## 8) Practical next step

If your goal is better telescope performance now:

1. Keep visual with proper telescope eyepieces (`~10-13 mm` upgrade class).
2. For imaging, follow the existing `camera-imaging-guide.md` prime-focus path using telescope-standard adapters/cameras.
3. Only test the Bresser microscope camera if you explicitly want an adapter-heavy experimental branch.

