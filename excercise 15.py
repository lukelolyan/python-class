def check_square_color(position):
    column = position[0]
    row = int(position[1])
    
    if (ord(column) - ord('a') + row) % 2 == 0:
        return "black"
    else:
        return "white"

# Read position from user
user_position = input("Enter a position on the chess board (e.g., a1, d5): ")

# Check and display the color of the square
square_color = check_square_color(user_position)
print(f"The square at position {user_position} is {square_color}.")
