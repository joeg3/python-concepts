# A dictionary is an unordered set of key/value pairs
# Entire dictionary is enclosed in curly braces

empty = {} # This is initialized as an empty dictionary
empty_dict = dict()   # Can also use Python's built in function to create an empty dictionary

# If using multiple lines, bue sure to indent values.
# Good practice to keep comma after last entry.
person = {
    'name': 'Jim',
    'gender': 'Male',
    'city': 'Madison',
    'age': 33,
    }

def test_access_value():
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
    person['state'] = 'WI'
    state = person['state']
    assert state == 'WI'

def test_remove_key_value():
    house = {'color': 'red', 'bedrooms': 3}
    assert house['bedrooms'] == 3
    del house['bedrooms'] # Specify key to remove key/value pair
    assert 'bedrooms' not in house

def test_modify_value():
    person['age'] += 1
    person['name'] = 'James'
    assert person['age'] == 34
    assert person['name'] == 'James'

def test_check_key_existence():
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

def test_create_dict_from_lists():
    mon_nums = ['1','2','3']
    mon_names = ['Jan','Feb','Mar']

    months = dict(zip(mon_nums, mon_names))
    assert months == {'1': 'Jan', '2': 'Feb', '3': 'Mar'}