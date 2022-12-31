from src.example_classes import Person
from src.example_classes import Student
from src.example_classes import MyClassWithDefaultConstructor

def test_attribute_references():
    # Like class level variables and methods in Java, called without an instance variable
    assert Person.person_int == 123

def test_instantiation():
    joe = Person('Joe', 33)
    assert joe.name == 'Joe'

def test_stylized_name():
    tim = Person('Tim', 33)
    assert tim.get_stylized_name() == "** Tim **"

def test_modify_attribute_values():
    steve = Person('Steve', 55)

    # Three approaches to modify an instance's attribute value:
    steve.age = 44 # Directly through the instance
    assert steve.age == 44
    
    steve.update_age(46) # Change value through a method
    assert steve.age == 46

    steve.increment_age(4) # Increment through a method
    assert steve.age == 50


def test_call_method_of_instance():
    person = Person('Joe', 33)
    assert person.return_variables() == 'Joe123'
    person.add_city('Minneapolis')
    assert person.cities == ['Minneapolis']

def test_child_class():
    student = Student('Doug', 22, 8, 'UofM')
    assert student.person_int + student.student_int == 444 # Sum class variables from child and parent classes
    assert student.return_class_var_sum() == 444

def test_child_class_override_parent_method():
    obj = Student('Doug', 22, 8, 'UofM')
    assert obj.get_stylized_name() == "|| Doug ||"

def test_class_with_class_as_attribute():
    doug = Student('Doug', 22, 8, 'UofM')
    assert doug.id_card.getIdCard() == "Id|8|University|UofM"

def test_create_object_with_default_constructor():
    obj = MyClassWithDefaultConstructor()
    assert obj.magicNumber() == 7
