#!/usr/bin/python3
"""
This module defines a rebellious class
that inherits from int
"""


class MyInt(int):
    """Implementation"""
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
