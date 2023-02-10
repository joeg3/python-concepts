from src.example_classes import Circle
from src.example_classes import Person
from src.example_classes import Student
from src.example_classes import Tree
from src.example_classes import ClassThatMakesAttributesPrivate
from src.example_classes import MyClassWithDefaultConstructor
from src.example_classes import Employee
from src.example_classes import Car

def test_instantiation():
    joe = Person('Joe', 33, 'IBM')
    assert joe.name == 'Joe'

def test_add_attributes_to_object():
    """ You can add attributes to an object even if they are not defined in the class """
    a_tree = Tree()
    a_tree.name = 'maple'
    assert a_tree.name == 'maple'

def test_stylized_name():
    tim = Person('Tim', 33, 'Hughes')
    assert tim.get_stylized_name() == "** Tim **"

def test_modify_attribute_values():
    steve = Person('Steve', 55, 'TRW')

    # Three approaches to modify an instance's attribute value:
    steve.age = 44 # Directly through the instance
    assert steve.age == 44
    
    steve.update_age(46) # Change value through a method
    assert steve.age == 46

    steve.increment_age(4) # Increment through a method
    assert steve.age == 50


def test_call_method_of_instance():
    person = Person('Joe', 33, 'IBM')
    assert person.return_variables() == 'Joe123'
    person.add_city('Minneapolis')
    assert person.cities == ['Minneapolis']

def test_child_class():
    student = Student('Doug', 22, 8, 'UofM')
    assert student.person_int + student.student_int == 444 # Sum class variables from child and parent classes
    assert student.return_class_var_sum() == 444

def test_check_if_class_is_subclass():
    assert issubclass(Student, Person)  # issubclass() is a built-in Python function

def test_child_class_override_parent_method():
    obj = Student('Doug', 22, 8, 'UofM')
    assert obj.get_stylized_name() == "|| Doug ||"

def test_class_with_class_as_attribute():
    doug = Student('Doug', 22, 8, 'UofM')
    assert doug.id_card.getIdCard() == "Id|8|University|UofM"

def test_create_object_with_default_constructor():
    obj = MyClassWithDefaultConstructor()
    assert obj.magicNumber() == 7

def test_class_private_attributes():
    """ This class shows two different approaches to encapsulating its attributes """
    obj = ClassThatMakesAttributesPrivate('Tim', 33)
    assert obj.name == 'Tim'
    obj.name = 'Jim'
    assert obj.name == 'Jim'
    assert obj.age == 33
    obj.age = 34
    assert obj.age == 34

def test_properties_for_computed_values():
    circle = Circle(8)
    assert circle.radius == 8
    assert circle.diameter == 16 # Refer to diameter like an attribute even though it's computing a value
    circle.radius = 4
    assert circle.diameter == 8  # It recalculates if radius changes
    # circle.diameter = 7        # If you don't specify a setter property for an attribute, you can't set from outside

def test_class_and_object_attributes():
    # Like class level variables and methods in Java, called without an instance variable
    assert Employee.state == 'MN'          # Access class attribute with class name
    a = Employee('Ted')
    assert a.state == 'MN'          # Access class attribute with object
    a.state = 'CA'                  # Ojbect changes class attribute
    assert a.state == 'CA'
    assert Employee.state == 'MN'          # Changing class attribute for object doesn't change it for class
    Employee.state == 'CO'
    assert a.state == 'CA'          # Changing class attribute with class doesn't change it for object

def test_class_and_object_methods():
    a1 = Employee('Ted')
    a2 = Employee('Ann')
    a3 = Employee('John')

    assert "Dr. John" == a3.give_title('Dr.')        # Instance method
    Employee.total_count()                           # Class method
    assert Employee.copyright() == "Our copyright"   # Static method

def test_dataclass():
    truck = Car("Toyota", 1987, 54000)  # Provide arguments in order they are specified in class
    car = Car(year=2021, name="Ford")   # Or use named arguments in any order (here we go with default for miles)
    assert truck.name == "Toyota"
    assert car.year == 2021
    assert car.miles == 0