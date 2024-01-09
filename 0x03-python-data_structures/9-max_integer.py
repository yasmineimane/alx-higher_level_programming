#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    my_list = sorted(my_list)
    return my_list.pop()
