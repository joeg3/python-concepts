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
