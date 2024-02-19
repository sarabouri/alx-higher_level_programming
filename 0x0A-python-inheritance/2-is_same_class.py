#!/usr/bin/python3
"""
This is module for is_sa_class function that returns True
if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    checks if obj is an instance of a_class or not
    :param obj: object
    :param a_class: Class
    :return: True or False
    """
    if type(obj) == a_class:
        return True
    return False
