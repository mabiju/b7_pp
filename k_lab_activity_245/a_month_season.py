# Program to print season based on month number

# Get user input
month = int(input("Enter month number (1-12): "))

# Determine season
if month == 12 or month == 1 or month == 2:
    season = "Winter"
elif month >= 3 and month <= 5:
    season = "Spring"
elif month >= 6 and month <= 8:
    season = "Summer"
elif month >= 9 and month <= 11:
    season = "Fall"
else:
    season = "Invalid month"

print("Season:", season)
