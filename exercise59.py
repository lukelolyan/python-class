# Read input from user
plate = input("Enter the license plate characters: ")

# Check if the input matches the older style license plate format
if len(plate) == 6 and plate[:3].isalpha() and plate[3:].isdigit():
    print("The characters represent an older style license plate.")
# Check if the input matches the newer style license plate format
elif len(plate) == 7 and plate[:4].isdigit() and plate[4:].isalpha():
    print("The characters represent a newer style license plate.")
else:
    print("The characters entered do not match any valid license plate style.")
