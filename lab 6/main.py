# got problem 16

class MyPoint:

    def __init__(self, coord_x, coord_y, color):
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__color = color

    def __str__(self):
        return f'Point ({self.__coord_x},{self.__coord_y}) of color {self.__color}.'

    def getValueX(self):
        return self.__coord_x

    def getValueY(self):
        return self.__coord_y

    def getColor(self):
        return self.__color

    def setCoordX(self, new_coord_x):
        self.__coord_x = new_coord_x

    def setCoordY(self, new_coord_y):
        self.__coord_y = new_coord_y


class PointRepository(MyPoint):

    def __init__(self, repository=[]):
        # super().__init__()
        self.__repository = repository.copy()

    def get_all_points(self):
        # Returns a list of all points
        return self.__repository

    def add_point(self, new_point):
        # adds a new point to the repository
        self.__repository.append(new_point)

    def shift_points_on_x_axis(self, way):
        # we will shift the points on the x axis by adding 1 to the current x
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

    def points_of_given_color(self, given_color):
        result_points = []
        for point in self.__repository:
            color = point.getColor()
            if color == given_color:
                result_points.append(point)
        return result_points


def commands():
    print("0 -> Quit program")
    print("1 -> Add a point to the repository")
    print("2 -> Get all points")  # function 2
    print("3 -> Get all points that are inside a given square")  # function 5
    print("4 -> Get a point at a given index ")
    print("5 -> Shift all points on the x axis")
    print("6 -> Get all points of a given color")


def menu():

    # we will create some starting points and add them to the repository

    repository = PointRepository()

    point1 = MyPoint(1, 2, "red")
    point2 = MyPoint(4, 1, "green")
    point3 = MyPoint(2, 7, "blue")

    repository.add_point(point1)
    repository.add_point(point2)
    repository.add_point(point3)

    """
    points = repository.get_all_points()

    print(points)
    print()
    print()
    print()
    print("------------")
    print()
    print()
    """
    while True:
        commands()

        comm = int(input("Your command: "))

        if comm == 0:
            quit()

        if comm == 1:
            print()
            print("New point information: ")

            new_x = int(input("x: "))
            new_y = int(input("y: "))
            new_color = input("Color: ")
            new_point = MyPoint(new_x, new_y, new_color)

            repository.add_point(new_point)

        if comm == 2:
            all_points = repository.get_all_points()
            for point in all_points:
                print(point.__str__())

        if comm == 3:
            # up-left corner and length given
            print("Up-left corner coordinates:")
            x_upLeftCorner = int(input("x: "))
            y_upLeftCorner = int(input("y: "))
            length = int(input("Side length: "))

            print()
            print("Points are: ")

            all_points = repository.get_all_points()
            for point in all_points:
                x = point.getValueX()
                y = point.getValueY()
                if (x >= x_upLeftCorner and
                    x_upLeftCorner + length >= x and
                        y >= y_upLeftCorner - length and y <= y_upLeftCorner):
                    print(point.__str__())

        if comm == 4:
            index = int(input("Index: "))
            searched_point = repository.get_point_at_index(index)
            print(searched_point.__str__())

        if comm == 5:
            way = input("Type + for a rigth shift or - for decreasing x: ")
            repository.shift_points_on_x_axis(way)
            all_points = repository.get_all_points()

            print("Now the points are: ")
            for point in all_points:
                print(point.__str__())

        if comm == 6:
            given_color = input("Color searched: ")
            searched_points = repository.points_of_given_color(given_color)
            for point in searched_points:
                print(point)

        print()
        print()
        print()
        print("------------")
        print()
        print()


menu()


"""





---

    repository.append(MyPoint(1, 2, "red"))
    repository.append(MyPoint(1, 5, "blue"))
    repository.append(MyPoint(4, 3, "green"))

    while True:

        comm = int(input("Your command: "))

        if comm == 0:
            quit()

        if comm == 1:



def commands():
    print("0 -> Quit program")
    print("1 -> Get and set the value of all properties for a point")
    print("2 -> Provide the representation of a point")



---


    print("Point coordinates:")
    x = int(input("X: "))
    y = int(input("Y: "))
    color = input("Color: ")

    point = MyPoint(x, y, color)

    print()
    commands()
    comm = int(input("Your command: "))

    if comm == 0:
        quit()

    if comm == 1:
        x = int(input("New x coordinate:"))
        MyPoint.__setCoordX(point.__coord_x)

        print(point.__coord_x)

        print("New y coordinate:")
        MyPoint.__setCoordY(point.__coord_y)

    if comm == 2:
        print(MyPoint.__str__(point))

     """


