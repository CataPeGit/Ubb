from program_functions import *

# we will test our functions using the following list


def reset_test_list():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def run_tests():
    """
    Run all tests
    """

    test_list = reset_test_list()
    test_add_number(test_list)

    test_list = reset_test_list()
    test_insert_number(test_list)

    test_list = reset_test_list()
    test_remove_index(test_list)

    test_list = reset_test_list()
    test_remove_between(test_list)

    test_list = reset_test_list()
    test_replace(test_list)

    test_list = reset_test_list()
    test_less(test_list)

    test_list = reset_test_list()
    test_sorted_by_score(test_list)

    test_list = reset_test_list()
    test_sorted_higher(test_list)

    test_list = reset_test_list()
    test_avg(test_list)

    test_list = reset_test_list()
    test_minimum_between(test_list)

    test_list = reset_test_list()
    test_mul(test_list)

    test_list = reset_test_list()
    test_filter_mul(test_list)

    test_list = reset_test_list()
    test_filter_greater(test_list)

    test_list = reset_test_list()
    test_undo(test_list)

    print("All tests are good!")


def test_add_number(test_list):  # 1
    """
    We will add a element and check if it is saved
    """
    add_number(test_list, 456)
    assert test_list[len(test_list) - 1] == 456
    add_number(test_list, 27)
    assert test_list[len(test_list) - 1] == 27
    add_number(test_list, 24)
    assert test_list[len(test_list) - 1] == 24


def test_insert_number(test_list):  # 2
    """
    We will add a element at a given index and see if it is saved 
    """
    insert_number(test_list, 1, 456)
    assert test_list[1] == 456
    insert_number(test_list, 5, 56)
    assert test_list[5] == 56
    insert_number(test_list, 8, 89)
    assert test_list[8] == 89


def test_remove_index(test_list):  # 3
    """
    We will remove an element from the list and see if it has been deleted
    We know that innitialy test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    remove_index(test_list, 7)
    assert test_list[7] == 8
    remove_index(test_list, 4)
    assert test_list[4] == 5
    remove_index(test_list, 1)
    assert test_list[1] == 2


def test_remove_between(test_list):  # 4
    """
    Testing remove_between(score_list, from_index, to_index)
    """
    remove_between(test_list, 6, 8)
    assert test_list[6] == 9
    remove_between(test_list, 4, 4)
    assert test_list[4] == 5
    remove_between(test_list, 1, 2)
    assert test_list[1] == 3


def test_replace(score_list):  # 5
    """
    Testing test_replace(score_list, index, new_value)
    """
    replace(score_list, 4, 56)
    assert score_list[4] == 56
    replace(score_list, 7, 465)
    assert score_list[7] == 465
    replace(score_list, 1, 9)
    assert score_list[1] == 9


def test_less(score_list):  # 6
    """
    Testing less(score_list, value)
    """
    list = less(score_list, 4)
    for number in range(len(list)):
        assert list[number] == number


def test_sorted_by_score(score_list):  # 7
    """
    Testing sorted_by_score(score_list)
    """
    list = sorted_by_score(score_list)
    assert list[3] == 6
    assert list[0] == 9
    assert list[1] == 8


def test_sorted_higher(score_list):  # 8
    """
    Testing sorted_higher(score_list, value)
    """
    list = sorted_higher(score_list, 5)
    assert list[0] == 6
    assert list[1] == 7
    assert list[2] == 8


def test_avg(score_list):  # 9
    """
    Testing avg(score_list, from_index, to_index)
    """
    assert avg(score_list, 3, 5) == 4
    assert avg(score_list, 1, 3) == 2
    assert avg(score_list, 7, 9) == 8


def test_minimum_between(score_list):  # 10
    """
    Testing minimum_between(score_list, from_index, to_index)
    """
    assert minimum_between(score_list, 3, 6) == 3
    assert minimum_between(score_list, 0, 6) == 0
    assert minimum_between(score_list, 7, 9) == 7


def test_mul(score_list):  # 11
    """
    Testing mul(score_list, value, from_index, to_index)
    """
    list = mul(score_list, 2, 1, 8)
    assert list[0] == 4
    assert list[1] == 6
    assert list[2] == 8


def test_filter_mul(score_list):  # 12
    """
    Testing filter_mul(score_list, value)
    """
    list = filter_mul(score_list, 2)
    assert list[0] == 4
    assert list[1] == 6
    assert list[2] == 8


def test_filter_greater(score_list):  # 13
    """
    Testing filter_greater(score_list, value)
    """
    list = filter_greater(score_list, 5)
    assert list[0] == 6
    assert list[1] == 7
    assert list[3] == 9


def test_undo(test_list):  # 14
    """
    Testing undo function
    """
    insert_number(test_list, 4, 45)
    undo(test_list)
    assert test_list[4] == 4
    insert_number(test_list, 7, 74)
    undo(test_list)
    assert test_list[7] == 7
    insert_number(test_list, 0, 65)
    undo(test_list)
    assert test_list[0] == 0


# We will test undo() with a copy of a the main function but with different variables
global last_score_list_test
last_score_list_test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_undo(test_list):  # press 14
    global last_score_list_test
    test_list = last_score_list_test.copy()
    return test_list


def test_save_list(test_list):
    global last_score_list_test
    last_score_list_test = test_list.copy()
