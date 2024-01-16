#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('A') <= ord(i) <= ord('Z'):
            print("{}".format(i), end="")
        else:
            i = chr(ord(i) - ord('a') + ord('A'))
            print("{}".format(i), end="")
