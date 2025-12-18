age = int(input("Enter age: "))
gender = input("Enter gender (male/female/other): ").lower()

if age <= 20 and gender not in ['male', 'female']:
    print("You are eligible to get the admission.")
else:
    print("You are not eligible to get the admission.")
