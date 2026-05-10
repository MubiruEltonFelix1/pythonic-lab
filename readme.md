<div align="center">

```
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗██╗ ██████╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║██║██╔════╝
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║██║██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║██║██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║██║╚██████╗
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝
                                                              LAB
```

### *Where Python stops being a tool and starts being a language.*

---

![Python](https://img.shields.io/badge/Python-3.12+-FFD43B?style=for-the-badge&logo=python&logoColor=black)
![Book](https://img.shields.io/badge/Based%20On-Fluent%20Python%202nd%20Ed-1a1a2e?style=for-the-badge&logo=bookstack&logoColor=white)
![Status](https://img.shields.io/badge/Status-Actively%20Growing-22c55e?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-6366f1?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/YOUR_USERNAME/pythonic-lab?style=for-the-badge&color=f59e0b)
![Last Commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/pythonic-lab?style=for-the-badge&color=0ea5e9)

</div>

---

## What This Is

This is not a tutorial repository. It is not a course. It has no completion percentage and no certificate at the end.

This is a **lab** — an active, evolving workspace where I go deep into the internals of Python, one concept at a time, and apply what I learn by building things. Every folder is an experiment. Every file is a question I asked and then answered in code.

The foundation is [**Fluent Python, 2nd Edition**](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) by Luciano Ramalho — arguably the finest book ever written about the Python language. Not Python syntax. The Python *language*. The data model. The protocol system. How Python's object machinery actually works under the hood.

Reading it is not enough. You have to build with it. This repo is that building.

---

## The Philosophy

```python
# There are two kinds of Python programmers.

# The first kind writes this:
result = []
for item in data:
    if item > 0:
        result.append(item * 2)

# The second kind understands WHY this is also correct,
# and exactly what Python is doing at every step:
result = [item * 2 for item in data if item > 0]

# And then goes deeper — understanding generators, lazy evaluation,
# the iterator protocol, and when each approach is actually better.

# This lab is about becoming the second kind.
```

The goal is not cleverness. Fluent Python is not about writing code that looks smart. It is about understanding your tools well enough to make the right choice — and understanding *why* it is the right choice. Code that looks clean because you understand it is completely different from code that looks clever because you wanted it to.

---

## Repository Structure

```
pythonic-lab/
│
├── 📖 README.md                    ← you are here
├── 📝 CONCEPTS.md                  ← running glossary as I learn
├── 🔬 EXPERIMENTS.md               ← findings, surprises, things that broke
│
├── 00_oop_foundations/             ← pre-experiment: classes, objects, methods, attributes
├── 01_data_model/                  ← the Python object protocol. __dunder__ everything.
├── 02_sequences/                   ← lists, tuples, generators, slicing internals
├── 03_dicts_sets/                  ← hash tables, defaultdict, the dict data model
├── 04_text_bytes/                  ← Unicode, encoding, bytes vs str, locale
├── 05_functions_as_objects/        ← first-class functions, closures, free variables
├── 06_design_patterns/             ← strategy & command implemented with functions, not classes
├── 07_closures_decorators/         ← parametrized decorators, class-based decorators
├── 08_type_hints/                  ← Protocols, gradual typing, structural subtyping
├── 09_object_protocol/             ← __slots__, __init__ vs __new__, ABCs
├── 10_interfaces/                  ← duck typing vs goose typing, virtual subclasses
├── 11_inheritance/                 ← MRO, super(), mixins done right
├── 12_operator_overloading/        ← __add__, __mul__, reflected operators
├── 13_iterators_generators/        ← iterator protocol, yield, yield from, coroutines
├── 14_context_managers/            ← with, __enter__/__exit__, contextlib
├── 15_concurrency/                 ← threading, asyncio, concurrent.futures
├── 16_metaprogramming/             ← descriptors, __getattr__, metaclasses
│
└── projects/                       ← applied: multiple concepts, one real thing
    ├── sensor_pipeline/            ← generator pipeline for IoT sensor data processing
    ├── config_system/              ← descriptor-based config with type validation
    ├── tiny_orm/                   ← mini ORM: metaclasses + descriptors + protocols
    └── async_data_fetcher/         ← async I/O + context managers + generators
```

Each folder contains:
- A `README.md` explaining what concept is being explored and what I found
- Python files with heavily commented, experiment-oriented code
- Sometimes benchmarks comparing approaches

---

## Where To Start

If you are reading this repository to learn alongside me, here is the order that makes sense:

```
00            (pre-experiment: classes and objects, beginner bridge)
       ↓
01 → 02 → 03  (the foundation: Python's data model and core structures)
       ↓
05 → 06 → 07  (functions as first-class citizens, the beating heart of Pythonic code)
       ↓
09 → 11 → 12  (how objects really work, how inheritance really works)
       ↓
13 → 14 → 15  (iteration, context, and concurrency — Python's async story)
       ↓
16            (metaprogramming last — everything else must come first)
       ↓
projects/     (where it all comes together)
```

Do not skip to metaprogramming. If you are new to OOP, start at 00 first, then move to 01. The Python data model chapter (01) is the prerequisite for everything else. Read it twice.

---

## Concepts Snapshot

A live sample of what lives in `CONCEPTS.md` — a glossary that grows with every session:

| Concept | One-Line Definition | Chapter |
|---|---|---|
| `__dunder__` methods | Special methods Python calls implicitly, not you directly | 1 |
| Descriptor Protocol | Objects that define `__get__`, `__set__`, `__delete__` for attribute access | 23 |
| Generator Expression | Lazy sequence evaluation — produces items one at a time, not all at once | 17 |
| `yield from` | Delegates iteration to a sub-generator; the backbone of coroutines | 17 |
| Closure | A function that retains access to variables from its enclosing scope after that scope exits | 9 |
| `nonlocal` | Declares that a variable in a nested function refers to the enclosing scope, not local | 9 |
| Structural Subtyping | If an object has the right methods, it satisfies the interface — no inheritance required | 13 |
| MRO | Method Resolution Order — the C3 linearization algorithm Python uses to resolve `super()` | 14 |
| `__slots__` | Replaces the instance `__dict__` with a fixed-memory tuple — faster, smaller footprint | 9 |
| `functools.wraps` | Preserves the original function's metadata when writing a decorator | 9 |

---

## Projects Gallery

The `projects/` folder is where isolation ends and application begins.

### `sensor_pipeline/`
> *Generators · Iterators · Context Managers · dataclasses*

A lazy data processing pipeline that simulates reading from IoT soil moisture and CO2 sensors. Each stage of the pipeline is a generator. Data flows through transformation steps without ever loading the full dataset into memory. Inspired by a real sensor network I am building in Uganda.

```python
pipeline = (
    normalize(reading)
    for reading in parse_csv(sensor_log)
    if reading.quality > THRESHOLD
)
```

### `config_system/`
> *Descriptors · Type Hints · __set_name__ · Protocols*

A descriptor-based configuration system with automatic type validation. Define a config class with typed attributes; the descriptor handles validation, coercion, and error messages automatically. No third-party libraries. Pure Python object protocol.

### `tiny_orm/`
> *Metaclasses · Descriptors · __init_subclass__ · ABCs*

A miniature ORM (Object-Relational Mapper) that demonstrates how frameworks like SQLAlchemy work at the metaclass level. Define a model class, get SQL generation, validation, and field introspection for free. This one breaks your brain. That is the point.

### `async_data_fetcher/`
> *asyncio · Context Managers · Generators · concurrent.futures*

An asynchronous data fetcher that combines `async with`, `async for`, and generator delegation into a coherent system. Benchmarks against synchronous and threaded equivalents.

---

## Current Focus

```python
# Week of: [update this manually every week]
current_chapter = "Chapter 23 — Attribute Descriptors"
current_question = "How does @property actually work under the descriptor protocol?"
currently_building = "projects/config_system — typed descriptors with __set_name__"
```

---

## Experiment Log

Selected entries from `EXPERIMENTS.md` — the things that surprised me:

**`[]` vs `list()` — which is faster and why?**
`[]` is faster. `list()` requires a global lookup and function call overhead. `[]` is a literal — the CPython compiler knows exactly what to do. Measured with `timeit`. The difference is small but the *reason* is fundamental.

**Why can't you use a list as a dict key?**
Because lists are mutable and therefore unhashable. The dict key lookup depends on `hash()`. `hash()` requires that an object's value does not change after hashing — if it did, you could never find it again. Lists can change. Hence: `TypeError: unhashable type: 'list'`. Tuples work because they are immutable.

**`__repr__` vs `__str__` — when does Python call which?**
`__repr__` is for developers: it should be unambiguous and ideally eval()-able back to the object. `__str__` is for end users: readable and human-friendly. When Python needs a string and only `__repr__` is defined, it falls back to `__repr__`. The reverse is not true. Always implement `__repr__`. Implement `__str__` only when you need a different human-facing form.

---

## Tech Stack

```python
environment = {
    "python":     "3.12+",
    "book":       "Fluent Python, 2nd Edition (Ramalho, 2022)",
    "testing":    "pytest",
    "profiling":  ["timeit", "memory_profiler", "cProfile"],
    "notebooks":  "Jupyter Lab",
    "linting":    "ruff",
    "formatting": "black",
    "type_check": "mypy",
}
```

---

## Running the Code

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/pythonic-lab.git
cd pythonic-lab

# Set up environment
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run any module
python 05_functions_as_objects/closures.py

# Run tests
pytest

# Profile a script
python -m cProfile -s cumulative 13_iterators_generators/lazy_loader.py
```

---

## Progress

| Module | Status | Key Files |
|---|---|---|
| 01 — Data Model | ✅ Complete | `card_deck.py`, `vector.py` |
| 02 — Sequences | 🔄 In Progress | `lazy_pipeline.py` |
| 03 — Dicts & Sets | ⏳ Queued | — |
| 04 — Text & Bytes | ⏳ Queued | — |
| 05 — Functions as Objects | ⏳ Queued | — |
| 06–16 | ⏳ Queued | — |
| `sensor_pipeline` project | 🔄 In Progress | — |

---

## Resources

These sit beside the book on the shelf:

- [**Fluent Python, 2nd Ed**](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) — Luciano Ramalho. The text.
- [**Python Data Model Docs**](https://docs.python.org/3/reference/datamodel.html) — The official spec. Read alongside Chapter 1.
- [**Python Glossary**](https://docs.python.org/3/glossary.html) — Underrated. Precise definitions of terms the book uses.
- [**Raymond Hettinger Talks**](https://www.youtube.com/results?search_query=raymond+hettinger+python) — Python core developer. His PyCon talks on itertools, super(), and dataclasses are essential.
- [**Brett Cannon's Blog**](https://snarky.ca/) — CPython internals explained by a core dev.
- [**realpython.com — Descriptors**](https://realpython.com/python-descriptors/) — The clearest external treatment of Chapter 23.

---

## About This Lab

I am a software engineering student, building at the intersection of Python, machine learning, mathematics, and environmental sensing. This repo exists because I believe the only way to truly understand a language is to build things in it — deliberately, curiously, and without shortcuts.

The projects in here are not academic exercises. The sensor pipeline connects to a real IoT system I am deploying to monitor soil carbon and moisture under trees in Uganda. The config system grew from a real need. The ORM exists because I wanted to understand SQLAlchemy, not just use it.

Every commit is a step toward writing Python that is not just correct, but deeply understood.

---

<div align="center">

*"A language that doesn't affect the way you think about programming is not worth knowing."*
— Alan Perlis

**`pythonic-lab`** · Built with curiosity · Kampala, Uganda

![Visitors](https://visitor-badge.liteapp.com/badge?page_id=YOUR_USERNAME.pythonic-lab)

</div>