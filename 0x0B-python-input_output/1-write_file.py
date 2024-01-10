#!/usr/bin/python3
"""
A module used to write
to a text file
"""


def write_file(filename="", text=""):
    """
    A function to
    write to a file
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
