#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = list()
    if (len(tuple_a) == 0):
        a = 0
        b = 0
    elif (len(tuple_a) == 1):
        a = tuple_a[0]
        b = 0
    elif (len(tuple_a) == 2):
        a = tuple_a[0]
        b = tuple_a[1]
    if (len(tuple_b) == 0):
        c = 0
        d = 0
    elif (len(tuple_b) == 1):
        c = tuple_b[0]
        d = 0
    elif (len(tuple_b) == 2):
        c = tuple_b[0]
        d = tuple_b[1]
    new = [int(a) + int(c), int(b) + int(d)]
    return (tuple(new))
