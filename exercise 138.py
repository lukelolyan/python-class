import random

def create_bingo_card():
    bingo_card = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
    
    for letter in bingo_card:
        lower_bound = 1 if letter == 'B' else 16 if letter == 'I' else 31 if letter == 'N' else 46 if letter == 'G' else 61
        numbers = random.sample(range(lower_bound, lower_bound + 15), 5)
        bingo_card[letter] = numbers
    
    return bingo_card

def display_bingo_card(bingo_card):
    print("B   I   N   G   O")
    for i in range(5):
        for letter in bingo_card:
            print(f"{bingo_card[letter][i]:2d}", end=" ")
        print()

if __name__ == "__main__":
    bingo_card = create_bingo_card()
    display_bingo_card(bingo_card)
