import random

def simulate_coin_flips():
    flips = ''
    count = 0
    flip_sequence = []
    while 'HHH' not in flips and 'TTT' not in flips:
        outcome = random.choice(['H', 'T'])
        flips += outcome
        flip_sequence.append(outcome)
        count += 1
    print(' '.join(flip_sequence), f"({count} flips)")
    return count

total_flips = 0
simulations = 10

for _ in range(simulations):
    total_flips += simulate_coin_flips()

average_flips = total_flips / simulations
print("Average number of flips needed over", simulations, "simulations:", average_flips)
