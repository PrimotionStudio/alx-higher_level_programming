#!/usr/bin/python3
"""
A module thata
load from json file
"""
import json


def load_from_json_file(filename):
    """
    a function that laods
    from a json file
    """

    with open(filename, "r") as f:
        return json.loads(f.read())
