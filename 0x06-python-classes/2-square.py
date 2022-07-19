#!/usr/bin/python3
"""
    Write a class that defines a Square

    Initializes a value and type checks the implementation
"""


class Square:
    """
        Creates a square class and type checks the values
    """

    def __init__(self, size=0):
        """
            Initializes the attribute of the Square
            class
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
