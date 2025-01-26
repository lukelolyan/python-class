

# 1
apples_3 = int(input())
apples_2 = int(input())
apples_1 = int(input())

bananas_3 = int(input())
bananas_2 = int(input())
bananas_1 = int(input())


apples_score = (apples_3 * 3) + (apples_2 * 2) + (apples_1 * 1)
bananas_score = (bananas_3 * 3) + (bananas_2 * 2) + (bananas_1 * 1)


if apples_score > bananas_score:
    print("A")
elif bananas_score > apples_score:
    print("B")
else:
    print("T")

#2 


n = int(input())
for _ in range(n):
    line = input().strip()
    count, char = line.split()
    count = int(count)
    print(char * count)

#3

def run_length_encode(line):
    encoded = []
    count = 1
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            count += 1
        else:
            encoded.append(f"{count} {line[i - 1]}")
            count = 1
    # Add the last character block
    encoded.append(f"{count} {line[-1]}")
    return " ".join(encoded)

def main():
    N = int(input("Enter the number of lines: "))
    result = []
    for _ in range(N):
        line = input().strip()
        result.append(run_length_encode(line))
    # Print the result
    for encoded_line in result:
        print(encoded_line)

if __name__ == "__main__":
    main()

#4
def main():
    flips = input().strip()
  
    grid = [[1, 2], [3, 4]]

    horizontal_flip = 0
    vertical_flip = 0

    for flip in flips:
        if flip == 'H':
            horizontal_flip += 1
        elif flip == 'V':
            vertical_flip += 1
          
    if horizontal_flip % 2 == 1:
        grid[0], grid[1] = grid[1], grid[0]

    if vertical_flip % 2 == 1:
        grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
        grid[1][0], grid[1][1] = grid[1][1], grid[1][0]

    for row in grid:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()

# 5
def apply_substitution(sequence, rules, step_count):
    steps = []  # To store the details of each substitution

    for _ in range(step_count):
        for rule_index, (pattern, replacement) in enumerate(rules, start=1):
            # Find the first occurrence of the pattern in the sequence
            pos = sequence.find(pattern)
            if pos != -1:
                # Perform the substitution
                new_sequence = sequence[:pos] + replacement + sequence[pos + len(pattern):]

                # Record the substitution details (1-indexed position)
                steps.append((rule_index, pos + 1, new_sequence))

                # Update the sequence
                sequence = new_sequence

                # Move to the next step
                break
    return steps


def main():
    # Read the substitution rules
    rules = []
    for _ in range(3):
        pattern, replacement = input().strip().split()
        rules.append((pattern, replacement))

    # Read S, I, F
    S, I, F = input().strip().split()
    S = int(S)

    # Apply the substitution rules
    steps = apply_substitution(I, rules, S)

    # Output the steps
    for step in steps:
        print(step[0], step[1], step[2])


if __name__ == "__main__":
    main()
































