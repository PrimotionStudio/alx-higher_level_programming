#!/bin/bash
# 101 post json sh
curl -s -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d "$(cat "$2")" $1
