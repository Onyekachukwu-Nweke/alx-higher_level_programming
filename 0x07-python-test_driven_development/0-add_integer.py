#!/usr/bin/python3
""" This module defines an integer addition """


def add_integer(a, b=98):
    """
        This function defines how integers will be
        summed

        Float arguments will be typecasted to integer

        Raises:
            TypeError is raised if any of the parameters is not
            an integer
    """

    values = []
    for x, param in [(a, 'a'), (b, 'b')]:
        if isinstance(x, int):
            values.append(x)
        elif isinstance(x, float):
            values.append(int(x))
        else:
            raise TypeError("{} must be an integer".format(param))

    return sum(values)
