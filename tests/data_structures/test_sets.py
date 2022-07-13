# A set is an unordered set of unique objects
# Even though sets use curly braces, they are not key/value pairs, just unique values
# You cannot assume any order with a set

empty_set = set()   # Can use Python's built in function to create an empty set

def test_create_set():
    vowels = {'a', 'e', 'e', 'i', 'o', 'o', 'u'} # Creates  {'a', 'e', 'i', 'o', 'u') but probably different order
    vowels = set('aeeioou')                      # Does same thing as previous line
    assert len(vowels) == 5

def test_union(): # A union creates a set of all unique objects from both sets
    vowels = set('aeeioou')
    union_set = vowels.union(set('minneapolis'))
    assert len(union_set) == 10 # 'a', 'e', 'i', 'o', 'u', 'm', 'n', 'p', 'l', 's' in some order

def test_create_sorted_list_from_set():
    city = set('minneapolis') # Creates set with duplicate letters removed
    assert len(city) == 9
    sorted_list = sorted(list(city)) # Creates list with letters sorted
    assert sorted_list == ['a', 'e', 'i', 'l', 'm', 'n', 'o', 'p', 's']
    assert type(sorted_list) is list

def test_differece_between_sets():
    set1 = set('abcde')
    set2 = set('defgh')
    d = set1.difference(set2) # Returns new set of objects that are in set1 but not in set2
    sorted_diff = sorted(list(d))
    assert sorted_diff == ['a', 'b', 'c']
    assert type(sorted_diff) is list

def test_intersection_between_sets():
    set1 = set('abcde')
    set2 = set('defgh')
    d = set1.intersection(set2) # Returns new set of objects that are in both sets
    sorted_int = sorted(list(d))
    assert sorted_int == ['d','e']
    assert type(sorted_int) is list