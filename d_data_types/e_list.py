# List data type in Python
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
# Accessing elements
print("First element:", my_list[0])
# Modifying elements
my_list[2] = 10
print("Modified list:", my_list)
# Appending elements
my_list.append(6)
print("Appended list:", my_list)
# Removing elements
my_list.remove(4)
print("List after removal:", my_list)
# Iterating through the list
for item in my_list:
    print("List item:", item)
# List comprehension
squared_list = [x**2 for x in my_list]
print("Squared list:", squared_list)
# Slicing the list
sliced_list = my_list[1:4]
print("Sliced list (index 1 to 3):", sliced_list)
# Length of the list
print("Length of the list:", len(my_list))
# Sorting the list
my_list.sort()
print("Sorted list:", my_list)
# Reversing the list
my_list.reverse()
print("Reversed list:", my_list)
# Clearing the list
my_list.clear()
print("Cleared list:", my_list)