#!/usr/bin/python3
"""

Module to print squares using #

"""


def print_square(size):
    """

    function to print a square out of #
    Args:
        size: the size of #
    Error:
        TypeError
        ValueError

    """
    if (not isinstance(size, int)) or (isinstance(size, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
