#!/usr/bin/python3
"""
Module contains a function that append a text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.
    Returns the number of characters added
    """
    with open(filename, "a", encoding='utf-8') as f:
            return (f.write(text))
