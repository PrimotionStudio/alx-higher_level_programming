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

    def to_json(self, attrs=None):
        """
        an annoying example
        really annoying
        """

        if (type(attrs) is list and all(type(i) is str for i in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        a really annoying process
        i just wanna sleep
        """

        for key, val in json.items():
            if hasattr(self, key):
                setattr(self, key, val)
