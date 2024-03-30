#!/usr/bin/python3
"""
github something
"""
from sys import argv
import requests


if __name__ == "__main__":
    h = {"Accept": "application/vnd.github+json",
         "X-GitHub-Api-Version": "2022-11-28"}
    res = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(argv[1], argv[2]), headers=h)
    objs = sorted(res.json(), reverse=True,
                  key=lambda x: x['commit']['author']['date'])[:10]
    for i in objs:
        print("{}: {}".format(i['sha'], i['commit']['author']['name']))
