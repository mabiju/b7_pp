# Program to simulate traffic light actions

# Get user input
color = input("Enter traffic light color (Red/Yellow/Green): ").capitalize()

# Determine action
if color == "Red":
    action = "Stop"
elif color == "Yellow":
    action = "Get Ready"
elif color == "Green":
    action = "Go"
else:
    action = "Invalid color"

print("Action:", action)
