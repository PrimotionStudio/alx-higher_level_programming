#!/usr/bin/python3
"""
A module with a class
called Base
by Martins Okanlawon
"""
import json


class Base:
    """
    A class called Base
    and its contents
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """
        the init function that
        create an instance of the Base Object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Adding JSON to the Base class
        """

        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save obj to json
        to file
        """

        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(Base.to_json_string([i.to_dictionary() for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Update the class Base by adding the static method
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
