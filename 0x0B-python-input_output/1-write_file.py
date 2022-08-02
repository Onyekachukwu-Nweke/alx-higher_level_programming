#!/usr/bin/python3
"""
This module writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Implementation
    Arg(s):
        filename: file
        text: text to be written into the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
