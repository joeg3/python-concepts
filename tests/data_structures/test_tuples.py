# A tuple is just like a list except it is immutable and uses parenthesis instead of square brackets

def test_create_empty_tuple():
    empty_tuple = tuple()  # Can use Python's built in function to create an empty tuple
    empty_tuple = ()       # Or just use parens
    assert len(empty_tuple) == 0

def test_create_single_element_tuple():
    # Every tuple needs to have at least one comma
    this_is_a_string = ('Hello')  # This just creates a string
    assert type(this_is_a_string) is str

    one_string_tuple = ('Hello',) # Include trailing comma if only one element
    assert len(one_string_tuple) == 1
    assert type(one_string_tuple) is tuple

def test_create_multiple_element_tuple():
    mult_element_tuple = ('a', 'b', 'c') # For multiple elements, don't follow last element with a comma
    assert len(mult_element_tuple) == 3

def test_create_from_list():
    cousins_list = ['Ed', 'Mike']
    cousins_tuple = tuple(cousins_list)
    assert len(cousins_tuple) == 2

def test_combine_tuples():
    cousins_tuple = ('Ed', 'Mike')
    friends_tuple = ('Kevin', 'Jeff')
    bestie_tuple = cousins_tuple + friends_tuple
    assert len(bestie_tuple) == 4

def test_retrieve_elements():
    letters = ('x', 'y', 'z')
    assert letters[1] == 'y' # Access like a list

    # Assign multiple variables at once
    l1, l2, l3 = letters
    assert l1 == 'x'
    assert l2 == 'y'
    assert l3 == 'z'

def test_overwrite_tuple():
    # While you can't modify a tuple, you can assign a new value, having the variable point to a different tuple
    nums = (1,2,3)
    assert nums == (1,2,3)
    nums = (4,5,6)
    assert nums == (4,5,6)

def test_loop_thru_tuple():
    sum = 0
    for x in (1,2,3):
        sum = sum + x
    assert sum == 6