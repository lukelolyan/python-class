import math
meal_cost = float(input("Enter the cost of the meal: "))

# Calculate tax, tip, and total cost
tax_amount = meal_cost * 0.08
tip_amount = meal_cost * 0.18
total_cost = meal_cost + tax_amount + tip_amount


print("Total: $", format(total_cost, '.2f'))