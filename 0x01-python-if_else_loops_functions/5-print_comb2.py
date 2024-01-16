#!/usr/bin/python3
for i in range(0, 100):
    x = str(i).zfill(2)
    if x == '99':
        print("{}".format(x))
    else:
        print("{}".format(x), end=", ")
