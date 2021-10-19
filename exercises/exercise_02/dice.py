"""
Library for handling dice throws in common games
"""
from __future__ import annotations

from dataclasses import dataclass
from random import randint
from typing import List


class Dice:
    def __init__(self, number_of_sides: int):
        if not isinstance(number_of_sides, int):
            raise TypeError("number_of_sides must be an integer")

        if number_of_sides <= 0:
            raise ValueError("Number of sides must be greater than 0")

        self.sides = number_of_sides
        self.side_up = None

    def roll(self):
        """Roll the dice"""
        self.side_up = randint(1, self.sides)


@dataclass
class Hand:
    """A hand full of dices"""

    dices: List[Dice]
    

    @classmethod
    def from_list_of_sides(cls, sides: List[int]) -> Hand:
        """Creates a Hand of dices from a list

        Parameters
        ----------
        sides : List[int]
            The number of sides of each die
        """
        dices = [Dice(side) for side in sides]
        return Hand(dices)

    def throw(self) -> None:
        for die in self.dices:
            die.roll()

    def get_sides_up(self) -> List[int]:
        return [dice.side_up for dice in self.dices if dice.side_up is not None]

    def __str__(self) -> str:
        sides_up = ", ".join(
            [str(side) for side in self.get_sides_up()]
        )
        return f"{self.__class__.__name__}({sides_up})"


if __name__ == "__main__":
    hand = Hand.from_list_of_sides([3, 6, 7, 8, 12, 20])
    print(hand)

    print("Throw hand")
    hand.throw()
    print(hand)
