# Dictionary data type in Python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)
# Accessing elements
print("Value for key 'a':", my_dict['a'])
# Modifying elements
my_dict['b'] = 10
print("Modified dictionary:", my_dict)
# Adding elements
my_dict['d'] = 4
print("Dictionary after adding an element:", my_dict)
# Removing elements
del my_dict['c']
print("Dictionary after removing an element:", my_dict)
# Iterating through the dictionary
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
# Dictionary comprehension
squared_dict = {k: v**2 for k, v in my_dict.items()}
print("Squared dictionary:", squared_dict)
# Length of the dictionary
print("Length of the dictionary:", len(my_dict))
# Sorting the dictionary by keys
sorted_dict_by_keys = dict(sorted(my_dict.items()))
print("Sorted dictionary by keys:", sorted_dict_by_keys)
# Sorting the dictionary by values
sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted dictionary by values:", sorted_dict_by_values)
# Clearing the dictionary
my_dict.clear()
print("Cleared dictionary:", my_dict)
# Note: Dictionaries are mutable, so operations like append, remove, and clear are applicable.
