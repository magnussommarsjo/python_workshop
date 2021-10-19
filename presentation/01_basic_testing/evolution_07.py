import pytest


def my_div(a, b):
    return a/b


def test_my_div():
    assert my_div(4, 2) == 2, "Passing Test"


def test_my_div_raises_error():
    with pytest.raises(ZeroDivisionError):
        my_div(4, 0)


if __name__ == "__main__":
    pytest.main(args = ['presentation/01_basic_testing/evolution_07.py'])
