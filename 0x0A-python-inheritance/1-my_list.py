#!/usr/bin/python3
"""
A module to sort
a list using a class
"""


class MyList(list):
    """
    A class for
    sorting a list
    Args:
        list: list
    """

    def print_sorted(self):
        """
        A method for
        sorting a list
        Args:
            self: MyList
        """

        print(sorted(self))
