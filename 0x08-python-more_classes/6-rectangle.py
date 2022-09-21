#!/usr/bin/python3
""" Creates an empty class called Rectangle """


class Rectangle:
    """ This class that defines a rectangle object """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Constructor for the Rectangle class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter for 'width' attribute """
        return self.__width

    @property
    def height(self):
        """ Getter for 'height' attribute """
        return self.__height

    @width.setter
    def width(self, width):
        """ Setter for 'width' attribute """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ Getter for 'height' attribute """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ Return area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return perimeter of current rectangle """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ return the printable representation of the Rectangle """
        if self.__width is 0 or self.__height is 0:
            return ""

        shape = []
        for i in range(self.__height):
            [shape.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                shape.append("\n")
        return ("".join(shape))

    def __repr__(self):
        """ Return string representation of the rectangle """
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """ Destructor method """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

