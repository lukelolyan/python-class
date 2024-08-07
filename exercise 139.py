def check_bingo(card):
    rows = len(card)
    cols = len(card[0])

    for i in range(rows):
        if all(cell == 0 for cell in card[i]):
            return True

    for j in range(cols):
        if all(card[i][j] == 0 for i in range(rows)):
            return True

    if all(card[i][i] == 0 for i in range(min(rows, cols))):
        return True

    if all(card[i][cols - i - 1] == 0 for i in range(min(rows, cols))):
        return True

    return False


bingo_card1 = [
    [0, 0, 0, 0, 0],
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]

bingo_card2 = [
    [1, 0, 6],
    [2, 0, 7],
    [3, 0, 8],
    [4, 0, 9],
    [5, 0, 10]
]

bingo_card3 = [
    [1, 2, 0],
    [4, 0, 6],
    [7, 8, 0]
]

bingo_card4 = [
    [1, 2, 3],
    [0, 0, 0],
    [7, 8, 9]
]


print("Bingo Card 1 - Winning Line:", check_bingo(bingo_card1))
print("Bingo Card 2 - Winning Line:", check_bingo(bingo_card2))
print("Bingo Card 3 - Winning Line:", check_bingo(bingo_card3))
print("Bingo Card 4 - Winning Line:", check_bingo(bingo_card4))
