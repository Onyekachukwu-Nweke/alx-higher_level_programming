#!/usr/bin/python3
""" This module looks up objects"""


def lookup(object):
    """This function looks up properties using
    ``dir``"""
    return list(dir(object))
