# The most commonly used data structure in Python is List. Python list is a
# container like an array that holds an ordered sequence of objects. The object can
# be anything from a string to a number or the data of any available type.
# A list can also be both homogenous as well as heterogeneous. It means we can store
# only integers or strings or both depending on the need. Next, every element rests
# at some position (i.e., index) in the list. The index can be used later to locate
# a particular item. The first index begins at zero, next is one, and so forth

# Creating a list we have two ways to do that

# 1. The square brackets [ ] represent the subscript operator in Python

# Empty List
L1 = []

# List of integers
L2 = [10, 20, 30]

# List of heterogenous data types
L3 = [1, "hello", 3.4]

# 2. Python includes a built-in list() method a.k.a constructor.

L4 = list([1,2,3,4])

# Using range() to Make a List of Numbers
range_list =  list(range(1, 6))
print(range_list)

# Nested List 
L5 = [1,2,3,["qaiser", "ali"],5,6,7,8,9,10]

# Check how many element in list 
print("Length of list: " ,len(L5))


# Accessing Element in list using index 
# Keep in mind index start from 0

print("Access Element Using Index", L5[3])

# Python has a special syntax for accessing the last element in a list. By asking for the item at index -1

print("Access Element Using Negative Index", L5[-1])

# Updating List Element 
L5[-1] = 4
print(L5)

# Removing Element from list

del L5[1]
print(L5)

# Removing an Element by Value
L5.remove(1)
print(L5)

# Removing an Element Using the pop() Method 
# The pop() method removes the last item in a list
L5.pop()
print(L5)

# Popping Element from any Position in a List
# You can use pop() to remove an item from any position in a list by including
# the index of the item you want to remove in parentheses.
L5.pop(1)
print(L5)

# List slicing
# Python comes with a magical slice operator which returns the part of a sequence.
# It operates on objects of different data types such as strings, tuples, and works
# the same on a Python list.

#The Python slicing operator syntax

# [start(optional):stop(optional):step(optional)]
# Keep in mind the stop index is not included it run upto stop - 1 index

L6 = [1,2,3,4,5,6,7,8,9]

# start from index 1 
print(L6[1:2])

# start from index 2 -> 4
print(L6[2:5:2])

# Slice list from the third index to second last index
print(L6[2:-1])

# Slice list from second to last 
print(L6[1:])

# Slice list from start to third index 
print(L6[:3])

# Reverse a list
# It creates a shallow copy of the Python list, which requires long enough space for
# holding the whole list.
# Here, you need a little pause and understand, why is the ‘-1’ after the second
# colon? It intends to increment the index every time by -1 and directs to traverse
# in the backward direction.

print(L6[::-1])

# Create a shallow copy

print(L6[::])

# Iterate Python List 
for element in L6:
    print(element)

# Iterate the python list and get the index

for index in range(len(L6)):
    print(L6[index])

for index, element in enumerate(L6):
    print(f"Index: {index} , Element: {element}")

# Sorting in List
# ascending 
L7 = [2,8,5,10,4]
L7.sort()
print(L7)

# descending 
L7.sort(reverse=True)
print(L7)

# sort the list and get new list by using sorted function in list
new_list = sorted(L7)
print(new_list)
# Find max and min list
max_element = max(L7)
min_element = min(L7)

print("Max Element in Array: ", max_element)
print("Min Element in Array: ", min_element)

# Reverse the order of list
L8 = [1,2,3,5,4]
L8.reverse()
print(L8)

# Sum the element in list 
sum_of_list = sum(L8)
print(sum_of_list)

# Add to list 
L9 = [1,2,3]
L10 = ['a','b','c']
print(L9+L10)

my_extended_list = L9 + L10
print(my_extended_list)

# Python List Comprehension, 
# The most economical way (in terms of code) to create a list in Python. List
# Comprehension is also the fastest method to traverse a list, apply some condition,
# and return a new list with selected elements.

# Example 1
squares = [value**2 for value in range(1, 11)]
print(squares)

# Example 2

string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print(numbers)

# Example 3

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)

# Check out below blogs for more detail and examples on List Comprehension
# https://realpython.com/list-comprehension-python/
# https://www.programiz.com/python-programming/list-comprehension