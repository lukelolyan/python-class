length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

    # 1 acre = 43560 square feet
area_acres = (length * width) / 43560

print("The area of the field is", round(area_acres, 2), "acres.")

