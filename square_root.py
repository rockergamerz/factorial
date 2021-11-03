def square_root(x):
    if isinstance(x, int):
        if x < 0:
            return (x ** 1/2(i))
        elif x > 0:
            return (x ** 1/2)
    else:
        return "input error"


def test_negative_integer():
    assert square_root(-4) == 2


def test_list():
    assert square_root([2, 3, 5]) == "input error"


def test_positive_integer():
    assert square_root(9) == 3


def test_float():
    assert square_root(10.5) == 3.240370349
