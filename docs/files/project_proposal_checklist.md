---
title: "ST310 group project: proposal checklist"
format:
  pdf:
    documentclass: article
    papersize: a4
    geometry:
      - margin=2.5cm
    fontsize: 11pt
    colorlinks: true
    pdf-engine: xelatex
---

Work through this list together before you submit your proposal. If the answer to a question is "no" or "not sure", fix it now, or choose another dataset or another outcome. It is much easier to change your mind now than after you have fit five models.

## The dataset

- [ ] **You have it.** You have downloaded the data and loaded it into R, and you have looked at the outcome and a few of the predictors.
- [ ] **You may use it.** Its terms of use allow a course project, and it contains no information that identifies individual people.
- [ ] **It is real.** The outcome was measured, not simulated. The dataset is not one of those used in the lectures or seminars.
- [ ] **It is big enough.** It has at least several hundred rows, and preferably a few thousand. With fewer, it is hard to tell competitors apart.
- [ ] **It has enough predictors** for a variety of models to differ: more than a handful.
- [ ] **You know what a row is**: a person, a household, a country in a year, a transaction. Write it down.
- [ ] **It does not need much cleaning.** The dataset does not require a significant amount of cleaning and preprocessing, or your group is confident you can handle it and will describe it in your submission.
- [ ] **Missing data.** There is no missing data, or you have a principled plan for how you will handle missing data and will describe it in your submission.

## The prediction task

- [ ] **You can state it in one sentence:** predict [the outcome] for [a row] from [the predictors].
- [ ] **The outcome is one variable,** either a number (regression) or a category (classification).
- [ ] **The predictors would be known at the time the prediction is made.** Nothing among them is recorded after the outcome, or computed from it.
- [ ] **The outcome is not just a formula of the predictors**, such as a total predicted from its parts, or a category defined by cutoffs on one of the predictors. If it were, there would be nothing to learn.
- [ ] **The outcome varies.** If one value or one class makes up almost all of the rows, you have thought about what a good prediction would be.
- [ ] **Someone would care.** You can say who would use these predictions, and for what decision or question.
- [ ] **You can imagine it deployed.** You can say where and when the model would be used, so that Part 2 has something to go wrong.
- [ ] **A first fit looks plausible.** If the first simple model you try predicts almost perfectly, find out why before going any further.

## Submitting the proposal

One member of your group submits the answers to these questions to the "Project proposal" assignment on Moodle by Monday 30 November at noon:

1. The dataset: its name, a link to where you got it, and its terms of use.
2. What a row is, and the number of rows and columns.
3. The prediction task, in one sentence.
4. Who would care about the predictions, and why.
5. Any item on the checklist you answered "no" or "not sure", and what you did about it.
