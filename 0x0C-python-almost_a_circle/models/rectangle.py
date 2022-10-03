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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for 'width' attribute """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter for 'width attribute """
        self.validate("width", width, 0)
        self.__width = width

    @property
    def height(self):
        """ Getter for 'height' attribute """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter for 'height' attribute """
        self.validate("height", height, 0)
        self.__height = height

    @property
    def x(self):
        """ Getter for 'x' attribute """
        return self.__x
    
    @x.setter
    def x(self, x):
        """ Setter for 'x' attribute """
        self.validate("x", x, 0)
        self.__x = x
    
    @property
    def y(self):
        """ Getter for 'y' attribute """
        return self.__y
    
    @y.setter
    def y(self, y):
        """ Setter for 'y' attribute """
        self.validate("y", y, 0)
        self.__y = y
