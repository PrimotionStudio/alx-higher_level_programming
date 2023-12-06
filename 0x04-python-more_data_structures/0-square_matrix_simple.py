#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = list()
    for i in matrix:
        new.append(list())
        for j in i:
            new[-1].append(j)
    for i in range(len(new)):
        for j in range(len(new[i])):
            new[i][j] = new[i][j]  ** 2
    return (new)
