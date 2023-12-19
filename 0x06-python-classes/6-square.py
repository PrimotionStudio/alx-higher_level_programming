#!/usr/bin/python3
"""
This module defines the Square class.

The Square class represents a square with a specified size and position.

Classes:
- Square: Represents a square with a specified size and position.

Attributes:
- __size (int): The size of each side of the square.
- __position (tuple): The position of the square as a tuple of two positive integers.

Methods:
- __init__(self, size=0, position=(0, 0)): Initializes a new square with the given size and position. If size or position is not provided, they default to 0 and (0, 0) respectively.
- area(self): Calculates and returns the area of the square.
- size (property): Gets the size of the square.
- size (setter): Sets the size of the square, ensuring it is a non-negative integer.
- position (property): Gets the position of the square.
- position (setter): Sets the position of the square, ensuring it is a tuple of two positive integers.
- my_print(self): Prints a visual representation of the square using '#' characters, respecting its position.
"""
class Square:
    """
    This class represents a square with a specified size and position.

    Attributes:
    - __size (int): The size of each side of the square.
    - __position (tuple): The position of the square as a tuple of two positive integers.

    Methods:
    - __init__(self, size=0, position=(0, 0)): Initializes a new square with the given size and position. If size or position is not provided, they default to 0 and (0, 0) respectively.
    - area(self): Calculates and returns the area of the square.
    - size (property): Gets the size of the square.
    - size (setter): Sets the size of the square, ensuring it is a non-negative integer.
    - position (property): Gets the position of the square.
    - position (setter): Sets the position of the square, ensuring it is a tuple of two positive integers.
    - my_print(self): Prints a visual representation of the square using '#' characters, respecting its position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square with the given size and position.

        :param size: The size of each side of the square. Defaults to 0 if not provided.
        :param position: The position of the square as a tuple of two positive integers. Defaults to (0, 0) if not provided.
        :raises TypeError: If the provided size or position is not of the correct type.
        :raises ValueError: If the provided size or position is invalid (size < 0 or position values < 0).
        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = int(size)
        except TypeError:
            raise TypeError("size must be an integer")

        try:
            a, b = position
            if int(a) < 0 or int(b) < 0:
                raise ValueError("position must be a tuple of 2 positive integers")
            self.__position = (a, b)
        except (TypeError, ValueError):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        """
        Gets the position of the square.

        :return: The position of the square as a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square, ensuring it is a tuple of two positive integers.

        :param value: The new position to set for the square.
        :raises TypeError: If the provided position is not of the correct type.
        :raises ValueError: If the provided position is invalid (position values < 0).
        """
        try:
            a, b = value
            if int(a) < 0 or int(b) < 0:
                raise ValueError("position must be a tuple of 2 positive integers")
            self.__position = (a, b)
        except (TypeError, ValueError):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculates and returns the area of the square.

        :return: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Gets the size of the square.

        :return: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square, ensuring it is a non-negative integer.

        :param value: The new size to set for the square.
        :raises TypeError: If the provided size is not of the correct type.
        :raises ValueError: If the provided size is invalid (size < 0).
        """
        try:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = int(value)
        except TypeError:
            raise TypeError("size must be an integer")

    def my_print(self):
        """
        Prints a visual representation of the square using '#' characters, respecting its position.

        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        a = self.position
        for m in range(a[1]):
            print()
        for i in range(self.__size):
            a = self.position
            for k in range(a[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()