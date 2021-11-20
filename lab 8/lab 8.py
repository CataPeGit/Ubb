from classes import *
from UI import *


def is_int(user_input):
    try:
        int(user_input)
        is_int = True
    except ValueError:
        is_int = False


def check_command(comm):
    if comm >= 0 and comm:
        return True
    return False


def main():
    vector = MyVector(0, "r", 1, [0, 1, 2, 3, 4, 5, 6])

    vectors = VectorRepository(vector)

    while True:

        commands()
        comm = int(input("Your command: "))
        print()

        if comm == 0:
            quit()

        if comm == 1:
            # taking all inputs and checking if the data types are correct
            nameId = input("Name id: ")
            colour = input("Colour: ")
            typeInteger = int(input("Integer type(positive integer): "))
            is_int(typeInteger)

            if typeInteger < 0:
                print("Please input a positive integer greater or equal to 1 ")
                continue

            count = int(
                input("Enter the total count of elements in the vector: "))
            is_int(count)
            vector_elements = []
            for i in range(0, count):
                number = int(input())
                is_int(number)
                vector_elements.append(number)

            vectors.add_a_vector_to_the_repository(
                MyVector(nameId, colour, typeInteger, vector_elements))

        if comm == 2:
            all_vecotors = vectors.get_all_vectors()
            print(all_vecotors)

        print()


main()
