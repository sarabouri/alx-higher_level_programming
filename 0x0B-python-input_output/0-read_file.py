#!/usr/bin/python3
"""This module defines a read_file function
that reads a file and prints it's content to stdout."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
