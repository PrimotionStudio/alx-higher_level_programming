#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string == None):
        return (0)
    num = {
          'I': 1,
          'V': 5,
          'X': 10,
          'L': 50,
          'C': 100,
          'D': 500,
          'M': 1000
    }
    su = 0
    pr = 0
    for i in reversed(roman_string):
        val = num[i]
        if (val < pr):
            su -= val
        else:
            su += val
        pr = val
    return  (su)
