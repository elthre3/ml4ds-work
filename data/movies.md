---
title: "Movies"
description: "58,788 films from the Internet Movie Database, up to 2005, with year, length, average user rating and vote counts."
---

| | |
|---|---|
| **Source** | IMDb data extracted by Hadley Wickham, shipped in the R package `ggplot2movies` (GPL-3). IMDb's terms restrict commercial use. |
| **Rows** | One row per film (58,788 rows), films with a known length and at least five user votes, 1893 to 2005. |
| **Columns** | `title`, `year`, `length` (minutes), `budget` (91% missing), `rating` (average user rating, 1 to 10), `votes`, `r1` to `r10` (the share of users giving each rating), `mpaa` (mostly blank), and seven genre indicators (`Action`, `Animation`, `Comedy`, `Drama`, `Documentary`, `Romance`, `Short`). |
| **Target** | `rating`. The ratings come from people who chose to watch a film and then to rate it. |
| **Notes** | `votes` and `r1` to `r10` are computed from the same users' ratings as `rating`, so they are not used as inputs. Lengths are as reported to IMDb; there is no director, cast, language or country. The course uses the 53,388 films from 1919 on that run 11 to 200 minutes (the loader below). |

## Loader

```r
library(tidyverse)
library(ggplot2movies)
mv <- movies |>
  filter(length <= 200, length > 10, year > 1918, votes >= 5)
```
