#!/bin/usr/python3
"""
Module content
base.py - create a Base class for other classes to inherit from
"""


class Base:
    """ Base class to inherit from """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
