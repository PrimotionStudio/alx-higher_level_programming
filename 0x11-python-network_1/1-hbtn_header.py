#!/usr/bin/python3
"""
1-hbtn_header.py
, sends a request to the URL and displays the
"""
from sys import argv
from urllib import request


req = request.Request(argv[1])
with request.urlopen(req) as response:
    print(dict(response.headers).get('X-Request-Id'))
