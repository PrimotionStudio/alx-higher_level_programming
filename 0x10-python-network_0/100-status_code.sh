#!/bin/bash
# Bash script that sends a request to a URL
curl -s -w %{http_code} $1
