#!/usr/bin/python3
"""
github something
"""
from sys import argv
import requests


if __name__ == "__main__":
    h = {"Accept": "application/vnd.github+json",
         "Authorization": "Bearer {}".format(argv[2]),
         "X-GitHub-Api-Version": "2022-11-28"}
    res = requests.get("https://api.github.com/user", headers=h, auth=(argv[1], argv[2]))
    if "id" in res.json().keys():
        print(res.json()["id"])
    else:
        print(None)
