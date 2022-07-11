# A dictionary is an unordered set of key/value pairs
# Entire dictionary is enclosed in curly braces
# Insertion order is not maintained with a dictionary

empty = {} # This is initialized as an empty dictionary

person = { 'Name': 'Jim',
           'Gender': 'Male',
           'City': 'Madison',
           'Age': 33 }

def test_basic_dictionary():
    name = person['Name']
    assert name == 'Jim'

def test_add_key_value():
    person['State'] = 'WI'
    state = person['State']
    assert state == 'WI'

def test_check_key_existence():
    # You can't do an operation on an uninitialized value
    # person['Dependants'] += 1
    # person['Dependants'] would first need to be initialized:
    if 'Dependants' in person:
        person['Dependants'] += 1
    else:
        person['Dependants'] = 1
    assert person['Dependants'] == 1

    # A more succicnt way:
    if 'Dependants' not in person:
        person['Dependants'] = 1
    person['Dependants'] += 1

    # Preferred way by Python programmers
    person.setdefault('Dependants', 0) # This initializes to 0 if needed. If already has a value, does nothing.
    person['Dependants'] +=1


def test_increment_dictionary_value():
    person['Age'] += 1
    assert person['Age'] == 34

def test_loop_dictionary():
    # Ordering is random
    for key in person:
        print ('key:', key, 'value:', person[key])

    # Use built-in sorted function to loop by alphabetical ordering of keys
    for key in sorted(person):
        print ('key:', key, 'value:', person[key])

    # Preferred way, using items() so you have both key and value as loop variables
    for k, v in sorted(person.items()):
        print ('key:', k, 'value:', v)

def test_dictionary_of_dictionaries():
    person1 = { 'Name': 'Jim', 'Age': 33 }
    person2 = { 'Name': 'Kay', 'Age': 30 }
    people = { } # Empty Dictionary
    people['Jim'] = person1
    people['Kay'] = person2
    assert len(people) == 2
    assert people['Kay']['Age'] == 30