# This file, example_classes.py is actually a module, containing one or more classes

class ExampleClass:
    """An example of a Python class"""

    # The __init__() method automatically gets invoked when instantiating a class
    # This is typically used to set the object to an initial state, and can optionally
    # have parameters like name shown here for setting instance variables
    def __init__(self, name):
        self.name = name   # Name is an instance variable, unique value for each instance
        self.cities = []   # Initialize for each object instance to empty list

    # Class variable shared and the same for all instances (note is isn't prefixed with 'self')
    my_num = 123

    # Instance methods

    # Note here we return instance variable concatenated with class variable
    def return_variables(self):
        return self.name + str(ExampleClass.my_num) # self.my_num would also work, but would be misleading

    def add_city(self, city):
        self.cities.append(city)

class ExampleClassChild(ExampleClass):

    # Since parent doesn't use the default constructor, we have to call it
    def __init__(self, name):
        super().__init__(name)
        #ExampleClass.__init__(self, name)
    
    child_num = 321

    def return_class_var_sum(self):
        return ExampleClassChild.child_num + ExampleClass.my_num

class MyClassWithDefaultConstructor:
    # If you don't specify a constructor, Python treats the class as if the following were present:
    # def __init__(self): # This is the default constructor that we don't have to specify
    
    def magicNumber(self):
        return 7


class Parent:
    # Default constructor
    p_num = 123

class Child(Parent):
    def __init__(self):
        super().__init__()
        #Parent.__init__(self)

    c_num = 321

    def return_class_var_sum(self):
        return Child.c_num + Parent.p_num


