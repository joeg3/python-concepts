""" It's a good practice to have a docstring at the top of modules """
""" This file, example_classes.py is actually a module, containing one or more classes """

class Person:
    """ You should also have docstrings describing each class
         An example of a Python class, class names should always be cammel-case
    """

    # The __init__() method automatically gets invoked when instantiating a class.
    # This is typically used to set the object to an initial state, and can optionally
    # have parameters like name shown here for setting instance variables.
    # The self parameter is required and must be the first one.
    def __init__(self, name, age):
        # Instance variables, unique for each instance.
        # Any variables prefixed with 'self' is available to every method in the class.
        # Variables like these, accessed through instances are called attributes
        self.name = name   # Set to value of argument passed in
        self.age = age
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
    def __init__(self, name, age, id, school):
        """ Initialize attributes of parent class """
        super().__init__(name, age)
        self.id_card = StudentIdCard(id, school) # Attribute not in parent class
    
    student_int = 321 # Class variable of Student class

    def return_class_var_sum(self):
        """ Sum class variables of this class and parent class """
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



