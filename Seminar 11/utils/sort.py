def bubble_sort(our_list):
    """
    seminar 10. ii. 1.
    Ordering a list of values using bubble sort.
    :param our_list: list of values
    :type our_list: list
    :return: ordered list
    :rtype: list
    """
    swapped = True
    iterations = 0

    while swapped:
        swapped = False
        for i in range(len(our_list) - iterations - 1):
            if our_list[i] > our_list[i+1]:
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                swapped = True
        iterations += 1
    return our_list


def minimum_selection_sort(list_of_values):
    """
    seminar 10. ii. 2.
    Ordering a list of values using minimum selection sort.
    :param list_of_values: list of values
    :type list_of_values: list
    :return: ordered list
    :rtype: list
    """
    for i in range(len(list_of_values)):
        minimum = list_of_values[i]
        minimum_position = i
        for j in range(i + 1, len(list_of_values)):
            if minimum > list_of_values[j]:
                minimum = list_of_values[j]
                minimum_position = j
        list_of_values[i], list_of_values[minimum_position] = list_of_values[minimum_position], list_of_values[i]
    return list_of_values


def maximum_selection_sort(list_of_values):
    """
    seminar 10. ii. 2.
    Ordering a list of values using maximum selection sort.
    :param list_of_values: list of values
    :type list_of_values: list
    :return: ordered list
    :rtype: list
    """
    for i in range(len(list_of_values) - 1,  -1,  -1):
        maximum = list_of_values[i]
        maximum_position = i
        for j in range(i):
            if maximum < list_of_values[j]:
                maximum = list_of_values[j]
                maximum_position = j
        list_of_values[i], list_of_values[maximum_position] = list_of_values[maximum_position], list_of_values[i]
    return list_of_values


def not_bubble_sort(list_of_values):
    """
    Sort a list with values in ascending order (not Bubble sort).
    :param list_of_values:
    :return: sorted list of values
    :rtype: list
    """
    for i in range(len(list_of_values) - 1):
        for j in range(i, len(list_of_values)):
            if list_of_values[i] > list_of_values[j]:
                list_of_values[i], list_of_values[j] = list_of_values[j], list_of_values[i]
    return list_of_values


def insertion_sort(list_of_values):
    """
    ii. 3
    Sorting the values of a given list in ascending order using insertion sort.
    :param list_of_values:
    :return: ordered list
    :rtype: list
    """
    for i in range(1, len(list_of_values)):
        searched_value = list_of_values[i]
        # iterating through the ordered part of the list
        for j in range(i + 1):
            if list_of_values[j] > searched_value:
                break
        list_of_values = list_of_values[:j] + [searched_value] + list_of_values[j:i] + list_of_values[i + 1:]
    return list_of_values


import numpy as np
import random
def quick_sort(list_of_values):
    """
    ii. 4
    Sorting the values of a given list in ascending order using quick sort.
    :param list_of_values:
    :return: ordered list
    :rtype: list
    """
    if len(list_of_values) <= 1:
        return list_of_values

    pivot = np.random.choice(list_of_values)
    # pivot = list_of_values[random.randint(0, len(list_of_values) - 1)]

    lower, same, higher = [], [], []
    for value in list_of_values:
        if value < pivot:
            lower.append(value)
        elif value == pivot:
            same.append(value)
        else:
            higher.append(value)

    return quick_sort(lower) + same + quick_sort(higher)


def my_sort(list_of_values, condition):
    """
    Sorting the values of a given list based on a given condition using bubble sort.
    :param list_of_values:
    :param condition: function having two parameters defining the correct relation between two elements in the list
    :type: callable (a reference to a function or a lambda expression)
    :return: ordered list
    :rtype: list
    """
    swapped = True
    iterations = 0

    while swapped:
        swapped = False
        for i in range(len(list_of_values) - iterations - 1):
            if not condition(list_of_values[i], list_of_values[i + 1]):
                list_of_values[i], list_of_values[i + 1] = list_of_values[i + 1], list_of_values[i]
                swapped = True
        iterations += 1
    return list_of_values


def in_built_sort(list_of_values, condition):
    """
    Sorting the values of a given list based on a given condition using insertion sort.
    :param list_of_values:
    :param condition: function having two parameters defining the correct relation between two elements in the list
    :type: callable (a reference to a function or a lambda expression)
    :return: ordered list
    :rtype: list
    """
    return sorted(list_of_values, key=condition)
