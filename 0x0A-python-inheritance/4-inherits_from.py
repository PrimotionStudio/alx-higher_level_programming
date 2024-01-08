#!/usr/bin/python3
"""
Module for checking for subclass
This woudl be awesome
"""


def inherits_from(obj, a_class):
    """
    This is the func that checks
    for the subclass of an obj
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
