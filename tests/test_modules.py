# A module is just any file with Python code
# A package is just a subdirectory with .py files

# There are three locations the interpreter searches when looking for a module:
# 1. Your current working directory
# 2. Your interpreter's site-packages locations. These are folders that contain any thire-party Python modules
#    you installed, including your own.
# 3. The standard library
# The interpreter looks in your current working directory first.

# For specific mechanics of importing, see src/calc.py which itself imports from calc_module.py

from src import calc

def test_import_module():
    """ Look at src/calc.py, which imports calc_module """
    result = calc.remainder_alert(3, 2)
    assert result == '@@'

def test_import_specific_function():
    """ Look at src/calc.py, which imports specific function calc_exponent from module """
    result = calc.square_number(3)
    assert result == 9

def test_import_module_with_alias():
    """ Look at src/calc.py, which imports calc_module and gives it alias cm """
    result = calc.cube_number(2)
    assert result == 8

def test_import_specific_function_with_alias():
    """ Look at src/calc.py, which imports specific function right_triangle_area from module and gives it alias rta """
    result = calc.get_right_triangle_area(3, 2)
    assert result == 3

def test_import_all_functions_of_module():
    """ Look at src/calc.py, which uses an asterisk to import all functions from module calc_module """
    result = calc.get_rectangle_area(3, 2)
    assert result == 6
