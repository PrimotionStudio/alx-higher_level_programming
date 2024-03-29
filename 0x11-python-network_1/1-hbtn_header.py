#!/usr/bin/python3
"""
1-hbtn_header.py
, sends a request to the URL and displays the
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
