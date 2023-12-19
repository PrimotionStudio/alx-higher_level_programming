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

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        try:
            if (value < 0):
                raise ValueError
            self.__size = int(value)
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
    def my_print(self):
        if (self.__size == 0):
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
