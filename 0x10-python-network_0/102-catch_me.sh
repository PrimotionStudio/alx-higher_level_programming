#!/bin/bash
# bash script
curl -sI 0.0.0.0:5000/catch_me | grep "Content-Length: " | sed "s/Content-Length: 178/You got me\!/g"
