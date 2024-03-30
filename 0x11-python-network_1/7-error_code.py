#!/usr/bin/python3
"""
 Python script that takes in a URL
"""
from sys import argv
import requests


if __name__ == "__main__":
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
