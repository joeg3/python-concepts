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

global_var = 'pine'

def test_none_returned_if_no_return_statement():
    # Functions that do not have a return statement return None
    x = do_nothing()
    assert x == None

def test_divide_with_positional_args():
    # It matters what order and position the args 8 and 2 are in
    assert 4 == divide(8, 2)

def test_divide_with_keyword_args():
    # It doesn't matter what order the args are in when using keyword args
    assert 4 == divide(dividend=8, divisor=2)
    assert 4 == divide(divisor=2, dividend=8)

def test_function_with_default_value():
    # Default parameter values are calcultaed when the function is defined, not when it's run.
    # So if using a mutable datatype like a list, you may get unexpected results.
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
    args = ('a','b','c')
    assert pipe_words(*args) == '|a|b|c|'

def test_function_arbitrary_keyword_args():
    person = create_person('Jim', 'Smith', age=55, city='St. Paul') # Last two args are arbitrarily made up
    assert person['first'] == 'Jim'
    assert person['last'] == 'Smith'
    assert person['age'] == 55
    assert person['city'] == 'St. Paul'

def test_check_string_has_character():
    assert check_string_has_character('a')
    assert not check_string_has_character('')

def test_function_modifies_mutable_argument():
    """ Something to be aware of, you would want your function to return the new value
        instead of modifying arguments """
    my_list = ['a', 'b', 'c']
    set_first_element_to_z(my_list)
    assert my_list == ['z', 'b', 'c']

def test_pass_function_as_arg():
    """ favorite_number() is a function below that just returns 7. Pass function favorite_number() to run_func().
        But in Python putting parens on end of function means "run it". So we pass it without parens.
    """
    assert run_func(favorite_number) == 7

def test_pass_func_as_arg_with_args():
    """ Here we pass the args the function needs along with the function """
    assert run_func_with_params(divide, 24, 3) == 8

def test_pass_func_and_positional_args():
    """ Here we pass our function that takes positional args """
    assert run_func_with_positional_args(pipe_words, 'a','b','c') == '|a|b|c|'

def test_example_of_inner_function():
    assert outer(7,8) == 15

def test_example_of_closure():
    f = colsure(7,8) # f is a closure, a function with the args that were passed to it, that hasn't been run
    assert f() == 15 # Run the closue code

def test_example_of_lambda_function():
    # This is regular way where we pass in a function defined somewhere else
    assert 9 == unary_num_operation(3, square)

    # Since fuunction is so small, we can replace it with a lambda
    # A lambda has zero or more comma-separated arguments, followed by a colon followed by the definition of the function
    assert 9 == unary_num_operation(3, lambda num: num * num)

def test_example_of_generator():
    """ A generator can only be run once because it creates its values on the fly, unlike lists, etc. that 
        are held in memory. But it's good for large datasets since it's not all in memory at the same time"""
    generator = my_generator_function(1,5)
    sum = 0
    for x in generator:
        sum += x
    assert sum == 10

def test_namespaces():
    nonlocal_var = 'oak'
    # def access_and_change_global():
    #     # If you try to access global variable AND change it, you get an error
    #     print(global_var)
    #     global_var = 'maple'

    def change_local():
        # If you only try to change it, it changes local global_var variable in the function
        global_var = 'palm'

    def change_nonlocal():
        nonlocal nonlocal_var # Since nonlocal_var is not global (it's in the test function), use nonlocal keyword to change it
        nonlocal_var = 'spruce'

    def change_global():
        global global_var # Use global keyword to modify global global_var variable
        global_var = 'birch'

    #access_and_change_global()
    change_local()
    assert global_var == 'pine'
    change_nonlocal()
    assert nonlocal_var == 'spruce'
    change_global()
    assert global_var == 'birch'

############################################## Functions #################################################

def do_nothing():
    pass

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

def pipe_words(*args):
    """ Accepts an arbitrary number of zero or more words and surrounds them by pipes
        An asterisk before fav_colors means an arbitrary number of args can be passed in
        The asterisk causes Python to make a tuple of all args passed in. 
        It's convention to name tuple parameter *args
    """
    piped_words = '|'
    for word in args:
        piped_words += (word + '|')
    return piped_words

def pipe_words_with_description(description, *args): # It's convention to name tuple argument *args
    """ If some parameters like 'description' in this case are not arbitrary, they must
        be placed first, and arbitrary parameter last
    """
    piped_words = description + ': |'
    for word in args:
        piped_words += (word + '|')
    return piped_words

# Double asterisk has Python create a person_info dictionary containing extra args after first, last args
def create_person(first, last, **kwargs): # It's convention to name arbitrary keyword parameter **kwargs
    """ The first and last parameters are always used, and other arbitrary key value pairs
        in function call are aded to person_info dictionary. You can add as many key/value
        pairs as you want when calling this function
    """
    kwargs['first'] = first
    kwargs['last'] = last
    return kwargs

# This function uses annotations as documentation that the a_string argument is a string
# and the functions returns a boolean.
# Note: In Python, annotations are infomrational only and don't do any kind of type checking
def check_string_has_character(a_string:str) -> bool:
    """Return True if input string has characters, otherwise returns False"""
    return bool(a_string) # Since a zero-length string evaluates to false, and non-zero to true, we can just pass to bool()

def set_first_element_to_z(a_list):
    a_list[0] = 'z'

def favorite_number():
    return 7

def run_func(func):
    return func()

def run_func_with_params(func, x, y):
    return func(x, y)

def run_func_with_positional_args(func, *args):
    return func(*args)

def outer(a,b):
    def inner(c,d):
        return c + d
    return inner(a,b) # Run inner() and return its result

def colsure(a,b):
    def inner():
        return a + b
    return inner  # Here we return the inner() function, not its result, as well as args passed in

def square(num):
    return num * num

# Used with lambda example
def unary_num_operation(num, func):
    return func(num)

def my_generator_function(first=0, last=10, step=1):
    num = first
    while num < last:
        yield num
        num += step