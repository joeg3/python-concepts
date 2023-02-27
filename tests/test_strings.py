
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

    # Can use parens for same effect:
    num = (3 + 4
          + 7)
    assert num == 14

def test_built_in_string_functions():
    """ Strings are immutable, so these functions do not modify the string they operate on """
    assert str(3) + "a" == "3a" # Use str() to create a string from another datatype
    assert len('abc') == 3      # String length
    assert '1|2|3'.split('|') == ['1','2','3']
    assert '&'.join(['1','2','3']) == '1&2&3'
    assert '12345'.replace('3', '') == '1245'

    hi = '  Hi    '
    assert hi.strip() == 'Hi'      # Trim leading and trailing
    assert hi.lstrip() == 'Hi    ' # Trim leading
    assert hi.rstrip() == '  Hi'   # Trim trailing
    assert hi.strip('i ') == 'H'   # Default is to strip leading/trailing whitespace, but can specify characters to strip

    name = "dr. Fred Smith jr."
    assert name.capitalize() == "Dr. fred smith jr." # Capitalize first character, and lower case the others
    assert name.title() == "Dr. Fred Smith Jr."      # Capitalize all words
    assert name.removeprefix("dr. ") == "Fred Smith jr."
    assert name.removesuffix(" jr.") == "dr. Fred Smith" 
    assert name.upper() == "DR. FRED SMITH JR."
    assert name.lower() == "dr. fred smith jr."
    assert name.swapcase() == "DR. fRED sMITH JR."

    # Search and Select
    sentence = "It's a great day to go to the beach!"
    assert sentence.startswith("It's")
    assert sentence.endswith("beach!")

    # Get index of first occurrence of "to". Functions find() and index() work the same if substring is found,
    # but if not found, find returns -1, and index() raises an exception.
    assert sentence.find("to") == 17
    assert sentence.find("slopes") == -1
    assert sentence.index("to") == 17
    # assert sentence.index("slopes") # Raises exception if not found
    assert sentence.rfind("to") == 23 # Index of last occurrence
    assert sentence.count("to") == 2  # Number of occurrences
    assert not sentence.isalnum()     # Not all characters letters or numbers for this sentence


def test_string_basics():
    assert 'az' == 'a' + 'z'    # Strings can concatenate
    x = 'bcde'
    assert 'abcde' == 'a' + x    # Concatenate a variable
    assert 'b' == x[0]           # Get a character from a string by its index (returns a string of length 1)
    assert 'cd' == x[1:3]        # Can also grab a slice of string (last position excluded)
    assert 'bcd' == x[:3]        # Default first index is 0
    assert 'cde' == x[1:]        # Default last index is end of string
    assert 'de' == x[-2:]        # Second-last (included) to the end
    assert 'bd' == x[::2]        # Step size of 2, get every other character
    # x[0] = 'z'                 # Python strings are immutable, can't set a character
    assert 'bc' in 'abcd'        # Check if substring in another

    string_with_tab = 'Column1\tColumn2'
    string_with_newline = 'Row1\nRow2'
    escape_newline = 'This \\n represents a newline'

def test_string_formatting():
    """ f-strings are preferrable, otherwise {} and format(), and might at times see old % style """
    # f-strings, where 'f' is for format
    first_name = 'fred'
    last_name = 'smith'
    full_name = f'{first_name} {last_name}'
    assert full_name == 'fred smith'
    assert f'Hi {full_name.title()}!' == 'Hi Fred Smith!'

    # New style {} and format()
    s_template = 'Hello {}!'
    s = s_template.format('World')
    assert s == 'Hello World!'

    s_template = 'Hello {} {}!' # Positional arguments
    s = s_template.format('Freddy', 'Mercury')
    assert s == 'Hello Freddy Mercury!'

    s_template = 'Hello {first} {last}!'  # Named arguments
    s = s_template.format(first='Freddy', last='Mercury')
    assert s == 'Hello Freddy Mercury!'
    
    assert 'x = 7' == '{m} = {n}'.format(m='x', n=7)
    t = '{m} = {n}'
    assert 'x = 7' == t.format(m='x', n=7)

    # Old % style
    # There are many formatting options. we use one here to limit the float to one decimail point
    str = 'String: %s, Int: %d%%, Float: %.1f, Any type: %s' # A %s accepts any type, %% is a literal percent sign
    new_str = str % ('Hi', 7, 3.3, 6)
    assert new_str == 'String: Hi, Int: 7%, Float: 3.3, Any type: 6'

    