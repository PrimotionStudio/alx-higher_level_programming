#!/usr/bin/python3
"""
This module contains a class called Rectangle
"""


class Rectangle:
    """
    This is a class that defines a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        The initialization function of this class
        Args:
            width: int
            height: int
        Error:
            TypeError
            ValueError
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        gets the width property of the class
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width property of the class
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        gets the height property of the class
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height property of the class
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the area of the rectangle class
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimiter of the class
        """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        returns a string repr of for print()
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += type(self).print_symbol
            if i != (self.__height - 1):
                rect += '\n'
        return rect

    def __repr__(self):
        """
        Return a string rep for eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Returns a string for deleting an object
        """
        if type(self).number_of_instances != 0:
            type(self).number_of_instances -= 1
        print("Bye rectangle...")
