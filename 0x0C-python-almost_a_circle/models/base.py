#!/usr/bin/python3
"""
This module defines a base model class
"""


class Base:
    """
    This class Represents the base model

    This class is the “base” of all other classes
    in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the base class instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
