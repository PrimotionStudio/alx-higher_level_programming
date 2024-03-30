#!/usr/bin/python3
"""
 Python script that takes in a URL
"""
from sys import argv
import requests


if __name__ == "__main__":
    payload = {'q': argv[2]}
    res = requests.post(argv[1], data=payload)
    print(res.text)
