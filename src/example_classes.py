# This file, example_classes.py is actually a module, containing one or more classes

class ExampleClass:
    """An example of a Python class"""

    # The __init__() method automatically gets invoked when instantiating a class
    # This is typically used to set the object to an initial state, and can optionally
    # have parameters like name shown here for setting instance variables
    def __init__(self, name):
        self.name = name # Name is an instance variable, unique value for each instance
        self.kids = []   # Initialize for each object instance to empty list

    # Class variable shared and the same for all instances
    my_num = 123

    def return_string(self):
        return 'Hi'

    def add_kid(self, kid):
        self.kids.append(kid)