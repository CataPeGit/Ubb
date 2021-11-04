

class MyPoint:

    def __init__(self, coord_x, coord_y, color):
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__color = color

    def __str__(self):
        return f'Point ({self.__coord_x},{self.__coord_y}) of color {self.__color}.'

    def __getValueX(self):
        return self.__coord_x

    def __getValueY(self):
        return self.__coord_y

    def __setCoordX(self, new_coord_x):
        self.__coord_x = new_coord_x

    def __setCoordY(self, new_coord_y):
        self.__coord_y = new_coord_y


def commands():
    print("0 -> Quit program")
    print("1 -> Get and set the value of all properties for a point")
    print("2 -> Provide the representation of a point")


def menu():

    print("Point coordinates:")
    x = int(input("X: "))
    y = int(input("Y: "))
    color = input("Color: ")

    point = MyPoint(x, y, color)

    print(MyPoint.__str__(point))


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
