#!/usr/bin/python3
"""This class inherits its properties from the Base class"""
from models.base import Base


class Rectangle(Base):
    """
    This class inherits from Base class
    from the base module
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This instantiates the Rectangular class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This is the getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is the setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This is the getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is the setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This is the getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """This is the setter for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This is the getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """This is the setter for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This calculates the area of the Rectangle"""
        return (self.__width * self.__height)
