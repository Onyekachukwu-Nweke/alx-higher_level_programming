#!/usr/bin/python3
"""Defines a Rectangle based on 0-rectangle"""


class Rectangle:
    """
    Defines a Rectangle with height and width and
    validate measurement
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """
        Defines the printable representation of the Rectangle
        using the ``#`` character
        """
        if self.__width == 0 or self.__height == 0:
            return("")
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """
        Defines the string representation of the
        Rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        Deletes an instance when called
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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

    def area(self):
        """Calcualates the area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Checks which of the rectangles is bigger
        or equal to the other

        Args:
            rect_1: first rectangle
            rect_2: second rectngle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        This function transforms the Rectangle
        to a square
        """
        return(cls(size, size))
