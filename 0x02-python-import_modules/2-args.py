#!/usr/bin/python3
from sys import argv
    
    if __name__ == "__main__":
        i = len(argv) - 1
        if i == 1:
            print("0 arguments.")
        elif i == 2:
            print("{} arguments:"format(i - 1))
        else:
            print("{} arguments:"format(i - 1))
        for j in range(i):
            print("{}: {}".format(j + 1, argv[j + 1]))
