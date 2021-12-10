def sequential_search_unordered(list_of_values, searched_value):
    """
    seminar 9. ii. 1.
    Get the index of the given value in an unordered list.
    :param list_of_values
    :param searched_value
    :return: last index where the value occurrence
    :rtype: int
    """
    index = -1
    for i, x in enumerate(list_of_values):
        if x == searched_value:
            index = i
            # return index --- if we want to return the first occurrence
    return index


def sequential_search_ordered(list_of_values, searched_value):
    """
    seminar 9. ii. 1.
    Get the index of the given value in an ordered list.
    :param list_of_values
    :param searched_value
    :return: first index where the value occurrence
    :rtype: int
    """
    i = 0
    while i < len(list_of_values) and list_of_values[i] < searched_value:
        i += 1
    if list_of_values[i] == searched_value:
        return i
    return -1


def binary_search(list_of_values, searched_value):
    """
    seminar 9. ii. 2.
    Get the index of the given element in an ordered list using binary search.
    :param list_of_values:
    :param searched_value:
    :return: index of the value in the list
    :rtype: int
    """
    if len(list_of_values) == 0:
        return -1
    m = len(list_of_values)//2
    if searched_value == list_of_values[m]:
        return m
    elif searched_value > list_of_values[m]:
        index = binary_search(list_of_values[m+1:], searched_value)
        if index == -1:
            return -1
        else:
            return m + 1 + index
    else:
        return binary_search(list_of_values[:m], searched_value)


def my_filter(list_of_values, criterion):
    """
    Filter elements of the list based on the given condition.
    :param list_of_values:
    :param criterion: function having one parameter defining the condition of inclusion of a value in the result list
    :type: callable (a reference to a function or a lambda expression)
    :return: the filtered list
    :rtype: list
    """
    result_list = []
    for x in list_of_values:
        if criterion(x):
            result_list.append(x)
    return result_list


def in_built_filter(list_of_values, criterion):
    """
    Filter elements of the list based on the given condition using Python's in-built function.
    :param list_of_values:
    :param criterion: function having one parameter defining the condition of inclusion of a value in the result list
    :type: callable (a reference to a function or a lambda expression)
    :return: the filtered list
    :rtype: list
    """
    return list(filter(criterion, list_of_values))


