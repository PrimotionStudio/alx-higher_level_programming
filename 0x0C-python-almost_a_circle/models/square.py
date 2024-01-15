#!/usr/bin/python3
"""
A module of a class
SQUARE that inherist from a class
RECTANGLE which inherits from BASE
by Martins Okanlawon
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    THis is a class thats inherist
    from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This initialization function
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overwrite the __str__ for square
        """

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        The getter property for the class
        """

        return self.width

    @size.setter
    def size(self, size):
        """
        The setter method for the size
        """

        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Update the class Square by adding the public method def
        update(self, *args, **kwargs) that assigns attributes
        """

        if len(args) == 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.width = v
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v
        else:
            for i in range(len(args)):
                if i < 5:
                    if i == 0:
                        self.id = args[i]
                    elif i == 1:
                        self.width = args[i]
                        self.height = args[i]
                    elif i == 2:
                        self.x = args[i]
                    elif i == 3:
                        self.y = args[i]

    def to_dictionary(self):
        """
        Update the class Square by adding the
        public method def to_dictionary(self)
        """

        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
