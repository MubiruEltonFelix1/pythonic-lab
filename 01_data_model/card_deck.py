"""A tiny playing-card deck example for data-model experiments."""

from __future__ import annotations

from dataclasses import dataclass
from random import choice

RANKS = [str(n) for n in range(2, 11)] + list("JQKA")
SUITS = "spades diamonds clubs hearts".split()


@dataclass(frozen=True, slots=True)
class Card:
    rank: str
    suit: str


class FrenchDeck:
    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position: int) -> Card:
        return self._cards[position]

    def draw_random(self) -> Card:
        return choice(self._cards)
