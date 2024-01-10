#!/usr/bin/python3
"""
A module to add
items to a json file
"""
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    try:
        objs = load("add_item.json")
    except FileNotFoundError:
        objs = []

    objs.extend(sys.argv[1:])
    save(objs, "add_item.json")
