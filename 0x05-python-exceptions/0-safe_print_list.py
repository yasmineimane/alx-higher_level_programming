#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        y = i + 1
    except IndexError:
        None
        y = i
    print()
    return y
