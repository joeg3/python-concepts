import copy # For copy.deepcopy()

# - Lists are ordered mutable collection of objects
# - Lists are like arrays, can hold any type of data
# - You don't need to declare list size or type
# - A list can hold different types of objects
# - If you need to ensure unique values, use a set
# - Printing variable my_list which is ['a','b','c'], would write ['a','b','c'] to the terminal
# - List methods change the list they operate on, using brackets usually does not.





def test_create_list():
    empty_list = list() # Can also use Python's built in function to create an empty list
    empty_list = []     # Or just brackets
    assert len(empty_list) == 0

    nums = [ 1, 2, 3] # Literal lists are created with literal values
    chars = ['a', 'b']
    list_of_lists = [nums, chars]
    assert len(list_of_lists) == 2

    another = [[1,2,3],['a','b','c']]
    assert len(another) == 2

    different_types = [3, 'hi', 4.4] # A list can have different types
    evens = [ 0, 2,
          4, 6 ] # Can use multilple lines for readability

    list_from_iterable = list('hello') # You can also create a list from other iterable data types (string, tuple, set)
    assert len(list_from_iterable) == 5

def test_if_in_list():
    nums = [1,2]
    assert 2 in nums
    assert 4 not in nums

def test_check_non_empty_list():
    nums = [ 1, 2, 3]
    assert nums           # Python way
    assert len(nums) != 0 # Another way
    if nums: # Common way to check if empty
        pass

def test_check_empty_list():
    chars = []
    assert not chars       # Python way
    assert len(chars) == 0 # Another way

def test_fill_list_with_range():
    a = list(range(5))
    assert a == [0,1,2,3,4]

    a = list(range(5, 10))
    assert a == [5,6,7,8,9]

    evens = list(range(0, 11, 2))
    assert evens == [0,2,4,6,8,10]

    a = list(range(10, 0, -2))
    assert a == [10,8,6,4,2]

def test_length_of_list():
    assert len([1,2,3,4]) == 4

def test_min_max_sum_of_list():
    nums = [1,2,3,4]
    assert min(nums) == 1
    assert max(nums) == 4
    assert sum(nums) == 10

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

def test_find_index_by_value():
    letters = ['a','b','c','b','a']
    index = letters.index('b')    # Returns only first occurrence if multiple entries of same value
    assert index == 1

def test_get_count_of_occurrences():
    letters = ['a','b','c','b','a']
    count = letters.count('b')
    assert count == 2

def test_remove_by_position():
    letters = ['a','b','c','d','e']
    letter = letters.pop()    # No arg returns last item
    assert letter == 'e'
    assert letters == ['a', 'b','c','d']
    letter = letters.pop(0)    # Can pass index position
    assert letter == 'a'
    assert letters == ['b','c','d']
    del letters[1]             # del also removes by index, but doesn't return removed vaalue like pop() does
    assert letters == ['b','d']

def test_delete_all_items_with_clear():
    letters = ['a','b','c','b','a']
    letters.clear()
    assert letters == []

def test_combine_two_lists():
    # Using extend(), if using append() with a list as a param, it add a list as last element
    letters = ['a','b','c']
    letters.extend(['x','y','z'])
    assert letters == ['a','b','c','x','y','z']

    # Using +
    letters += ['m','n']
    assert letters == ['a','b','c','x','y','z','m','n']

def test_change_list_by_index():
    nums = [1, 99, 3]
    nums[1] = 2
    assert nums == [1,2,3]

def test_change_list_by_slice():
    nums = [1, 99, -1, 4]
    nums[1:3] = [2, 3]
    assert nums == [1,2,3,4]
    nums[1:3] = []
    assert nums == [1,4]

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

def test_create_string_from_list():
    letters = ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'i', 'z', 'z', 'a']
    str = ''.join(letters) # You can use a delimiter, here we use empty string
    assert str == "I love pizza"

def test_copying_lists():
    orig_list = ['a','b']
    
    # Ways to copy list
    list1 = orig_list        # orig_list and list1 point to the same list in memory, modifying one will modify the other
    list2 = orig_list.copy() # orig_list and list2 point to different places in memory
    list3 = list(orig_list)  # orig_list and list3 point to different places in memory
    list4 = orig_list[:]     # orig_list and list4 point to different places in memory

    orig_list.append('c')
    list1.append('d')
    list2.append('e')
    list3.append('f')
    list4.append('g')

    assert orig_list == ['a','b','c','d']
    assert list1 == ['a','b','c','d']
    assert list2 == ['a','b','e']
    assert list3 == ['a','b','f']
    assert list4 == ['a','b','g']

def test_copy_with_deepcopy():
    # copy() works if all list values are immutable like ints and strings
    # If list element is mutable like another list it's really a memory reference
    l = [1,2,[4,5]]
    c = l.copy()
    dc = copy.deepcopy(l)

    l[2][0] = 7  # Change to l changes c
    c[2][1] = 8  # Change to c changes l
    dc[2][0] = 9 # dc is its own memory location

    assert l == [1,2,[7,8]]
    assert c == [1,2,[7,8]]
    assert dc == [1,2,[9,5]]


def test_select_with_bracket_notation():
    list1 = ['a','b','c','d']
    assert list1[0] == 'a' # Normal zero-based indexing
    assert list1[-1] == 'd' # Use negative numbers to count right to left starting at -1
    assert list1[-2] == 'c'
    assert "ad" == list1[0] + list1[-1] # Easy to select first or last element with index [0] or [-1]

def test_slice_list():
    list1 = ['a','b','c','d','e','f','g','h']
    # This uses a [start:stop:step] notation. Defaults: start = 0, stop = max index of list, step = 1
    assert list1[0:6:2] == ['a','c','e'] # Start at index 0, every 2nd letter, stopping at (but not including) index 6
    assert list1[2:] == ['c','d','e','f','g','h'] # Start at index 2, default step 1, default stop at end of list
    assert list1[::3] == ['a','d','g'] # Every 3rd letter
    assert list1[:3] == ['a','b','c'] # All letters up to (but not including) index 3
    assert list1[-2:] == ['g','h']    # Last two elements

def test_join_items_from_list():
    list1 = ['a','b','c','d','e','f','g', 'h']
    first3 = ''.join(list1[0:3])
    assert first3 == "abc"

def test_reverse_list():
    # Clever way to reverse a list
    list1 = ['a','b','c']
    backwards = list1[::-1] # Iterate backwards from last element
    assert "cba" == ''.join(backwards)

    # Using reverse() function
    list1.reverse()
    assert list1 == ['c','b','a']

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

def test_sorting_lists():
    # Permanently sort list
    list1 = ['b', 'a', 'd', 'c']
    list1.sort()                  # Permanently changes list
    assert list1 == ['a','b','c', 'd']
    list1.sort(reverse=True)
    assert list1 == ['d','c','b', 'a']

    # Maintain order of original list
    list1 = ['b', 'a', 'd', 'c']
    list2 = sorted(list1)
    assert list1 == ['b', 'a', 'd', 'c']
    assert list2 == ['a','b','c', 'd']

    # Reverse list order
    list1 = ['a','b','c', 'd']
    list1.reverse()              # Permanently changes list, does not return its value
    assert list1 == ['d', 'c', 'b', 'a']

def test_list_comprehension():
    # Regular way to create a list of squares
    squares = []
    for num in range(1,5):
        squares.append(num**2)
    assert squares == [1,4,9,16]

    # Same code using list comprehension
    squares = [num**2 for num in range(1,5)]
    assert squares == [1,4,9,16]



