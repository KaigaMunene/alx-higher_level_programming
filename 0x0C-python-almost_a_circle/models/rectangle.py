#!/usr/bin/python3
"""
Module for rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """ rectangle inherits from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize contructor method """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
