
# Strings with single or double quotes cannot span multiple lines
s1 = "Hello" # You can use double quotes for a string
s2 = 'World' # Most Python programmers use single quotes for a string

# To print a long line, you can break it up by quoting each line and indenting
print("######################################"
    " Running Basic Python Tests "
    "########################################")

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

def test_bool():
    """Show what values in Python evaluate to either true or false"""
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

def test_string():
    assert "a3" == "a" + str(3) # Have to use str(), Python can't concatinate numbers and strings
    assert 'az' == 'a' + 'z'    # But strings can concatenate
    x = 'bcde'
    assert 'abcde' == 'a' + x    # Concatenate a variable
    assert 'b' == x[0]           # Get a character from a string by its index (returns a string of length 1)
    assert 'cd' == x[1:3]        # Can also grab a slice of string (last position excluded)
    assert 'bcd' == x[:3]        # Default first index is 0
    assert 'cde' == x[1:]        # Default last index is end of string
    assert 'de' == x[-2:]        # Second-last (included) to the end
    # x[0] = 'z'                 # Python strings are immutable, can't set a character
    assert 3 == len('abc')       # String length
    assert 'bc' in 'abcd'        # Check if substring in another
    assert ['1','2','3']  == '1|2|3'.split('|')
    assert 'Hi' == '  Hi    '.strip()        # Trim before and after
    assert 'Hi    ' == '  Hi    '.lstrip()   # Trim on left
    assert '  Hi' == '  Hi    '.rstrip()   # Trim on right
    url = 'https://www.ibm.com'
    assert 'www.ibm.com' == url.removeprefix('https://')
    assert 'Fred' == 'Fred Jr.'.removesuffix(' Jr.')
    assert 'fred smith'.title() == 'Fred Smith'
    assert 'fred'.upper() == 'FRED'
    assert 'Fred'.lower() == 'fred'

    string_with_tab = 'Column1\tColumn2'
    string_with_newline = 'Row1\nRow2'

def test_string_formatting():
    # f-strings, where 'f' is for format
    first_name = 'fred'
    last_name = 'smith'
    full_name = f'{first_name} {last_name}'
    assert full_name == 'fred smith'
    assert f'Hi {full_name.title()}!' == 'Hi Fred Smith!'

    s_template = 'Hello {}!'
    s = s_template.format('World')
    assert s == 'Hello World!'
    s_template = 'Hello {first} {last}!'
    s = s_template.format(first='Freddy', last='Mercury')
    assert s == 'Hello Freddy Mercury!'
    assert 'x = 7' == '{m} = {n}'.format(m='x', n=7)
    t = '{m} = {n}'

    name = 'Jim'
    assert 'jim' == name.lower()
    assert 'Jim' == name # lower() doesn't alter variable, just returns lowercase value

def test_logical_operators():
    a = 3
    if(2 < a and a < 5):
        assert True

    if(2 < a and not a > 5):
        assert True

# The 'pass' statement is a no-op, used where Python requires a statement, or in creating minimal classes
def test_pass():
    pass # Remember to implement later