---
title: "Palmer penguins"
description: "344 penguins of three species measured at Palmer Station, Antarctica, 2007–2009: bill, flipper, body mass, sex, island."
---

| | |
|---|---|
| **Source** | Gorman, Williams and Fraser (2014), Palmer Station Long Term Ecological Research program, packaged by Horst, Hill and Gorman as the R package `palmerpenguins`. The package and its data are CC0. |
| **Rows** | One row per penguin (344): Adelie, Chinstrap and Gentoo. Two penguins lack all four measurements and eleven lack `sex`, so use `drop_na()` on the columns you use. |
| **Columns** | `species`, `island`, `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`, `sex`, `year`. |
| **Target** | In the loader below, `chinstrap`: 1 for a Chinstrap, 0 for an Adelie (219 penguins with complete measurements). |
| **Notes** | Write `palmerpenguins::penguins`: the `modeldata` package also has a `penguins` (7 columns, no `year`), which masks this one if it is attached later. `island` separates Chinstrap from Gentoo completely (Chinstraps are only on Dream, Gentoos only on Biscoe), so a model that uses it solves an easier problem. Adelie and Chinstrap are nearly separable on the bill measurements, so `glm` may warn about fitted probabilities of 0 or 1. |

## Loader

```r
library(palmerpenguins)
pg <- palmerpenguins::penguins |>
  dplyr::filter(species != "Gentoo") |>
  tidyr::drop_na(bill_length_mm, bill_depth_mm, flipper_length_mm) |>
  dplyr::mutate(chinstrap = as.numeric(species == "Chinstrap"))
```
