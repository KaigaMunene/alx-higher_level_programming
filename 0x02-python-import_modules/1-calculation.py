#!/usr/bin/python3
from calculator_1 import add, subtract, mutiplication, division

if (__name__ == "__main__"):
    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, subtract(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mutiplication(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, division(a, b)))
