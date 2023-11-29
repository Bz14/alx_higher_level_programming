#!/usr/bin/python3
def uppercase(str):
    for s in str:
        print("{}".format(chr(ord(s) - 32) if s >= 'a'
                          and s <= 'z' else s), end='')
    print('')
