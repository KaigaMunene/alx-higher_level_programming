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

    def to_json(self):
        """ Return dictionary content of this Student object """
        return (self.__dict__)

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__dict__[key] = value
