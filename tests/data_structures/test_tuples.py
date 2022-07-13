# A tuple is an ordered immutable collection of objects

empty_tuple = tuple()   # Can use Python's built in function to create an empty tuple

vowels = ('a', 'e', 'i', 'o', 'u') # This is a tuple and not a list because it uses parens instead of square brackets

def test_tuple_basics():
    assert vowels[1] == 'e' # Access like a list

def test_single_object_tuple():
    # Every tuple needs to have at least one comma
    one_string_tuple = ('Hello')  # This gives an error
    one_string_tuple = ('Hello',) # Include trailing comma if only one object
    assert len(one_string_tuple) == 1
    assert type(one_string_tuple) is tuple