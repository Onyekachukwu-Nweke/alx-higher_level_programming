#!/usr/bin/python3
"""Defines a Rectangle based on 0-rectangle"""


class Rectangle:
    """
    Defines a Rectangle with height and width and
    validate measurement
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter of width measurement"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width measurement"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height measurement"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for height measurement"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
