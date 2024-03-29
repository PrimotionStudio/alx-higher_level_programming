#!/usr/bin/python3
"""ython script that takes in a UR
"""
from sys import argv
from sys import request, parse


if __name__ == "__main__":
    url = argv[1]
    email = {'email' : argv[2] }
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
       print(the_page.decode('utf-8'))
