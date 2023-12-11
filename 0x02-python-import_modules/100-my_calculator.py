#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    res = 0
    if sys.argv[2] == "+":
        res = int(sys.argv[1]) + int(sys.argv[3])
    elif sys.argv[2] == "-":
        res = int(sys.argv[1]) - int(sys.argv[3])
    elif sys.argv[2] == "*":
        res = int(sys.argv[1]) * int(sys.argv[3])
    elif sys.argv[2] == "/":
        res = int(sys.argv[1]) / int(sys.argv[3])
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {res}")
