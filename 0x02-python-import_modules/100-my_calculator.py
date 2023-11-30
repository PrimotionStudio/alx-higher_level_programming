#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if (len(argv) != 4) or not argv[1].isnumeric() or not argv[3].isnumeric():
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = argv[1]
    b = argv[3]
    ans = ""
    operator = argv[2]
    if operator == '+':
        ans = add(int(a), int(b))
    elif operator == '-':
        ans = sub(int(a), int(b))
    elif operator == '*':
        ans = mul(int(a), int(b))
    elif operator == '/':
        ans = div(int(a), int(b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, argv[2], b, ans))
