"""Pre-Experiment 0: beginner OOP foundations before dunder methods."""

from __future__ import annotations


class Playlist:
    """A tiny object used to explain class and instance ideas."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.songs: list[str] = []

    def add_song(self, title: str) -> None:
        self.songs.append(title)

    def play(self) -> str:
        if not self.songs:
            return f"{self.name} has no songs yet."
        return f"Now playing: {self.songs[0]}"

    def describe(self) -> str:
        return f"Playlist(name={self.name}, songs={len(self.songs)})"


def main() -> None:
    print("Pre-Experiment 0: Classes and Objects")
    print("A class is a blueprint. An object is a real thing made from it.\n")

    study_mix = Playlist("Study Mix")
    chill_mix = Playlist("Chill Mix")

    study_mix.add_song("River Flows in You")
    study_mix.add_song("Experience")
    chill_mix.add_song("Sunset Lover")

    print("These are two different objects from the same class:")
    print("-", study_mix.describe())
    print("-", chill_mix.describe())

    print("\nEach object can do things through methods:")
    print("-", study_mix.play())
    print("-", chill_mix.play())

    print("\nWhy this matters:")
    print("Once this feels natural, dunder methods in Experiment 1 will feel less scary.")
    print("They are just extra hooks that make objects work with Python syntax.")


if __name__ == "__main__":
    main()
