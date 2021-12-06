def factorial(n):
    """
    ex. 1
    Calculating the factorial of a given number.
    n! = 1 * 2 * ... * n
    n! = n * (n-1)!
    :param n: given number
    :type n: int
    :return: factorial of the number
    :rtype:int
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    """
    ex. 2
    Calculating the n-th element of the Fibonacci sequence.
    fibonacci(0) = 1
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    :param n: given number
    :type n: int
    :return: n-th element of the Fibonacci sequence
    :rtype: int
    """
    if n < 0:
        raise ValueError("Only positive numbers")
    elif n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def multiplication(n):
    """
    ex. 3
    Calculate recursively the function f(n) = 3 * n
    f(0) = 0
    f(n) = 3 + 3 + ... + 3 (n times)
    f(n) = 3 + f(n - 1)
    :param n: given number
    :type n: int (greater than 0
    :return:
    :rtype: int
    """
    if n < 0:
        raise ValueError("Function not defined for negative numbers")
    elif n == 0:
        return 0
    else:
        return 3 + multiplication(n - 1)


def sum(n):
    """
    ex. 4
    Calculating the sum of first n integers.
    sum(n) = 1 + 2 + ... + n
    sum(n) = n + sum(n - 1)
    :param n: given number
    :type n: int
    :return: sum of elements till n
    :rtype: int
    """
    if n < 0:
        raise ValueError("Function not defined for negative numbers")
    elif n == 0:
        return 0
    else:
        return n + sum(n - 1)


def pascal(n):
    """
    ex. 5
    Calculating the n-th line in Pascal's triangle.
    1
    1 1
    1 2 1
    1 3 3 1
    :param n: number of the row
    :type n: int
    :return: the n-th line of the triangle
    :rtype: list
    """
    if n < 1:
        raise ValueError("The number of the row should be greater than 0")
    elif n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n - 1)
        for i in range(len(previous_line) - 1):
            line += [previous_line[i] + previous_line[i + 1]]
        line += [1]
        return line


def minimum(list_of_values):
    """
    ex. 6.a
    Calculating the minimum value of a list
    :param list_of_values: list of integer number
    :type list_of_values: list
    :return: minimum value of the list
    :rtype: int
    """
    if len(list_of_values) == 0:
        return None
    elif len(list_of_values) == 1:
        return list_of_values[0]
    else:
        return min(list_of_values[0], minimum(list_of_values[1:]))


def maximum(list_of_values):
    """
    ex. 6.b
    Calculating the maximum value of a list
    :param list_of_values: list of integer number
    :type list_of_values: list
    :return: maximum value of the list
    :rtype: int
    """
    if len(list_of_values) == 0:
        return None
    elif len(list_of_values) == 1:
        return list_of_values[0]
    else:
        return max(list_of_values[0], maximum(list_of_values[1:]))


def recursive_min(list_of_values):
    """
    ex. 7.
    Calculating the minimum value of a nested list.
    :param list_of_values: list of integers
    :type list_of_values: list
    :return: minimum value of the nested list
    :rtype: int
    """
    if len(list_of_values) == 0:
        return None
    elif len(list_of_values) == 1:
        if isinstance(list_of_values[0], list):
            return recursive_min(list_of_values[0])
        else:
            return list_of_values[0]
    else:
        current_minimum = list_of_values[0]
        if isinstance(list_of_values[0], list):
            current_minimum = recursive_min(list_of_values[0])
        return min(current_minimum, recursive_min(list_of_values[1:]))


def count(value, list_of_values):
    """
    ex. 8.
    Calculating the occurence of the given value in the specified nested list.
    :param value: given value
    :type value: int
    :param list_of_values: list of integers
    :type list_of_values: list
    :return: number of occurence of the value in the given list
    :rtype: int
    """
    if len(list_of_values) == 0:
        return 0
    else:
        if isinstance(list_of_values[0], list):
            return count(value, list_of_values[0]) + count(value, list_of_values[1:])
        else:
            return int(value == list_of_values[0]) + count(value, list_of_values[1:])
