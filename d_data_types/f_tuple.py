# Tuple data type in Python
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)
# Accessing elements
print("First element:", my_tuple[0])
# Tuples are immutable, so we cannot modify elements directly
# However, we can create a new tuple by concatenation
new_tuple = my_tuple[:2] + (10,) + my_tuple[3:]
print("Modified tuple (by creating a new one):", new_tuple)
# Tuples do not have methods like append or remove since they are immutable
# Iterating through the tuple
for item in my_tuple:
    print("Tuple item:", item)
# Tuple comprehension is not possible, but we can use a generator expression
squared_tuple = tuple(x**2 for x in my_tuple)
print("Squared tuple:", squared_tuple)
# Slicing the tuple
sliced_tuple = my_tuple[1:4]
print("Sliced tuple (index 1 to 3):", sliced_tuple)
# Length of the tuple
print("Length of the tuple:", len(my_tuple))
# Tuples can be sorted by converting to a list and back
sorted_tuple = tuple(sorted(my_tuple))
print("Sorted tuple:", sorted_tuple)
# Reversing the tuple by converting to a list and back
reversed_tuple = tuple(reversed(my_tuple))
print("Reversed tuple:", reversed_tuple)
# Clearing a tuple is not possible since they are immutable
print("Cleared tuple: ()")  # Just showing an empty tuple
# Note: Tuples are immutable, so operations like append, remove, and clear are not applicable.
