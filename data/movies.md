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
| **Notes** | `votes` and `r1` to `r10` come from the same users' ratings, so they are not honest predictors of `rating`. Lengths are as reported to IMDb; there is no director, cast, language or country. |

## Loader

```r
library(ggplot2movies)
mv <- movies
```
