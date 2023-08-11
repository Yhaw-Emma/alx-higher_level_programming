#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    num_args = len(sys.argv)
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    x = int(sys.argv[1])
    oprt = sys.argv[2]
    y = int(sys.argv[3])
    if oprt == '+':
        print("{} {} {} = {}".format(x, oprt, y, add(x, y)))
    elif oprt == '-':
        print("{} {} {} = {}".format(x, oprt, y, sub(x, y)))
    elif oprt == '*':
        print("{} {} {} = {}".format(x, oprt, y, mul(x, y)))
    elif oprt == '/':
        print("{} {} {} = {}".format(x, oprt, y, div(x, y)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
