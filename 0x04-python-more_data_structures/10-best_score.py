#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return (None)
    if len(a_dictionary) == 0:
        return (None)
    bk = None
    f = 0
    for i in a_dictionary:
        if f == 0:
            bk = i
            f = 1
        else:
            if a_dictionary[i] > a_dictionary[bk]:
                bk = i
                f = 1
    return (bk)
