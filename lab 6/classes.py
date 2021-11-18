import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from numpy import sqrt


class MyPoint:

    def __init__(self, coord_x, coord_y, color):
        # initializing the class private variables
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__color = color

    def __str__(self):
        # returnig a string containing information about the point
        return f'Point ({self.__coord_x},{self.__coord_y}) of color {self.__color}.'

    def getValueX(self):
        # returning the point coordinate on the x axis
        return self.__coord_x

    def getValueY(self):
        # returning the point coordinate on the y axis
        return self.__coord_y

    def getColor(self):
        # returning the point color
        return self.__color

    def setCoordX(self, new_coord_x):
        # setting a new value for the x coordinate
        self.__coord_x = new_coord_x

    def setCoordY(self, new_coord_y):
        # setting a new value for the y coordinate
        self.__coord_y = new_coord_y

    def setColor(self, new_color):
        # change the color of the point
        self.__color = new_color


class PointRepository(MyPoint):

    def __init__(self, repository=[]):
        # initializing the repository
        self.__repository = repository.copy()

    def get_all_points(self):
        # Returns a list of all points in the repository
        return self.__repository

    def add_point(self, new_point):
        # adds a new point to the repository
        self.__repository.append(new_point)

    def shift_points_on_x_axis(self, way):
        """
        Shifting the points on the x axis by adding or substracting 1 from the current x
        """
        if way == "+":
            for point in self.__repository:
                x = point.getValueX()
                point.setCoordX(x + 1)
        elif way == "-":
            for point in self.__repository:
                x = point.getValueX()
                point.setCoordX(x - 1)

    def get_point_at_index(self, index):
        # Returns the point found at a given index
        return self.__repository[index]

    def get_distance_between_two_points(self, index1, index2):
        """
        We will get the two points using their index location in the repository
        The distance will be sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
        """
        point1 = self.__repository[index1]
        point2 = self.__repository[index2]
        dist = sqrt(
            (point2.getValueX() - point1.getValueX()) ** 2
            + (point2.getValueY() - point1.getValueY())**2
        )
        return dist

    def points_of_given_color(self, given_color):
        result_points = []
        for point in self.__repository:
            color = point.getColor()
            if color == given_color:
                result_points.append(point)
        return result_points

    def update_point_at_index(self, index, newX, newY, new_color):
        self.__repository[index].setCoordX(newX)
        self.__repository[index].setCoordY(newY)
        self.__repository[index].setColor(new_color)

    def delete_point_at_index(self, index):
        del self.__repository[index]

    def points_in_square(self, x_upLeftCorner, y_upLeftCorner, length):
        all_points = self.__repository.copy()
        for point in all_points:
            x = point.getValueX()
            y = point.getValueY()
            if (x >= x_upLeftCorner and
                x_upLeftCorner + length >= x and
                    y >= y_upLeftCorner - length and y <= y_upLeftCorner):
                print(point.__str__())

    def delete_point_in_square(self, x_upLeftCorner, y_upLeftCorner, length):
        all_points = self.__repository.copy()
        index = 0
        for point in all_points:
            x = point.getValueX()
            y = point.getValueY()
            index += 1
            if (x >= x_upLeftCorner and x_upLeftCorner + length >= x and y >= y_upLeftCorner - length and y <= y_upLeftCorner):
                del all_points[index]
        self.__repository = all_points.copy()

    def plot_points_in_chart(self):
        all_x = []
        all_y = []
        all_colors = []
        for point in self.__repository:
            all_x.append(point.getValueX())
            all_y.append(point.getValueY())
            all_colors.append(point.getColor())

        plt.scatter(all_x, all_y, c=[color for color in all_colors])
        plt.show()

    def get_3_data_examples(self):
        point1 = MyPoint(1, 2, "red")
        point2 = MyPoint(4, 1, "green")
        point3 = MyPoint(2, 7, "blue")

        self.__repository.append(point1)
        self.__repository.append(point2)
        self.__repository.append(point3)

    def get_10_data_examples(self):
        # point 1
        point = MyPoint(6, 4, "aquamarine")
        self.__repository.append(point)

        point = MyPoint(3, 2, "azure")
        self.__repository.append(point)

        point = MyPoint(8, 7, "violet")
        self.__repository.append(point)

        # point 4
        point = MyPoint(1, 9, "brown")
        self.__repository.append(point)

        point = MyPoint(5, 4, "grey")
        self.__repository.append(point)

        point = MyPoint(5, 4, "khaki")
        self.__repository.append(point)

        # point 7
        point = MyPoint(4, 7, "red")
        self.__repository.append(point)

        point = MyPoint(3, 1, "blue")
        self.__repository.append(point)

        point = MyPoint(2, 6, "green")
        self.__repository.append(point)

        # point 10
        point = MyPoint(8, 9, "khaki")
        self.__repository.append(point)
