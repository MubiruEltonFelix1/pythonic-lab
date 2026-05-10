# 01 Data Model

<div align="left">

![Python](https://img.shields.io/badge/Python-3.12%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)
![Experiment](https://img.shields.io/badge/Experiment-01%20%7C%20Data%20Model-1f2937?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Progress-22c55e?style=for-the-badge)

</div>

Imagine you have a small box on your desk.

At first, it is just a box. But if the box can tell you what is inside, show its label when someone asks for its name, and open itself in a predictable way, it starts to feel less like a plain object and more like something you can naturally work with.

That is the basic idea behind this chapter.

Python is full of objects, and many of them know how to behave in special ways. A few of those behaviors are built in already. When we create our own objects, we can teach Python how they should behave too.

The special method names that make this happen are often called dunder methods because they usually begin and end with double underscores, like `__str__` or `__len__`.

In plain English: Experiment 1 asks, "How can I teach my own object to behave like a normal Python thing?"

## Before You Start (Recommended)

If classes and objects still feel confusing, do this first:

- open `../00_oop_foundations/README.md`
- run `pre_experiment_0.py`

That pre-experiment is intentionally simple and removes most of the OOP confusion before dunder methods.

## What Experiment 1 Is Doing

Experiment 1 uses two tiny examples to show how this works in practice:

- `Vector2D` is a simple 2D point. It learns how to print itself, compare itself, behave like a sequence of numbers, and answer whether it should count as true or false.
- `FrenchDeck` is a small deck of cards. It learns how to act like a normal Python collection so that `len(deck)` and `deck[:3]` work.

The runnable entrypoint is [`experiment_1.py`](experiment_1.py). When you run it, Python will:

- show the vector in a readable form;
- turn the vector into a tuple;
- measure the vector using `abs()`;
- decide whether the vector counts as true;
- treat the deck like a sequence with a size and slices.

So the experiment is not "build a math library". It is "teach a small class to participate in Python's built-in behavior." That is what makes code feel Pythonic.

## Why This Matters

In beginner code, it is common to make objects that only work through custom methods.

That is not wrong. It is usually the first step.

But Pythonic code goes one step further: it lets your object speak the same language as built-in Python types.

That means Python can do useful things with your object automatically, using familiar syntax.

## Normal Object vs Pythonic Object

Imagine a simple `Playlist` object.

### Version 1: Normal beginner style

```python
class Playlist:
	def __init__(self, songs):
		self.songs = songs

	def size(self):
		return len(self.songs)

	def as_text(self):
		return ", ".join(self.songs)

my_list = Playlist(["Numb", "Halo", "Calm Down"])
print(my_list.size())
print(my_list.as_text())
```

This works, but you must remember custom method names like `size()` and `as_text()`.

### Version 2: Pythonic style

```python
class Playlist:
	def __init__(self, songs):
		self.songs = songs

	def __len__(self):
		return len(self.songs)

	def __str__(self):
		return ", ".join(self.songs)

my_list = Playlist(["Numb", "Halo", "Calm Down"])
print(len(my_list))
print(my_list)
```

Now the object behaves like a natural Python collection. That is the difference.

## Why Double Underscores Exist

Double-underscore method names are special protocol names reserved by Python.

Examples:

- `__len__` is what Python checks when you call `len(obj)`.
- `__str__` is what Python checks when you call `print(obj)`.
- `__iter__` is what Python checks before looping over an object.

The syntax looks unusual on purpose. It marks these methods as language hooks, not ordinary app methods.

## Are Dunder Methods Always Needed?

No.

Use normal methods for domain actions:

- `account.deposit(100)`
- `sensor.calibrate()`
- `student.register(course)`

Use dunder methods when you want your object to integrate with Python syntax and built-ins:

- `len(obj)`
- `print(obj)`
- `for x in obj`
- `obj1 == obj2`
- `abs(obj)`

So it is not "always use dunders". It is "use them when you want built-in Python behavior."

## What We Learn

By the end of Experiment 1, you should feel comfortable with these ideas:

- one object can have both a developer-friendly view and a user-friendly view;
- an object can become iterable so Python can unpack or loop through it;
- an object can define its own meaning for `abs()` and truth/false checks;
- a custom collection can support `len()` and slicing with just a few methods.

The bigger lesson: Python gives you a shared behavior contract. If your class follows it, your code becomes easier to read and easier to use.

## What Deviates From Normal Python

The difference from beginner-style code is this:

- beginner style asks you to memorize object-specific method names;
- pythonic style lets you use familiar Python expressions.

In this chapter, instead of creating many custom helper names, I teach the object to answer Python's built-in questions.

That is why this feels different: less custom API, more language integration.

## A Gentle Definition

An object is just a thing with data and behavior.

For example:

- a person object might store a name and know how to introduce itself;
- a bank account object might store a balance and know how to add or subtract money;
- a deck of cards object might store cards and know how to report its size.

The special methods are the hidden hooks Python uses to ask an object to do one of those jobs.

## Simple Case Scenario

Suppose I am building a music app.

I create a `Playlist` object for songs. Later, I want to:

- print the playlist nicely,
- check how many songs it has,
- loop through songs one by one.

If my object is not Pythonic, I need custom method names for each of those actions.

If my object is Pythonic, I can use normal Python:

- `print(playlist)`
- `len(playlist)`
- `for song in playlist`

That is the practical reason dunder methods matter. They let ordinary Python syntax work with your own objects.

## Files

- [`vector.py`](vector.py) - the core data-model example
- [`card_deck.py`](card_deck.py) - the sequence-protocol example
- [`experiment_1.py`](experiment_1.py) - runnable demonstration

## Run It

From inside `01_data_model/`, run:

```bash
python experiment_1.py
```

## My Takeaway So Far

The big lesson is simple: Pythonic code is not about showing off. It is about making objects feel natural to use. Dunder methods help with that by connecting your class to the language features people already know.
