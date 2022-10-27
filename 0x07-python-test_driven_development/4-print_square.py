#!/usr/bin/python3
"""
prints out a square
"""


def print_square(size):
    """
    Prints out a square shape
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
