#!/usr/bin/python3
"""Defines the Square class."""


class Square:
    """Represents a square with a specified size.

    Attributes:
    - __size (int): The size of each side of the square.
    Methods:
    - __init__(self, size=0): Initializes a new square with the given size.
      If size is not provided, it defaults to 0.
      :param size: The size of each side of the square.
    - area(self): Calculates and returns the area of the square.
    """
    def __init__(self, size=0):
        """Initializes a new square with the given size.
        :param size: The size of each side of the square.
            Defaults to 0 if not provided.
        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = int(size)
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates and returns the area of the square.
        :return: The area of the square.
        """

        return self.__size ** 2

    @property
    def size(self):
        """Gets the size of the square.
        :return: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square,
            ensuring it is a non-negative integer
        :param value: The new size to set for the square.
        """
        try:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = int(value)
        except TypeError:
            raise TypeError("size must be an integer")
    def __eq__(self, square):
        """Checks if the area of the current square is
        equal to the area of another square.
        """
        return self.area() == square.area()

    def __ne__(self, square):
        """Checks if the area of the current square is
        not equal to the area of another square.
        """
        return self.area() != square.area()

    def __lt__(self, square):
        """Checks if the area of the current square is
        less than the area of another square.
        """
        return self.area() < square.area()

    def __le__(self, square):
        """Checks if the area of the current square is
        less than or equal to the area of another square.
        """
        return self.area() <= square.area()

    def __gt__(self, square):
        """Checks if the area of the current square is
        greater than the area of another square.
        """
        return self.area() > square.area()

    def __ge__(self, square):
        """Checks if the area of the current square is
        greater than or equal to the area of another square.
        """
        return self.area() >= square.area()
