#!/usr/bin/python3
'''Module of is same class function'''


def is_same_class(obj, a_class):
    '''Cheks if an object is exactly an instance of the specified class
    '''
    return type(obj) == a_class
