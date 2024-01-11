#!/usr/bin/python3
"""
Module for somethin
I just am ...
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for l in lines:
            f.write(l)
            if search_string in l:
                f.write(new_string)
