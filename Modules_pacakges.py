#calculator.py
def add (a,b):
    """Return the sum of two numbers."""
    return a+b

def subtract (a,b):
    """Return the subtraction of two numbers."""
    return a-b

def multiply (a,b):
    """Return the product of two numbers."""
    return a * b

def divide (a,b):
    """Return the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a/b