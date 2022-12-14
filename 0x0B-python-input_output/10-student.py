#!/usr/bin/python3
"""
Module content
Create a 'Student' class with public attributes and methods
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return dictionary content of this Student object """
        if attrs is None:
            return (self.__dict__)

        kv = {}
        for key in attrs:
            if key in self.__dict__:
                kv[key] = self.__dict__[key]
        return (kv)
