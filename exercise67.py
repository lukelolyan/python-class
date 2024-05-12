def calculate_admission_cost():
    total_cost = 0
    while True:
        age = input("Enter the age of the guest (or press Enter to finish): ")
        if age == "":
            break
        age = int(age)
        if age <= 2:
            cost = 0
        elif 3 <= age <= 12:
            cost = 14.00
        elif age >= 65:
            cost = 18.00
        else:
            cost = 23.00
        total_cost += cost

    print(f"The total admission cost for the group is: ${total_cost:.2f}")

calculate_admission_cost()
