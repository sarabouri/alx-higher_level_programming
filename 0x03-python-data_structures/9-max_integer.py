#!/usr/bin/python
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_value = max(my_list)
        c = int(max_value)
        return c
