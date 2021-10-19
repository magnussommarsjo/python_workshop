
from unittest.mock import Mock, call, patch

from exercise_02.yahtzee import Hand, Yahtzee


def test_yahtzee_evaluate_hand():
    hand = Hand([])
    hand.get_sides_up = Mock(return_value=[6]*6)

    yahtzee = Yahtzee()
    with patch('builtins.print') as mock_print:
        yahtzee.evaluate_hand(hand)
    
    calls = [
        call("Sixes"),
        call("Three of a kind"),
        call("Four of a kind"),
    ]
    mock_print.assert_has_calls(calls, any_order=True)


