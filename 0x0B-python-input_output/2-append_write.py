#!/usr/bin/python3
"""
A module that append
a text to a file
"""


def append_write(filename="", text=""):
    """
    A function that
    appends a text
    to a file
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
