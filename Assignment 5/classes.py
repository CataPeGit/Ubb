from functions import *


class Planes:

    def __init__(self, id, company, seat_number, destination, passager_list):
        self.__id = id
        self.__company = company
        self.__seat_number = seat_number
        self.__destination = destination

        self.__passenger_list_objects = passager_list.copy()
        self.__passager_list = []
        for passenger in passager_list:
            self.__passager_list.append(str(passenger))

    def __str__(self):
        # returnig a string containing information about the plane
        return f"Plane data: \n Id: {self.__id} \n Company: {self.__company} \n Number of seats: {self.__seat_number} \n Destination: {self.__destination} \n List of passagers: {self.__passager_list}"

    # getter methods
    def get_id(self):
        """
        getter method - get the id of the plane
        """
        return self.__id

    def get_company(self):
        """
        getter method - get the name of the airline company
        """
        return self.__company

    def get_seat_number(self):
        """
        getter method - get the number of seats in the plane
        """
        return self.__seat_number

    def get_destination(self):
        """
        getter method - get the destination 
        """
        return self.__destination

    def get_passager_list(self):
        """
        getter method - get the list of passengers
        """
        return self.__passager_list

    def get_passager_list_as_object(self):
        """
        getter method - get the memory location of the list of passengers
        """
        return self.__passenger_list_objects

    def get_passager_list_with_substrings(self, substring):
        """
        getter method - get the list of passengers whose first name starts with a given substring
        """
        searched_names = []
        for passenger in self.__passager_list:
            names = passenger.split()
            first_name = names[0]
            if find_substring(first_name, substring):
                searched_names.append(first_name)

        return searched_names

    def get_string_by_concatenation(self):
        """
        getter method - get the string obtained by concatenation of the
                        number of passengers in the plane and the destination
        """
        number_of_passagers = str(len(self.__passager_list))
        destination = self.__destination
        return number_of_passagers + destination

    # setter methods
    def set_id(self, new_id):
        """
        setter method - set the id of the plane
        """
        self.__id = new_id

    def set_company(self, new_company):
        """
        setter method - set the name of the airline company
        """
        self.__company = new_company

    def set_seat_number(self, new_seat_number):
        """
        setter method - set the number of seats in the plane
        """
        self.__seat_number = new_seat_number

    def set_destination(self, new_destination):
        """
        setter method - set the destination 
        """
        self.__destination = new_destination

    def set_passager_list(self, new_passager_list):
        """
        setter method - set the list of passengers
        """
        self.__passager_list = new_passager_list.copy()

    def add_passager_to_list(self, passager, index):
        # add the passager to the list at a given index
        self.__passager_list[index].append(passager)

    def remove_passager_from_list(self, index):
        # remove the passager at the given index from the list
        del self.__passager_list[index]

    # Sorting funtions
    def sort_passengers_by_last_name(self):
        # Sort the passengers in a plane by last name
        passenger_list = self.get_passager_list()

        sortSur(passenger_list)

        self.set_passager_list(passenger_list)


class Passenger:

    def __init__(self, first_name, last_name, passport_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__passport_number = passport_number

    def __str__(self):
        # returnig a string containing information about the passager
        return f"{self.__first_name} {self.__last_name}"

    # getters
    def get_first_name(self):
        """
        getter method - get passager first name
        """
        return self.__first_name

    def get_last_name(self):
        """
        getter method - get passager last name
        """
        return self.__last_name

    def get_passport_number(self):
        """
        getter method - get passport number
        """
        return self.__passport_number

    # setters
    def set_first_name(self, new_first_name):
        """
        setter method - set passager first name
        """
        self.__first_name = new_first_name

    def set_last_name(self, new_last_name):
        """
        setter method - set passager last name
        """
        self.__last_name = new_last_name

    def set_passport_number(self, new_passport_number):
        """
        setter method - set passport number
        """
        self.__passport_number = new_passport_number
