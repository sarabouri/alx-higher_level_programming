#!/usr/bin/python3
"""
This module defines lookup(obj) function that
returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    returns the list of available
    attributes and methods of obj
    :param obj: object
    """
    return dir(obj)
