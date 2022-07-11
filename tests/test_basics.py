import pprint

def test_print():
    print('Hi')
    person1 = { 'Name': 'Jim', 'Age': 33 }
    pprint.pprint(person1) # Use this to pretty print complex objects
