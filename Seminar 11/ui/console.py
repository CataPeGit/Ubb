from infrastructure.shape_repo import ShapeRepository
from utils.backtrack import permutations, combinations


class Console:
    def __init__(self, shape_repo=None):
        if shape_repo is None:
            self.__shapes = ShapeRepository.generate_repository(10)
        else:
            self.__shapes = shape_repo

    @staticmethod
    def menu_options():
        print(f"{'0':>3} - Exit")
        print(f"{'h':>3} - Print options")
        print(f"{'p':>3} - Print shapes in the repo")
        print(f"{'a':>3} - Add new shape")
        print(f"{'2':>3} - seminar 10. iii. 2 Filter shapes with more than k sides")
        print(f"{'3':>3} - seminar 10. iii. 3 Filter shapes with perimeter higher "
              f"than a given value and name with length")
        print(f"{'4':>3} - seminar 10. iii.4 Sort shapes by perimeter")
        print(f"{'5':>3} - seminar 10. iii.5 Sort shapes by perimeter with names starting with given prefix")
        print()
        print(f"{'6':>3} - Permutations")
        print(f"{'7':>3} - Combinations")

    def start(self):
        Console.menu_options()
        print(self.__shapes)
        choice = input(">>> ")
        while choice != "0":
            if choice == "h":
                Console.menu_options()
            elif choice == "p":
                print(self.__shapes)
            elif choice == "a":
                try:
                    nr_of_sides = int(input("Number of sides: "))
                    length_of_sides = []
                    while len(length_of_sides) < nr_of_sides:
                        try:
                            length_of_sides.append(int(input("Length of side: ")))
                        except ValueError:
                            print("The length of a side should be integer")
                    self.__shapes.add(length_of_sides)
                except ValueError:
                    print("The number of sides should be integer")
            elif choice == "2":
                try:
                    k = int(input("K: "))
                    print("My filter result:\n", self.__shapes.my_more_than_k(k))
                    print("In-built filter result:\n", self.__shapes.in_built_more_than_k(k))
                except ValueError:
                    print("K should be an integer")
            elif choice == "3":
                try:
                    min_input = int(input("Minimum perimeter:"))
                    name_length = int(input("length of the string:"))
                    print("My filter result:\n", self.__shapes.my_higher_perimeter(min_input,name_length))
                    print("In-built filter result:\n", self.__shapes.in_built_higher_perimeter(min_input,name_length))

                except ValueError:
                    print("Minimum perimeter and length of the name should be integers!")
            elif choice == "4":
                desc = input("Do you want to order decreasing? (y/n) ")
                print(self.__shapes.my_sort_by_perimeter(desc in "yY"))
                print(self.__shapes.in_built_sort_by_perimeter(desc in "yY"))
            elif choice == "5":
                desc = input("Do you want to order decreasing? (y/n) ")
                prefix = input("Prefix: ")
                print(self.__shapes.my_sort_by_perimeter_starts_with(prefix, desc in "yY"))
                print(self.__shapes.in_built_sort_by_perimeter_starts_with(prefix, desc in "yY"))
            elif choice == "6":
                try:
                    n = int(input("n = "))
                    print(f"Permutations of {n}:")
                    for permutation in permutations(n):
                        print(f"\t{permutation}")
                except ValueError:
                    print("n should be an integer!")
            elif choice == "7":
                try:
                    n = int(input("n = "))
                    k = int(input("k = "))
                    print(f"Combination of {n} by {k}:")
                    for combination in combinations(range(1, n + 1), k):
                        print(f"\t{combination}")
                except ValueError:
                    print("n and k should be an integer!")
            else:
                print(f"{choice} option not defined")
            choice = input(">>> ")
