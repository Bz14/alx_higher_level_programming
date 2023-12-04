#!/usr/bin/python3
def max_integer(my_list=[]):
    maxVal = 0
    if (len(my_list) == 0):
        return None
    for val in my_list:
        if val > maxVal:
            maxVal = val
    return maxVal
