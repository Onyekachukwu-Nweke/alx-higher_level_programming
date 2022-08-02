#!/usr/bin/python3
"""
This module convert a Python Object to JSON String
and write it to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """Implementation of Save JSON to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
