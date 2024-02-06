#!/usr/bin/python3
"""
Module for a function that writes text into file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    Returns the number of characters written
    """
    with open(filename, "w", encoding='utf-8') as f:
        return (f.write(text))
