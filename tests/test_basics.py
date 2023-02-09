

def test_line_continuation():
    # Backslash is a reserved line continuation character to break up long lines of code
    str = 'I want to have this long string \
on two lines'
    assert str == 'I want to have this long string on two lines'
    num = 3 + 4 \
          + 7
    assert num == 14

    # Can use parens for same effect:
    num = (3 + 4
          + 7)
    assert num == 14

def test_multiple_variable_creation_one_line():
    a = b = c = 8
    assert a == 8
    assert b == 8
    assert c == 8

    x, y, z = 3, 'hi', 7.7
    assert x == 3
    assert y == 'hi'
    assert z == 7.7

def test_types():
    assert type(4) == int
    assert type('hi') == str # Use keyword str, not string 'str'
    assert isinstance(5, int)

def test_none():
    assert not None         # In a conditional test, None evaluates to False
    #assert None == False   # But None isn't equal to False (this will give an error)
    assert None != True     # But None isn't equal to True  either (which makes sense)
    x = None       
    if x is None: # This is the typical way to distinguish None from a boolean False
        assert x is None 
    elif x:
        assert x is True
    else:
        assert x is False

def test_type_converstion():
    assert bool(1) == True
    assert int(False) == 0
    assert int(45.32) == 45
    assert int('81') == 81
    assert float(True) == 1.0
    assert float(77) == 77.0
    assert float('23') == 23.0
    assert 16 + 5.0 == 21.0   # Adding ints and floats results in a float

def test_bool():
    """ The Python function bool() converts any Python data type to a boolean """
    assert bool(0) == False     # int
    assert bool(0.0) == False   # float
    assert bool('') == False    # empty string
    assert bool([]) == False    # empty list
    assert bool({}) == False    # empty dictionary
    assert bool(set()) == False # empty set
    assert bool(None) == False  # Python 'None' value

    assert bool(1) == True               # int
    assert bool(-1) == True              # negative
    assert bool(0.001) == True           # float
    assert bool('Hi') == True            # non-empty string
    assert bool([1,2]) == True           # non-empty list
    assert bool({1:'a', 2:'b'}) == True  # non-empty dictionary

def test_ints():
    assert 1_000_000 == 1000000 # Use underscore as a digit separator instead of a comma
    assert 9 / 5 == 1.8         # Returns floating point
    assert 9 // 5 == 1          # No remainder with //
    assert 9 % 5 == 4           # Standard modulus
    assert divmod(9,5) == (1,4) # Get both quotient and remainder
    assert int(12.3) == 12      # Removes fractional part
    assert int('123') == 123
    assert 3 ** 2 == 9          # Use ** for exponents
    a = b = 7
    a -= 2
    b += 3
    assert a == 5
    assert b == 10

# The 'pass' statement is a no-op, used where Python requires a statement, or in creating minimal classes
def test_pass():
    pass # Remember to implement later

def test_meta():
    """ Reserved Python functions """
    func_name = test_meta.__name__
    docstring = test_meta.__doc__
    assert func_name == 'test_meta'
    assert docstring == ' Reserved Python functions '