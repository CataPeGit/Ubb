from UI import *
from classes import *
from tests import *
import matplotlib.pyplot as plt


def command_valid(comm):
    if comm >= 0 and comm <= 12:
        return True
    return False


def menu():

    # we will create some starting points and add them to the repository

    # repository.get_3_data_examples()
    # repository.get_10_data_examples()

    while True:
        commands()

        comm = int(input("Your command: "))

        if command_valid(comm) == False:
            print("Command does not exist! Please enter a valid one.")

        if comm == 0:
            quit()

        if comm == 1:
            # Add a point to the repository
            print()
            print("New point information: ")

            new_x = int(input("x: "))
            new_y = int(input("y: "))
            new_color = input("Color: ")

            new_point = MyPoint(new_x, new_y, new_color)
            repository.add_point(new_point)

        if comm == 2:
            # Get all points in the repository
            all_points = repository.get_all_points()
            for point in all_points:
                print(point.__str__())

        if comm == 3:
            # Get a point at a given index in the repository
            index = int(input("Index: "))
            searched_point = repository.get_point_at_index(index)
            print(searched_point.__str__())

        if comm == 4:
            # Get all points of a given color in the repository
            given_color = input("Color searched: ")
            searched_points = repository.points_of_given_color(given_color)
            for point in searched_points:
                print(point)

        if comm == 5:
            # Get all points that are inside a given square from the repository
            # Given the up-left corner and length of the square
            print("Up-left corner coordinates:")
            x_upLeftCorner = int(input("x: "))
            y_upLeftCorner = int(input("y: "))
            length = int(input("Side length: "))

            print()
            print("Points are: ")

            repository.points_in_square(x_upLeftCorner, y_upLeftCorner, length)

        if comm == 6:
            # Get the minimum distance between two points from the repository
            index1 = int(input("First point index: "))
            index2 = int(input("Second point index: "))
            print(repository.get_distance_between_two_points(index1, index2))

        if comm == 7:
            # Update a point at a given index of the repository
            index = int(input("index: "))
            newX = int(input("New x: "))
            newY = int(input("New y: "))
            newColor = input("New color: ")
            repository.update_point_at_index(index, newX, newY, newColor)

        if comm == 8:
            # Delete the point located at the given index of the repository
            index = int(input("index: "))
            repository.delete_point_at_index(index)

        if comm == 9:
            # Delete all points that are inside a given square from the repository
            # Given the up-left corner and length of the square
            print("Up-left corner coordinates:")
            x_upLeftCorner = int(input("x: "))
            y_upLeftCorner = int(input("y: "))
            length = int(input("Side length: "))
            repository.delete_point_in_square(
                x_upLeftCorner, y_upLeftCorner, length)

        if comm == 10:
            # Plot all points in a chart using the matplotlib library
            repository.plot_points_in_chart()

        if comm == 11:
            # Shift all points on the x axis in the desired way
            way = input("Type + for a rigth shift or - for decreasing x: ")
            repository.shift_points_on_x_axis(way)
            all_points = repository.get_all_points()

            print("Now the points are: ")
            for point in all_points:
                print(point.__str__())

        if comm == 12:
            # test all functions
            run_tests()
            print("Tests are all good!")

        if comm == 13:
            repository.get_3_data_examples()
            print("Examples added!")

        if comm == 14:
            repository.get_10_data_examples()
            print("Examples added!")

        print()
        print()
        print()
        print("------------")
        print()
        print()


repository = PointRepository()
menu()


