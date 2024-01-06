#!/usr/bin/python3
'''
Module for text indentaion

'''

def text_indentation(text):
    '''

    Function for text indent
    Args:
        text: string
    Error:
        TypeError

    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sen = []
    delim = ['.', '?', ':']
    for i in range(len(text)):
        if text[i] in delim:
            sen.append(text[i])
            print((''.join(sen)).strip(), end="\n\n")
            sen = []
        else:
            sen.append(text[i])

    if sen:
        print((''.join(sen)).strip(), end="")