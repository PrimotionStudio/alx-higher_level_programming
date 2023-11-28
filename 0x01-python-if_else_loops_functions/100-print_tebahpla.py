#!/usr/bin/python3
i = 90
flag = 1
while (i >= 65):
    if (flag % 2 != 0):
        i += 32
    else:
        i -= 32
    flag += 1
    print(chr(i), end="")
    i -= 1
