#!/usr/bin/python3
"""
This module reads a file and prints its
contents
"""


def read_file(filename=""):
    with open(filename) as f:
        for line in f:
            print(line, end="")
