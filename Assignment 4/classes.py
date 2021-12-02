import matplotlib.pyplot as plt
import numpy as np
import sys


class MyVector:

    def __init__(self, name_id, colour, typeInteger, values):
        self.__name_id = name_id
        self.__colour = colour
        self.__typeInteger = typeInteger
        self.__values = values

    def __str__(self):
        # returnig a string containing information about the point
        return f"Name id is {self.__name_id}. Colour is {self.__colour}. Type is {self.__typeInteger}. Values are {self.__values}."

    def get_name_id(self):
        """
        getter method - get the name
        """
        return self.__name_id

    def get_colour(self):
        """
        getter method - get the colour
        """
        return self.__colour

    def get_type(self):
        """
        getter method - get the type
        """
        return self.__typeInteger

    def get_values(self):
        """
        getter method - get the value
        """
        return self.__values

    def set_name_id(self, new_name):
        """
        setter method - set the name
        """
        self.__name_id = new_name

    def set_colour(self, new_colour):
        """
        setter method - set the colour
        """
        self.__colour = new_colour

    def set_type(self, new_type):
        """
        setter method - set the type
        """
        self.__typeInteger = new_type

    def set_values(self, new_value):
        """
        setter method - set the value
        """
        self.__values = new_value

    def add_scalar(self, scalar):
        # updates the vector's values by adding scalar
        i = 0
        while i < len(self.__values):
            self.__values[i] += scalar
            i += 1

    def add(self, vector_to_add):
        # adds the values with "vector_to_add"
        if len(vector_to_add) != len(self.__values):
            print("Vectors have different lengths.")
            print()
            return

        i = 0
        while i < len(self.__values):
            self.__values[i] += vector_to_add[i]
            i += 1

    def substract(self, vector_to_add):
        # substracts the values with "vector_to_add"
        if len(vector_to_add) != len(self.__values):
            print("Vectors have different lengths.")
            print()
            return

        i = 0
        while i < len(self.__values):
            self.__values[i] -= vector_to_add[i]
            i += 1

    def multiplication(self, vector_to_add):
        # multiplication of the values with "vector_to_add"
        if len(vector_to_add) != len(self.__values):
            print("Vectors have different lengths.")
            print()
            return

        if len(vector_to_add) == 0 or len(self.__values):
            print("Vector has no values.")
            print()
            return None

        i = 0
        while i < len(self.__values):
            self.__values[i] *= vector_to_add[i]
            i += 1

    def sum_of_elements(self):
        # return the sum of elements in a vector
        sum = 0
        values = self.get_values()
        for i in values:
            sum += i
        return sum

    def product_of_elements(self):
        # return the product of elements in a vector
        i = 0
        product = 0
        while i < len(self.__values):
            product *= self.__values[i]
            i += 1
        return product

    def average_of_elements(self):
        # return the average of elements in a vector
        i = 0
        sum = 0
        while i < len(self.__values):
            sum += self.__values[i]
            i += 1
        i -= 1
        return sum / i

    def minimum_of_a_vector(self):
        # return the minimum of elements in a vector
        i = 0
        minimum = 9999999999999999
        while i < len(self.__values):
            if self.__values[i] < minimum:
                minimum = self.__values[i]
            i += 1
        return minimum

    def maximum_of_a_vector(self):
        # return the minimum of elements in a vector
        i = 0
        maximum = -9999999999999999
        while i < len(self.__values):
            if self.__values[i] > maximum:
                maximum = self.__values[i]
            i += 1
        return maximum


