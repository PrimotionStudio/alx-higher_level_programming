#!/usr/bin/python3
'''

Module to add two integers

Returns the sum of the integers

Raises type error in each cases

'''


def add_integer(a, b=98):
    '''

    Function to add two integers
    
    Args:
        a: num1
        b: num2
    
    Return:
        the sum of the two numbers
    
    Error:
        raises type error its event
    
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (a + b)
