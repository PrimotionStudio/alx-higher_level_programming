#!/usr/bin/python3
"""
A module used to
save to json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function used to
    save to json file
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)
