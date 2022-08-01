#!/usr/bin/python3
"""
This module checks if the object is an instance of a class that
inherited (directly or indirectly) from the specified class

Returns: True or False
"""


def inherits_from(obj, a_class):
    """
    Implementation of what the module does
    Args:
        obj: Object to be checked
        a_class: object to be checked against
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
