import math

# Prompt user for input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Compute the roots
if discriminant < 0:
    print("The quadratic equation has no real roots.")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The quadratic equation has one real root: {root}")
else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The quadratic equation has two real roots: {root1} and {root2}")
