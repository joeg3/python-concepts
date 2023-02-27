import copy

# A dictionary is an unordered set of key/value pairs
# Entire dictionary is enclosed in curly braces

def test_create_dictionary():
    empty = {}            # Initialize an empty dictionary
    empty_dict = dict()   # Can also use Python's built in function 

    # If using multiple lines, bue sure to indent values.
    # Good practice to keep comma after last entry.
    person = {
        'name': 'Jim',
        'gender': 'Male',
        'city': 'Madison',
        'age': 33,
        }
    
    # Using dict() allows you to not use curly braces and quotes on the keys
    person = dict(name='Jim', gender='Male', city='Madison', age=33)
    assert person == {'name': 'Jim', 'gender': 'Male', 'city': 'Madison', 'age': 33}

def test_create_dict_from_list():
    # This converts a lists of two-element list into a dict
    # This can also be done with a list of two-element tuples, a tuple of two-element lists, etc.
    list = [['a','b'], ['c','d'], ['e','f']]
    d = dict(list)
    assert d == {'a': 'b', 'c': 'd', 'e': 'f'}

def test_get_dict_length():
    letters = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert 3 == len(letters)

def test_get_all_keys():
    letters = {'a': 'b', 'c': 'd', 'e': 'f'}
    letters_dict_keys = letters.keys() # keys() returns dict_keys() which is iterable view of keys, use list() to get a list of keys
    keys_list = list(letters_dict_keys)
    assert keys_list == ['a', 'c', 'e']

def test_get_all_values():
    letters = {'a': 'b', 'c': 'd', 'e': 'f'}
    values_list = list(letters.values())
    assert values_list == ['b', 'd', 'f']

def test_get_all_key_value_pairs():
    letters = {'a': 'b', 'c': 'd', 'e': 'f'}
    key_value_list = list(letters.items())
    assert key_value_list == [('a','b'), ('c','d'), ('e','f')]

def test_access_value():
    person = {'name': 'Jim', 'gender': 'Male', 'city': 'Madison', 'age': 33}
    name = person['name']
    assert name == 'Jim'

def test_get_to_access_value_or_set_default():
    house = {'color': 'red', 'bedrooms': 3}
    assert 3 == house.get('bedrooms', 2)    # Value exists for 'bedrooms', return its value instead of default
    assert 1 == house.get('bathrooms', 1)   # Key of 'bathrooms' doesn't exist, return default value
    assert 'bathrooms' not in house         # Even though previous line returned a value for 'bathrooms', it doesn't create key/value
    assert 'red' == house.get('color')      # You don't have to specify a default with get()
    assert None == house.get('wine cellar') # If no default specified and key doesn't exist, get() returns None

def test_add_key_value():
    person = {'name': 'Jim', 'gender': 'Male', 'city': 'Madison', 'age': 33}
    person['state'] = 'WI'
    state = person['state']
    assert state == 'WI'

def test_remove_item_with_del():
    house = {'color': 'red', 'bedrooms': 3}
    assert house['bedrooms'] == 3
    del house['bedrooms'] # Specify key to remove key/value pair
    assert 'bedrooms' not in house

def test_remove_item_with_pop():
    house = {'color': 'red', 'bedrooms': 3}
    assert house['bedrooms'] == 3
    house.pop('bedrooms') # Specify key to remove key/value pair
    assert 'bedrooms' not in house

def test_remove_all_items_with_clear():
    house = {'color': 'red', 'bedrooms': 3}
    house.clear()
    assert house == {}

def test_modify_value():
    person = {'name': 'Jim', 'gender': 'Male', 'city': 'Madison', 'age': 33}
    person['age'] += 1
    person['name'] = 'James'
    assert person['age'] == 34
    assert person['name'] == 'James'

def test_check_key_existence():
    person = {'name': 'Jim', 'gender': 'Male', 'city': 'Madison', 'age': 33}
    # Accessing person['employer'] gives error if key doesn't exist
    # When using get(), if key doesn't exist, None is returned
    assert None == person.get('employer')

    # You can't do an operation on an uninitialized value
    # person['Dependants'] += 1
    # person['Dependants'] would first need to be initialized:
    if 'dependants' in person.keys():
        person['dependants'] += 1
    else:
        person['dependants'] = 1
    assert person['dependants'] == 1

    # A more succicnt way:
    if 'dependants' not in person: # keys() is default, we omit it here
        person['dependants'] = 0
    person['dependants'] += 1

    # Preferred way by Python programmers
    person.setdefault('dependants', 0) # This initializes to 0 if needed. If already has a value, does nothing.
    person['dependants'] += 1

