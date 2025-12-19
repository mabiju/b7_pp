# Program to calculate simple interest based on given rate and time

# Get user input
principal = float(input("Enter principal amount: "))
time = float(input("Enter time in years: "))

# Determine rate based on time
if time == 1:
    rate = 6
elif time == 2:
    rate = 7
elif time == 3:
    rate = 9
elif time > 3:
    rate = 12
else:
    rate = 0

# Calculate simple interest
if rate != 0:
    interest = (principal * rate * time) / 100
    print("Simple Interest:", interest)
else:
    print("Invalid time entered")
