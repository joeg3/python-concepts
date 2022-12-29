# import calc

# Terminology
# - Arguments are passed to a function when calling it
# - Parameters are part of the function definition

# For mutable objects like lists, dictionaries, and sets, Python functions
# are "call by reference", where if a function changes the argument
# passed to it, the object will be changed in the calling code.

# For immutable ojects like strings, integers, and tuples, Python functions
# are "call by value", where a change to the argument passed
# to the function does not change the value in the calling code

def test_divide_with_positional_args():
    # It matters what order and position the args 8 and 2 are in
    assert 4 == divide(8, 2)

def test_divide_with_keyword_args():
    # It doesn't matter what order the args are in when using keyword args
    assert 4 == divide(dividend=8, divisor=2)
    assert 4 == divide(divisor=2, dividend=8)

def test_function_with_default_value():
    assert format_address_default('1910 Robinson', 'Redondo', 'CA', 55902) == '1910 Robinson, Redondo, CA 55902 USA'
    assert format_address_default('1910 Robinson', 'Redondo', 'CA', 55902, 'United States') == '1910 Robinson, Redondo, CA 55902 United States'

def test_function_with_optional_value():
    assert format_address_optional('1910 Robinson', 'Redondo', 'CA', 55902, 'USA') == '1910 Robinson, Redondo, CA 55902 USA'
    assert format_address_optional('1910 Robinson', 'Redondo', 'CA', 55902) == '1910 Robinson, Redondo, CA 55902'

# With keyword assignment, we can modify order of arguments
def test_function_with_keyword_assignment():
    # Convention is no spaces for keyword assignment: city='Redondo'
    assert format_address_default(city='Redondo', street='1910 Robinson', state='CA', country='U.S.A.', zip=55902) == '1910 Robinson, Redondo, CA 55902 U.S.A.'

def test_function_modifies_list():
    my_list = [1,2,3]
    modify_list(my_list)
    assert my_list == [2,3,1] # Function modifies original list

def test_prevent_function_modifying_list():
    my_list = [1,2,3]
    modify_list(my_list[:]) # If [:] is appended to argument, a copy is passed to the function and original not modified
    assert my_list == [1,2,3]

def test_function_arbitrary_args():
    assert pipe_words('a','b','c') == '|a|b|c|'
    assert pipe_words_with_description('Some letters','a','b','c') == 'Some letters: |a|b|c|'

def test_function_arbitrary_keyword_args():
    person = create_person('Jim', 'Smith', age=55, city='St. Paul') # Last two args are arbitrarily made up
    assert person['first'] == 'Jim'
    assert person['last'] == 'Smith'
    assert person['age'] == 55
    assert person['city'] == 'St. Paul'


def test_check_string_has_character():
    assert check_string_has_character('a')
    assert not check_string_has_character('')

############################## Functions ##############################

def divide(dividend, divisor):
    """Python functions are documented with triple-quotes called docstrings
        This function divides the divisor into the dividend and returns the quotient
    """
    quotient = dividend / divisor
    return quotient

def format_address_default(street, city, state, zip, country='USA'):
    """Return formatted address, default for 'country' is 'USA'
       Note that the default parameter needs to be the last parameter. Otherwise, 
       omitting it would mess up the other argument postions in the call.
       Also, convention is no spaces for default: country='USA'
    """
    return street + ", " + city + ", " + state + " " + str(zip)  + " " + country

def format_address_optional(street, city, state, zip, country=''):
    """Return formatted address, use empty string default for country to make it optional
       Note that the optional parameter needs to be the last parameter. Otherwise, 
       omitting it would mess up the other argument postions in the call.
    """
    if country:
        return street + ", " + city + ", " + state + " " + str(zip)  + " " + country
    else:
        return street + ", " + city + ", " + state + " " + str(zip)

def modify_list(some_list):
    """Moves first element to last postition"""
    first = some_list.pop(0)
    some_list.append(first)

def pipe_words(*word_list):
    """ Accepts an arbitrary number of words and surrounds them by pipes
        An asterisk before fav_colors means an arbitrary number of args can be passed in
        The asterisk causes Python to make a tuple of all args passed in
    """
    piped_words = '|'
    for word in word_list:
        piped_words += (word + '|')
    return piped_words

def pipe_words_with_description(description, *word_list): # It's convention to name arbitrary parameter *args
    """ If some parameters like 'description' in this case are not arbitrary, they must
        be placed first, and arbitrary parameter last
    """
    piped_words = description + ': |'
    for word in word_list:
        piped_words += (word + '|')
    return piped_words

# Double asterisk has Python create a person_info dictionary containing extra args after first, last args
def create_person(first, last, **person_info): # It's convention to name arbitrary keyword parameter **kwargs
    """ The first and last parameters are always used, and other arbitrary key value pairs
        in function call are aded to person_info dictionary. You can add as many key/value
        pairs as you want when calling this function
    """
    person_info['first'] = first
    person_info['last'] = last
    return person_info

# This function uses annotations as documentation that the a_string argument is a string
# and the functions returns a boolean.
# Note: In Python, annotations are infomrational only and don't do any kind of type checking
def check_string_has_character(a_string:str) -> bool:
    """Return True if input string has characters, otherwise returns False"""
    return bool(a_string) # Since a zero-length string evaluates to false, and non-zero to true, we can just pass to bool()

