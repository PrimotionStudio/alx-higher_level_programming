#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = list()
    for i, v in a_dictionary.items():
        if (v == value):
            a.append(i)
    for j in a:
        del a_dictionary[j]
    return (a_dictionary)
