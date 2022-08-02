#!/usr/bin/python3
"""
This module unserializes JSON Strings to Python
Objects
"""
import json


def from_json_string(my_str):
    """
    Implementation
    Arg(s):
        my_obj: object to be unserialized
    """
    return (json.loads(my_str))
