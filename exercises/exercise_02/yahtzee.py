"""
Yatzehee game rules
https://en.wikipedia.org/wiki/Yahtzee

Not at all a full implementation
"""
from __future__ import annotations


from typing import Callable, Dict
from collections import Counter

from exercise_02.dice import Hand
from exercise_02.yahtzee_rules import *


class Yahtzee:
    rules: Dict[str, Callable] = {
        "Yahtzee": eval_yahtzee,
        "Aces": eval_aces,
        "Twos": eval_twos,
        "Threes": eval_threes,
        "Fours": eval_fours,
        "Fives": eval_fives,
        "Sixes": eval_sixes,
        "Three of a kind": eval_three_of_a_kind,
        "Four of a kind": eval_four_of_a_kind,
        "Full house": eval_full_house,
    }

    def evaluate_hand(self, hand: Hand):
        print(hand)
        sides = hand.get_sides_up()
        summary = Counter(sides)
        print("\nWhat you have on hand")
        print("---------------------")
        for name, evaluation in self.rules.items():
            if evaluation(summary):
                print(name)


if __name__ == "__main__":
    yahtzee = Yahtzee()

    hand = Hand.from_list_of_sides([6] * 5)
    hand.throw()
    yahtzee.evaluate_hand(hand)

