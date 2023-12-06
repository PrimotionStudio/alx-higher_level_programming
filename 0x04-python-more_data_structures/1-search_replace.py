#!/usr/bin/python3
def search_replace(my_list, search, replace):
    b = list()
    for i in my_list:
        b.append(i)
    for i in range(len(b)):
        if (b[i] == search):
            b[i] = replace
    return (b)
