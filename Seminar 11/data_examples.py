from utils.sort import *
from utils.search import *
from utils.criterions import *
from utils.backtrack import *


def sort_examples():
    """
    Sort function examples.
    """
    a = [370, 2, 1, 407, 153, 16, 25, 17, 0, 371, 37]
    print(f"\n{a = }")
    print("ii. 1. BUBBLE SORT")
    print(f"\tfunction call:\t bubble_sort(a.copy())")
    print(f"\tinput:\t{a}")
    print(f"\toutput:\t{bubble_sort(a.copy())}")
    print("ii. 2.SELECTION SORT")
    print("\tMINIMUM SELECTION")
    print(f"\t\tfunction call:\t minimum_selection_sort(a.copy())")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{minimum_selection_sort(a.copy())}")
    print("\tMAXIMUM SELECTION")
    print(f"\t\tfunction call:\t maximum_selection_sort(a.copy())")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{maximum_selection_sort(a.copy())}")
    print("ii. 3. INSERTION SORT")
    print(f"\tfunction call:\t insertion_sort(a.copy())")
    print(f"\tinput:\t{a}")
    print(f"\toutput:\t{insertion_sort(a.copy())}")
    print("ii. 4. QUICK SORT")
    print(f"\tfunction call:\t quick_sort(a.copy())")
    print(f"\tinput:\t{a}")
    print(f"\toutput:\t{quick_sort(a.copy())}")


def search_examples():
    """
    Search function examples.
    """
    a = [1, 3, 6, 2, 9, 0, 2]
    print(f"{a = }")
    print("Seminar 9. ii. 1. SEQUENTIAL SEARCH ON UNORDERED LIST")
    print(f"\t{sequential_search_unordered(a, 2) = }")
    print(f"\t{sequential_search_unordered(a, 4) = }")
    print(f"\t{sequential_search_unordered(a, 9) = }")

    a.sort()
    print(f"\n{a = }")
    print("Seminar 9. ii. 1. SEQUENTIAL SEARCH ON ORDERED LIST")
    print(f"\t{sequential_search_ordered(a, 2) = }")
    print(f"\t{sequential_search_ordered(a, 4) = }")
    print(f"\t{sequential_search_ordered(a, 9) = }")

    print(f"\n{a = }")
    print("Seminar 9. ii. 2. BINARY SEARCH")
    print(f"\t{binary_search(a, 2) = }")
    print(f"\t{binary_search(a, 4) = }")
    print(f"\t{binary_search(a, 9) = }")


def filter_examples():
    """
    Filter function examples.
    """
    a = [370, 2, 1, 407, 153, 16, 25, 17, 0, 371, 37]
    print(f"\n{a = }")
    print("FILTER EVEN NUMBERS")
    print(f"\t{in_built_filter(a, is_even) = }")
    print(f"\t{my_filter(a, is_even) = }")
    print("i. 1. FILTER ARMSTRONG NUMBERS")
    print(f"\t{in_built_filter(a, is_armstrong) = }")
    print(f"\t{my_filter(a, is_armstrong) = }")
    print("i. 2. FILTER ARMSTRONG AND EVEN NUMBERS")
    print(f"\t{in_built_filter(a, criterion_i_2) = }")
    print(f"\t{my_filter(a, criterion_i_2) = }")
    print("i. 3. FILTER NUMBERS")
    print(f"\t{in_built_filter(a, criterion_i_3) = }")
    print(f"\t{my_filter(a, criterion_i_3) = }")


def backtracking_examples():
    """
    Examples for algorithms using backtracking.
    """
    print("\nBACKTRACK")
    print("PERMUTATIONS OF 3")
    for permutation in permutations(3):
        print("\t", permutation)
    print("COMBINATION OF [1, 2, 3] in groups of 2")
    for combination in combinations(range(1, 4), 2):
        print("\t", combination)
    print("COMBINATION OF ['a', 'b', 'c'] in groups of 2")
    for combination in combinations(["a", "b", "c"], 2):
        print("\t", combination)
    print("COMBINATION OF even number from [1, 3, 4, 6, 5] in groups of 2")
    for combination in even_combination([1, 3, 4, 6, 5], 2):
        print("\t", combination)


def run_all():
    """
    Print all data examples
    """
    search_examples()
    filter_examples()
    sort_examples()
    backtracking_examples()
