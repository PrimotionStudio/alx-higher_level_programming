#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        sum = a / b
    except:
        sum = None
    finally:
        print("Inside result: {}".format(sum))
    return (sum)