class VectorRepository(MyVector):

    num_of_vectors = 1

    def __init__(self):
        # initializing the repository
        self.__repository = []

    def add_a_vector_to_the_repository(self, new_vector):
        # adds a vector to the repository
        self.__repository = np.append(self.__repository, new_vector)

    def get_all_vectors(self):
        return self.__repository

    def get_vector_at_given_index(self, index):
        # get the vector at the given index
        return self.__repository[index]

    def get_vectors_having_sum(self, sum):
        # Get the list of vectors having a given sum of elements
        i = 0
        list_of_vectors = []
        while i < len(self.__repository):
            item = self.__repository[i]
            vec_sum = item.sum_of_elements()
            if vec_sum == sum:
                print(item.__str__())
            i += 1

        return list_of_vectors

    def delete_vectors_between(self, index1, index2):
        # Delete all vectors that are between two given indexes
        index1 += 1
        result = self.__repository.copy()
        while index1 < index2:
            result = np.delete(result, index1)
            index2 -= 1

        self.__repository = result.copy()

    def update_color_by_name_id(self, the_id, new_color):
        # Update the color of a vector identified by name_id
        i = 0
        result = self.__repository.copy()
        while i < len(result):
            id_now = result[i].get_name_id()
            if(id_now == the_id):
                result[i].set_colour(new_color)
            i += 1

        self.__repository = result.copy()

    def update_vector_at_given_index(self, index, new_name, new_colour, new_typeInteger, new_values):
        # update a vector at a given index
        vector_changed = self.get_vector_at_given_index(index)
        vector_changed.set_name_id(new_name)
        vector_changed.set_colour(new_colour)
        vector_changed.set_type(new_typeInteger)
        vector_changed.set_values(new_values)

    def update_vector_by_name_id(self, name_id_searched, new_name, new_colour, new_typeInteger, new_values):
        # updating a vector in the repository by name_id
        for vector in range(len(self.__repository)):
            if self.__repository[vector].get_name_id() == name_id_searched:
                vector_changed = self.get_vector_at_given_index(vector)
                vector_changed.set_name_id(new_name)
                vector_changed.set_colour(new_colour)
                vector_changed.set_type(new_typeInteger)
                vector_changed.set_values(new_values)

    def delete_vector_at_index(self, index):
        # deleting a vector in the repository at a given index
        self.__repository = np.delete(self.__repository, index)

    def delete_vector_by_name(self, name_id_searched):
        # deleting a vector in the repository by name_id
        length = len(self.__repository)
        result = []
        for vector in range(length):
            if self.__repository[vector].get_name_id() != name_id_searched:
                result.append(self.__repository[vector])
        self.__repository = result.copy()

    def add_4_data_example(self):
        # add vectors to the repository
        length = len(self.__repository)
        good = 0
        for vector in range(length):
            if self.__repository[vector].get_name_id() == "v1" or self.__repository[vector].get_name_id() == "v2" or self.__repository[vector].get_name_id() != "v3" or self.__repository[vector].get_name_id() != "v4":
                good = 1
                print(
                    "One or more of the examples have the name_id already taken, please pick something else instead of: v1, v2 ,v3 or v4!")
                break
        if good == 0:
            self.__repository = np.append(
                self.__repository, MyVector("ex1", "r", 1, [0, 1, 2]))
            self.__repository = np.append(
                self.__repository, MyVector("ex2", "g", 2, [6, 4, 2]))
            self.__repository = np.append(
                self.__repository, MyVector("ex3", "y", 3, [3, 2, 0]))
            self.__repository = np.append(
                self.__repository, MyVector("ex4", "b", 4, [3, 7, 8]))

    def plot_vectors_in_chart(self):
        # plot vectors in a chart by types and values and colour
        for vector in range(len(self.__repository)):
            point_array = []
            current_vector = self.__repository[vector]
            current_type = current_vector.get_type()
            current_values = current_vector.get_values()

            for point in range(len(current_vector.get_values())):
                point_array.append(current_values[point])

            points = np.array(point_array)
            current_type = point_interpretation(current_type)
            plt.plot(point_array, marker=current_type,
                     color=current_vector.get_colour())

        plt.show()
        # Two  lines to make our compiler able to draw:
        # plt.savefig(sys.stdout.buffer)
        # sys.stdout.flush()

    def check_id(self, nameId):
        # check if id already exists in the vector repository
        length = len(self.__repository)
        for vector in range(length):
            if self.__repository[vector].get_name_id() == nameId:
                return False
        return True


def point_interpretation(current_type):
    # determine colour based on type and return it
    if current_type == 1:
        current_type = "o"
    elif current_type == 2:
        current_type = "s"
    elif current_type == 3:
        current_type = "v"
    elif current_type > 3:
        current_type = "D"
    return current_type
