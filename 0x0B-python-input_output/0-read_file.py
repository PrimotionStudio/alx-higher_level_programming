#!/usr/bin/python3
"""
A module for openin and
reading a text file
"""


def read_file(filename=""):
    """
    A function for opening
    and closing a text file
    """

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
