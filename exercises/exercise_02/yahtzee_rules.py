"""
Yatzehee game rules
https://en.wikipedia.org/wiki/Yahtzee

Not at all a full implementation
"""

from typing import Dict


def eval_yahtzee(summary: Dict) -> bool:
    return len(summary) == 1 and summary.values() == 5


def eval_aces(summary: Dict) -> bool:
    return any(key == 1 for key in summary.keys())


def eval_twos(summary: Dict) -> bool:
    return any(key == 2 for key in summary.keys())


def eval_threes(summary: Dict) -> bool:
    return any(key == 3 for key in summary.keys())


def eval_fours(summary: Dict) -> bool:
    return any(key == 4 for key in summary.keys())


def eval_fives(summary: Dict) -> bool:
    return any(key == 5 for key in summary.keys())


def eval_sixes(summary: Dict) -> bool:
    return any(key == 6 for key in summary.keys())


def eval_three_of_a_kind(summary: Dict) -> bool:
    return any(value >= 3 for value in summary.values())


def eval_four_of_a_kind(summary: Dict) -> bool:
    return any(value >= 4 for value in summary.values())


def eval_full_house(summary: Dict) -> bool:
    return 3 in summary.values() and 2 in summary.values()
