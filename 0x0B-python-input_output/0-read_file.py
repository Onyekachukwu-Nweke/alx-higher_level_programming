#!/usr/bin/python3
"""
This module reads a file and prints its
contents
"""


def read_file(filename=""):
    """
    Implementation

    Arg(s):
        filename: file
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
