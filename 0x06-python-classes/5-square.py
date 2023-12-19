#!/usr/bin/python3
"""Defines the Square class."""


class Square:
    """Represents a square with a specified size.

    Attributes:
    - __size (int): The size of each side of the square.
    Methods:
    - __init__(self, size=0): Initializes a new square with the given size.
    - area(self): Calculates and returns the area of the square.
    - my_print(self): Prints a visual representation of
    the square using '#' characters.
      If the size is 0, it prints an empty line.
    """
    def __init__(self, size=0):
        """Initializes a new square with the given size.
        :param size: The size of each side of the square
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
        ensuring it is a non-negative integer.
        :param value: The new size to set for the square.
        :raises TypeError: If the provided size is not an integer.
        :raises ValueError: If the provided size is less than 0.
        """
        try:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = int(value)
        except TypeError:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Prints a visual representation of the
        square using '#' characters.
        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
