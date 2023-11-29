#!/usr/bin/python3
turn = 0
for i in range(ord('z'), ord('a') - 1, -1):
    if turn:
        print("{}".format(chr(i - 32)), end='')
        turn = 0
    else:
        print("{}".format(chr(i)), end='')
        turn = 1
