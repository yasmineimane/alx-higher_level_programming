#!/usr/bin/python3
"""

Module to return JSON representation of a string

"""
import json


def to_json_string(my_obj):
    """
    Returns JSON representation of string

    my_obj(str): the string
    """
    return (json.dumps(my_obj))
