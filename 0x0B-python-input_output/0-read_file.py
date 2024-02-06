#!/usr/bin/python3
"""
Module contains a function that read a file.
"""


def read_file(filename=""):
    """
    Reads from a file to stdout.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
