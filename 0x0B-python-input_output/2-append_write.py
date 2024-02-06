#!/usr/bin/python3
"""

Module appends to a file

"""


def append_write(filename='', text=''):
    """
    Appends text to the end of file
    Returns the no. of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
