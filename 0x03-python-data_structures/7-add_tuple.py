#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = [0, 0]
    for i in range(2):
        if len(tuple_a) - 1 < i and len(tuple_b) - 1 < i:
            res[i] = 0
        elif len(tuple_a) - 1 < i:
            res[i] = 0 + tuple_b[i]
        elif len(tuple_b) - 1 < i:
            res[i] = tuple_a[i] + 0
        else:
            res[i] = tuple_a[i] + tuple_b[i]
    return tuple(res)
