#!/usr/bin/python3
""" Creates an empty class called Rectangle """


class Rectangle:
    """ This class that defines a rectangle object """
    number_of_instances = 0
    print_symbol = "#"

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
            [shape.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                shape.append("\n")
        return ("".join(shape))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.
        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __repr__(self):
        """ Return string representation of the rectangle """
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """ Destructor method """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
