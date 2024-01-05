#!/usr/bin/python3
"""
This module contains a class called Rectangle
"""


class Rectangle:
    """
    This is a class that defines a rectangle
    """

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
