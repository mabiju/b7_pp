a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Find the largest side
if a > b and a > c:
    hypotenuse = a
    x, y = b, c
elif b > a and b > c:
    hypotenuse = b
    x, y = a, c
else:
    hypotenuse = c
    x, y = a, b

if hypotenuse**2 == x**2 + y**2:
    print("The triangle is right-angled.")
else:
    print("The triangle is not right-angled.")
