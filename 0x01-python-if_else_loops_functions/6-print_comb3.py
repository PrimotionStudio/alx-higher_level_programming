#!/usr/bin/python3
for i in range(0, 90):
    last_digit = int(i % 10)
    first_digit = int(i / 10)
    if (int(i / 10) < int(i % 10)):
        print(f"{int(i / 10)}{int(i % 10)}", end="")
        if (i == 89):
            print("")
        else:
            print(", ", end="")
