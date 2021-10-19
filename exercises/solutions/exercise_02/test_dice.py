import pytest
from unittest.mock import patch, Mock


from exercise_02.dice import Dice, Hand


def test_dice_init_raises_value_error():
    with pytest.raises(ValueError):
        Dice(-1)

def test_dice_init_raises_type_error():
    with pytest.raises(TypeError):
        Dice("1")


def test_dice_roll():
    dice = Dice(10)

    with patch('exercise_02.dice.randint', return_value=2):
        dice.roll()

    assert dice.side_up == 2


def test_hand_from_list_of_sides():

    hand = Hand.from_list_of_sides([1, 2])
    assert len(hand.dices) == 2
    assert 1 in [dice.sides for dice in hand.dices]
    assert 2 in [dice.sides for dice in hand.dices]


def test_hand_throw():
    d1 = Dice(6)
    d1.roll = Mock()
    d2 = Dice(6)
    d2.roll = Mock()

    hand = Hand([d1, d2])
    hand.throw()

    d1.roll.assert_called_once()
    d2.roll.assert_called_once()


def test_hand_get_sides_up():
    d1 = Dice(6)
    d2 = Dice(6)
    d3 = Dice(6)
    d1.side_up=1
    d2.side_up=2
    d3.side_up=None

    hand = Hand([d1, d2, d3])
    sides_up = hand.get_sides_up()

    assert len(sides_up) == 2
    assert 1 in sides_up
    assert 2 in sides_up


