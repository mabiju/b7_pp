# Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Calculations
sum_ab = a + b
difference_ab = a - b
product_bc = b * c

# Output results
print("Sum of first two numbers:", sum_ab)
print("Difference (first - second):", difference_ab)
print("Product of second and third:", product_bc)

# Comparison
print("Is sum equal to product?", sum_ab == product_bc)
