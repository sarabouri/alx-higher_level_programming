#!/usr/bin/python3
from sys import argv
    
if __name__ == "__main__":
    i = len(argv) - 1
    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("{} arguments:"format(i))
    else:
        print("{} arguments:"format(i))
    for j in range(i):
        print("{}: {}".format(j + 1, argv[j + 1]))
