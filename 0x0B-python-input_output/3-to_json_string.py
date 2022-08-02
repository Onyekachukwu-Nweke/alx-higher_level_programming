#!/usr/bin/python3
"""
This module serializes Python objects to JSON
Strings
"""
import json


def to_json_string(my_obj):
    """
    Implementation
    Arg(s):
        my_obj: object to be serialized
    """
    return (json.dumps(my_obj))
