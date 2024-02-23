#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    result = dict(a_dictionary)
    for i in result:
        result[i] = result.get(i)*2
    return result
