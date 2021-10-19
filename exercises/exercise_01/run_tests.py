"""
If you are struggeling with the command
>
> pytest exercises/exercise_01/test_vector.py
>
you can simply run this script
"""


import pytest


def run_tests():
    pytest.main(args=["exercises/exercise_01/test_vector.py"])


if __name__ == "__main__":
    run_tests()
