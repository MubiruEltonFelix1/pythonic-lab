"""Runnable walkthrough for Experiment 1.

This script shows how Python can use a user-defined object through its own
built-in behaviors when the right special methods are implemented.
"""

from __future__ import annotations

from card_deck import FrenchDeck
from vector import Vector2D


def main() -> None:
    vector = Vector2D(3, 4)
    print("Experiment 1: teaching Python to treat custom objects like native values")
    print("vector repr:", repr(vector))
    print("vector str:", str(vector))
    print("vector as tuple:", tuple(vector))
    print("vector magnitude:", abs(vector))
    print("vector is truthy:", bool(vector))
    print("vector equals another:", vector == Vector2D(3, 4))

    deck = FrenchDeck()
    print("deck size:", len(deck))
    print("top three cards:", deck[:3])
    print("random card:", deck.draw_random())


if __name__ == "__main__":
    main()
