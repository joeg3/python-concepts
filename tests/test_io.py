import pprint
import pytest

def test_print():
    print('Hi')

def test_pprint():
    person1 = { 'Name': 'Jim', 'Age': 33 }
    pprint.pprint(person1) # Use this to pretty print complex objects like a dictionary

@pytest.mark.skip('Running this will stop execution to prompt for input')
def test_get_input_from_terminal():
    word = input("Please enter a word: ") # Returns a string
    age = input("Enter your age: ")
    age = int(age) # Convert to int

# For the next two test cases, I wanted to close the file in the fixture after the test to ensure
# it gets closed even if something went wrong during the test case. Maybe there's a better way,
# but to get it to work, I mark parameterize with the file name so the fixture can be reused with
# any filename. The the test uses that fixture as an argument.
@pytest.mark.parametrize('open_close_file_path', ['tests/test_read_file.txt'], indirect=True)
def test_read_file_line_at_a_time(open_close_file_path):
    line = open_close_file_path.readline()
    while line != '':
        print(line)
        line = open_close_file_path.readline()

@pytest.mark.parametrize('open_close_file_path', ['tests/test_read_file.txt'], indirect=True)
def test_read_file_in_single_operation(open_close_file_path):
    lines_list = open_close_file_path.readlines()
    for line in lines_list: # Could also have done the following and not needed lines_list : for line in open_close_file_path.readlines()
        print(line)
    assert len(lines_list) == 3

def test_read_open_close_file_in_single_operation():
    with open('tests/test_read_file.txt', 'r') as reader: # Use 'r' for read
        content = reader.readlines()
        assert len(content) == 3
    # No need to explicitly open or close the file

@pytest.mark.skip('Unfinished')
def test_write_open_close_file_in_single_operation():
    content = ['a', 'b', 'c']
    with open('tests/test_read_file.txt', 'w') as writer: # Use 'w' for write
        for line in content:
            writer.write(line)
    # No need to explicitly open or close the file
