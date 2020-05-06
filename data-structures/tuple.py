# Tuples are data structures that look a lot like lists. Unlike lists, tuples are 
# immutable (meaning that they cannot be modified once created). This restricts 
# their use because we cannot add, remove, or assign values; however, it gives us 
# an advantage in space and time complexities. A common tuple use is the swapping 
# of  numbers: a, b = b, a Here  is a tuple, and it assigns itself the values of.
# Another awesome use of tuples is as keys in a dictionary. In other words,
# tuples are hashable

# Create a tuple

T1 = (1,3)
print(T1)

T2 = (1, "Qaiser", "Ali", 2)
print(T2)

L1= [1,3,4]
T3 = tuple(L1)
print(T3)

# Nested Tuple
T4 = ((1,2,3),(4,5,6))

# Tuple 0 to 9
T5 = tuple(x for x in range(10))
print(T5)

# You need to place a comma after the first element to create a tuple of size "one"

T6 = (6,)
print(T6)

# Access Tuple Value
print(T2[1] + T2[2])

# Tuple Suppot indexing, reverse indexing and slicing just like list
# All these operation done in List.py check out list.py
# tuples are immutable, so it seems no way to modify them or delete item in tuple.
# Traversing is also same as tuple.
