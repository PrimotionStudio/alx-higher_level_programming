#!/usr/bin/python3
"""
The Module adds a new attr
to an obj if possible
"""


def add_attribute(obj, attr, value):
    """
    this func checks if an obj has an attr
    then sets it else returns error
    Args:
        obj
        attr
        value
    Error:
        TypeError
    """
    if not hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
