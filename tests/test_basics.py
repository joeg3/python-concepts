import pprint

# Strings with single or double quotes cannot span multiple lines
s1 = "Hello" # You can use double quotes for a string
s2 = "World" # Most Python programmers use single quotes for a string

def test_print():
    print('Hi')
    person1 = { 'Name': 'Jim', 'Age': 33 }
    pprint.pprint(person1) # Use this to pretty print complex objects

def test_bool():
    """Show what values in Python evaluate to either true or false"""
    assert bool(0) == False     # int
    assert bool(0.0) == False   # float
    assert bool('') == False    # empty string
    assert bool([]) == False    # empty list
    assert bool({}) == False    # empty dictionary
    assert bool(None) == False  # Python 'None' value

    assert bool(1) == True               # int
    assert bool(-1) == True              # negative
    assert bool(0.001) == True           # float
    assert bool('Hi') == True            # non-empty string
    assert bool([1,2]) == True           # non-empty list
    assert bool({1:'a', 2:'b'}) == True  # non-empty dictionary

def test_string():
    assert "a3" == "a" + str(3) # Have to use str(), Python can't concatinate numbers and strings