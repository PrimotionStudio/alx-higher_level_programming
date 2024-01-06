#!/usr/bin/python3
'''
Module to divide a matrix by an arg
and returns a new matrix
the old matrix remains unchanged
'''


def matrix_divided(matrix, div):
    '''
    divides each element of a matrix by div the arg
    Args:
        matrix: the list of lists
        div: the div to divide everything by
    Returns:
        a new list of lists with the divided element
    Errors:
        TypeError
        ZeroDivisionError
    '''
    flag = 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        '''
        if flag is 0
        assign the length of the sub-list to list_lenght
        else
        check if length is the same
        
        also change the flag to 1 so that the code wont run again
        '''
        if flag == 0:
            list_length = len(matrix[i])
        else:
            if len(matrix[i]) != list_length:
                raise TypeError("Each row of the matrix must have the same size")
        flag = 1
        new_matrix.append([])
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            d = "{:.2f}".format(matrix[i][j] / div)
            new_matrix[i].append(float(d))
    return new_matrix
