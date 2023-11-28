#!/usr/bin/python3
char = ord('a')
while char <= ord('z'):
    if chr(char) != 'q' and chr(char) != 'e':
        print("{}".format(chr(char)), end='')
    char += 1
