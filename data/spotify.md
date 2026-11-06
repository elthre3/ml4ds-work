---
title: "Spotify tracks"
description: "10,000 tracks from Spotify playlists of six genres, with audio features, a release date and Spotify's popularity score."
---

| | |
|---|---|
| **Source** | Collected from the Spotify Web API by Kaylin Pavlik and published as a TidyTuesday dataset (21 January 2020). The course file is a random sample of 10,000 of its tracks. Spotify's terms restrict commercial use. |
| **Rows** | One row per track and playlist (11,554 rows): 1,101 tracks are in more than one playlist. For one row per track, use `distinct(track_id, .keep_all = TRUE)`, as the loader below does. |
| **Columns** | `track_id`, `track_name`, `track_artist`, `track_popularity` (0 to 100), `release_date`, `release_year`, `playlist_genre`, `playlist_subgenre`, and the audio features `danceability`, `energy`, `key`, `loudness`, `mode`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`, `duration_ms`. |
| **Target** | `track_popularity`, Spotify's score in January 2020. It rewards recent plays, so `release_year` carries recency as well as era. A tenth of the tracks score exactly 0. |
| **Notes** | The genre is the playlist's, not the track's. No missing values in the features; one track has no name. Six genres, no lyrics, no artist history, no play counts. |

## Loader

```r
library(tidyverse)
sp <- read_csv("https://ml4ds.com/files/spotify_tracks.csv") |>
  distinct(track_id, .keep_all = TRUE) |>          # one row per track
  mutate(duration_min = duration_ms / 60000)
```
