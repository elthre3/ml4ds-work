# Interpretation slides parked for the next lecture

On 15 November 2026 the convenor moved partial dependence for models other than a GAM, ICE, and feature importance out of the ensembles lecture and into the next one. These slides were built, reviewed and revised for the ensembles deck; they are kept here so that the next lecture's build can start from them. The folder name starts with an underscore, so Quarto does not render it.

## What is here

`interpretation-slides.qmd`, in deck order:

1. "A flexible (e.g. tree-based) model fits interactions, unlike GAM": a random forest on the simulated interaction.
2. "Partial dependence": the definition, with the notation of Causal Dependence Plots (Loftus, Bynum and Hansen 2024).
3. "Flexible model fits, unlike GAM; but the univariate plot is wrong": the forest's PDP only, then the same with ICE curves.
4. "PDP and ICE: recap".
5. Part divider "feature importance", then "Feature/variable importance", "Permutation and extrapolation", "Permutation with correlated inputs", "Leave one covariate out".
6. The conclusion's two lines and the three references these slides cite (Hooker et al. 2021; Lei et al. 2018; Loftus, Bynum and Hansen 2024).

## What the slides need from the ensembles deck

The chunks use objects that the ensembles deck defines: the setup chunk (`mv`, `mv_train`, `mv_tune`, `genres`, `inputs`, `f_all`, `mse`, the colors `v_dark`, `v_blue`, `v_teal`, `m_pink` and others), the simulated interaction from "True model non-additive; GAM is wrong" (`f1`, `f2`, `df_int`, `fit_gam_wrong`), and the random forest on the films from "Out-of-bag predictions" (`rf_mv`, with `mtry = 3` fixed so that the leave-one-out refits are comparable). Packages: tidyverse, patchwork, mgcv, randomForest, pdp, MASS (`kde2d`). `randomForest` masks `margin`, so the code calls `ggplot2::margin`. The next lecture will need to recreate these objects, or share a setup file, and its random numbers will differ from the ensembles deck's.

## Decisions already made

- ICE transparency by the size of the interaction's multiplier: opacity grows with $|\cos(\pi x_2/2)|$ (strength $\cos^4$, alpha range 0.03 to 0.75, after the convenor's 15 November note that too many curves were dark), and the figures are 8 by 3.9 inches, less wide than before.
- Spine wording rule 4: ICE evaluates the fitted model at a modified input that may correspond to no plausible unit; this is in a speaker note.
- For an additive model with independent inputs, permutation importance is $2\,\mathrm{Var}\,f_j$ and leave-one-covariate-out is $\mathrm{Var}\,f_j$ (checked by simulation during the revisions): a candidate seminar exercise.
- The ensembles deck keeps "Partial dependence plots for a GAM" (the GAM's component plots, named as PDPs) and the Box slide, so the next lecture can refer back to them.

## Readings that went with these slides

From the ensembles week's page, now removed there: IML, "Partial Dependence Plot (PDP)" (sections "Definition and estimation", "Examples", "Limitations"); IML, "Permutation Feature Importance" (opening paragraph, "Theory", "Example and interpretation"; stop before "Conditional feature importance"); IML, "Leave One Feature Out (LOFO) Importance" (start through "Examples", then "LOFO versus PFI"; the lecture's LOCO is the same method). Optional: ESL section 10.13, pp. 367–370; Hooker, Mentch and Zhou (2021); Lei et al. (2018), section 6. The next week's page already lists the IML PDP, ICE and permutation chapters; it does not list LOFO.

## Notes

- Nothing here is rendered or checked by the build; render it inside the next lecture's deck before use.
- The slides were last rendered as part of the ensembles deck at commit 6dc9b42 on branch claude/08-ensembles.
