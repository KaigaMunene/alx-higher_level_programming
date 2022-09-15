#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ This class defines a square object """
    def __init__(self, size=0):
        """ Constructor for the Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
