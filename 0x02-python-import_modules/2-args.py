#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    print("{} {}{}".format(length - 1, "arguments" if
                           length - 1 != 1 else "argument",
                           "." if length - 1 == 0 else ":"))
    for i in range(1, length):
        print("{}: {}".format(i, sys.argv[i]))
