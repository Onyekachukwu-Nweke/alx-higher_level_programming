#!/usr/bin/python3
"""
    Write a class that defines a Square

    Initializes a value, type checks the implementation
    and computes the Area of the square
"""


class Square:
    """
        Square Implementation
    """

    def __init__(self, size=0):
        """
            Initializes the attribute of the Square
            class
        """

        self.size = size

    @property
    def size(self):
        """
            Getter for size
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """
            Setter for size
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
            Computes the Area of the Square
        """

        return (self.__size ** 2)

    def my_print(self):
        """
            Prints the length and height in #
        """

        if self.__size == 0:
            print("")
            return
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print("")
