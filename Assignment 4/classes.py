import numpy as np


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
        return self.__type

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
        self.__type = new_type

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
        i = 0
        while i < len(self.__values):
            self.__values[i] += vector_to_add[i]
            i += 1

    def substract(self, vector_to_add):
        # substracts the values with "vector_to_add"
        i = 0
        while i < len(self.__values):
            self.__values[i] -= vector_to_add[i]
            i += 1

    def multiplication(self, vector_to_add):
        # multiplication of the values with "vector_to_add"
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

    def get_point_at_index(self, index):
        # Returns the point found at a given index
        return self.__repository[index]

    # def get_all_vectors(self):
        # returns all vectors inside the repository
        # for item in range(len(self.__repository)):
        #   self.__repository[item].__str__()

    def add_a_vector_to_the_repository(self, new_vector):
        # adds a vector to the repository
        self.__repository = np.append(self.__repository, new_vector)

    def get_all_vectors(self):
        return self.__repository

    def get_vector_at_given_index(self, index):
        # get the vector at the given index
        vector = self.__repository[index]
        print(vector.__str__())

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

    def add_4_data_example(self):
        # add vectors to the repository
        self.__repository = np.append(
            self.__repository, MyVector("v1", "red", 1, [0, 1, 2]))
        self.__repository = np.append(
            self.__repository, MyVector("v2", "green", 2, [6, 4, 2]))
        self.__repository = np.append(
            self.__repository, MyVector("v3", "pink", 3, [3, 2, 0]))
        self.__repository = np.append(
            self.__repository, MyVector("v3", "blue", 4, [3, 7, 8]))
