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

    vectors = VectorRepository()

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
            # function 11
            sum = int(input("Sum searched:"))
            print()
            print(f"The vectors with sum of elements = {sum} have the id's:")
            list = vectors.get_vectors_having_sum(sum)

        if comm == 3:
            # function 19 --- used numpy to delete array
            index1 = int(input("Index 1:"))
            index2 = int(input("Index 2:"))
            vectors.delete_vectors_between(index1, index2)

        if comm == 4:
            # function 22
            # Update the color of a vector identified by name_id.
            id = input("Id to updated:")
            colour = input("New colour:")
            vectors.update_color_by_name_id(id, colour)

        if comm == 5:
            vectors.add_4_data_example()

        if comm == 6:
            list = vectors.get_all_vectors()
            print("The vectors are:")
            for item in range(len(list)):
                print(list[item].__str__())

        if comm == 7:
            index = int(input("Index: "))
            vectors.get_vector_at_given_index(index)

        print()


main()
