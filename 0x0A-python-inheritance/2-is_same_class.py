#!/usr/bin/python3
"""This module checks if two classes are of the
same instances"""


def is_same_class(obj, a_class):
    """This function checks if the two classes
    are of the same instance

    Args:
        obj: The object to be checked
        a_class: Type to be checked against
    """
    return type(obj) == a_class
