# https://github.com/SREagle999/lab10-GH-AN
# Partner 1: Abhay Narayan
# Partner 2: Gabriel Harris

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return b/a

def log(a, b):
    if b <= 0:
        raise ValueError("Cannot divide by negative number!")
    return math.log(b, a)

def exp(a, b):
    math.pow(a, b)

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)

def exponent(a, b):
    return a ** b