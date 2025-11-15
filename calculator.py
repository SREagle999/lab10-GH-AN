import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a/b

def log(a, b):
    if b <= 0:
        raise ValueError("Cannot divide by negative number!")
    return math.log(b, a)

def exp(a, b):
    math.pow(a, b)