
# - Lists are ordered mutable collection of objects
# - Lists are like arrays, can hold any type of data
# - You don't need to declare list size or type
# - A list can hold different types of objects
# - List methods change the list they operate on, using brackets usually does not.


# These are called literal lists where they are created with literal values
nums = [ 1, 2, 3]
chars = [ ]   # Empty list
empty_list = list()   # Can also use Python's built in function to create an empty list

list_of_lists = [nums, chars]
another = [[1,2,3],['a','b','c']]

different_types = [3, 'hi', 4.4] # A list can have different types

# A list can span multiple lines for readability
evens = [ 0, 2,
          4, 6 ]

def test_if_in_list():
    assert 2 in nums

def test_check_non_empty_list():
    assert nums           # Python way
    assert len(nums) != 0 # Another way

def test_check_empty_list():
    assert not chars       # Python way
    assert len(chars) == 0 # Another way

def test_fill_list_with_range():
    a = list(range(5))
    assert a == [0,1,2,3,4]

    a = list(range(5, 10))
    assert a == [5,6,7,8,9]

    a = list(range(0, 10, 2))
    assert a == [0,2,4,6,8]

    a = list(range(10, 0, -2))
    assert a == [10,8,6,4,2]

def test_length_of_list():
    assert len([1,2,3,4]) == 4

def test_if_in_list():
    nums = [1,2]
    assert 2 in nums
    assert 4 not in nums

def test_using_in_operator():
    word = "minneapolis"
    vowels = ['a','e','i','o','u']
    total_found = []
    unique_found = []
    for letter in word:
        if letter in vowels:
            total_found.append(letter)
            if letter not in unique_found:
                unique_found.append(letter)
    assert len(total_found) == 5
    assert len(unique_found) == 4

def test_remove_by_value():
    letters = ['a','b','c','b','a']
    letters.remove('b')    # Remove by value, not index, but only first occurrence
    assert letters == ['a','c','b','a']

def test_remove_by_position():
    letters = ['a','b','c','b','a']
    letter = letters.pop()    # No arg returns last item
    assert letter == 'a'
    assert letters == ['a', 'b','c','b']
    letter = letters.pop(0)    # Can pass index position
    assert letter == 'a'
    assert letters == ['b','c','b']
    del letters[1]             # Use del() to also remove by index
    assert letters == ['b','b']


def test_combine_two_lists():
    letters = ['a','b','c']
    letters.extend(['x','y','z'])
    assert letters == ['a','b','c','x','y','z']

def test_change_list_value():
    nums = [1, 99, 3]
    nums[1] = 2
    assert nums == [1,2,3]

def test_append_to_list():
    nums = [1,2]
    nums.append(3) # Adds to last postion
    assert nums == [1,2,3]

def test_insert_into_list():
    letters = ['a','b','d']
    letters.insert(2,'c') # First arg is index position to insert *before*, so use append() to add to last position
    assert letters == ['a','b','c','d']

def test_create_list_from_string():
    s = "I love pizza"
    str_list = list(s)
    assert 12 == len(str_list) # str_list is ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'i', 'z', 'z', 'a']

def test_copying_lists():
    list1 = ['a','b']
    list2 = list1 # These now point to the same list in memory, modifying one will modify the other
    list1.append('c')
    assert list2 == ['a','b','c']
    list2 = list1.copy() # Now list1 and list2 point to different places in memory
    list2.append('d')
    assert list1 == ['a','b','c']
    assert list2 == ['a','b','c','d']

def test_select_with_bracket_notation():
    list1 = ['a','b','c','d']
    assert list1[0] == 'a' # Normal zero-based indexing
    assert list1[-1] == 'd' # Use negative numbers to count right to left starting at -1
    assert list1[-2] == 'c'
    assert "ad" == list1[0] + list1[-1] # Easy to select first or last element with index [0] or [-1]

def test_select_by_start_stop_step():
    list1 = ['a','b','c','d','e','f','g', 'h']
    # This uses a [start:stop:step] notation. Defaults: start = 0, stop = max index of list, step = 1
    assert list1[0:6:2] == ['a','c','e'] # Start at index 0, every 2nd letter, stopping at (but not including) index 6
    assert list1[2:] == ['c','d','e','f','g','h'] # Start at index 2, default step 1, default stop at end of list
    assert list1[::3] == ['a','d','g'] # Every 3rd letter
    assert list1[:3] == ['a','b','c'] # All letters up to (but not including) index 3

def test_join_items_from_list():
    list1 = ['a','b','c','d','e','f','g', 'h']
    first3 = ''.join(list1[0:3])
    assert first3 == "abc"

def test_reverse_list():
    # Clever way to reverse a list
    list1 = ['a','b','c']
    backwards = list1[::-1] # Iterate backwards from last element
    assert "cba" == ''.join(backwards)

def test_lists_and_for_loops():
    list1 = ['a','b','c']
    list2 = []
    for i in list1:
        i = '_' + i
        list2.append(i)
    assert list2 == ['_a','_b','_c']

def test_slice_list_for_loop():
    list1 = ['a','b','c', 'd', 'e']
    list2 = []
    for i in list1[:3]: # Just iterate over first three elements
        i = '_' + i
        list2.append(i)
    assert list2 == ['_a','_b','_c']