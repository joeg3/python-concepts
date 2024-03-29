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

def test_logical_operators():
    a = 3
    if 2 < a and a < 5:
        assert True

    if 2 < a < 5: # Do this if 'and-ing' multiple comparisions with same variable
        assert True

    if 2 < a and not a > 5:
        assert True

def test_use_in_for_multiple_comparisons():
    """ Instead of using a bunch of logical operators, do comparisions with in """
    """ You can see if it's 'in' a string, list, set, tuple, or dictionary """
    vowels = 'aeiou'
    if 'i' in vowels:
        assert True

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

def test_for_loop_with_list():
    x = -1
    for i in [1, 2, 3]:
        x = i
    assert x == 3

def test_loop_list_range():
    x = -1
    nums = [1,2,3,4,5]
    for i in nums[:3]: # Loop only through first three items in list
        x = i
    assert x == 3

def test_for_with_string():
    c = '!'
    for i in "fred":
        c = i
    assert c == 'd'

def test_for_with_range_default():
    """ You can use range() in a for loop to create a stream of a large data set without having to create it """
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

# Use a while loop to mofify a list, dictionary, etc. If you used a for loop, it could
# get messed up from the list length changing while iterating through it.
def test_use_while_to_modify_list():
    nums = [1,3,6,3,5,2,3,7]
    while 3 in nums:
        nums.remove(3)

    assert len(nums) == 5 # Removed all 3's

def test_iterate_multiple_lists_with_zip():
    l1 = ['a','b','c']
    l2 = ['1','2','3']
    l3 = ['x','y','z']
    str = ''

    for c1, c2, c3 in zip(l1, l2, l3):
        str += f"{c1}{c2}{c3}"

    assert str == 'a1xb2yc3z'

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

def test_break_with_else():
    # Use break with else structure if you wanat to run code if break never called
    sum = 0
    for i in [1,2,3,4]:
        sum += i
        if sum >= 1000000:
            break
    else: # Break not called
        sum = 777
    assert sum == 777

    # Break with else is handy to run code if you never enter the loop
    i = 0
    nums = []
    for num in nums:
        i = num
        break
    else:
        i = 7
    assert i == 7

def test_continue():
    sum = 0
    x = 0
    while x < 5:
        x += 1
        if x == 3:
            continue
        sum += x # This is not reached when x is 3
    assert sum == 12

# def match_example(status):
#     match status:
#         case 1:
#             return "1 has matched"
#         case 2:
#             return "2 has matched"
#         case _:
#             return "Default, anything other than 1 or 2 will match here"