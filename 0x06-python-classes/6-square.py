#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        try:
            if (size < 0):
                raise ValueError
            self.__size = int(size)
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
        try:
            a, b = position
            if (int(a) < 0 or int(b) < 0):
                raise ValueError
            self.__position = (a, b)
        except (TypeError, ValueError):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        try:
            a, b = value
            if (int(a) < 0 or int(b) < 0):
                raise ValueError
            self.__postion = (a, b)
        except (TypeError, ValueError):
            raise TypeError("position must be a tuple of 2 positive integers")
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
