# Colors Helper — archived

> **This repository is archived as of 2026-06-28.** Use one of these instead:
>
> - **Palette data (live, browse-able):** <https://harchaoui.org/warith/colors/>
>   — base, emotions, concepts, and color psychology, all keyed off the same
>   curated Apple-inspired hex set.
>
> - **Code (modern, maintained):** <https://github.com/warith-harchaoui/front>
>   — specifically the `front-colors` skill, which now hosts:
>   - WCAG contrast audit with OKLCH-neighbour fix suggestions
>     (`front-colors/scripts/audit_contrast.py`)
>   - Color-vision-deficiency simulation — protanopia / deuteranopia /
>     tritanopia, Machado et al. 2009 matrices
>     (`front-colors/scripts/simulate_cvd.py`)
>   - Shared primitives — sRGB ↔ linear, hex ↔ RGB, OKLab / OKLCH, WCAG
>     luminance / contrast, perceptual `lighten` / `darken`, palette
>     accessors, `Color` class
>     (`front-colors/scripts/_colors.py`)
>   - The unified palette CSV — one row per color, semantic projections
>     (Base / Emotion / Concepts / Psychology±) as columns
>     (`front-colors/references/palette.csv`)
>
> No more changes will land here. The package is *not* on PyPI; the
> historical install instructions below are kept only for users with
> existing scripts that pinned the old commit hash.

## What this repository was

`Colors Helper` was a small Python library shipping a curated palette
(Apple system colors + light counterparts derived via
[Tint & Shade Generator](https://maketintsandshades.com)) and a handful
of utility functions for hex / RGB conversion and palette CSV
management.

Why it's archived: the math here was naïve (a `+70` channel offset
isn't a perceptual lighten), the CSV column name drifted out of sync
with the live file (`"Hex Code"` in code vs `Hexcode` in the published
CSV), there were no contrast / OKLCH / CVD primitives, and the
`os-helper` git dependency made the package hard to reuse. All those
gaps are addressed properly inside `front-colors`.

The Apple-curated palette itself remains valuable and lives on at
<https://harchaoui.org/warith/colors/> and inside
[`front-colors/references/palette.csv`](https://github.com/warith-harchaoui/front/blob/main/front-colors/references/palette.csv).

## Historical install (do not use for new work)

```bash
pip install --force-reinstall --no-cache-dir \
    git+https://github.com/warith-harchaoui/colors-helper.git@main
```

## Author

[Warith Harchaoui](https://deraison.ai)
