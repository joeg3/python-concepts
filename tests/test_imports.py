# By convention, standard library imports should be first, followed
# by a blank line, then import your modules

# Five ways to import
from src import calc_module # Every function from calc_module is available here with syntax calc_module.function_name()
from src import calc_module as cm # Import module and give it an alias
from src.calc_module import right_triangle_area # Import specific function
from src.calc_module import right_triangle_area as rta # Import a specific function and give it an alias
from src.calc_module import * # Import all functions of module
# !!!!! The previous line, importing all functions of module isn't recommended because of the potential for name collisions.
# It's recommended to import the functions you'll use, or import the entire module and use dot notation.

# Note, some modules have submodules
from os import path   # Import the path submodule from the os module, can call path.abspath()

# Import individual classes
from src.example_classes import Person
from src.example_classes import Student
from src.example_classes import MyClassWithDefaultConstructor

# You can use aliases when importing classes
from src.example_classes import MyClassWithDefaultConstructor as dc

# You can also import multiple classes from same module on one line:
from src.example_classes import Person, Student, MyClassWithDefaultConstructor

# You can also import an entire module and access the classes through dot notation
# This may helps to eliminate naming conflicts
import src.example_classes as ec

# You can also import all classes from a module, but is not recommended because:
# 1. It helps to be able to see the classes imported and what the program uses
# 2. Can make name collisions more likely
from src.example_classes import *

def test_verify_imports():
    assert calc_module.right_triangle_area(3, 2) == 3 # Import module, use dot notation to use any function in module
    assert cm.right_triangle_area(3, 2) == 3          # Import module, give it an alias
    assert right_triangle_area(3, 2) == 3             # Import specific function
    assert rta(3, 2) == 3                             # Import specific function, give it an alias
    path.abspath('.')                                 # path is a submodule of os, so need dot notation to access its functions

def test_verify_class_imports():
    p = Person('Mary', 44, 'Itron')
    s = Student('Alice', 22, 1, 'UofM')
    d1 = dc()
    d2 = MyClassWithDefaultConstructor()
    ec.Person('Greg', 66, 'IBM')