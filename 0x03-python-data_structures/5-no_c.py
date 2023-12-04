#!/usr/bin/python3
def no_c(my_string):
    ls = list(my_string)
    for i in range(len(my_string)):
        if ls[i] == 'c' or ls[i] == 'C':
            ls[i] = ''
    return ''.join(ls)
