#!/usr/bin/python3
"""

Module returns an object from JSON

"""
import json


def from_json_string(my_str):
    """
    Returns a python object from a JSON string
    """
    return (json.loads(my_str))
