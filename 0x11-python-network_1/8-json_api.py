#!/usr/bin/python3
"""
 Python script that takes in a URL
"""
from sys import argv
import requests


if __name__ == "__main__":
    try:
        payload = {'q': argv[1]}
        res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        obj = res.json()
        if obj:
            print("[{}] {}".format(obj['id'], obj['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except IndexError:
        pass
