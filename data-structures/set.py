# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

# However, a set itself is mutable. We can add or remove items from it.

# Creating a Set

S1 = { 1, 2, 3, 4, 5}
print(S1)

S2 = set([1,2,3,4,5])
print(S2)

S3 = {1,2,3, (4,5)}
print(S3)

# Add value into set
S1.add(7)
print(S1)

#Add multiple element
S1.update([10,11,12])
print(S1)


# dicard or remove function

S1.discard(1)
S1.remove(2)
print(S1)

# remove all the items from a set using the clear() method

S2.clear()
print(S2)

# we can remove and return an item using the pop() method

my_pop_elment = S1.pop()
print(my_pop_elment)

# mathematical set operations

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Union: ", A.union(B))
print("Intersection: ", A.intersection(B))
print("Difference: ", A.difference(B))
print("Symmetric Difference: ", A.symmetric_difference(B))

# Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.

# Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.
forzen_set =  {12,2,3,5}
print(forzen_set)