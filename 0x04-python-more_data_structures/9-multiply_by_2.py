#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b = dict()
    for i in a_dictionary:
        b.update({i: int(a_dictionary[i]) * 2})
    return (b)
