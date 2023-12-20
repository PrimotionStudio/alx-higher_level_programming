"""Initializes a MagicClass object with a given radius."""
import math


class MagicClass:
    def __init__(self, radius):
        """Initializes a MagicClass object with a given radius.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the circle.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates and returns the circumference of the circle.
        """
        return 2 * math.pi * self.__radius
