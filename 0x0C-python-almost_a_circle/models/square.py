#!/usr/bin/python3
"""This class inherits its properties from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inherits from Base class
    from the base module
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This instantiates a new Square class
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This function returns the string representation
        of the Square class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = self.height = value