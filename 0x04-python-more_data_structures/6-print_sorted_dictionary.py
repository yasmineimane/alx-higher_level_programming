#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    result = list(a_dictionary.keys())
    result.sort()
    for i in result:
        print("{0}: {1}".format(i, a_dictionary.get(i)))
