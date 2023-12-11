#!/usr/bin/python3
def max_integer(my_list=[]):
    maxVal = float("-inf")
    if (len(my_list) == 0):
        return None
    for val in my_list:
        if val > maxVal:
            maxVal = val
    return maxVal
