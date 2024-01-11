#!/usr/bin/python3
"""
Print Pascal Triangle
And MATH
"""


def pascal_triangle(n):
    """
    Function to print 
    and ret pascal triangle
    """

    if n == 0:
        return []
    if n == 1:
        return [1]
    pas = [0, 1, 0]
    for i in range(n):
        newpas = [0]
        for j in range(len(pas)):
            if j == (len(pas) - 1):
                newpas.append(0)
            else:
                newpas.append(pas[j] + pas[j + 1])
        pas = list(newpas)
    return pas[1: -1]

print([pascal_triangle(i) for i in range(5)])
