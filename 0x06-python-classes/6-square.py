#!/usr/bin/python3
"""
    Write a class that defines a Square

    Initializes a value, type checks the implementation
    and computes the Area of the square

    And Checks for Positions of the square
"""


class Square:
    """
        Square Implementation
    """

    def __init__(self, size=0, position=(0, 0)):
        """
            Initializes the attribute of the Square
            class
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
            Getter for position
        """

        return (self.__position)

    @position.setter
    def position(self, value):
        """
            Setter for Position
        """

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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
            [print("") for i in range(0, self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                [print("#", end="") for k in range(self.__size)]
                print("")
