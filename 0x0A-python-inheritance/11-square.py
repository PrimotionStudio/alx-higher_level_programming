#!/usr/bin/python3
"""
a module for square
inherits from  rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This is th class for the Square
    based on Rectangle
    """

    def __init__(self, size):
        """
        creation of a new instance of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        calcs the area of the square
        """

        return self.__size ** 2

    def __str__(self):
        """
        impl for print and str
        """

        return "[{}] {:d}/{:d}".format(self.__class__.__name__,
                                       self.__size, self.__size)
