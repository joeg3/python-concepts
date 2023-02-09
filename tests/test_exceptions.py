from src.my_exception import WrongTeamException

def test_exception_basic():
    """ This is the most basic try/except. Since we have no arguments to the except, the block 
        will catch any exception type. """
    try:
        quotient = 1/0
    except:
        # If no exception in try block, this block is skipped
        print('You tried to divide by zero')

def test_exception_novice():
    """ Here we specify an exception type to catch. 
         If try block throws something other than a ZeroDivisionError, then it's an unhandled exeption and execution stops"""
    try:
        quotient = 1/0
    except ZeroDivisionError as e:
        print('You tried to divide by zero: ', e)
        

def test_exception_advanced():
    """ For Python, this is called a try-except block
        If exception thrown, you get what's called a traceback
        When experimenting with code and you get a traceback, look at last line to see the
        type of exception that was raised so you know what to use in the except block you'll write. """
    try:
        quotient = 1/0
        pass      # This line will not be reached if previous line throws an exception
    except ZeroDivisionError as e:  # Except clause can list more than one exception: except(ZeroDivisionError, RuntimeError)
        print('You tried to divide by zero: ', e)
    except Exception as o:
        # You can specify different types of exception to catch.
        print('Some other exception occurred: ', o)
    else:
        # Optional else, No exception raised if we got here, useful to isolate code that can generate exception to try block and put the rest here
        print(quotient)
    finally:
        pass # The optional finally clause runs whether or not the try statement produces an exception

def test_raise_exception():
    try:
        # Something isn't right, so purposely raise an exception
        raise Exception
    except Exception:
        print('You raised an exception')

def test_use_my_exception():
    try:
        team = 'Bears'
        if team != 'Packers':
            raise WrongTeamException(f"You submitted the wrong team: {team}")
    except WrongTeamException as w:
        print('WrongTeamException: ', w)