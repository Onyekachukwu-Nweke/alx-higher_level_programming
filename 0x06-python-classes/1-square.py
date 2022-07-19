#!/usr/bin/python3
"""
    1-square.py: write a class Square with private instance attribute
    size
"""


class Square:
    """
        Creates a class and initializes a private instance attribute
    """

    def __init__(self, size):
        """
            Initializes the instance values
        """

        self.__size = size
