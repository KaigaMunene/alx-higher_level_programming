#!/usr/bin/python3
""" Creates an empty class called Rectangle"""


class Rectangle:
    """ A class that defines a rectangle object """
    def __init__(self, width=0, height=0):
        """ Constructor for the Rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for 'width' attribute """
        return self.__width

    @property
    def height(self):
        """ Getter for 'width' attribute """
        return self.__height

    @width.setter
    def width(self, value):
        """ Setter for 'width' attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        """ Getter for 'height' attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
