#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Implementation"""
    def __init__(self, size):
        """Initialization of Square Class
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """String Representation of the Class"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
