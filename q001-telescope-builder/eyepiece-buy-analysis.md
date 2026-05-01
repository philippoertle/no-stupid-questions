# Eyepiece (Okular) Analysis and Swiss Buy Shortlist

This document turns the current eyepiece discussion into a practical purchase guide for the DIY refractor build.

## 1) Build Context (from project docs)

- Telescope type: Kepler refractor
- Objective focal length: `f_obj = 900 mm` (builder-confirmed)
- Objective diameter: `D = 106 mm` (nominal)
- Current eyepieces: 1.25" Plossl `25 mm` and `10 mm`
- Effective focal ratio:
  - `f/# = f_obj / D = 900 / 106 ~= 8.5`

Core equations used in this analysis:

- Magnification: `M = f_obj / f_eye`
- Exit pupil: `D_exit = D / M = f_eye / (f/#)`
- Approx. true field: `TFOV ~= AFOV / M`

## 2) Is "the eyepiece is bad" a realistic diagnosis?

Short answer: **yes, but only partly in this project**.

From `aberration-analysis.md` and the diagnostic scripts:

- A strong halo at full aperture was reported.
- A `40 mm` stop strongly reduced halo.
- Visual and camera behavior were reported as similar.

Interpretation:

- This strongly indicates a **primary objective/marginal-ray issue** (chromatic/spherical residuals and possibly edge-zone behavior).
- A better eyepiece can still improve:
  - perceived contrast,
  - internal reflection/ghost control,
  - edge behavior and comfort.
- But it is unlikely to fully cure full-aperture halo by itself.

So an eyepiece upgrade is valid, but should be treated as a **secondary lever** after aperture/alignment/stray-light optimization.

## 3) Three Eyepiece Proposals by Budget (CHF)

Prices and stock are market snapshots and can change quickly.

### A) Under 50 CHF

**Recommendation:** `TS Optics Plossl 10mm 1.25"`

- Typical observed price signal: about `EUR 34.90` (~`CHF 33-40`, plus shipping/import effects depending on seller)
- Typical source seen: Astroshop listing
- Why this pick:
  - low-risk budget test purchase,
  - straightforward compatibility with the existing 1.25" setup.

Numbers on this telescope:

- `M = 900 / 10 = 90x`
- `D_exit ~= 10 / 8.5 ~= 1.18 mm`

Tradeoff:

- This is still a Plossl-class eyepiece, so improvement versus current Plossls may be moderate rather than dramatic.

### B) 50 to 150 CHF

**Recommendation:** `Celestron X-Cel LX 12mm (60 deg AFOV)`

- Observed price signal: around `CHF 139`
- Swiss availability signal seen in listings: in-stock style indicators ("Lager"/stock)
- Why this pick:
  - good comfort and eye relief for practical observing,
  - better coatings and typical contrast/ghost behavior than basic entry-level pieces,
  - excellent all-round focal length for this 900 mm scope.

Numbers on this telescope:

- `M = 900 / 12 = 75x`
- `D_exit ~= 12 / 8.5 ~= 1.41 mm`
- `TFOV ~= 60 / 75 ~= 0.8 deg`

Tradeoff:

- Strong value tier, but not the final word in scatter control or edge correction versus premium options.

### C) Over 150 CHF

**Recommendation:** `Baader Morpheus 12.5mm (76 deg AFOV)`

- Observed Swiss price signals: about `CHF 259` (range often ~`CHF 250-280`)
- Availability signals seen: sometimes low/limited stock at specific Swiss listings
- Why this pick:
  - very strong long-term eyepiece quality,
  - excellent comfort, contrast, and broad apparent field,
  - remains useful even if the telescope is upgraded later.

Numbers on this telescope:

- `M = 900 / 12.5 = 72x`
- `D_exit ~= 12.5 / 8.5 ~= 1.47 mm`
- `TFOV ~= 76 / 72 ~= 1.06 deg`

Tradeoff:

- Price premium; still cannot by itself remove objective-driven chromatic/spherical behavior.

## 4) Recommendation Summary (What to Buy First)