def test_loop_through_keys():
    fav_teams = {'Joe': 'Packers', 'Nina': 'Bears', 'Isabel': 'Vikings', 'Matt': 'Packers', 'Andy': 'Bears'}
    
    # Items returned in order inserted
    for name in fav_teams: # Default is to return keys
        print(f"{name}'s favorite team: {fav_teams[name]}")

    for name in fav_teams.keys(): # We explicitly return keys
        print(f"{name}'s favorite team: {fav_teams[name]}")

    # Use built-in sorted function to loop by alphabetical ordering of keys
    for name in sorted(fav_teams.keys()):
        print(f"{name}'s favorite team: {fav_teams[name]}")

def test_loop_through_values():
    fav_teams = {'Joe': 'Packers', 'Nina': 'Bears', 'Isabel': 'Vikings', 'Matt': 'Packers', 'Andy': 'Bears'}

    for team in fav_teams.values():
        print(f"{team} are a favorite team")

    # Use a set to not have duplicates
    for team in set(fav_teams.values()):
        print(f"{team} are a favorite team")

def test_loop_through_key_and_values():
    fav_teams = {'Joe': 'Packers', 'Nina': 'Bears', 'Isabel': 'Vikings'}

    for name, team in fav_teams.items():
        print(f"Name: {name}, Team: {team}")

def test_list_of_dictionaries():
    # Make 20 residents
    residents = []
    for age in range(20):
        person =  {'city': 'Wausau', 'age': age}
        residents.append(person)
    
    # Display first 4
    for person in residents[:4]:
        print(person)
    
    assert len(residents) == 20

def test_list_in_dictionary():
    # One key has a list as a value
    parent = {
        'city': 'Los Angeles',
        'age' : 33,
        'kids': ['grace', 'ann', 'lenny'],
    }

    # Each key has a list for its value
    parents_and_kids = {
        'fred': ['tim', 'jim'],
        'lisa': ['dan', 'joan']
    }

def test_dictionary_in_dictionary():
    members = {
        'Jim': {'city': 'Wausau', 'age': 33},
        'Mike': {'city': 'Weston', 'age': 30},
    }
    assert len(members) == 2
    assert members['Mike']['age'] == 30

    for member_name, info in members.items():
        print(f"\nMember name: {member_name}")
        city = info['city']
        age = info['age']
        print(f"\tCity: {city}, age: {age}")

def test_copy_dictionaries():
    # Using assignment
    d1 = {'a': 'b', 'c': 'd'}
    d2 = d1     # Results in d1 and d2 pointing to same dict in memory
    d1['c'] = 'z'
    assert d2 == {'a': 'b', 'c': 'z'}

    # Using copy(), works for immutable values like these
    c1 = {'a': 'b', 'c': 'd'}
    c2 = c1.copy()   # c1 and c2 point to different locations in memory
    c1['c'] = 'x'
    assert c2 == {'a': 'b', 'c': 'd'}

    # Using deepcopy(), works for mutable values
    b1 = {'a': 'b', 'c': ['m','n']}
    b2 = copy.deepcopy(b1)
    b1['c'][1] = 'o'
    assert b1 == {'a': 'b', 'c': ['m','o']}
    assert b2 == {'a': 'b', 'c': ['m','n']}

def test_combine_dictionaries():
    # Using {**a, **b}
    # For duplicate keys, keeps only second one. This is a shallow copy. See deepcopy() if you need full copies
    d1 = {'a': 'b', 'c': 'd'}
    d2 = {'c': 'g', 'e': 'f'}
    d1_d2 = {**d1, **d2}
    assert d1_d2 == {'a': 'b', 'c': 'g', 'e': 'f'}

    # Using update()
    d1.update(d2) # update() doesn't create new dict, it updates
    assert d1 == {'a': 'b', 'c': 'g', 'e': 'f'}

def test_create_dict_from_lists():
    mon_nums = ['1','2','3']
    mon_names = ['Jan','Feb','Mar']

    months = dict(zip(mon_nums, mon_names))
    assert months == {'1': 'Jan', '2': 'Feb', '3': 'Mar'}