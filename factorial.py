def factorial(x):
    if isinstance(x, int):
        if x < 0:
            return "cannot be determined"
        elif x > 0:

            # total = 1
            # for i in range(1, x+1):
            #     total *= i
            return x * factorial(x-1)

        elif x == 0:
            return 1
        else:
            return "input error"


def test_factorial_zero():
    assert factorial(0) == 1


def test_negative_number():
    assert factorial(-1) == "cannot be determined"


def test_list():
    assert factorial([1, 2, 3]) == "input error"


def test_positive_int():
    assert factorial(5) == 120


print(factorial(5))
