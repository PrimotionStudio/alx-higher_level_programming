#!/usr/bin/python3
"""
Python script that takes in a URL
"""
from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])
    if 'X-Request-Id' in req.__dict__['headers']:
        print(str(req.__dict__['headers']['X-Request-Id']))
