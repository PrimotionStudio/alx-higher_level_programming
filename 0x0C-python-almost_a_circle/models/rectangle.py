#!/usr/bin/python3
"""
A module with a class
called Rectangle that inherits
from a class called Base
by Martins Okanlawon
"""
from models.base import Base


class Rectangle(Base):
    """
    A class called Rectangle
    and its contents
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        the init function that
        create an instance of the Rectangle Object
        """

        super().__init__(id)
        arg = {'width': width, 'height': height}
        for k, v in arg.items():
            if not isinstance(v, int):
                raise TypeError("{} must be an integer".format(k))
            if v <= 0:
                raise ValueError("{} must be > 0".format(k))
        arg = {'x': x, 'y': y}
        for k, v in arg.items():
            if not isinstance(v, int):
                raise TypeError("{} must be an integer".format(k))
            if v < 0:
                raise ValueError("{} must be >= 0".format(k))
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        public getter for the width funtion
        """

        return self.__width

    @width.setter
    def width(self, width):
        """
        public setter for the width function
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        public getter for the height funtion
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        public setter for the height function
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        public getter for the x funtion
        """

        return self.__x

    @x.setter
    def x(self, x):
        """
        public setter for the x function
        """

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x


    @property
    def y(self):
        """
        public getter for the y funtion
        """

        return self.__y

    @y.setter
    def y(self, y):
        """
        public setter for the y function
        """
   
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        returns the area of the rect
        """

        return self.__width * self.__height

    def display(self):
        """
        returns a display for a rect with the dimensisons
        set
        """

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        overrides the __str__ method
        """

        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        added an update method to the class
        """

        if len(args) == 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'width':
                    self.__width = v
                elif k == 'height':
                    self.__height = v
                elif k == 'x':
                    self.__x = v
                elif k == 'y':
                    self.__y = v
        else:
            for i in range(len(args)):
                if i < 5:
                    if i == 0:
                        self.id = args[i]
                    elif i == 1:
                        self.__width = args[i]
                    elif i == 2:
                        self.__height = args[i]
                    elif i == 3:
                        self.__x = args[i]
                    elif i == 4:
                        self.__y = args[i]

    def to_dictionary(self):
        """
        Update the class Rectangle by adding the public method def
        to_dictionary(self): that returns the
        dictionary representation of a Rectangle
        """

        return {'id': self.id, 'width': self.__width,
                'height': self.__height,'x': self.__x, 'y': self.__y}
