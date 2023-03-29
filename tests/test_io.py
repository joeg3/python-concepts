import json
from datetime import datetime
from os import scandir
from pathlib import Path
from time import sleep
import pprint
import pytest

def test_print():
    print('Hi')

def test_pprint():
    person1 = { 'Name': 'Jim', 'Age': 33 }
    pprint.pprint(person1) # Use this to pretty print complex objects like a dictionary

@pytest.mark.skip('Running this will stop tests to prompt for input')
def test_get_input_from_terminal():
    word = input("Please enter a word: ") # Returns a string
    age = input("Enter your age: ")
    age = int(age) # Convert to int

# For the next two test cases, I wanted to close the file in the fixture after the test to ensure
# it gets closed even if something went wrong during the test case. Maybe there's a better way,
# but to get it to work, I mark parameterize with the file name so the fixture can be reused with
# any filename. The the test uses that fixture as an argument.
@pytest.mark.parametrize('open_close_file_path', ['text_files/read_from_file.txt'], indirect=True)
def test_read_file_line_at_a_time(open_close_file_path):
    file_lines = []
    line = open_close_file_path.readline()
    while line != '':
        file_lines.append(line)
        line = open_close_file_path.readline()
    assert len(file_lines) == 3

@pytest.mark.parametrize('open_close_file_path', ['text_files/read_from_file.txt'], indirect=True)
def test_read_file_in_single_operation(open_close_file_path):
    lines_list = open_close_file_path.readlines()
    for line in lines_list: # Could also have done the following and not needed lines_list : for line in open_close_file_path.readlines()
        print(line)
    assert len(lines_list) == 3

def test_read_open_close_file_in_single_operation():
    with open('text_files/read_from_file.txt', 'r') as reader: # Use 'r' for read
        content = reader.readlines()
        assert len(content) == 3 
    # No need to explicitly open or close the file

@pytest.mark.skip('Unfinished')
def test_write_open_close_file_in_single_operation():
    content = ['a', 'b', 'c']
    with open('text_files/read_from_file.txt', 'w') as writer: # Use 'w' for write
        for line in content:
            writer.write(line)
    # No need to explicitly open or close the file


### New file tests

# In Python, only text is written to or read from files. For numerical data convert to string before
# writing to file, or convert to numerical after reading form file

def test_file_exists(read_file_name):
    path = Path(read_file_name)
    assert path.exists()

################## Reading Files #######################
def test_read_file_to_string(read_file_name):
    path = Path(read_file_name)
    contents = path.read_text().rstrip() # rstrip() will strip any whitespace or new lines at end of file.
    assert contents == 'a\nb\nc'

def test_read_file_to_lines(read_file_name):
    path = Path(read_file_name)
    contents = path.read_text()   # Don't need rstrip(), splitlines() returns all lines with text
    lines = contents.splitlines()
    assert lines == ['a', 'b', 'c']

def test_read_file_specify_encoding(read_file_name):
    path = Path(read_file_name)
    contents = path.read_text(encoding='utf-8').rstrip() # Specify if file from system with different default encoding
    assert contents == 'a\nb\nc'

def test_read_file_with_try_except_block(read_file_name):
    path = Path(read_file_name)
    try:
        contents = path.read_text().rstrip()
    except FileNotFoundError:
        print(f"Sorry, file {path} doesn't exist.")
    else:
        assert contents == 'a\nb\nc'

def test_read_files_in_downloads_folder():
    now = datetime.today()
    sleep(10) # Manually create file in download folder so we have one after timestamp from previous line
    downloads_folder = str(Path.home() / "Downloads")
    dir_items = scandir(downloads_folder)
    for item in dir_items:
        if item.is_file():
            file_name = item.name
            last_modified = datetime.utcfromtimestamp(item.stat().st_mtime)
            if last_modified > now:
                print("New file >>>>>>>>>>>>", file_name, last_modified)
            else:
                print("Old file <<<<<<<<<<<<", file_name, last_modified)
            # you can filter here unwanted files older than X

################## Writing Files #######################
def test_write_string_to_file(write_file_name):
    path = Path(write_file_name)

    # Creates file if it doesn't exist, and closes it properly
    # If file exists, write_text() erases the file's contents before writing
    path.write_text("Hello")
    contents = path.read_text()
    assert contents == 'Hello'

################# JSON Files ##########################
def test_write_and_read_json_file(json_file_name):
    nums = [1,2,3,4,5,6]

    # Write json to file
    path = Path(json_file_name)
    json_text = json.dumps(nums) # Generates string of argument in JSON format
    path.write_text(json_text)

    # Read json from file
    contents = path.read_text()
    nums_from_file = json.loads(contents)
    assert nums == nums_from_file
