# There are three locations the interpreter searches when looking for a module:
# 1. Your current working directory
# 2. Your interpreter's site-packages locations. These are folders that contain any thire-party Python modules
#    you installed, including your own.
# 3. The standard library
# The interpreter looks in your current working directory first.

# Two ways to import. The first one, we would call os.getcwd(), the second one, we can just do getcwd().
# Note in the second one, os is not visible, just getcwd().
# The first way is sometimes better because if there was another module where we imported getcwd, Python wouldn't 
# know from which module we want to invoke getcwd().
import os             # Import os module, would have to call os.getcwd() or os.path.abspath()
from os import getcwd # Import getcwd() function from os module, can call getcwd()
from os import path   # Import path submodule from os module, can call path.abspath()

import datetime
import random
import sys
import time

# Module terminology:
# from <standard library module> import <submodule>
# import <standard library module>

def test_working_dir():
    cwd = getcwd()
    print(cwd)
    # Or using other way to import
    cwd = os.getcwd()
    

def test_python_level():
    assert sys.version_info[0] >= 3

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
    time.sleep(2) # Sleep for 2 seconds

def test_random_int():
    x = random.randint(1, 10) # Returns random integer from the inclusive range
    assert x >= 1
    assert x <= 10