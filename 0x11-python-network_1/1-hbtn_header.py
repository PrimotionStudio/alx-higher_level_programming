#!/usr/bin/python3
"""
1-hbtn_header.py
"""
from sys import argv
from urllib import request


with request.urlopen(argv[1]) as response:
    print(dict(response.headers).get('X-Request-Id'))
