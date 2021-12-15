def is_even(x):
    """
    Defines if a given number is even.
    :param x: given number
    :type x: int
    :return: if the number is even
    :rtype: bool
    """
    return x % 2 == 0


def is_armstrong(x):
    """
    Defines if a given number is an Armstrong number.
    :param x: given number
    :type x: int
    :return: if the number is Armstrong number
    :rtype: bool
    """
    s = 0
    c = x
    while x != 0:
        s += (x % 10)**3
        x //= 10
    return s == c


def is_prime(x):
    """
    Defines if a given number is prime.
    :param x: given number
    :type x: int
    :return: if the number is prime
    :rtype: bool
    """
    if x < 0:
        raise ValueError("Negative number")
    if x > 1:
        for number in range(2, x // 2):
            if x % number == 0:
                return False
        return True
    else:
        return False


def is_perfect_square(x):
    """
    Defines if a given number is perfect square.
    :param x: given number
    :type x: int
    :return: if the number is perfect square
    :rtype: bool
    """
    nr = 2
    if 0 <= x < 2:
        return True
    while nr <= x/2:
        if nr*nr == x:
            return True
        nr += 1
    return False


def condition_i_2(x):
    """
    i. 2.
    Defines if a given number is armstrong and even.
    :param x: given number
    :type x: int
    :return: if the condition is true
    :rtype: bool
    """
    return is_even(x) and is_armstrong(x)


def condition_i_3(x):
    """
    i. 3.
    Defines if a given number is armstrong or even or perfect square or prime.
    :param x: given number
    :type x: int
    :return: if the condition is true
    :rtype: bool
    """
    return is_armstrong(x) or is_even(x) or is_prime(x) or is_perfect_square(x)

