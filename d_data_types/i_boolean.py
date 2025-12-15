# Boolean data type in Python
my_bool_true = True
my_bool_false = False
print("Boolean True:", my_bool_true)
print("Boolean False:", my_bool_false)
# Logical operations
and_result = my_bool_true and my_bool_false
or_result = my_bool_true or my_bool_false
not_result = not my_bool_true
print("AND operation (True and False):", and_result)
print("OR operation (True or False):", or_result)
print("NOT operation (not True):", not_result)
# Boolean in conditional statements
if my_bool_true:
    print("The condition is True")
else:
    print("The condition is False")
if my_bool_false:
    print("The condition is True")
else:
    print("The condition is False")
# Boolean conversion
int_to_bool = bool(1)  # Non-zero integers are True
zero_to_bool = bool(0)  # Zero is False
empty_str_to_bool = bool("")  # Empty string is False
non_empty_str_to_bool = bool("Hello")  # Non-empty string is True
print("Integer 1 to Boolean:", int_to_bool)
print("Integer 0 to Boolean:", zero_to_bool)
print("Empty string to Boolean:", empty_str_to_bool)
print("Non-empty string to Boolean:", non_empty_str_to_bool)
# Note: Booleans are immutable, so operations like append, remove, and clear are
# not applicable.