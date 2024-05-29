import random

def simulate_coin_flips():
    flips = ''
    count = 0
    while 'HHH' not in flips and 'TTT' not in flips:
        outcome = random.choice(['H', 'T'])
        flips += outcome
        print(outcome, end=' ')
        count += 1
    print("\nNumber of flips needed:", count)
    return count

total_flips = 0
simulations = 10

for _ in range(simulations):
    total_flips += simulate_coin_flips()

average_flips = total_flips / simulations
print("Average number of flips needed over", simulations, "simulations:", average_flips)
