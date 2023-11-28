#!/usr/bin/python3
char = ord('a')
while char <= ord('z'):
    print("{}".format(chr(char)), end='')
    char += 1
