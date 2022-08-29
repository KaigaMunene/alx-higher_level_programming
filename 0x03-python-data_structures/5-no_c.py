#!/usr/bin/python3
def no_c(my_string):
    for char in my_string:
        if char != "c" and char != "C":
            x = ''.join(char)
            print(x, end="")
