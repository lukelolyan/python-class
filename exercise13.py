def calculate_change(cents):
    coins = [200, 100, 25, 10, 5, 1]
    coin_names = ['toonies', 'loonies', 'quarters', 'dimes', 'nickels', 'pennies']
    change = []

    for i in range(len(coins)):
        num_coins = cents // coins[i]
        cents %= coins[i]
        if num_coins > 0:
            change.append((num_coins, coin_names[i]))

    return change

# Read the number of cents from the user
cents = int(input("Enter the amount in cents: "))
result = calculate_change(cents)

print("Change to be given:")
for num, coin in result:
    print(f"{num} {coin}")
