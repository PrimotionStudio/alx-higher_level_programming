#!/usr/bin/python3
"""
A student class
About something
"""


class Student:
    """
    A student class
    im sleepy
    """

    def __init__(self, first_name, last_name, age):
        """
        the init func
        of thois class
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        an annoying example
        really annoying
        """

        return self.__dict__