If buying one eyepiece now:

1. Best value/performance balance for this project: **X-Cel LX 12mm**
2. Best long-term premium option: **Morpheus 12.5mm**
3. Cheapest test option: **TS Optics Plossl 10mm**

## 5) Practical Next Steps (Aligned with project diagnostics)

1. Buy one eyepiece in the `~12 mm` class (mid-tier or premium).
2. Re-run the aperture sweep protocol with consistent target and focus procedure.
3. Compare against current 10 mm Plossl:
   - halo score,
   - veiling/ghost behavior,
   - detail score.
4. Keep objective-centered mitigations as primary path:
   - intermediate stop (`~70-80 mm`) tests,
   - objective mounting stress check,
   - alignment and stray-light control.

Expected outcome:

- Better eyepiece should improve usability and contrast,
- but full-aperture halo behavior will likely still be governed mainly by objective and beam geometry.

## 6) Quick Purchase Checklist (1-minute pre-checkout)

Use this before clicking buy.

- [ ] **Barrel size matches focuser:** eyepiece is `1.25"` (or includes usable `1.25"` mode if dual-barrel).
- [ ] **Focal length in target range:** around `10-13 mm` for this `900 mm` scope (`~70x` to `~90x`).
- [ ] **Eye relief is comfortable:** ideally `>= 15 mm` if you want easier viewing (or observe with glasses).
- [ ] **AFOV fits your preference:** about `50 deg` (classic), `60 deg` (comfortable upgrade), `~76 deg` (immersive).
- [ ] **Coatings and build are specified:** fully multi-coated optics and blackened internals preferred for contrast.
- [ ] **Weight is acceptable:** heavier eyepieces can upset balance on light mounts/focusers.
- [ ] **Stock signal is real:** listing shows in-stock/short lead time, not backorder only.
- [ ] **Total landed price is acceptable:** include shipping, VAT/import handling, and return cost to Switzerland.
- [ ] **Return policy is clear:** check return window and condition requirements.
- [ ] **No expectation mismatch:** eyepiece upgrade helps contrast/comfort, but will not fully fix objective-driven halo.

Optional but useful:

- [ ] Buy from a seller with clear exchange handling in case eye relief or ergonomics are not a good personal fit.

## 7) Pass/Fail Snapshot for the Three Recommendations

Legend: `Pass` = clearly meets the checklist intent, `Conditional` = acceptable but with caveats.

| Check | TS Optics Plossl 10 mm (<50 CHF) | Celestron X-Cel LX 12 mm (50-150 CHF) | Baader Morpheus 12.5 mm (>150 CHF) |
|------|------------------------------------|----------------------------------------|-------------------------------------|
| 1.25" compatibility | Pass | Pass | Pass (dual barrel, 1.25"/2") |
| Focal length fit (10-13 mm) | Pass | Pass | Pass |
| Comfort / eye relief | Conditional (typically tighter) | Pass | Pass |
| AFOV preference flexibility | Conditional (~52 deg class) | Pass (60 deg) | Pass (76 deg) |
| Coatings / stray-light control | Conditional (budget class) | Pass | Pass |
| Weight / balance on light setup | Pass (usually light) | Pass (moderate) | Conditional (heavier) |
| Swiss stock probability | Conditional (varies by seller/import) | Pass (good Swiss listing signals) | Conditional (often available, sometimes limited stock) |
| Landed CHF risk | Pass (lowest risk) | Pass (still manageable) | Conditional (highest total cost) |
| Return-policy sensitivity | Conditional (depends strongly on seller) | Conditional (seller-dependent) | Conditional (seller-dependent) |
| Expected impact on your current issue | Conditional (small to moderate) | Pass (moderate practical gain) | Pass (strongest eyepiece-side gain) |

### Decision shortcut

- If you want **minimum spend**: choose **TS Optics 10 mm Plossl**.
- If you want **best value for this project**: choose **X-Cel LX 12 mm**.
- If you want **best long-term eyepiece quality**: choose **Morpheus 12.5 mm**.
