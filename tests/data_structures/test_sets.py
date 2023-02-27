# A set is an unordered set of unique objects
# Even though sets use curly braces, they are not key/value pairs, just unique values
# You cannot assume any order with a set


def test_create_set():
    empty_set = set()
    assert len(empty_set) == 0

    vowels = {'a', 'e', 'e', 'i', 'o', 'o', 'u'} # Creates  {'a', 'e', 'i', 'o', 'u') but probably different order
    vowels = set('aeeioou')                      # Does same thing as previous line
    assert len(vowels) == 5

def test_get_length():
    assert len({'a', 'b', 'c'}) == 3

def test_create_set_from_data_structure():
    list = ['a', 'b', 'b', 'c']
    set_from_list = set(list)
    assert len(set_from_list) == 3

    tuple = ('a', 'b', 'b', 'c')
    set_from_tuple = set(tuple)
    assert len(set_from_tuple) == 3

    dict = {'a': 'b', 'c': 'd'}
    set_from_dict = set(dict)  # Returns keys of dict
    assert len(set_from_dict) == 2

def test_if_in_set():
    my_set = set(('a', 'b', 'c'))
    assert 'b' in my_set

def test_add_to_set():
    my_set = {'a', 'b', 'c'}
    my_set.add('d')
    assert my_set == {'a', 'b', 'c', 'd'}

def test_remove_from_set():
    my_set = {'a', 'b', 'c'}
    my_set.remove('b')
    assert my_set == {'a', 'c'}

def test_create_sorted_list_from_set():
    city = set('minneapolis') # Creates set with duplicate letters removed
    assert len(city) == 9
    sorted_list = sorted(list(city)) # Creates list with letters sorted
    assert sorted_list == ['a', 'e', 'i', 'l', 'm', 'n', 'o', 'p', 's']
    assert type(sorted_list) is list

def test_create_frozen_set():
    my_set = set(('a', 'b', 'c'))
    fs = frozenset(my_set) # Creates an immutable set
    # fs.add('d') # This throws error

def test_differece_between_sets():
    set1 = set('abcde')
    set2 = set('defgh')
    d1 = set1.difference(set2) # Returns new set of objects that are in set1 but not in set2
    d2 = set1 - set2           # Another way to get difference
    sorted_diff = sorted(list(d1))
    assert sorted_diff == ['a', 'b', 'c']
    assert type(sorted_diff) is list

def test_union():
    set1 = set('abcde')
    set2 = set('defgh')
    u1 = set1.union(set2) # Returns new set of objects that are in set1 and/or set2
    u2 = set1 | set2      # Another way to do union
    sorted_union = sorted(list(u1))
    assert sorted_union == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    assert type(sorted_union) is list

def test_intersection_between_sets():
    set1 = set('abcde')
    set2 = set('defgh')
    d1 = set1.intersection(set2) # Returns new set of objects that are in both sets
    d2 = set1 & set2             # Another way to get intersection
    sorted_int = sorted(list(d1))
    assert sorted_int == ['d','e']
    assert type(sorted_int) is list

""" In addition to difference, union, and intersection, you can also do exclusive or, subset, proper subset, superset, proper subsset """

def test_iterate_set():
    my_set = {'a', 'b', 'c'}
    str = ''
    for letter in my_set:
        str += letter
    
    assert len(str) == 3
