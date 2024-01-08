#!/usr/bin/python3
"""
A class MyInt
That is the opposite
of the int class
"""


class MyInt(int):
    """
    The class MyInt
    inherits from int
    """

    def __eq__(self, obj):
        """
        a func for changing
        eq to ne
        """
        return super().__ne__(obj)

    def __ne__(self, obj):
        """
        a func for changing ne
        to eq
        """
        return super().__eq__(obj)
