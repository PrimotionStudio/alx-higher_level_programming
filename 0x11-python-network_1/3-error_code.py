#!/usr/bin/python3
"""ython script that takes in a UR
"""
from sys import argv
from urllib import request


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
