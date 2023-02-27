""" It's a good practice to have a docstring at the top of modules """
""" Modules should be lowercase with underscores separating words """

def get_remainder(dividend, divisor):
    """ Divides the divisor into the dividend and returns the remainder """
    remainder = dividend % divisor
    return remainder

def calc_exponent(num, exp):
    return num ** exp

def right_triangle_area(base, height):
    return (base * height) / 2

def rectangle_area(length, width):
    return length * width
