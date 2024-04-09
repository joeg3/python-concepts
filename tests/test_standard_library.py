import datetime
from importlib.metadata import version
import os
from random import choice
from random import randint
import sys
import time

def test_working_dir():
    cwd = os.getcwd()
    
def test_python_level():
    assert sys.version_info[0] >= 3

def test_get_python_version():
    # Constructs something like; 3.10.9.final
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}.{sys.version_info.releaselevel}"
    assert version[0] == '3'

def test_get_version_of_package():
    pytest_version = version('pytest') # Returns something like: 8.1.1
    assert pytest_version[0] == '8'

def test_environment_variables():
    os.environ # All the system's environment variables
    os.getenv('HOME') # Just the HOME environment variable

def test_datetime_current_minute():
    minute = datetime.datetime.now().minute
    assert minute < 60

def test_datetime():
    datetime.date.today() # This returns a weird format: datetime.date(2002, 6, 30)

    # These return an integer
    datetime.date.today().day
    datetime.date.today().month
    datetime.date.today().year

    datetime.date.isoformat(datetime.date.today())

    time.strftime("%H:%M") # Return something like: 17:33
    time.strftime("%A:%p") # Return something like: Tuesday PM

def test_sleep():
    time.sleep(1) # Sleep for one second

def test_random_choice():
    # choice() works on both lists and tuples
    letters = ['a','b','c','d']
    random_letter = choice(letters)
    assert random_letter in letters

def test_random_int():
    x = randint(1, 10) # Returns random integer from the inclusive range
    assert x >= 1
    assert x <= 10