#!/bin/bash
# Bash script that sends a request to a URL
curl -sI -w %{http_code} $1
