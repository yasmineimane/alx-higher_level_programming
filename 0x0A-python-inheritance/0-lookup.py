#!/usr/bin/python3
"""Module for lookup method."""


def lookup(obj):
    """Looks up object attribute and methods.
    Args:
        obj (object): the object.
    
    Returns:
        list: the of attributs.
    """

    return dir(obj)
