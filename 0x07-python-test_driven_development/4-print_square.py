#!/usr/bin/python3
"""
prints concatenation of "My name is " with the 2 string arguments
"""


def print_square(size):
    """
    Prints out "My name is " + first_name + last_name
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size is type(float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for element in range(size):
            print("#", end="")
        print()
