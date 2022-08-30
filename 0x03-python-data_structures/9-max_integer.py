#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in my_list:
        if len(my_list) < 1:
            return None
        else:
            return sorted(my_list)[-1]
