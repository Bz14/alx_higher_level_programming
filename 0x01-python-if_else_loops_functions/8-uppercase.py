#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if s >= 'a' and s <= 'z':
            print("{}".format(chr(ord(s) - 32)), end='')
        else:
            print("{}".format(s), end='')
    print('')
