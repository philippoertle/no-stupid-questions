# Samsung NX300 telescope adapter note

## Quick conclusion

- The `Samsung NX300` appears to have no menu setting for "release/shoot without lens."
- The camera expects a physical lens-detect switch in the mount to be pressed.
- A proper `NX-to-T2` adapter usually solves this by pressing that switch.
- If you still get "no lens," adapter thickness/tolerance is likely the issue.
- Shim/tape workarounds are reported by users, but are at-your-own-risk.

## Key sources

- Photo Stack Exchange (direct NX300 + telescope question):  
  https://photo.stackexchange.com/questions/65468/can-a-samsung-nx300-shoot-without-a-lens-for-attaching-to-a-telescope
- DPReview forum thread ("where is shoot without lens"):  
  https://www.dpreview.com/forums/thread/3502012
- User blog showing adapter-switch engagement issue and shim example:  
  http://recordingphotons.blogspot.com/2014/04/legacy-glass-on-samsung-nx300.html
- NX300 manual error page mirror (lens remount/error context):  
  https://www.manualslib.com/manual/443018/Samsung-Nx300.html?page=170

## Full report

See:
- `reports/literature-search-report.md`
- `reports/literature-search-report-t2-flat-mount.md`

## Project layout

- `reports/` literature and sourcing reports
- `cad/cnc/source/` CNC CAD generators/scripts
- `cad/cnc/exports/` CNC outputs (`.step`, `.stl`, drawing PDF)
- `cad/print/source/` home 3D-print CAD sources (next step)
- `cad/print/exports/` 3D-print exports (`.stl`, `.3mf`, slicer-ready)
