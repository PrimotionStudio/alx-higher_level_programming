#!/usr/bin/python3
"""
a module for rectangle
inherits from  base geometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is th class for the Rect
    based on Base Geometry
    """

    def __init__(self, width, height):
        """
        creation of a new instance of the rect
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        calcs the area of the rect
        """

        return self.__width * self.__height

    def __str__(self):
        """
        impl for print and str
        """

        return "[{}] {:d}/{:d}".format(self.__class__.__name__,
                                       self.__width, self.__height)
