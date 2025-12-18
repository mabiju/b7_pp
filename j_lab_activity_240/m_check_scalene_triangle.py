a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a != b and b != c and a != c:
    print("The triangle is scalene.")
else:
    print("The triangle is not scalene.")
