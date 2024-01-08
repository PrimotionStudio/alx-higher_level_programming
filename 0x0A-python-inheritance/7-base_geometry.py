#!/usr/bin/python3
"""
A module for a class called
BASEGEOMETRY
"""


class BaseGeometry:
    """
    This is a class called
    BaseGeometry
    """

    def area(self):
        """
        checks for area stuff
        and stuff of the area
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates integer
        and intgers validate
        Args:
            name: string
            value: +ve int
        Errors:
            TypeError
            ValueError
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
