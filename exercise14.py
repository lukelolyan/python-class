# Read height in feet and inches from the user
feet = float(input("Enter the height in feet: "))
inches = float(input("Enter the height in inches: "))

# Convert height to centimeters
total_inches = feet * 12 + inches
centimeters = total_inches * 2.54

# Display the equivalent height in centimeters
print(f"The equivalent height is", centimeters," centimeters.")
