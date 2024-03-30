#!/bin/bash
# Bash script that takes in a URL
curl -sI -X OPTIONS $1 | grep "Allow: " | sed "s/Allow: //g"
