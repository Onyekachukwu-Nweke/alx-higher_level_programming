#!/usr/bin/python3
"""Defines a text-indentation function"""


def text_indentation(text):
    """
    This function prints text with two new lines
    if '.?:' is encountered

    Arg(s):
        text (str)

    Raises:
        TypeError: text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for l in '.?:':
        text = text.replace(l, "{}\n\n".format(l))
    lines = text.splitlines()
    for index, line in enumerate(lines):
        print(line.strip(), end="" if index == len(lines) - 1 else "\n")
