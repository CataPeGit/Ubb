from logic.recursive import *


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    try:
        factorial(-1)
        assert False
    except ValueError:
        assert True


def test_fibonacci():
    assert fibonacci(0) == 1
    assert fibonacci(1) == 1
    assert fibonacci(5) == 8
    try:
        fibonacci(-1)
        assert False
    except ValueError:
        assert True


def test_multiplication():
    assert multiplication(0) == 0
    assert multiplication(1) == 3
    assert multiplication(5) == 15
    try:
        multiplication(-1)
        assert False
    except ValueError:
        assert True


def test_sum():
    assert sum(0) == 0
    assert sum(1) == 1
    assert sum(5) == 15
    try:
        sum(-1)
        assert False
    except ValueError:
        assert True


def test_pascal():
    assert pascal(1) == [1]
    assert pascal(2) == [1, 1]
    assert pascal(5) == [1, 4, 6, 4, 1]
    try:
        pascal(-1)
        assert False
    except ValueError:
        assert True


def test_minimum():
    assert minimum([]) is None
    assert minimum([6]) == 6
    assert minimum([3, 2, 1]) == 1
    assert minimum([4, 2, 5, 1, 6, 3]) == 1


def test_maximum():
    assert maximum([]) is None
    assert maximum([6]) == 6
    assert maximum([3, 2, 1]) == 3
    assert maximum([4, 2, 5, 1, 6, 3]) == 6


def test_recursive_min():
    assert recursive_min([]) is None
    assert recursive_min([[2, 9, [1, 13], 8, 6]]) == 1
    assert recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7


def test_count():
    assert count(2, []) == 0
    assert count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4
    assert count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2


def run_all():
    test_factorial()
    test_fibonacci()
    test_multiplication()
    test_sum()
    test_pascal()
    test_minimum()
    test_maximum()
    test_recursive_min()
    test_count()
    print("All tests passed\n")
