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
        if width is not isinstance(int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """ Getter for 'height' attribute """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter for 'height' attribute """
        if height is not isinstance(int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """ Getter for 'x' attribute """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter for 'x' attribute """
        if x is not isinstance(int):
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be > 0")

        self.__x = x

    @property
    def y(self):
        """ Getter for 'y' attribute """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter for 'y' attribute """
        if y is not isinstance(int):
            raise TypeError("height must be an integer")
        if y <= 0:
            raise ValueError("height must be > 0")

        self.__y = y

    def area(self):
        """ Method to calculate area """
        return self.__width * self.__height

    def display(self):
        """
        prints rectangle to stdout with instance "#"
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        returns string representation of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
            )

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        returns the dictionary representation of the rectangle
        """
        return {"x": self.__x,
                "y": self.__y,
                "id": self.id,
                "height": self.__height,
                "width": self.__width
                }
