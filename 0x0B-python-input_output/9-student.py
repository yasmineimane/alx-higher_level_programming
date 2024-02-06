#!/usr/bin/python3
"""
Module retrieves a dict representation of a class
"""


class Student():
    """
    Defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiates object of class Student

        first_name (str): first name
        last_name (str): last name
        age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dict representation of an instance
        """
        return self.__dict__
