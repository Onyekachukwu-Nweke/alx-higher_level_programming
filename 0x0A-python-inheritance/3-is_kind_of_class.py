#!/usr/bin/python3
"""
This module checks if the object is an instance of,
or if the object is an instance of a class that
inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    This function is the implementation of what
    this module does
    """
    if isinstance(obj, a_class):
        return True
    return False
