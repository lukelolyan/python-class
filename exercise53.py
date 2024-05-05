rating = float(input("Enter the employee's rating: "))

if rating == 0.0:
    print("Performance: Unacceptable")
    print("Raise Amount: $0.00")
elif rating == 0.4:
    print("Performance: Acceptable")
    print("Raise Amount: $960.00")
elif rating >= 0.6:
    print("Performance: Meritorious")
    print(f"Raise Amount: ${2400.00 * rating:.2f}")
else:
    print("Invalid rating entered. Please enter 0.0, 0.4, or a value greater than or equal to 0.6.")
