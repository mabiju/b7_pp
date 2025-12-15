# Set data type in Python
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)
# Accessing elements (sets are unordered, so we cannot access by index)
print("Set contains 3:", 3 in my_set)
# Modifying elements (adding elements)
my_set.add(6)
print("Set after adding an element:", my_set)
# Removing elements
my_set.remove(4)
print("Set after removing an element:", my_set)
# Iterating through the set
for item in my_set:
    print("Set item:", item)
# Set comprehension
squared_set = {x**2 for x in my_set}
print("Squared set:", squared_set)
# Length of the set
print("Length of the set:", len(my_set))
# Sorting the set (by converting to a list)
sorted_set = sorted(my_set)
print("Sorted set (as list):", sorted_set)
# Reversing the set (by converting to a list)
reversed_set = list(reversed(my_set))
print("Reversed set (as list):", reversed_set)
# Clearing the set
my_set.clear()
print("Cleared set:", my_set)
# Note: Sets are mutable, so operations like add, remove, and clear are applicable.
