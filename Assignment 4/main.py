from numpy import True_
from classes import *
from UI import *
from tests import *


def is_int(user_input):
    # check if input is integer
    try:
        int(user_input)
        return True
    except ValueError:
        print("Please enter a integer!")
        return False


def check_command(comm):
    # Check if command exists
    if comm >= 0 and comm:
        return True
    return False


def check_comm(comm):
    if comm >= 0 and comm <= 13:
        return True
    return False


def check_colour(colour):
    if str(colour) == "r" or colour == "g" or colour == "b" or colour == "y" or colour == "m":
        return True
    print("Color used is not good (possible values are ‘r’, ‘g’, ‘b’, ‘y’ and ‘m’).")
    print()
    return False


def main():
    vectors = VectorRepository()

    vectors.add_a_vector_to_the_repository(MyVector("v1", "r", 1, [1, 3, 4]))
    vectors.add_a_vector_to_the_repository(MyVector("v2", "g", 1, [1, 2]))
    vectors.add_a_vector_to_the_repository(MyVector("v3", "b", 1, [6, 7]))
    vectors.add_a_vector_to_the_repository(MyVector("v4", "y", 1, [7, 4]))
    vectors.add_a_vector_to_the_repository(MyVector("v5", "m", 1, [9, 8]))

    while True:

        commands()
        comm = int(input("Your command: "))

        if check_comm(comm) == False:
            print("Please enter a valid command!")
            print()
            continue

        print()

        # controller
        if comm == 0:
            quit()

        if comm == 1:
            # taking all inputs and checking if the data types are correct
            nameId = input("Name id: ")
            if vectors.check_id(nameId) == False:
                print("Id is already taken!")
                print()
                continue

            colour = input("Colour (one letter): ")[0].lower()
            if check_colour(colour) == False:
                continue

            try:
                typeInteger = int(input("Integer type(positive integer): "))
                if is_int(typeInteger) == False:
                    continue

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
            except ValueError:
                print("Please enter a integer!")

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
            if vectors.check_id(new_name) == False:
                print("Id is already taken!")
                print()
                continue
            new_colour = input("New colour: ")[0].lower()
            if check_colour(new_colour) == False:
                continue
            else:
                try:
                    new_typeInteger = int(input("New type: "))
                    if new_typeInteger < 1:
                        print(
                            "Please input a positive integer greater or equal to 1.")
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
                except ValueError:
                    print("Please enter a integer!")

        if comm == 5:
            # update a vector identified by name_id
            name_id_searched = input("Searched name_id: ")
            new_name = input("New name:")
            if vectors.check_id(new_name) == False:
                print("Id is already taken!")
                print()
                continue

            new_colour = input("New colour: ")[0].lower()
            try:
                new_typeInteger = int(input("New type: "))
                if new_typeInteger < 1:
                    print("Please input a positive integer greater or equal to 1.")
                    print()
                    continue
                if check_colour(new_colour) == False:
                    continue
                else:
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
            except ValueError:
                print("Please enter a integer!")

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

        if comm == 9:
            # function 11
            # Get the list of vectors having a given sum of elements
            sum = int(input("Sum searched:"))
            print()
            print(f"The vectors with sum of elements = {sum} have the id's:")
            list = vectors.get_vectors_having_sum(sum)

        if comm == 10:
            # function 19
            # Delete all vectors that are between two given indexes
            index1 = int(input("Index 1:"))
            index2 = int(input("Index 2:"))
            vectors.delete_vectors_between(index1, index2)

        if comm == 11:
            # function 22
            # Update the color of a vector identified by name_id
            id = input("Id to updated:")
            colour = input("New colour:")[0].lower()
            if check_colour(colour) == False:
                continue
            else:
                vectors.update_color_by_name_id(id, colour)

        if comm == 12:
            vectors.add_4_data_example()

        if comm == 13:
            if __name__ == "__main__":
                unittest.main()

        print()


main()

