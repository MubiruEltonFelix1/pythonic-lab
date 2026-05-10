"""A small 2D vector used to explore Python's data model."""

from __future__ import annotations

from math import hypot
from typing import Iterator


class Vector2D:
    """Two-dimensional vector with a few core data model methods."""

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x!r}, y={self.y!r})"

    def __str__(self) -> str:
        return f"({self.x:g}, {self.y:g})"

    def __iter__(self) -> Iterator[float]:
        yield self.x
        yield self.y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __abs__(self) -> float:
        return hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))
