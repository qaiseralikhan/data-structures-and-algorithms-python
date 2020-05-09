# Dictionaries are yet another kind of compound type. They are Python’s built-in mapping type. They map keys, which can be any immutable type, to values, which can be any type (heterogeneous), just like the elements of a list or tuple. In other languages, they are called associative arrays since they associate a key with a value.
# strings, lists, and tuples — are sequence types, which use integers as indices to access the values they contain within them.
# You also might wonder why we use dictionaries at all when the same concept of mapping a key to a value could be implemented using a list of tuples:
# The reason is dictionaries are very fast, implemented using a technique called hashing, which allows us to access a value very quickly. By contrast, the list of tuples implementation is slow. If we wanted to find a value associated with a key, we would have to iterate over every tuple, checking the 0th element. What if the key wasn’t even in the list? We would have to get to the end of it to find out.
# The dictionary is the first compound type that we’ve seen that is not a sequence, so we can’t index or slice a dictionary.

#Creation of dictionary
D1 = {1: "qaiser", "2": "ali"}
print(D1)

# Starting with an empty dictionary
D2 = {}
D2[1] = "qaiser"
D2[2] = "ali"
print(D2)

# Note: 1 and 2 is not index but it is key of value qaiser and ali

# Accesing and modification of value
D2[1] = D2[1].upper()
print(D2)

# Access All Keys
print(D2.keys())

# The keys method returns what Python 3 calls a view of its underlying keys. A view object has some similarities to the range object — it is a lazy promise, to deliver its elements when they’re needed by the rest of the program. We can iterate over the view, or turn the view into a list like this:

print(list(D2.keys()))

# The values method is similar; it returns a view object which can be turned into a list:

print(list(D2.values()))

# The items method also returns a view, which promises a list of tuples — one tuple for each key:value pair:

print(list(D2.items()))

# Get value by calling get function and pass the key
print(D2.get(1))

# Copy a dictionary 
copy_d = D2.copy()
print(copy_d)

# Append in dictionary
D2[3] = "Khan"
print(D2)

# Create a Python dictionary
sixMonths = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30}

# Delete a specific element
print(sixMonths.pop(6)) 
print(sixMonths)

# Remove a specific element
del(sixMonths[5]) 
print(sixMonths)

# Delete an random element
print(sixMonths.popitem())
print(sixMonths)

# Delete all elements from the dictionary
sixMonths.clear()
print(sixMonths)

# iteration on dictionary

for key, value in D2.items():
    print(f"key: {key} , Value: {value}")
    
# Dictionary Comprehension

weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
week_dist = {w:len(w) for w in weekdays}
print(week_dist)

#  in or not in operator on dictionary

print("fri" in weekdays)
print("qaiser" not in weekdays)


# sorting on dictionary
print(sorted(weekdays))
print(sorted(weekdays, reverse = True))