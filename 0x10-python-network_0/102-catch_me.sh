#!/bin/bash
curl -s $1 | sed "s/*/You got me!/"
