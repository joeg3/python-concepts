from src.example_classes import ExampleClass

def test_attribute_references():
    # Like class level variables and methods in Java, called without an instance variable
    assert ExampleClass.my_num == 123

def test_instantiation():
    ec = ExampleClass('Jim')
    assert ec.name == 'Jim'

def test_call_method_of_instance():
    ec = ExampleClass('Ed')
    ec.add_kid('Dave')
    assert ec.kids == ['Dave']