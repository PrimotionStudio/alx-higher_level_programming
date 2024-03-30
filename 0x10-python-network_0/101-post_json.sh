#!/bin/bash
# 101 post json sh
curl -s -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d $2 $1
