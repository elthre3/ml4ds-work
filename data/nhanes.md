---
title: "NHANES"
description: "Health measurements and survey answers for 20,293 participants of the US National Health and Nutrition Examination Survey, 2009 to 2012."
---

| | |
|---|---|
| **Source** | The US National Health and Nutrition Examination Survey (NHANES), run by the National Center for Health Statistics, cycles 2009--10 and 2011--12; shipped as `NHANESraw` in the R package `NHANES` (Pruim, R., *NHANES: Data from the US National Health and Nutrition Examination Study*, version 2.1.4, [CRAN](https://CRAN.R-project.org/package=NHANES)). Survey documentation: [cdc.gov/nchs/nhanes](https://www.cdc.gov/nchs/nhanes/). |
| **Rows** | One row per participant (20,293 rows, all ages). The course uses the 9,203 adults (20 and over) with every column below recorded (the loader). |
| **Columns** | Among the package's 79: `Gender`, `Age` (80 means 80 or older), `Race1` (the survey's five groups: Black, Hispanic, Mexican, White, Other), `Poverty` (family income over the poverty guideline), `Weight` (kg), `Height` (cm), `BMI` (weight over height squared), `Pulse`, `BPSysAve` (systolic blood pressure, mm Hg), `TotChol` and `DirectChol` (total and HDL cholesterol, mmol/L), `PhysActive` (moderate or vigorous sports or recreation), `Diabetes` (ever told by a doctor or health professional that they have diabetes). |
| **Targets** | `Diabetes`, a yes or no answer (14% of the adults used); `BPSysAve`. |
| **Notes** | NHANES oversamples some groups on purpose, and the course does not use its survey weights, so the rows are not a sample of the US population: shares and averages computed from them describe these participants, not the country. Diabetes is what participants report having been told, so undiagnosed diabetes counts as no. |

## Loader

```r
library(tidyverse)
library(NHANES)
nh <- NHANESraw |>
  filter(Age >= 20) |>
  select(Diabetes, Gender, Age, Race1, Poverty, Weight, Height, BMI, Pulse, BPSysAve, TotChol, DirectChol, PhysActive) |>
  drop_na() |>
  mutate(diabetes = as.numeric(Diabetes == "Yes"), male = as.numeric(Gender == "male"),
         active = as.numeric(PhysActive == "Yes"))
```
