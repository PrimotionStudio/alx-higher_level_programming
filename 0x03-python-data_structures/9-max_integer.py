#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return (None)
    mx = 0
    count = 1
    for i in my_list:
        if (count == 1):
            mx = i
        if (mx < i):
            mx = i
        count = 0
    return (mx)
