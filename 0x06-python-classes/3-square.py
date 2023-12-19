#!/usr/bin/python3
class Square:
    """
    This class represents a square with a specified size.

    Attributes:
    - __size (int): The size of each side of the square.

    Methods:
    - __init__(self, size=0): Initializes a new square with the given size. If size is not provided, it defaults to 0.
    - area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with the given size.

        :param size: The size of each side of the square. Defaults to 0 if not provided.
        :raises TypeError: If the provided size is not an integer.
        :raises ValueError: If the provided size is less than 0.
        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = int(size)
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculates and returns the area of the square.

        :return: The area of the square.
        """
        return self.__size ** 2