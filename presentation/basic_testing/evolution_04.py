
def my_div(a, b):
    return a/b


def test_my_div():
    assert my_div(4, 2) == 2, "Passing Test"

    assert my_div(4, 0) == 2, "Failing Test"

if __name__ == "__main__":
    test_my_div()
