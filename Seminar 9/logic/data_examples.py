from logic.recursive import *


def factorial_examples():
    print("Exercise 1.")
    print(f"\tfactorial(0) = {factorial(0)}")
    print(f"\tfactorial(1) = {factorial(1)}")
    print(f"\tfactorial(5) = {factorial(5)}")
    print("-" * 50)
    print()


def fibonacci_examples():
    print("Exercise 2.")
    print(f"\tfibonacci(0) = {fibonacci(0)}")
    print(f"\tfibonacci(1) = {fibonacci(1)}")
    print(f"\tfibonacci(5) = {fibonacci(5)}")
    print("-" * 50)
    print()


def multiplication_examples():
    print("Exercise 3.")
    print(f"\tmultiplication(0) = {multiplication(0)}")
    print(f"\tmultiplication(1) = {multiplication(1)}")
    print(f"\tmultiplication(5) = {multiplication(5)}")
    print("-" * 50)
    print()


def sum_examples():
    print("Exercise 4.")
    print(f"\tsum(0) = {sum(0)}")
    print(f"\tsum(1) = {sum(1)}")
    print(f"\tsum(5) = {sum(5)}")
    print("-" * 50)
    print()


def pascal_examples():
    print("Exercise 5.")
    print(f"\tpascal(1) = {pascal(1)}")
    print(f"\tpascal(2) = {pascal(2)}")
    print(f"\tpascal(3) = {pascal(3)}")
    print(f"\tpascal(4) = {pascal(4)}")
    print(f"\tpascal(5) = {pascal(5)}")
    print("-" * 50)
    print()


def minimum_example():
    print("Exercise 6.a.")
    print(f"\tminimum([]) = {minimum([])}")
    print(f"\tminimum([6] = {minimum([6])}")
    print(f"\tminimum([3, 2, 1]) = {minimum([3, 2, 1])}")
    print(f"\tminimum([4, 2, 5, 1, 6, 3]) = {minimum([4, 2, 5, 1, 6, 3])}")
    print("-" * 50)
    print()


def maximum_example():
    print("Exercise 6.b.")
    print(f"\tmaximum([]) = {maximum([])}")
    print(f"\tmaximum([6] = {maximum([6])}")
    print(f"\tmaximum([3, 2, 1]) = {maximum([3, 2, 1])}")
    print(f"\tmaximum([4, 2, 5, 1, 6, 3]) = {maximum([4, 2, 5, 1, 6, 3])}")
    print("-" * 50)
    print()


def recursive_min_example():
    print("Exercise 7.")
    print(f"\trecursive_min([]) = {recursive_min([])}")
    print(f"\trecursive_min([[2, 9, [1, 13], 8, 6]]) = {recursive_min([[2, 9, [1, 13], 8, 6]])}")
    print(f"\trecursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) = {recursive_min([2, [[13, -7], 90], [1, 100], 8, 6])}")
    print("-" * 50)
    print()


def count_example():
    print("Exercise 8.")
    print(f"\tcount(2, []) = {count(2, [])}")
    print(f"\tcount(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) = {count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]])}")
    print(f"\tcount(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) = {count(7, [[9, [7, 1, 13, 2], 8], [7, 6]])}")
    print("-" * 50)
    print()


def print_all():
    factorial_examples()
    fibonacci_examples()
    multiplication_examples()
    sum_examples()
    pascal_examples()
    minimum_example()
    maximum_example()
    recursive_min_example()
    count_example()
