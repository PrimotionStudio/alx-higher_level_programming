#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            if (size < 0):
                raise ValueError
            self.__size = int(size)
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)
