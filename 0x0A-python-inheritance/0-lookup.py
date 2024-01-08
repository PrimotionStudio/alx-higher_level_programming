#!/usr/bin/python3
"""
A modul that returns a list of all attr nd met of an obj
"""


def lookup(obj):
    """
    A function that retuyrns a list of all attr and meth of an obj
    """
    return dir(obj)
