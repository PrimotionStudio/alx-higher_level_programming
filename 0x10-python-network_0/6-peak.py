#!/usr/bin/python3
def find_peak(list_of_integers):
    x = list_of_integers
    i = 1
    if x == []:
        return (None)
    peak = x[i]
    if len(x) < 3:
        return (max(x))
    while i < len(x) - 1:
        try:
            if x[i] > x[i + 1] and x[i] > x[i - 1]:
                peak = x[i]
            i += 1
        except IndexError:
            return peak
    return peak
