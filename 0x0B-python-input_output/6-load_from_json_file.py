#!/usr/bin/python3
"""This module loads files from JSON"""
import json


def load_from_json_file(filename):
    """Implementation"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
