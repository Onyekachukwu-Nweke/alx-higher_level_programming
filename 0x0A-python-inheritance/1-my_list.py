#!/usr/bin/python3
"""This module inherits the list object"""


class MyList(list):
    """This class inherits some properties the
    ``list`` object"""
    def __init__(self):
        """Initializes object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
