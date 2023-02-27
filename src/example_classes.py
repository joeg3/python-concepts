from dataclasses import dataclass

""" It's a good practice to have a docstring at the top of modules """
""" This file, example_classes.py is actually a module, containing one or more classes """

class Tree(): # Parens are optional unless you have a parameter
    """ Simplest possible class """
    pass

class Person:
    """ You should also have docstrings describing each class
         An example of a Python class, class names should always be cammel-case
    """

    # The __init__() method automatically gets invoked when instantiating a class.
    # This is typically used to set the object to an initial state, and can optionally
    # have parameters like name shown here for setting instance variables (this is the only way
    # to set object attributes at creation time).
    # The self parameter is required and must be the first one.
    def __init__(self, name, age, org):
        # Instance variables, unique for each instance.
        # Any variables prefixed with 'self' is available to every method in the class.
        # Variables like these, accessed through instances are called attributes
        self.name = name   # Set to value of argument passed in
        self.age = age
        self.org = "Employer: " + org
        self.cities = []   # Attribute for each instance, don't have to use passed in parameter

    # Class variables shared and the same for all instances (note is isn't prefixed with 'self')
    planet = 'Earth'
    person_int = 123 # Class variable of Person class

    # Instance methods
    def update_age(self, age):
        self.age = age
    def increment_age(self, years):
        self.age += years
    def get_stylized_name(self):
        return f"** {self.name} **"

    # Note here we return instance variable concatenated with class variable
    def return_variables(self):
        return self.name + str(Person.person_int) # self.person_int would also work, but would be misleading

    def add_city(self, city):
        self.cities.append(city)

class Student(Person):
    """ Child class must be after parent in the file """

    # Since parent doesn't use the default constructor, we have to call it
    def __init__(self, name, age, id, org):
        """ Initialize attributes of parent class """
        super().__init__(name, age, org)      # If we ommited __init__() here, the __init__() of the parent class would be called by default
        self.org = "School: " + org           # org is in parent class, but we initialize it specific to students here
        self.id_card = StudentIdCard(id, org) # Attribute not in parent class
    
    student_int = 321 # Class variable of Student class

    def return_class_var_sum(self):
        """ Sum class variables of this class and parent class, this method only in child class """
        return Student.student_int + Person.person_int

    def get_stylized_name(self):
        """ Override parent method """
        return f"|| {self.name} ||"

class StudentIdCard:
    def __init__(self, id, university):
        self.id = id
        self.university = university

    def getIdCard(self):
        return f"Id|{self.id}|University|{self.university}"


class MyClassWithDefaultConstructor:
    # If you don't specify a constructor, Python treats the class as if the following were present:
    # def __init__(self): # This is the default constructor that we don't have to specify
    
    def magicNumber(self):
        return 7

class ClassThatMakesAttributesPrivate():
    """ Users of class think the attribute is 'name', but internally we use 'hidden_name' """
    """ The decorators allow you to access the attribute without having to use getters/setters and still """
    """ encapsulates hidden_name. But if they know about hidden_name, they can still directly read/write it """
    def __init__(self, input_name, input_age):
        self.hidden_name = input_name
        self.__age = input_age
    
    @property # This allows you to access attribute 'name'
    def name(self):
        return self.hidden_name
    @name.setter # This allows you to set the attribute
    def name(self, input_name):
        self.hidden_name = input_name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, input_age):
        self.__age = input_age

class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    """ This behaves like an attribute even though it's doing a calculation. """
    @property
    def diameter(self):
        return 2 * self.radius

class Employee():
    """ Demonstrate how class and object attributes and methods work """

    # Class attributes, not preceeded with self, not in __init__() block
    state = 'MN'
    count = 0

    def __init__(self, name):
        self.name = name        # Attributes preceeded with 'self' are instance attributes
        Employee.count += 1     # Update class attribute (preceeded with class name)

    # Instance method with self as parameter
    def give_title(self, title):
        return f"{title} {self.name}"

    # For class methods, use @classmethod decorator and make first parameter 'cls' by python convention, which refers to the class itself
    @classmethod
    def total_count(cls):
        return cls.count   # Could have used Employee.count too

    # Static methods affect neither the class or object and is a way to add miscellaneous code.
    @staticmethod
    def copyright():
        return "Our copyright"

@dataclass
class Car:
    """
    Dataclasses are like classes except they have no methods, they just hold data
    Not limited to Python data types, can use your own classes too """
    name: str
    year: int
    miles: int = 0  # You can specify a default