#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = 0
    weight = 0
    for x, y in my_list:
        weight += y
        total += x * y
    return total / weight
