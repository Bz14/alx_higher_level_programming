#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueSet = set(my_list)
    total = 0
    for value in uniqueSet:
        total += value
    return total
