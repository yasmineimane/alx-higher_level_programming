#!/usr/bin/python3
"""
Module converts class to JSON
"""


def class_to_json(obj):
    """
    Returns dictionary descriptioon for JSON serilaisation of a project
    """
    return obj.__dict__
