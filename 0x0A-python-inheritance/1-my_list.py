#!/usr/bin/python3
"""This module inherits the list object"""


class MyList(list):
    """This class inherits some properties the
    ``list`` object"""
    def print_sorted(self):
        print(sorted(self))
