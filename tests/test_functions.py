#import calc

# The 'def' keyword names the function and any arguments

# Python functions are "call by reference" for mutable objects
# like lists, dictionaries, and sets, where a change to the argument
# passed to the function changes the value in the calling code.

# Python functions are "call by value" for immutable ojects like
# strings, integers, and tuples, where a change to the argument passed
# to the function does not change the value in the calling code

def test_add():
    assert add(1,1) == 2

def test_check_string_has_character():
    assert check_string_has_character('a')
    assert not check_string_has_character('')

def test_function_with_default_value():
    assert format_address('1910 Robinson', 'Redondo', 'CA', 55902) == '1910 Robinson, Redondo, CA 55902 USA'

# With keyword assignment, we can modify order of arguments
def test_function_with_keyword_assignment():
    assert format_address(street='1910 Robinson', city='Redondo', state='CA', country='U.S.A.', zip=55902) == '1910 Robinson, Redondo, CA 55902 U.S.A.'

def add(x, y):
    """Python functions are documented with triple-quotes called docstrings"""
    """This function adds x and y and returns the result"""
    return x + y

# This function uses annotations as documentation that the a_string argument is a string
# and the functions returns a boolean.
# Note: In Python, annotations are infomrational only and don't do any kind of type checking
def check_string_has_character(a_string:str) -> bool:
    """Return True if input string has characters, otherwise returns False"""
    return bool(a_string) # Since a zero-length string evaluates to false, and non-zero to true, we can just pass to bool()

# How to add a default value to an argument
def format_address(street:str, city:str, state:str, zip:int, country:str='USA') -> str:
    """Return formatted address, default for 'country' is 'USA'"""
    return street + ", " + city + ", " + state + " " + str(zip)  + " " + country