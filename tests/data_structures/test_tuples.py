# A tuple is just like a list except it is immutable and uses parenthesis instead of square brackets

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