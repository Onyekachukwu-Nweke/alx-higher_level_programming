#!/usr/bin/python3
"""
Defines the class BaseGeometry
"""


class BaseGeometry:
    """Representation of BaseGeometry class"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates the input
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
