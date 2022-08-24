from re import X


nums = [ 1, 2, 3]

# A colon introduces an indented block of code (python calls blocks "suites")
def test_if_else():
    if not nums:    # Python way to check if list is empty
        assert len(nums) == 0
    else:
        assert len(nums) > 0

def test_if_elif_else():
    if nums[0] > 0:
        assert nums[0] > 0
    elif nums[0] < 0:
        assert nums[0] < 0
    else:
        assert nums[0] == 0

def test_walrus_operator():
    # New in Python 3.8

    # Old way:
    a = 4
    b = 2 * 9
    diff = a - b
    if diff < 0:
        print('diff < zero: ', diff)

    # With walrus operator, make assignement in if statement
    if (diff := a - b) < 0:
        print('diff < zero: ', diff)

def test_for_with_list():
    x = -1
    for i in [1, 2, 3]:
        x = i
    assert x == 3

def test_for_with_string():
    c = '!'
    for i in "fred":
        c = i
    assert c == 'd'

def test_for_with_range_default():
    x = 0
    for i in range(5): # Specify to run loop 5 times, by default starting at zero and incrmenting by one each iteration
        x += i
    assert x == 10

def test_for_with_range_specified():
    x = 0
    for i in range(10, 2, -2): # Specify start of 10, end of 2, and optional (default is 1) step of -2 to decrement 10, 8, 6, ...
        x += i                 # Note it doesn't include the stop value (in this case 2), but up to it
    assert x == 28

def test_while_loop():
    sum = 0
    x = 0
    while x < 5:
        sum += x
        x += 1
    assert sum == 10

def test_break():
    sum = 0
    x = 0
    while x < 5:
        sum += x
        if sum >= 3:
            break
        x += 1
    assert sum == 3
    assert x == 2

# The 'pass' statement is a no-op, used where Python requires a statement, or in creating minimal classes
def test_pass():
    pass # Remember to implement later

def match_example(status):
    match status:
        case 1:
            return "1 has matched"
        case 2:
            return "2 has matched"
        case _:
            return "Default, anything other than 1 or 2 will match here"