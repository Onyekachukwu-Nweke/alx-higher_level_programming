#!/usr/bin/python3
"""Defines the square pattern a given character is printed"""


def print_square(size):
    """
    This function prints a square pattern with a
    given character

    Args:
        size (int)

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
