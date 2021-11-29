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

            if typeInteger < 1:
                print("Please input a positive integer greater or equal to 1.")
                continue

            count = int(
                input("Enter the total count of elements in the vector: "))
            is_int(count)
            vector_elements = []
            print("Values:")
            for i in range(0, count):
                number = int(input())
                is_int(number)
                vector_elements.append(number)

            vectors.add_a_vector_to_the_repository(
                MyVector(nameId, colour, typeInteger, vector_elements))

        if comm == 2:
            # get all vectors
            list = vectors.get_all_vectors()
            print("The vectors are:")
            for item in range(len(list)):
                print(list[item].__str__())

        if comm == 3:
            # get vector at a given index
            index = int(input("Index: "))
            vector = vectors.get_vector_at_given_index(index)
            print(vector.__str__())

        if comm == 4:
            # update vector at a given index
            index = int(input("Index: "))
            new_name = input("New name:")
            new_colour = input("New colour: ")

            new_typeInteger = int(input("New type: "))
            if new_typeInteger < 1:
                print("Please input a positive integer greater or equal to 1.")
                print()
                continue

            count = int(
                input("Enter the total count of elements in the vector: "))
            is_int(count)
            vector_elements = []
            print("Values:")
            for i in range(0, count):
                number = int(input())
                is_int(number)
                vector_elements.append(number)

            vectors.update_vector_at_given_index(
                index, new_name, new_colour, new_typeInteger, vector_elements)

        if comm == 5:
            # update a vector identified by name_id
            name_id_searched = input("Searched name_id: ")
            new_name = input("New name:")
            new_colour = input("New colour: ")

            new_typeInteger = int(input("New type: "))
            if new_typeInteger < 1:
                print("Please input a positive integer greater or equal to 1.")
                print()
                continue

            count = int(
                input("Enter the total count of elements in the vector: "))
            is_int(count)
            vector_elements = []
            print("Values:")
            for i in range(0, count):
                number = int(input())
                is_int(number)
                vector_elements.append(number)

            vectors.update_vector_by_name_id(
                name_id_searched, new_name, new_colour, new_typeInteger, vector_elements)

        if comm == 6:
            # delete vector by index
            index = int(input("Index: "))
            vectors.delete_vector_at_index(index)

        if comm == 7:
            # delete vector by name_id
            name_id_searched = input("Searched name_id: ")
            vectors.delete_vector_by_name(name_id_searched)

        if comm == 8:
            # plot all vectors in a chart based on the type and colour
            vectors.plot_vectors_in_chart()

        if comm == 10:
            vectors.add_4_data_example()

        if comm == 11:
            # function 11
            sum = int(input("Sum searched:"))
            print()
            print(f"The vectors with sum of elements = {sum} have the id's:")
            list = vectors.get_vectors_having_sum(sum)

        if comm == 19:
            # function 19 --- used numpy to delete array
            index1 = int(input("Index 1:"))
            index2 = int(input("Index 2:"))
            vectors.delete_vectors_between(index1, index2)

        if comm == 22:
            # function 22
            # Update the color of a vector identified by name_id.
            id = input("Id to updated:")
            colour = input("New colour:")
            vectors.update_color_by_name_id(id, colour)

        print()


main()
