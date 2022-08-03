#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represent a class Student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student class
        Args:
            first_name(str): First Name
            last_name(str): Last Name
            age(int): Age of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves JSON Representation"""
        return self.__dict__
