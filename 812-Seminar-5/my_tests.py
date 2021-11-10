from point_list import distance, increase_x, k_closest, highest_distance


def test_distance():
    try:
        distance([], 1, 2)
        assert False
    except IndexError:
        assert True

    assert distance([[1, 1], [1, 1]], 0, 1) == 0
    assert distance([[0, 0], [1, 1]], 0, 1) == 2**(1/2)


def test_increase_x():
    assert increase_x([[1, 1], [3, 1]], -1) == [[0, 1], [2, 1]]
    assert increase_x([[1, 2], [4, 1]], 2) == [[3, 2], [6, 1]]
    assert increase_x([], 5) == []


def test_k_closest():
    try:
        k_closest([], 1, 1)
        assert False
    except IndexError:
        assert True

    try:
        k_closest([[1, 2]], 0, -1)
        assert False
    except ValueError:
        assert True

    try:
        k_closest([[1, 2]], 0, 2)
        assert False
    except ValueError:
        assert True

    assert k_closest([[0, 0], [0, 1], [0, 2]], 0, 1) == [[0, 1]]


def test_highest_distance():
    assert highest_distance([]) is None
    assert highest_distance([[1, 1]]) is None
    assert highest_distance([[0, 0], [0, 1], [0, 2]]) == 2.0


# tests for filter_color, same_color_distance and same_color_k_closest should be included
# functions with file operations don't have to be tested


def all_tests():
    test_distance()
    test_increase_x()
    test_k_closest()
    test_highest_distance()
