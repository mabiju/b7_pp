a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print("The perimeter of the triangle is:", perimeter)
else:
    print("Invalid triangle. Perimeter cannot be calculated.")
