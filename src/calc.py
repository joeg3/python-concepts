# Five ways to import
from src import calc_module # Every function from calc_module is available here with syntax calc_module.function_name()
from src.calc_module import calc_exponent # Import specific function
from src import calc_module as cm # Import module and give it an alias
from src.calc_module import right_triangle_area as rta # Import a specific function and give it an alias
from src.calc_module import * # Import all functions of module
# !!!!! The previous line, importing all functions of module isn't recommended because of the potential for name collisions.
# It's recommended to import the functions you'll use, or import the entire module and use dot notation.

# Note, some modules have submodules
from os import path   # Import the path submodule from the os module, can call path.abspath()

""" This is just a module that relies on importing another module """

def remainder_alert(dividend, divisor):
    """ Uses the import of the entire module """
    remainder = calc_module.get_remainder(dividend, divisor)
    if remainder:
        return '@@'
    else:
        return remainder

def square_number(num):
    """ Uses the import of a specific function"""
    return calc_exponent(num, 2)

def cube_number(num):
    """ Uses import of module with alias """
    return cm.calc_exponent(num, 3)

def get_right_triangle_area(base, height):
    """ Uses import of function with alias"""
    return rta(base, height)

def get_rectangle_area(length, width):
    """ Uses import all functions of module !!! Not recommended to do this !!! """
    return rectangle_area(length, width)
