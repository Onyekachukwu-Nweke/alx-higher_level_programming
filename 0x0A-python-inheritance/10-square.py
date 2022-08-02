#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Implementation"""
    def __init__(self, size):
        """Initialization of Square Class"""
        super().__init__(size, size)
