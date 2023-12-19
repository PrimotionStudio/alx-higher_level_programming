#!/usr/bin/python3
"""Defines the Square class."""


class Square:
    """Represents a square with a specified size.
    
    Attributes:
    - __size (int): The size of each side of the square.
    Methods:
    - __init__(self, size): Initializes a new square with the given size.
    """
    def __init__(self, size):
        """Initializes a new square with the given size."""
        self.__size = size
