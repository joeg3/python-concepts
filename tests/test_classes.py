from src.example_classes import ExampleClass
from src.example_classes import ExampleClassChild
from src.example_classes import MyClassWithDefaultConstructor
from src.example_classes import Child

def test_attribute_references():
    # Like class level variables and methods in Java, called without an instance variable
    assert ExampleClass.my_num == 123

def test_instantiation():
    ec = ExampleClass('Joe')
    assert ec.name == 'Joe'

def test_call_method_of_instance():
    ec = ExampleClass('Joe')
    assert ec.return_variables() == 'Joe123'
    ec.add_city('Minneapolis')
    assert ec.cities == ['Minneapolis']

def test_child_class():
    obj = ExampleClassChild('Name from class child')
    assert obj.my_num + obj.child_num == 444 # Sum variables from child and parent classes
    assert obj.return_class_var_sum() == 444

def test_create_object_with_default_constructor():
    obj = MyClassWithDefaultConstructor()
    assert obj.magicNumber() == 7

def test_parent_variable_access():
    obj = Child()
    assert obj.c_num + obj.p_num == 444 # Sum variables from child and parent classes
    assert obj.return_class_var_sum() == 444