---
title: "ST310 group project"
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

The group project is 30% of your mark for ST310. Your group uses a real dataset of your choice to run a common task framework (CTF) prediction competition, like the ones in the course, and then considers what could go wrong once the winning model is put to use.

These instructions may be clarified as questions come up. That much flexibility is necessary for an open-ended project where each group picks its own data.

## Part 1: a CTF competition on your data

**Introduction** (roughly one paragraph). Describe your dataset and the prediction task. Is the task well motivated? Why would anyone care about predicting this outcome, and does the task have any important limitations?

**Competitors** (roughly one sentence to one paragraph per model). Choose the competitor models. Aim for a variety of the model types covered in the course. For each model, explain how you tuned it, how you know whether it is well tuned or not, and any choices you made about how to use it.

One model must be fit using your own implementation of gradient descent. The only restriction on this model is that the gradient of the loss function should not be a constant. You are free to use a simple model and a simple loss function to make the derivation and computation manageable.

**Results** (roughly one paragraph). Explain the result of the competition, and comment on anything that seemed interesting.

## Part 2: what could possibly go wrong?

Suppose the winner of your competition, or another top competitor, has now been chosen and deployed in the real world. Describe two different kinds of bad things that might happen (roughly one paragraph each):

1. one in which the model's accuracy falls significantly after deployment;
2. one that involves interpretation rather than accuracy.

At least one of the two should also illustrate the problem with a simulation, applying your actual fitted model from Part 1 to simulated or synthetic data.

## Grading expectations

For grading purposes you should keep in mind three high level goals.

1. **I must be absolutely certain that you (meaning your team) did the work.** If you use any resources online to find examples of code then you should cite the resource. It's also helpful to put comments in your code explaining it, for example:

    ```
    dataset |>
      some_function() |> # to do something
      another_function()  # for something else
    ```

2. **I should be able to understand what you did.** State your motivating question(s), describe your dataset, and explain your models and methods clearly and concisely. Make sure that your document is formatted properly and the plots and other outputs display correctly. Double check this for the final PDF file before you submit it.

3. **I should be convinced that you understand what you did.** Some software libraries are easy enough to use that you can get impressive results without knowing how or why. But this is not a course on how to use software libraries, it's a course on machine learning. Without sacrificing clarity or brevity, your explanations should show deep understanding.

Notably absent from this list: getting significant results, using the most cutting edge methods, etc.

The marks are divided as follows.

| Component | Marks |
|---|---:|
| Part 1: introduction | 10 |
| Part 1: competitors, including your own gradient descent | 30 |
| Part 1: results | 10 |
| Part 2: accuracy after deployment | 10 |
| Part 2: interpretation | 10 |
| Application of course concepts | 10 |
| Quality of the analysis | 10 |
| Quality of code and writing | 10 |
| **Total** | **100** |

## Use of AI tools is forbidden in this course

This includes the project.

## Proposal

Once your group has chosen a dataset and a prediction task, work through the proposal checklist together. Then one (**only one**) member of your group submits your answers to the "Project proposal" assignment on Moodle by Monday 30 November at noon. Proposals are not marked. The checklist is there to help you find out early whether your dataset and task will work.

## Report and submission

Your group writes one Quarto (`.qmd`) document with all of your analysis and interpretation, in R. Structure it to make it easy to read and navigate. Use sections and subsections. Break up code into multiple chunks, include comments, and break long lines of code so they don't extend off the side of the page.

Every team member should check every part of the document, ask each other clarifying questions, and write whatever comments and explanations are necessary to make sure that **everyone is responsible for all parts of the project**. It's very important that you have some time for this stage before the submission deadline, so you can make edits and changes if necessary.

One member of your group submits the rendered PDF and the `.qmd` source to the "Project submission" assignment on Moodle by Thursday 17 December at noon.
