

def test_exception_basics():
    # For Python, this is called a try-except block
    # If exception thrown, you get what's called a traceback
    # When experimenting with code and you get a traceback, look at last line to see the
    # type of exception that was raised so you know what to use in the except block you'll write.
    try:
        quotient = 1/0
        pass      # This line will not be reached if previous line throws an exception
    except ZeroDivisionError as e:  # Except clause can list more than one exception: except(ZeroDivisionError, RuntimeError)
        # If no exception in try block, this block is skipped
        # If try block throws something other than a ZeroDivisionError, then it's an unhandled exeption and execution stops
        print('You tried to divide by zero: ', e)
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
