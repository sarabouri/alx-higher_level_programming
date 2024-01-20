#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[0] == None:
        return None
    else:
        length = len(sentence)
        c = sentence[0]
        result = [length, c]
        return result
