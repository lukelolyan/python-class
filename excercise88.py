def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Input lengths from the user
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check if the lengths can form a triangle
if is_triangle(side1, side2, side3):
    print("The lengths can form a triangle.")
else:
    print("The lengths cannot form a triangle.")
