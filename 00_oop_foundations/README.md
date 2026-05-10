# 00 OOP Foundations (Pre-Experiment)

<div align="left">

![Python](https://img.shields.io/badge/Python-3.12%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)
![Pre Experiment](https://img.shields.io/badge/Pre--Experiment-00%20%7C%20OOP%20Foundations-1f2937?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-22c55e?style=for-the-badge)

</div>

If Experiment 1 feels heavy, start here.

This pre-experiment explains classes and objects in plain language before we touch dunder methods.

## The Story

Imagine a bakery app.

You do not want to store each cake in separate variables forever. You want a reusable blueprint.

- The blueprint is the class.
- A real cake made from that blueprint is an object.

That is all OOP starts with.

## What You Will Learn Here

- what a class is;
- what an object is;
- how methods describe behavior;
- how attributes store data;
- why this is useful before writing Pythonic code.

## Quick Intuition

- `class` = template
- `object` = real thing created from template
- method = what the thing can do
- attribute = what the thing knows

## Case Scenario

In this pre-experiment we model a simple `Playlist` object.

A playlist has data:
- `name`
- `songs`

A playlist has behavior:
- `add_song(...)`
- `play()`
- `describe()`

This gives you the OOP base. Then in Experiment 1, we make that same idea more Pythonic with special methods.

## Run It

From inside `00_oop_foundations/`, run:

```bash
python pre_experiment_0.py
```

## Bridge To Experiment 1

After this pre-experiment, move to `01_data_model/README.md`.

Pre-Experiment 0 teaches:
- "what is an object"

Experiment 1 teaches:
- "how Python talks to that object"
