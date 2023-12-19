#!/usr/bin/python3
"""
This module defines the Square class.

The Square class represents a square with a specified size.

Classes:
- Square: Represents a square with a specified size.

Attributes:
- __size (int): The size of each side of the square.

"""

class Square:
    """
    This class represents a square with a specified size.

    Attributes:
    - __size (int): The size of each side of the square.

    Methods:
    - __init__(self, size): Initializes a new square with the given size.
    """

    def __init__(self, size):
        """
        Initializes a new square with the given size.

        :param size: The size of each side of the square.
        """
        self.__size = size