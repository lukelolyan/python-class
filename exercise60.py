import random

# Define the spaces on the roulette wheel
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [i for i in range(1, 37) if i not in red_numbers]

# Simulate a spin of the roulette wheel
selected_number = random.randint(0, 36)

# Display the selected number and corresponding bets
if selected_number == 0:
    print("Pay 0")
elif selected_number == 00:
    print("Pay 00")
else:
    print(f"The spin resulted in {selected_number}...")
    print(f"Pay {selected_number}")
    if selected_number in red_numbers:
        print("Pay Red")
    else:
        print("Pay Black")
    if selected_number % 2 == 0 and selected_number != 0:
        print("Pay Even")
    else:
        print("Pay Odd")
    if selected_number >= 1 and selected_number <= 18:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")
